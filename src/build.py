"""Build index.html from src.html.

The recorded audio (about 5 MB of base64 mp3) is not duplicated in src/; it is
read back from the current index.html and re-embedded, so the repo stays the
single source of truth.  Run from anywhere:  python3 src/build.py
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "index.html")
HEAD = ('<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>')

src = open(os.path.join(HERE, "src.html"), encoding="utf8").read()
logo = open(os.path.join(HERE, "logo.b64"), encoding="utf8").read().strip()
old = open(OUT, encoding="utf8").read()
m = re.search(r'<script type="application/json" id="audioData">(.*?)</script>', old, re.S)
if not m or len(m.group(1)) < 1000:
    raise SystemExit("could not find the embedded audio in index.html")

page = src.replace("__LOGO__", logo).replace("__AUDIO__", m.group(1))
open(OUT, "w", encoding="utf8").write(HEAD + page + "</body></html>")
print("index.html", round(len(HEAD + page) / 1e6, 2), "MB")
