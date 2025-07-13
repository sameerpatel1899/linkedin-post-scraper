from scraper.scraper import scrape_posts
from utils.exporter import export_to_json, export_to_csv

if __name__ == "__main__":
    keyword = input("Enter keyword or hashtag: ")
    start_date = input("Start date (YYYY-MM-DD): ")
    end_date = input("End date (YYYY-MM-DD): ")
    post_type = input("Post type filter (text, image, video, etc): ")

    data = scrape_posts(keyword, start_date, end_date, post_type)
    export_to_json(data)
    export_to_csv(data)
    print(f"Scraped {len(data)} posts.")
