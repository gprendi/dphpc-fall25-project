#!/usr/bin/env python3
import re
import sys
import matplotlib.pyplot as plt


def parse_log(path):
    # Regexes for the three things we care about
    unroll_re = re.compile(r"^Unroll factor:\s*(\d+)")
    first_re = re.compile(r"PyTorch CPU - .* - first/backward:\s*([\d.]+)ms")
    median_re = re.compile(r"PyTorch CPU - .* - median/backward:\s*([\d.]+)ms")

    blocks = []
    current = {}

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            m = unroll_re.search(line)
            if m:
                # If we already have a complete block, store it
                if {"unroll", "first", "median"} <= current.keys():
                    blocks.append(current)
                current = {"unroll": int(m.group(1))}
                continue

            m = first_re.search(line)
            if m and current:
                current["first"] = float(m.group(1))
                continue

            m = median_re.search(line)
            if m and current:
                current["median"] = float(m.group(1))
                continue

    # Flush last block
    if {"unroll", "first", "median"} <= current.keys():
        blocks.append(current)

    if not blocks:
        raise ValueError("No data blocks found in log file.")

    # Sort by unroll factor
    blocks.sort(key=lambda d: d["unroll"])

    xs = [b["unroll"] for b in blocks]
    first = [b["first"] for b in blocks]
    median = [b["median"] for b in blocks]

    return xs, first, median


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} LOGFILE")
        sys.exit(1)

    log_path = sys.argv[1]
    xs, first, median = parse_log(log_path)

    # plt.plot(xs, first, marker="o", label="first/backward (ms)")
    plt.plot(xs, median, marker="o", label="median/backward (ms)")

    plt.xlabel("Unroll factor")
    plt.ylabel("Time [ms]")
    plt.title("PyTorch backward time vs unroll factor")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
