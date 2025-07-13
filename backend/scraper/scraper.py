from selenium import webdriver  # ✅ This was missing
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

from .linkedin_auth import load_cookies


def scrape_posts(keyword, start_date, end_date, post_type_filter):
    driver = webdriver.Chrome()
    load_cookies(driver)

    search_url = f"https://www.linkedin.com/search/results/content/?keywords={keyword}&origin=SWITCH_SEARCH_VERTICAL"
    driver.get(search_url)
    time.sleep(5)

    posts_data = []

    for _ in range(5):  # Scroll a few times
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    post_blocks = driver.find_elements(By.CLASS_NAME, "update-components-text")  # 🧠 This class name might need updating

    for post in post_blocks:
        try:
            content = post.text
            print("POST TEXT:", content)
            posts_data.append({"content": content})
        except:
            continue

    driver.quit()
    return posts_data





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from .linkedin_auth import load_cookies

# def scrape_posts(keyword, start_date, end_date, post_type_filter):
#     driver = webdriver.Chrome()
#     load_cookies(driver)

#     search_url = f"https://www.linkedin.com/search/results/content/?keywords={keyword}&origin=SWITCH_SEARCH_VERTICAL"
#     driver.get(search_url)
#     time.sleep(3)

#     posts_data = []

#     # Scroll and collect
#     for _ in range(10):  # Scroll multiple times
#         posts = driver.find_elements(By.CLASS_NAME, "update-components-actor")  # Update with correct selector
#         for post in posts:
#             try:
#                 # Extract post data here (content, author, likes, etc.)
#                 pass
#             except:
#                 continue
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         time.sleep(2)

#     driver.quit()
#     return posts_data
