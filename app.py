from flask import Flask, render_template, request, redirect
import csv

from service import shortner, save_data

app = Flask(__name__)
db = {}

with open('urls.csv', 'r') as f:
	reader = csv.DictReader(f)
	for c in reader:
		db = c

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template("index.html")

	if request.method == 'POST':
		url = request.form['url']
		if "http" not in url:
			url = "http://" + url
		short_url = shortner(url)
		db[short_url] = url
		save_data(db)
		return render_template('result.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_url(short_url):
	url = db[short_url]
	return redirect(url)
	return redirect("https://www.naver.com")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")