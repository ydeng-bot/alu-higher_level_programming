#!/usr/bin/python3
"""Reads stdin line by line and computes log metrics."""
import sys

total_size = 0
status_codes = {}
line_count = 0
valid_codes = ("200", "301", "400", "401", "403", "404", "405", "500")
just_printed = False


def print_stats():
    """Print the accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))
    sys.stdout.flush()


try:
    for line in sys.stdin:
        parts = line.split()
        try:
            code = parts[-2]
            size = int(parts[-1])
        except (IndexError, ValueError):
            continue

        total_size += size
        if code in valid_codes:
            status_codes[code] = status_codes.get(code, 0) + 1
        line_count += 1
        just_printed = False

        if line_count % 10 == 0:
            print_stats()
            just_printed = True

    if not just_printed:
        print_stats()
except KeyboardInterrupt:
    print_stats()
    raise
