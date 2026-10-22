from spotify_starter import DATA_REVISION, DATA_SHA256, get_data_url
def test_metadata():
    assert DATA_REVISION == "c4609440b24ac4075899f6e60b33775acbe00827"
    assert DATA_SHA256 == "b202fa49909b2d5cef71a04b1d21243cfeb36414535f2ca9272aa646721177bd"
    assert "c4609440b24ac4075899f6e60b33775acbe00827" in get_data_url()
