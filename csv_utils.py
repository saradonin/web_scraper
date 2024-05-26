import csv
import os


CSV_FILE = 'prev_product_list.csv'


def load_prev_list():
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    return []


def save_list_to_csv(product_list):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "price", "link"])
        writer.writeheader()
        writer.writerows(product_list)
