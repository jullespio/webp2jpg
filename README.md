# WebP to JPEG Converter

A simple command-line tool to convert `.webp` images to `.jpg` format. Supports single-file and batch directory conversion.

## 🛠 Installation

### Option 1: Automatic Setup (Recommended)

Run the install script (works on Linux/macOS and Windows via Git Bash):

```bash
bash install.sh
```

This will:
- Create a virtual environment
- Install dependencies from `requirements.txt`
- Activate the environment

### Option 2: Manual Setup

```bash
git clone https://github.com/your-username/webp2jpg.git
cd webp2jpg
python -m venv venv
source venv/bin/activate  # On Windows (Git Bash): source venv/Scripts/activate
pip install -r requirements.txt
```

## 🚀 Usage

Convert a single file:
```bash
python cli.py image.webp
```

Convert a directory of `.webp` files:
```bash
python cli.py path/to/webp_images/
```

Specify output directory:
```bash
python cli.py path/to/webp_images/ -o path/to/output/
```

## 📦 Packaging

To install as a command-line tool:
```bash
pip install -e .
webp2jpg path/to/webp_images/
```
