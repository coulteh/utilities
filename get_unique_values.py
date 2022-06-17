import sys
import pathlib

FILENAME = pathlib.Path(sys.argv[-1])
OUTFILE = FILENAME.with_stem(FILENAME.stem + '_unique')

def get_set_from_file(filename):
    """Get a set of unique values from a file."""
    with open(filename, 'r') as f:
        return {line.strip() for line in f}


def write_set_to_file(set_of_values):
    """Write a set of values to a file."""
    with open(OUTFILE, 'w') as f:
        for value in set_of_values:
            f.write(value + '\n')

def main():
    """Main function."""
    write_set_to_file(get_set_from_file(FILENAME))

if __name__ == "__main__":
    main()
