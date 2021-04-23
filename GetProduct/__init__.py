import logging

import azure.functions as func
import requests
from bs4 import BeautifulSoup
from GetProduct.Product import Product


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    url = req.params.get('url')
    if not url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            url = req_body.get('url')

    if url:
        page = BeautifulSoup(requests.get(url).content, 'html.parser')
        page.find('section', class_='related products').decompose()
        title = page.find('h1', class_='product_title entry-title').text
        price_in_discount = True if page.find('span', class_='onsale') is not None else False
        price_element = page.find('p', class_='price')
        original_price = True if price_in_discount else None
        price = price_element.find('span', class_='woocommerce-Price-amount amount').text.replace("€", "") if price_in_discount else price_element.find('span', class_='woocommerce-Price-amount amount').text.replace("€", "")
        in_stock = True if page.find('p', class_='stock').attrs['class'][1] == 'in-stock' else False
        amount_in_stock = int(page.find('p', class_='stock in-stock').text.split(" ")[0]) if in_stock else 0
        product = Product(1, title, price_in_discount, price, original_price, in_stock, amount_in_stock)
        return func.HttpResponse(f"Found the following product information: {product}")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
