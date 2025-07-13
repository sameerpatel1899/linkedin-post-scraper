import json
import pandas as pd
import os

# ✅ Always get the full path to the output folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Create the folder if not exists

def export_to_json(data, filename="scraped_posts.json"):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def export_to_csv(data, filename="scraped_posts.csv"):
    filepath = os.path.join(OUTPUT_DIR, filename)
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)




# import json
# import pandas as pd

# def export_to_json(data, filename="output/scraped_posts.json"):
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)

# def export_to_csv(data, filename="output/scraped_posts.csv"):
#     df = pd.DataFrame(data)
#     df.to_csv(filename, index=False)
