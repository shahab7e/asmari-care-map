# Asmari Care Map

**مراکز طرف قرارداد با آسماری** — نقشه و فهرست مراکز درمانی طرف قرارداد در شهر تهران.

🔗 **https://shahab7e.github.io/asmari-care-map/**

- فیلتر بر اساس نوع خدمت (دندان‌پزشکی، آزمایشگاه، تصویربرداری، …)
- جستجو در نام، خیابان و محله
- «نزدیک من» و مرتب‌سازی بر اساس فاصله
- مسیریابی با برنامه‌ی مسیریاب گوشی، تماس، و اشتراک‌گذاری لینک هر مرکز

> این یک پروژه‌ی شخصی و غیررسمی است. پیش از مراجعه، قرارداد و ساعت کاری مرکز را تلفنی بپرسید.

## How it works

A single static page (`index.html`) with the data embedded — no server, no build tooling beyond Python.

| File | Purpose |
|------|---------|
| `template.html` | The app (Leaflet map + UI). Edit this, not `index.html`. |
| `data/centers.csv` | Source list of centers with coordinates |
| `icons.json` | Service-type icons |
| `build.py` | Cleans the CSV (Tehran only, Persian digits, de-duplicated city names) and writes `index.html` |

```bash
python build.py            # uses data/centers.csv
```

Map tiles: OpenStreetMap. To use Neshan maps instead, put a Neshan web key in `NESHAN_KEY` at the top of `template.html` and rebuild.
