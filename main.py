import requests
import os
from dotenv import load_dotenv, find_dotenv
from bs4 import BeautifulSoup
from send_email import send_email
from csv_utils import load_prev_list, save_list_to_csv

load_dotenv(find_dotenv())

URL = os.environ.get("URL")


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
            "price": price_text,
            "link": name_href
        }
        product_list.append(product)

    return product_list


def scrape_and_compare(prev_list):
    try:
        content = request_content(URL)
        product_list = extract_product_info(content)
        print("Scraped successfully!")

        exclude_words = ["alhambra", "armaf", "paris corner", "zimaya"]
        new_products = [item for item in product_list if item not in prev_list
                        and not any(word in item['name'].lower() for word in exclude_words)]

        if new_products:
            send_email(new_products)
            save_list_to_csv(product_list)
        else:
            print("Nothing new.")

    except Exception as error:
        print("An error occured: ", error)


def main():
    prev_list = load_prev_list()
    scrape_and_compare(prev_list)


if __name__ == "__main__":
    main()
