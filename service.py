import hashlib
import csv

def shortner(url, length=8):
	m = hashlib.sha256()
	m.update(url.encode('utf-8'))
	return m.hexdigest()[:length]

def save_data(db):
    with open('urls.csv','w') as f:
        w = csv.writer(f)
        w.writerow(db.keys())
        w.writerow(db.values())