# Utility script to merge two npbench SQLite databases into a new one.
import argparse
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import utilities as util

RESULT_COLUMNS: Sequence[str] = (
    "timestamp",
    "benchmark",
    "kind",
    "domain",
    "dwarf",
    "preset",
    "mode",
    "framework",
    "version",
    "details",
    "validated",
    "time",
)

LCOUNT_COLUMNS: Sequence[str] = (
    "timestamp",
    "benchmark",
    "kind",
    "domain",
    "dwarf",
    "mode",
    "framework",
    "version",
    "details",
    "count",
    "npdiff",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Merge two npbench SQLite databases into a new output database.",
    )
    parser.add_argument("db1", help="First input npbench database path.")
    parser.add_argument("db2", help="Second input npbench database path.")
    parser.add_argument("outdb", help="Destination database path.")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite outdb if it already exists.",
    )
    return parser.parse_args()


def validate_inputs(db_paths: Sequence[Path], overwrite: bool) -> None:
    for path in db_paths[:2]:
        if not path.exists():
            raise FileNotFoundError(f"Input database not found: {path}")

    outdb = db_paths[2]
    if outdb.exists() and not overwrite:
        raise FileExistsError(
            f"Destination database already exists: {outdb}. "
            "Use --overwrite to replace it."
        )
    if outdb.exists() and overwrite:
        outdb.unlink()


def open_connection(db_path: Path) -> sqlite3.Connection:
    conn = util.create_connection(str(db_path))
    if conn is None:
        raise ConnectionError(f"Could not open database: {db_path}")
    return conn


def fetch_rows(
    conn: sqlite3.Connection,
    table: str,
    columns: Sequence[str],
    label: str,
) -> List[Tuple]:
    """Return rows (without id column) if the table exists; otherwise return []."""
    info = conn.execute(f"PRAGMA table_info({table});").fetchall()
    if not info:
        print(f"{label}: table '{table}' not found, skipping.")
        return []

    col_names = {row[1] for row in info}
    missing = [c for c in columns if c not in col_names]
    if missing:
        raise ValueError(f"{label}: table '{table}' is missing columns {missing}")

    col_list = ", ".join(columns)
    rows = conn.execute(f"SELECT {col_list} FROM {table};").fetchall()
    return rows


def insert_rows(
    conn: sqlite3.Connection,
    rows: List[Tuple],
    insert_sql: str,
) -> int:
    if not rows:
        return 0
    conn.executemany(insert_sql, rows)
    conn.commit()
    return len(rows)


def merge_table(
    dest_conn: sqlite3.Connection,
    sources: Iterable[Tuple[str, sqlite3.Connection]],
    table: str,
    columns: Sequence[str],
    insert_sql: str,
) -> Tuple[int, int]:
    copied = [0, 0]
    for idx, (label, conn) in enumerate(sources):
        rows = fetch_rows(conn, table, columns, label)
        copied[idx] = insert_rows(dest_conn, rows, insert_sql)
    return copied[0], copied[1]


def main() -> None:
    args = parse_args()
    db1, db2, outdb = (Path(args.db1), Path(args.db2), Path(args.outdb))

    validate_inputs((db1, db2, outdb), args.overwrite)

    with closing(open_connection(db1)) as conn1, closing(
        open_connection(db2)
    ) as conn2, closing(open_connection(outdb)) as dest:
        # Ensure output schema exists
        util.create_table(dest, util.sql_create_results_table)
        util.create_table(dest, util.sql_create_lcounts_table)

        sources = [(f"{db1}", conn1), (f"{db2}", conn2)]

        res_counts = merge_table(
            dest, sources, "results", RESULT_COLUMNS, util.sql_insert_into_results_table
        )
        lc_counts = merge_table(
            dest,
            sources,
            "lcounts",
            LCOUNT_COLUMNS,
            util.sql_insert_into_lcounts_table,
        )

    print(f"results: copied {res_counts[0]} rows from {db1} and {res_counts[1]} rows from {db2}")
    print(f"lcounts: copied {lc_counts[0]} rows from {db1} and {lc_counts[1]} rows from {db2}")
    print(f"merged database written to {outdb}")


if __name__ == "__main__":
    main()
