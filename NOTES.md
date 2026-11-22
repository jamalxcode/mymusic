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
- Not used (decided 2026-11-22): recommendations are built from the Anghami likes only.

## 2026-11-22 — Anghami likes imported

- Pasted from Anghami web in two chunks → `data/anghami/raw/list_{1,2}.txt`
  (format per line: `title<TAB>E-if-explicit<TAB>artist<TAB>`; list_2 has a page header to skip).
- 9,677 lines → 5,096 unique lines → **4,815 unique songs** after merging remasters/live/edit variants
  (`scripts/normalize_anghami.py` → `data/anghami/likes.csv`).
- Anghami says the playlist has **8.4K** songs, so roughly 3,500 are missing from the paste —
  the web page loads songs lazily while scrolling. Paste the rest later into `data/anghami/raw/` and rerun.
- 2,983 artists (`scripts/artists.py` → `data/anghami/artists.csv`).
- Script mix: 4,707 Latin, 68 Cyrillic, 40 Arabic.

## Taste profile (from 4,815 songs)

Ordered by weight. Your core is **70s–80s Western pop and rock**, with strong French and dance sides.

1. **Classic rock & AOR (70s–80s)** — Rolling Stones (35), Rod Stewart, Billy Joel, Elton John, Sting/The Police,
   Supertramp, Foreigner, Bob Seger, Eagles, Dire Straits, Bon Jovi, AC/DC, Fleetwood Mac, Tom Petty, Journey.
2. **80s synth-pop & new wave** — Kim Wilde (24), Duran Duran, ABC, Roxy Music, Human League, Yazoo,
   Alphaville, Eurythmics, Bananarama, Thompson Twins, Fine Young Cannibals.
3. **French chanson & variété** — ~340 French titles: Johnny Hallyday, Mylène Farmer, Alizée, Marie Laforêt,
   Mireille Mathieu, Joe Dassin, Dalida, Patricia Kaas, France Gall, Francis Cabrel, Lara Fabian, Zaz.
4. **Disco, funk & soul** — Donna Summer, Bee Gees, Boney M., CHIC, Kool & The Gang, Stevie Wonder,
   George Benson, Earth Wind & Fire, Marvin Gaye.
5. **Divas & big ballads** — ABBA (27), Céline Dion, Tina Turner, Cher, Demis Roussos, Chris de Burgh.
6. **Modern pop & dance** — David Guetta (22), Taylor Swift, Dua Lipa, Lana Del Rey, Coldplay, Alan Walker,
   Robin Schulz, Sia, Bebe Rexha, Ava Max.
7. **60s–70s singer-songwriters** — Simon & Garfunkel, Cat Stevens, Carole King, Jim Croce, Joan Baez.
8. **Country & outlaw** — Johnny Cash (21), Waylon Jennings, Willie Nelson, Kris Kristofferson, Kenny Rogers.
9. **Acoustic / YouTube covers & piano covers** — Jasmine Thompson, Boyce Avenue, First To Eleven,
   Madilyn Bailey, Christina Grimmie, piano cover channels (~100 songs).
10. **90s–2000s Eurodance** — Groove Coverage, Kate Ryan, DJ Bobo, SNAP!, O-Zone, Bad Boys Blue.
11. **Blues** — Shemekia Copeland, Eric Clapton, Robert Cray, Chris Rea.
12. **Arab & French-Arab crossover** — small but present: Khaled, Rachid Taha, Fairuz, Hiba Tawaji,
    Nancy Ajram, Amr Diab, Umm Kulthum.
13. **Russian pop** — Руки Вверх (17), Ленинград.

Other traits: lots of live versions (~150), covers of songs you already like, and mostly major-key,
melodic, singalong songs. Almost no hip-hop, metalcore or jazz.

## Recommendations log

- **Discover 01** (`playlists/discover-01.md`, 129 songs): two rounds of candidates (~250) were checked
  against the library; ~120 were dropped because you already like that artist — your library is very deep
  in the obvious picks, so this list leans on second-tier and lesser-known artists in the same styles.
  Rule used: **artist must be absent** from `likes.csv`. 10 songs share a title with a different song you
  have (e.g. Ultravox "Vienna" vs Billy Joel "Vienna") — kept on purpose.
- To recheck any candidate list: `python3 scripts/check_new.py <file.tsv>` (columns: style, artist, title, why).

## Plan
1. ✅ Anghami normalized (partial — 4,815 of ~8.4K). YouTube not used — Anghami only.
2. Dedupe; count artists; tag each artist with genre / region / era / language.
3. Rank styles by weight → taste profile in this file.
4. For top styles, pick artists and tracks absent from my library → `playlists/*.md`
   with a reason and a YouTube link per song.
