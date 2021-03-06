#!/usr/bin/env python3

import argparse
from gendiff.libs.diff_flat import generate_diff


# poetry run gendiff -h
# poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json
# poetry run gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml
def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', type=str,
                        help='set format of output')

    args = parser.parse_args()
    if args.first_file and args.second_file:
        print(generate_diff(args.first_file, args.second_file, args.format))
    else:
        print(args.accumulate(args.first_file))


if __name__ == '__main__':
    main()
