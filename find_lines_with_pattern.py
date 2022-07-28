import sys
import pathlib

from get_unique_values import OUTFILE

FILENAME = pathlib.Path(sys.argv[1])
OUTFILE = FILENAME.with_stem(FILENAME.stem + '_match')
SEARCH_PATTERN = sys.argv[-1]

def find_pattern(filename, pattern):
    """Find a pattern in a file and return any lines that match in a list."""
    with open(filename, 'r') as f:
        return [line for line in f if pattern in line]

def write_list_to_file(list_of_values):
    """Write a list of values to a file."""
    with open(OUTFILE, 'w') as f:
        for value in list_of_values:
            f.write(value)

def main():
    """Main function."""
    write_list_to_file(find_pattern(FILENAME, SEARCH_PATTERN))

if __name__ == "__main__":
    main()