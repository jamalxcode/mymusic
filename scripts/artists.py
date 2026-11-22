"""Count songs per artist from data/anghami/likes.csv -> data/anghami/artists.csv."""
import csv, collections, re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
# Names that contain separators but are one act.
KEEP = ["AC/DC", "Simon & Garfunkel", "Daryl Hall & John Oates", "Earth, Wind & Fire", "Kool & The Gang",
        "KC & The Sunshine Band", "Bob Seger & The Silver Bullet Band", "Tom Petty & The Heartbreakers",
        "Bob Marley & The Wailers", "Ike & Tina Turner", "Peter, Paul and Mary", "Crosby, Stills, Nash & Young",
        "Lilly Wood & The Prick", "Eurythmics, Annie Lennox & Dave Stewart", "Hall & Oates",
        "Huey Lewis & The News", "Katrina & The Waves", "Sly & The Family Stone", "Echo & The Bunnymen",
        "Siouxsie & The Banshees", "Florence + The Machine", "Mumford & Sons", "Brooks & Dunn"]
ALIAS = {"Eurythmics, Annie Lennox & Dave Stewart": "Eurythmics", "Hall & Oates": "Daryl Hall & John Oates"}

def split(artist):
    out = []
    for k in KEEP:
        if k.casefold() in artist.casefold():
            i = artist.casefold().index(k.casefold())
            out.append(ALIAS.get(k, k)); artist = artist[:i] + "," + artist[i + len(k):]
    out += [a.strip() for a in re.split(r",|\s+&\s+|\s+feat\.?\s+|\s+with\s+|\s+x\s+|/", artist) if a.strip()]
    return out

c, script = collections.Counter(), collections.Counter()
for r in csv.DictReader((root / "data/anghami/likes.csv").open(encoding="utf-8")):
    for a in split(r["artist"]):
        c[a] += 1
    t = r["title"] + r["artist"]
    script["arabic" if re.search(r"[؀-ۿ]", t) else "cyrillic" if re.search(r"[Ѐ-ӿ]", t)
           else "latin"] += 1
with (root / "data/anghami/artists.csv").open("w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["artist", "songs"]); w.writerows(c.most_common())
print(len(c), "artists;", dict(script))
