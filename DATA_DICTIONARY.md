# Data dictionary

| Column | Description |
|---|---|
| `track_id` | Spotify track identifier |
| `artists` | Artist credit; multiple artists may be separated by `;` |
| `album_name` | Album name |
| `track_name` | Track title |
| `popularity` | Spotify popularity score, 0–100; not streams or revenue |
| `duration_ms` | Track duration in milliseconds |
| `explicit` | Explicit-content indicator |
| `danceability` | 0–1 danceability measure |
| `energy` | 0–1 energy measure |
| `key` | Encoded musical key |
| `loudness` | Overall loudness in dB |
| `mode` | Major/minor modality indicator |
| `speechiness` | Spoken-word measure |
| `acousticness` | Acoustic confidence measure |
| `instrumentalness` | Instrumental-content measure |
| `liveness` | Live-audience measure |
| `valence` | Musical positiveness measure |
| `tempo` | Estimated BPM |
| `time_signature` | Estimated time signature |
| `track_genre` | Dataset genre label |

The raw file also has an index-like `Unnamed: 0` column.

Important: a `track_id` may occur in multiple rows. Investigate before deduplicating.
