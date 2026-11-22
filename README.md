# mymusic

My music library and taste profile, plus playlists of new music made from it.

## Goal
Read my Anghami and YouTube playlists, work out the styles I like, and build new playlists
in those styles from songs and artists I have **not** listened to yet.

## Layout
- `data/anghami/` — exports of my Anghami playlists (raw + normalized `artist,title` CSV)
- `data/youtube/` — exports of my YouTube playlists
- `NOTES.md` — what has been learned so far: sources, access, taste profile, decisions
- `playlists/` — generated recommendation playlists (`discover-01.md`: 129 songs)
- `scripts/` — `normalize_anghami.py`, `artists.py`, `check_new.py`

## Sources
| Source | Playlist | Size | Status |
|---|---|---|---|
| Anghami — Liked songs | https://play.anghami.com/playlist/108250894 | ~8,370 songs | 4,815 unique imported (`data/anghami/likes.csv`) |
| YouTube | — | — | link not given yet |
