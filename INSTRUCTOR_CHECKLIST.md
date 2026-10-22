# Instructor checklist

- Create `github.com/zhouy185/spotify-starter`.
- Commit this folder's contents to the repo root.
- Test in a fresh Colab runtime:

```python
%pip install -q git+https://github.com/zhouy185/spotify-starter.git
from spotify_starter import get_data_path, verify_file
p = get_data_path()
print(p, verify_file(p))
```

- Test the current MotherDuck workflow before release.
- Never commit tokens or downloaded data.

Pinned revision: `c4609440b24ac4075899f6e60b33775acbe00827`  
SHA-256: `b202fa49909b2d5cef71a04b1d21243cfeb36414535f2ca9272aa646721177bd`
