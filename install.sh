#!/usr/bin/env bash

# Detect OS type
OS="$(uname -s)"

echo "🛠️  Setting up webp2jpg environment..."

# Step 1: Create virtual environment
python -m venv venv || {
    echo "❌ Failed to create virtual environment."
    exit 1
}

# Step 2: Activate the virtual environment
if [[ "$OS" == "Linux" || "$OS" == "Darwin" ]]; then
    source venv/bin/activate
elif [[ "$OS" == "MINGW64_NT"* || "$OS" == "MSYS_NT"* ]]; then
    source venv/Scripts/activate
else
    echo "⚠️  Unsupported OS: $OS"
    exit 1
fi

# Step 3: Install dependencies
echo "📦 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt || {
    echo "❌ Failed to install dependencies."
    exit 1
}

# Step 4: Verify Pillow installation
python -c "import PIL" 2>/dev/null && echo "✅ Pillow installed successfully." || {
    echo "❌ Pillow installation failed."
    exit 1
}

echo ""
echo "✅ Installation complete."
echo "To run the CLI tool, use:"
echo ""
echo "  python cli.py input_folder/ -o output_folder/"
echo ""
echo "Or activate the environment later with:"
if [[ "$OS" == "Linux" || "$OS" == "Darwin" ]]; then
    echo "  source venv/bin/activate"
else
    echo "  source venv/Scripts/activate"
fi
