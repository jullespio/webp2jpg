from pathlib import Path
from PIL import Image

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
    for webp_file in source_dir.glob("*.webp"):
        dest_file = output_dir / (webp_file.stem + ".jpg")
        convert_webp_to_jpeg(webp_file, dest_file)
