# webp2jpg

A simple, tiny CLI tool to convert WebP images to JPEG format. It can convert individual files or all `.webp` images in a folder, while copying non-WebP files to the output directory.

## Behavior

- Converts `.webp` images to `.jpg`
- Recursively processes folders
- Copies non-WebP files alongside converted images
- Reports how many images were converted and how many were copied

## Installation

```bash
pip install .
```

Make sure you're in the root of the project directory when running the command above.

## Usage

### After Installation

Once installed via `pip`, you can use the `webp2jpg` command directly from the terminal:

```bash
webp2jpg path/to/file_or_folder -o path/to/output/
```

### Example

```bash
webp2jpg ./webp_images -o ./converted_images
```

This will:
- Convert all `.webp` files to `.jpg`
- Copy all non-WebP files to the output folder
- Inform how many were converted and how many were copied

### Developer Mode (Run from source)

If you haven't installed the tool and wish to run it from the source:

```bash
python cli.py path/to/file_or_folder -o path/to/output/
```

## Dependencies

- Python 3.7+
- [Pillow](https://pypi.org/project/Pillow/)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## License

MIT

## Author

Julles Pio
