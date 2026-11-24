# andikimran.com

Static website for Andik Imran, PropNex property consultant. Hosted on Vercel.

## Edit the site
All words live in `source/content.py`, `source/content_extra.py` and `source/content_estates.py`.
Loan rules live at the top of `source/calc.js`.

Rebuild after editing:

```
cd source
python3 build.py prod
```

This regenerates the HTML at the repo root. Commit and push; Vercel redeploys automatically.
