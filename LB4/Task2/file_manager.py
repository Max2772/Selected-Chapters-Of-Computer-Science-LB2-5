"""
Class for zipping files in Task2.

Subject: IGI
Lab Work: 4
Variant: 3
Version: 1.0
Author: Bibikau M.A.
Date: 20.04.2025
"""

import zipfile
from pathlib import Path


class FileManager:
    """Handles reading, writing and zipping files."""

    def __init__(self, directory: Path):
        self.directory = directory

    def read(self, filename: str) -> str:
        """Read text from filename in the script directory."""
        path = self.directory / filename
        if not path.exists():
            raise FileNotFoundError(f"File not found: {path}")
        with open(path, encoding="utf-8") as f:
            return f.read()

    def write(self, filename: str, content: str):
        """Write content to filename."""
        with open(self.directory / filename, "w", encoding="utf-8") as f:
            f.write(content)

    def zip_file(self, source: str, archive: str) -> dict:
        """
        Zip source into archive and return archive info.

        Returns: Dict with name, size, compress_size for the archived entry.
        """
        src = self.directory / source
        arc = self.directory / archive
        with zipfile.ZipFile(arc, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(src, arcname=src.name)
            info = zf.getinfo(src.name)
            return {
                "name": info.filename,
                "size": info.file_size,
                "compress_size": info.compress_size,
            }
