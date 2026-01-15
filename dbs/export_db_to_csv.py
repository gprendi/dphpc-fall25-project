"""
Export the bundled benchmark SQLite database to CSV files.

The script is intentionally small and self contained: it hard-codes the
database path and writes one CSV per table into ./exports/.
"""

import csv
import sqlite3
from pathlib import Path


# Pick any of the databases in the repo; adjust the filename if needed.
DB_PATH = Path(__file__).parent / "linear_algebra.db"
OUTPUT_DIR = Path(__file__).parent / "exports"


def export_table(cur: sqlite3.Cursor, table: str) -> Path:
    cur.execute(f"SELECT * FROM {table}")
    columns = [col[0] for col in cur.description]
    rows = cur.fetchall()

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / f"{table}.csv"
    with out_path.open("w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(columns)
        writer.writerows(rows)
    return out_path


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "SELECT name FROM sqlite_master "
        "WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    )
    tables = [row[0] for row in cur.fetchall()]
    if not tables:
        raise SystemExit(f"No tables found in {DB_PATH}")

    for table in tables:
        out = export_table(cur, table)
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()
