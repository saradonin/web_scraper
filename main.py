import requests
import schedule
import time
import os
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup
from send_email import send_email

load_dotenv(find_dotenv())

URL = os.environ.get("URL")
prev_list = []


def request_content(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def extract_product_info(content):
    s = content.find('div', class_='listning-boxes container-fluid')
    products = s.find_all('div', class_='product-info row')
    product_list = []

    for item in products:
        name_h2 = item.find('h2', class_='product-name')
        name_a = name_h2.find('a')
        price_1 = item.find('span', class_='price_1')
        price_2 = item.find('span', class_='price_2')

        name_title = name_a.get('title', 'N/A').strip() if name_a else 'N/A'
        name_href = name_a.get('href', 'N/A') if name_a else 'N/A'
        price_1_text = price_1.get_text(strip=True) if price_1 else 'N/A'
        price_2_text = price_2.get_text(strip=True) if price_2 else 'N/A'
        price_text = price_1_text + price_2_text

        product = {
            "name": name_title,
            "link": name_href,
            "price": price_text
        }
        product_list.append(product)

    return product_list


def print_list(list):
    print("Scraping results:")
    for item in list:
        print(f"{item['name']} - {item['price']} PLN\n {item['link']}")


def compare_lists(list_1, list_2):
    return [item for item in list_1 if item not in list_2]


def scrape_and_compare():
    global prev_list
    try:
        content = request_content(URL)
        new_product_list = extract_product_info(content)
        new_products = compare_lists(new_product_list, prev_list)
        print_list(new_products)
        print(new_products)
        prev_list = new_product_list
    except Exception as error:
        print("An error occured", error)


scrape_and_compare()
schedule.every(30).minutes.do(scrape_and_compare)

while True:
    schedule.run_pending()
    time.sleep(1)
