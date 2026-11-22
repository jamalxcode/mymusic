# Notes

## 2026-11-22 — first attempt

### Anghami
- Liked-songs playlist id: **108250894** (`https://play.anghami.com/playlist/108250894`), ~8,370 songs.
- The share link is an `anghami.app.link` Branch.io redirect; the real URL is the `play.anghami.com` one above.
- The cloud session first had no network access to Anghami. A personal environment
  "Music playlists" was created allowing play.anghami.com, api.anghami.com, www.anghami.com,
  www.youtube.com and music.youtube.com.
- Even then, `play.anghami.com` returned **HTTP 406** to a plain request (bot protection), and
  Anghami has no official public API. Scraping around that was not attempted without the owner's OK.
- Workable ways to get the list in:
  1. Anghami desktop/web: open the playlist, select all, copy, paste as text → `data/anghami/raw.txt`.
  2. A third-party transfer tool (e.g. TuneMyMusic/Soundiiz) exporting the playlist to CSV.
  3. Screenshots (slow for 8k songs).

### YouTube
- No playlist link provided yet. Needs to be Public/Unlisted, or a Google Takeout CSV.

## Taste profile
_Not built yet — waiting for the data._

## Plan
1. Normalize every source to `artist,title,source` CSV in `data/`.
2. Dedupe; count artists; tag each artist with genre / region / era / language.
3. Rank styles by weight → taste profile in this file.
4. For top styles, pick artists and tracks absent from my library → `playlists/*.md`
   with a reason and a YouTube link per song.
