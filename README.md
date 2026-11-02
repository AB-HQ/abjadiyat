# أبجديات

مبادرة لتعزيز مهارات القراءة والنطق — مدرسة الحمرية (الحلقة الثانية والثالثة، بنين).

الموقع: https://ab-hq.github.io/abjadiyat/

## Layout
- `index.html` — the built, deployed page (GitHub Pages serves it as is).
- `src/src.html` — the source. Edit this, then run `python3 src/build.py` to rebuild `index.html`.
  The build re-embeds the logo (`src/logo.b64`) and the recorded audio already inside `index.html`.
- `firestore.rules` — the Firestore security rules. They are published from the Firebase console
  (Firestore → Rules); keep this file in sync with what is published.
