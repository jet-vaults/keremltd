"""Generate responsive AVIF + WebP variants for the Kerem site.

Usage:  python tools/optimize_images.py <source-dir>

Source originals are NOT committed (they live on the old WordPress site).
Outputs go to wwwroot/assets/img/<name>-<width>.{avif,webp}.
"""
import json
import os
import sys

from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "wwwroot", "assets", "img")
WIDTHS = [480, 800, 1200, 1600]

# name -> (source filename, crop aspect or None)
SOURCES = {
    "hero": ("maze.jpg", None),
    "pinsker": ("pinsker.jpg", None),
    "cordovero": ("cordovero.jpg", None),
    "marshall": ("marshall.webp", None),
    "grofit": ("grofit.jpg", None),
    "bernstein": ("bernstein.png", (4, 5)),
    "arlozorov": ("arlozorov.jpg", None),
    "weisburg4": ("weisburg4.jpg", None),
    "weisburg6": ("weisburg6.jpg", None),
    "nahmani": ("nahmani.jpg", None),
    "mazeh": ("maze.jpg", None),
    "herut": ("herut.jpg", None),
    "talpiot": ("talpiot.jpg", None),
    "yafo": ("yafo.jpg", None),
    "rothschild": ("rothschild.jpg", None),
    "hoshea": ("hoshea.jpg", None),
    "hoshea-2": ("x_hosha2.jpg", None),
    "batshua": ("batshua.jpg", None),
    "marshall-2": ("x_home2.jpg", (4, 5)),
    "marshall-street": ("x_7e11dd_99ab19b6378549039c13ab112a491ac7mv2.jpg", None),
    "marshall-balcony": ("x_7e11dd_460d60e04f574f1cbaf3f76b109bb496mv2.jpg", None),
    "apt-1": ("x_apt-2_1.jpg", None),
    "apt-2": ("x_apt-2_2.jpg", None),
    "apt-3": ("x_apt-2_3.jpg", None),
    "apt-4": ("x_apt-2_4.jpg", None),
    "apt-5": ("x_apt-2_5.jpg", None),
    "apt-6": ("x_apt-2_6.jpg", None),
    "apt-7": ("x_apt-2_7.jpg", None),
    "apt-8": ("x_apt-2_8.jpg", None),
    "grofit-interior": ("x_Group-Introduction-3-Tel-Aviv_INT_View_02_Balcony-002.jpg", None),
    "arlozorov-interior": ("x_Arlozorov-53-Ramat-Gan_INT_View_01.jpg", None),
    "ceo": ("x_rani.jpg", (4, 5)),
    "tel-aviv": ("x_ta.jpg", (21, 9)),
}


def crop_to(im, aspect):
    if not aspect:
        return im
    aw, ah = aspect
    w, h = im.size
    target = aw / ah
    if w / h > target:
        nw = int(h * target)
        x = (w - nw) // 2
        return im.crop((x, 0, x + nw, h))
    nh = int(w / target)
    y = (h - nh) // 2
    return im.crop((0, y, w, y + nh))


def main(src_dir):
    os.makedirs(OUT, exist_ok=True)
    manifest = {}
    for name, (fn, aspect) in SOURCES.items():
        path = os.path.join(src_dir, fn)
        if not os.path.exists(path):
            print("missing", fn)
            continue
        im = Image.open(path)
        im = ImageOps.exif_transpose(im).convert("RGB")
        im = crop_to(im, aspect)
        w, h = im.size
        widths = [x for x in WIDTHS if x < w] + [min(w, max(WIDTHS))]
        widths = sorted(set(widths))
        out = []
        for tw in widths:
            th = round(h * tw / w)
            r = im.resize((tw, th), Image.LANCZOS)
            avif = os.path.join(OUT, f"{name}-{tw}.avif")
            webp = os.path.join(OUT, f"{name}-{tw}.webp")
            r.save(avif, "AVIF", quality=58, speed=4)
            r.save(webp, "WEBP", quality=80, method=6)
            out.append({"w": tw, "h": th, "avif": os.path.getsize(avif), "webp": os.path.getsize(webp)})
        manifest[name] = {"w": w, "h": h, "sizes": out}
        print(name, w, h, [(o["w"], o["avif"] // 1024, o["webp"] // 1024) for o in out])
    with open(os.path.join(ROOT, "tools", "images.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1)


if __name__ == "__main__":
    main(sys.argv[1])
