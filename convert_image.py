import argparse
import sys
from PIL import Image
from pathlib import Path

IMAGE_FILE = Path(sys.argv[1])
FORMAT = sys.argv[2].lower()

def convert_image(image_file, format):
    """Convert an image to a different format."""
    image = Image.open(image_file)
    image.save(image_file.with_suffix('.{}'.format(format)))

def main():
    convert_image(IMAGE_FILE, FORMAT)


if __name__ == "__main__":
    main()
