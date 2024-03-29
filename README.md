# utilities
A collection of silly little utilities I've put together

## get_unique_values.py
Takes a text file and returns each unique line from it.

Usage:
`python get_unique_values.py <path_to_filename>`

Creates `filename_unique.suffix`

## convert_image.py
Takes a path to an existing image and converts it to a different format.

Usage:
`python convert_image.py <path_to_image> <format>`

Creates `image.new_format`

Uses Pillow to convert the image. Supported formats are here: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html

## find_lines_with_pattern.py
Reads a file, and a search pattern (a string), and returns each line in the file that matches the pattern. This is a simple pattern match - no regex.

Usage:
`python find_lines_with_pattern.py <path_to_file> <search_string>`

Creates `file_match.suffix`