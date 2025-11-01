"""Convert an image to grayscale using OpenCV."""

from pathlib import Path
from typing import Tuple

import cv2


def convert_to_grayscale(
    input_path: str = "InputImage.jpg", output_path: str = "GrayImage.jpg"
) -> Tuple[Path, Path]:
    """Read ``input_path`` and save its grayscale version to ``output_path``.

    Args:
        input_path: The path to the color image that should be converted.
        output_path: The path where the grayscale image will be written.

    Returns:
        A tuple containing the resolved input and output paths.

    Raises:
        FileNotFoundError: If the input image cannot be read by OpenCV.
    """

    input_file = Path(input_path)
    output_file = Path(output_path)

    image = cv2.imread(str(input_file))
    if image is None:
        raise FileNotFoundError(f"Unable to read image: {input_file}")

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if not cv2.imwrite(str(output_file), grayscale_image):
        raise OSError(f"Unable to write grayscale image to: {output_file}")

    return input_file.resolve(), output_file.resolve()


def main() -> None:
    """Convert ``InputImage.jpg`` to grayscale and report the output path."""

    input_file, output_file = convert_to_grayscale()
    print(f"Converted {input_file} to grayscale at {output_file}.")


if __name__ == "__main__":
    main()
