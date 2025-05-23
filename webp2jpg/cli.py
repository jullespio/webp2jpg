import argparse
from pathlib import Path
from webp2jpg.converter import convert_webp_to_jpeg, batch_convert

def main():
    parser = argparse.ArgumentParser(description="Convert .webp images to .jpg format.")
    parser.add_argument("input", type=Path, help="Input .webp file or folder")
    parser.add_argument("-o", "--output", type=Path, help="Optional output directory")

    args = parser.parse_args()
    input_path = args.input
    output_path = args.output or input_path

    if input_path.is_file():
        if input_path.suffix.lower() != ".webp":
            print("✗ Error: Input file must have a .webp extension.")
            return
        dest = output_path if output_path.is_file() else output_path / (input_path.stem + ".jpg")
        convert_webp_to_jpeg(input_path, dest)
    elif input_path.is_dir():
        batch_convert(input_path, output_path)
    else:
        print("✗ Error: Input path is invalid.")

if __name__ == "__main__":
    main()
