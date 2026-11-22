"""Flag candidates whose artist or title is already in data/anghami/likes.csv."""
import csv, re, sys, unicodedata
from pathlib import Path
root = Path(__file__).resolve().parent.parent
def n(s): return re.sub(r"[^\w]+", " ", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode() or s).casefold().strip() if s.isascii() or unicodedata.normalize("NFKD", s).encode("ascii","ignore").strip() else s.casefold()
likes = list(csv.DictReader((root / "data/anghami/likes.csv").open(encoding="utf-8")))
artists = " | ".join(n(r["artist"]) for r in likes)
titles = {n(r["title"]) for r in likes}
bad = 0
for r in csv.DictReader((root / sys.argv[1]).open(encoding="utf-8"), delimiter="\t"):
    a, t = n(r["artist"]), n(r["title"])
    hits = []
    if re.search(rf"(^|\W){re.escape(a)}(\W|$)", artists): hits.append("artist known")
    if any(t == x or x.startswith(t + " ") for x in titles): hits.append("title known")
    if hits: bad += 1; print(f"{r['artist']} — {r['title']}: {', '.join(hits)}")
print(f"{bad} flagged", file=sys.stderr)
