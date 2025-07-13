from selenium import webdriver
import time
import pickle
import os

# ✅ Always locate project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
COOKIES_FILE = os.path.join(BASE_DIR, 'cookies.pkl')

def login_and_save_cookies():
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    time.sleep(60)  # Manually login
    cookies = driver.get_cookies()
    with open(COOKIES_FILE, "wb") as f:
        pickle.dump(cookies, f)
    driver.quit()

def load_cookies(driver):
    if not os.path.exists(COOKIES_FILE):
        raise Exception("Cookies not found! Run login_and_save_cookies first.")
    cookies = pickle.load(open(COOKIES_FILE, "rb"))
    driver.get("https://www.linkedin.com")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()




# from selenium import webdriver
# import time
# import pickle
# import os

# # ✅ Always find the cookies path no matter where the script runs from
# BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# COOKIES_PATH = os.path.join(BASE_DIR, 'cookies.pkl')

# def login_and_save_cookies():
#     driver = webdriver.Chrome()
#     driver.get("https://www.linkedin.com/login")
#     time.sleep(60)  # Give user time to login manually
#     cookies = driver.get_cookies()
#     with open(COOKIES_PATH, "wb") as f:
#         pickle.dump(cookies, f)
#     driver.quit()

# def load_cookies(driver):
#     if not os.path.exists(COOKIES_PATH):
#         raise Exception("Cookies not found! Run login_and_save_cookies first.")
#     cookies = pickle.load(open(COOKIES_PATH, "rb"))
#     driver.get("https://www.linkedin.com")
#     for cookie in cookies:
#         driver.add_cookie(cookie)
#     driver.refresh()




# from selenium import webdriver
# import time
# import pickle
# import os

# def login_and_save_cookies():
#     driver = webdriver.Chrome()
#     driver.get("https://www.linkedin.com/login")
#     time.sleep(60)  # Give user time to login manually
#     cookies = driver.get_cookies()
#     with open("cookies.pkl", "wb") as f:
#         pickle.dump(cookies, f)
#     driver.quit()

# def load_cookies(driver):
#     if not os.path.exists("cookies.pkl"):
#         raise Exception("Cookies not found! Run login_and_save_cookies first.")
#     cookies = pickle.load(open("cookies.pkl", "rb"))
#     driver.get("https://www.linkedin.com")
#     for cookie in cookies:
#         driver.add_cookie(cookie)
#     driver.refresh()
