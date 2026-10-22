"""Reproducible access to the course Spotify dataset."""
from __future__ import annotations
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
import os, shutil, tempfile

DATA_REVISION = "c4609440b24ac4075899f6e60b33775acbe00827"
DATA_FILENAME = "spotify_tracks.csv"
DATA_URL = "https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset/resolve/c4609440b24ac4075899f6e60b33775acbe00827/dataset.csv"
DATA_SHA256 = "b202fa49909b2d5cef71a04b1d21243cfeb36414535f2ca9272aa646721177bd"

def get_data_url() -> str:
    return DATA_URL

def _cache_dir() -> Path:
    override = os.environ.get("SPOTIFY_STARTER_CACHE")
    return Path(override).expanduser() if override else Path.home() / ".cache" / "spotify_starter"

def _digest(path: Path) -> str:
    h = sha256()
    with path.open("rb") as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    return h.hexdigest()

def verify_file(path: str | Path) -> bool:
    p = Path(path)
    return p.is_file() and _digest(p) == DATA_SHA256

def get_data_path(cache_dir: str | Path | None = None, *, force: bool = False, timeout: int = 120) -> Path:
    directory = Path(cache_dir).expanduser() if cache_dir else _cache_dir()
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / DATA_FILENAME
    if not force and verify_file(target):
        return target

    fd, temp_name = tempfile.mkstemp(prefix="spotify_tracks_", suffix=".part", dir=directory)
    os.close(fd)
    temp = Path(temp_name)
    try:
        request = Request(DATA_URL, headers={"User-Agent": "BUSADMIN-O712/spotify-starter"})
        with urlopen(request, timeout=timeout) as response, temp.open("wb") as out:
            shutil.copyfileobj(response, out)
        actual = _digest(temp)
        if actual != DATA_SHA256:
            raise RuntimeError(f"Dataset checksum mismatch: expected {DATA_SHA256}, got {actual}.")
        temp.replace(target)
        return target
    except Exception as exc:
        temp.unlink(missing_ok=True)
        if isinstance(exc, RuntimeError):
            raise
        raise RuntimeError("Could not download the pinned Spotify dataset.") from exc
