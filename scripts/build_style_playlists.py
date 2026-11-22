"""Sort data/anghami/likes.csv into style playlists using data/anghami/artist_styles.tsv.

Writes one TuneMyMusic CSV per playlist to exports/style-playlists/ plus a summary.
Song order inside each playlist: by artist, then title.
"""
import csv, re
from collections import defaultdict
from pathlib import Path

root = Path(__file__).resolve().parent.parent
NAMES = {
    "classic-rock": "Classic Rock", "hard-rock": "Hard Rock & Metal", "80s-pop": "80s Pop & New Wave",
    "oldies": "Oldies & 70s Pop", "disco-soul": "Disco, Funk & Soul", "songwriter-folk": "Singer-Songwriter & Folk",
    "country": "Country", "blues-jazz": "Blues & Jazz", "french": "French Chanson & Pop",
    "modern-pop": "Modern Pop", "dance": "Dance & Electronic", "alt-rock": "Alternative & Indie Rock",
    "covers": "Acoustic & Piano Covers", "arabic-world": "Arabic & World", "russian": "Russian Pop",
    "classical": "Classical & Soundtracks",
}
styles = {r["artist"]: r["style"] for r in
          csv.DictReader((root / "data/anghami/artist_styles.tsv").open(encoding="utf-8"), delimiter="\t")}

ns = {"__file__": str(root / "scripts/artists.py")}
exec((root / "scripts/artists.py").read_text(encoding="utf-8").split("c, script =")[0], ns)
split = ns["split"]

groups, unknown = defaultdict(list), []
for r in csv.DictReader((root / "data/anghami/likes.csv").open(encoding="utf-8")):
    text = r["title"] + r["artist"]
    if re.search(r"[؀-ۿ]", text):
        s = "arabic-world"
    elif re.search(r"[Ѐ-ӿ]", text):
        s = "russian"
    elif re.search(r"\b(piano|lullaby)\b", text, re.I) or re.search(r"\(cover\)|acoustic cover", text, re.I):
        s = "covers"
    else:
        parts = split(r["artist"])
        s = styles.get(parts[0] if parts else r["artist"])
        if s not in NAMES:
            unknown.append(r); s = "modern-pop"
    groups[s].append(r)

out = root / "exports/style-playlists"
out.mkdir(parents=True, exist_ok=True)
for f in out.glob("*.csv"):
    f.unlink()
lines = ["# Style playlists", "", "| Playlist | Songs | File |", "|---|---|---|"]
for code, name in NAMES.items():
    rows = sorted(groups.get(code, []), key=lambda r: (r["artist"].casefold(), r["title"].casefold()))
    if not rows:
        continue
    fn = f"{list(NAMES).index(code) + 1:02d}-{code}.csv"
    with (out / fn).open("w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh); w.writerow(["Track name", "Artist name", "Album", "Playlist name"])
        for r in rows:
            w.writerow([r["title"], r["artist"], "", name])
    lines.append(f"| {name} | {len(rows)} | `{fn}` |")
lines += ["", f"Total: {sum(len(v) for v in groups.values())} songs. Unlabelled artists (put in Modern Pop): {len(unknown)}."]
(out / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
