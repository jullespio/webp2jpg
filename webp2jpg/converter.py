from pathlib import Path
from PIL import Image
import shutil

def convert_webp_to_jpeg(source: Path, destination: Path):
    if source.suffix.lower() != ".webp":
        return
    try:
        with Image.open(source) as img:
            rgb_img = img.convert("RGB")
            destination.parent.mkdir(parents=True, exist_ok=True)
            rgb_img.save(destination, "JPEG")
            print(f"✓ Converted: {source.name} → {destination.name}")
    except Exception as e:
        print(f"✗ Failed to convert {source.name}: {e}")

def batch_convert(source_dir: Path, output_dir: Path):
    converted_count = 0
    copied_count = 0

    output_dir.mkdir(parents=True, exist_ok=True)

    for file in source_dir.iterdir():
        dest_file = output_dir / (file.stem + ".jpg") if file.suffix.lower() == ".webp" else output_dir / file.name

        if file.suffix.lower() == ".webp":
            convert_webp_to_jpeg(file, dest_file)
            converted_count += 1
        else:
            try:
                shutil.copy2(file, dest_file)
                copied_count += 1
                print(f"• Copied non-webp: {file.name}")
            except Exception as e:
                print(f"✗ Failed to copy {file.name}: {e}")

    print(f"\n✓ {converted_count} WebP image(s) converted to JPEG.")
    print(f"• {copied_count} non-WebP file(s) copied.")
