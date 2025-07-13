import sys
import os

# Add backend folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))


from flask import Flask, render_template, request
from scraper.scraper import scrape_posts
from utils.exporter import export_to_csv, export_to_json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
        if request.method == "POST":
            try:
                print("Scraping started...")
                keyword = request.form["keyword"]
                start_date = request.form["start_date"]
                end_date = request.form["end_date"]
                post_type = request.form["post_type"]

                data = scrape_posts(keyword, start_date, end_date, post_type)

                print("Scraping finished. Posts found:", len(data))
                export_to_csv(data)
                export_to_json(data)

                return render_template("index.html", data=data)

            except Exception as e:
                print("🔥 Error occurred:", str(e))
                return render_template("index.html", error=str(e))

        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
