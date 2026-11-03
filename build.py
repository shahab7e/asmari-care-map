# Rebuild index.html from the CSV: python build.py [path/to/centers.csv]  (default: data/centers.csv)
import csv, json, re, sys

FA = str.maketrans('0123456789٠١٢٣٤٥٦٧٨٩يك', '۰۱۲۳۴۵۶۷۸۹۰۱۲۳۴۵۶۷۸۹یک')

def clean(s, title=False):
    s = s.translate(FA).strip()
    if title:  # every center is in Tehran, so the «- تهران» / «(تهران)» suffix is just noise
        s = re.sub(r'\s*(?:[-–]\s*تهران|\(\s*تهران\s*\))\s*$', '', s).strip(' -–')
    else:  # addresses: drop the leading «تهران -» for the same reason
        s = re.sub(r'^تهران\s*[-–،,]\s*', '', s)
    return re.sub(r'\s+', ' ', s)

rows = []
for r in csv.DictReader(open(sys.argv[1] if len(sys.argv) > 1 else 'data/centers.csv', encoding='utf-8-sig')):
    try:
        lat, lng = float(r['lat']), float(r['lng'])
    except ValueError:
        continue
    # Tehran city only; bbox also drops rows with broken coordinates
    if r['city'] == 'تهران' and 35.55 < lat < 35.85 and 51.1 < lng < 51.65:
        rows.append({'id': int(r['id']), 'title': clean(r['title'], True), 'type': r['type'], 'phone': r['phone'],
                     'address': clean(r['address']), 'lat': round(lat, 6), 'lng': round(lng, 6)})

# icons.json: service-type SVGs taken from iranassistance.com/medical-centers
icons = open('icons.json', encoding='utf-8').read()
html = (open('template.html', encoding='utf-8').read()
        .replace('/*DATA*/', json.dumps(rows, ensure_ascii=False)).replace('/*ICONS*/', icons))
open('index.html', 'w', encoding='utf-8').write(html)
print(len(rows), 'centers')
