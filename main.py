import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

user_data_dir = "C:/Users/gyuri/AppData/Local/Google/Chrome/User Data"

chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_id = "bigCookie"
cookies_id = "cookies"
product_prefix = "product"
product_price_prefix = "productPrice"
products_selector = "#products .product"
upgradeable_selector = ".crate.upgrade.enabled"


cookie = driver.find_element(By.ID, cookie_id)

while not driver.find_element(By.ID, cookies_id).text.__contains__("million"):
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text

    match = re.search(r'[\d,]+', cookies_count)
    cookies_count = int(match.group(0).replace(',', ''))

    try:
        upgrade = driver.find_element(By.CSS_SELECTOR, upgradeable_selector)
        upgrade.click()
    except Exception as e:
        pass

    for i in range(len(driver.find_elements(By.CSS_SELECTOR, products_selector))):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
        if not product_price.isdigit():
            continue

        product_price = int(product_price)
        if cookies_count >= product_price:
            prouct = driver.find_element(By.ID, product_prefix + str(i))
            prouct.click()
            break

driver.quit()
