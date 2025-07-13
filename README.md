LinkedIn Post Scraper (Python + Selenium + Flask)

A browser automation tool that scrapes detailed posts from LinkedIn based on keyword, date range, and post type. It works both via **command-line (CLI)** and a **web interface (Flask)**.

---

## 🚀 Features

✅ Scrapes LinkedIn posts based on:
- Keyword or hashtag
- Date range (from – to)
- Post type (text, video, image, etc.)

✅ Extracts:
- Full post content (even with "See more")
- Post author, likes, and post date
- Output as CSV and JSON

✅ Works with:
- CLI (terminal)
- Web UI (Flask form)

---

## 🛠️ Tech Stack

- Python 3.x
- Selenium (browser automation)
- Flask (web UI)
- BeautifulSoup (if extended)
- Pandas (for export to CSV)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/linkedin-post-scraper.git
cd linkedin-post-scraper
````

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv env
```

Activate it:

* On Windows:

  ```bash
  .\env\Scripts\activate
  ```
* On Mac/Linux:

  ```bash
  source env/bin/activate
  ```

### 3. Install Required Libraries

```bash
pip install -r backend/requirements.txt
```

---

## 🔐 4. Log into LinkedIn & Save Cookies (One Time)

You must login manually once to authenticate your session.

### Run this:

```bash
cd backend
python
```

Then inside the Python shell:

```python
from scraper.linkedin_auth import login_and_save_cookies
login_and_save_cookies()
```

A Chrome browser will open. **Manually log into LinkedIn**, wait 60 seconds. Cookies will be saved.

Type `exit()` to leave Python.

✅ Done! Now you can scrape without logging in again.

---

## ✅ CLI Mode (Terminal)

```bash
cd backend
python main.py
```

You’ll be asked:

```
Enter keyword or hashtag: hiring
Start date (YYYY-MM-DD): 2024-01-01
End date (YYYY-MM-DD): 2024-12-31
Post type filter (text, image, video, etc): text
```

✅ It will:

* Launch browser
* Scroll through LinkedIn
* Scrape matching posts
* Save to:

  * `output/scraped_posts.csv`
  * `output/scraped_posts.json`

---

## 🌐 Web App Mode (Flask)

To use the UI:

```bash
cd frontend
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

### On the Web Form:

* Enter keyword (e.g., "hiring")
* Pick a start date and end date
* Select post type (text/image/etc.)
* Click **Scrape**

✅ It will:

* Show loading message
* Open browser and scrape
* Display results on screen
* Save files to `/output/` folder

---

## 🧹 Project Structure

```
linkedin-post-scraper/
│
├── backend/
│   ├── scraper/         # Contains LinkedIn scraper and auth
│   ├── utils/           # Export to CSV/JSON
│   ├── main.py          # CLI entry point
│   └── requirements.txt
│
├── frontend/
│   ├── templates/       # HTML form (index.html)
│   └── app.py           # Flask app
│
├── output/              # Scraped data gets saved here
├── cookies.pkl          # Saved LinkedIn session cookies (not in Git)
├── .gitignore
└── README.md
```

---

## ⚠️ Notes

* ❌ Do **not** share or upload `cookies.pkl` to GitHub.
* ⛔ This tool is for **educational/personal use only.**
* 🛑 Scraping LinkedIn may violate their TOS. Use responsibly.

---

## 🙌 Credits

Built with ❤️ by Sameer Patel
sameerpatelgo@gmail.com

Contributions, improvements, and ideas welcome!

```
