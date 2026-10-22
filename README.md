# spotify-starter

Starter repository for **BUSADMIN O712 — Assignment 2: Music Streaming Analytics**.

It provides reproducible access to the public Spotify tracks dataset and intentionally contains no assignment solutions.

## Student use

```python
%pip install -q git+https://github.com/zhouy185/spotify-starter.git
```

```python
from spotify_starter import get_data_path, get_data_url

DATA_PATH = get_data_path()
DATA_URL = get_data_url()
print(DATA_PATH)
```

## Dataset source

Maharshi Pandya, **Spotify Tracks Dataset**  
https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset

The source dataset contains 114,000 rows and 125 genres. The source page identifies the license as BSD.

Pinned revision: `c4609440b24ac4075899f6e60b33775acbe00827`  
Pinned SHA-256: `b202fa49909b2d5cef71a04b1d21243cfeb36414535f2ca9272aa646721177bd`

The CSV is not stored in this repository. `get_data_path()` downloads and verifies it.
