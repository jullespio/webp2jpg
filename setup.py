from setuptools import setup, find_packages

setup(
    name="webp2jpg",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["Pillow>=10.0.0"],
    entry_points={
        "console_scripts": [
            "webp2jpg=cli:main"
        ]
    },
    author="Julles",
    description="A CLI tool for converting WebP images to JPEG.",
    python_requires=">=3.7",
)
