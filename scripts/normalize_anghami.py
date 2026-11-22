"""Turn Anghami copy-paste dumps (title<TAB>E?<TAB>artist<TAB>) into one deduped CSV."""
import csv, re, sys, unicodedata
from pathlib import Path

root = Path(__file__).resolve().parent.parent
raw = sorted((root / "data/anghami/raw").glob("*.txt"))
out = root / "data/anghami/likes.csv"

def key(s):
    s = unicodedata.normalize("NFKC", s).casefold()
    s = re.sub(r"\s*[\(\[][^)\]]*(remaster|version|live|edit|mono|stereo|radio|mix|feat|with)[^)\]]*[\)\]]", "", s)
    s = re.sub(r"\s+-\s+.*(remaster|version|live|edit).*$", "", s)
    return re.sub(r"\W+", " ", s).strip()

seen, rows, total = set(), [], 0
for f in raw:
    for line in f.read_text(encoding="utf-8").splitlines():
        parts = line.split("\t")
        if len(parts) < 3 or not parts[0].strip() or not parts[2].strip():
            continue
        total += 1
        title, explicit, artist = parts[0].strip(), parts[1].strip() == "E", parts[2].strip()
        k = (key(title), key(artist))
        if k in seen:
            continue
        seen.add(k)
        rows.append({"artist": artist, "title": title, "explicit": int(explicit)})

with out.open("w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=["artist", "title", "explicit"])
    w.writeheader(); w.writerows(rows)
print(f"{total} lines read, {len(rows)} unique songs -> {out.relative_to(root)}", file=sys.stderr)
