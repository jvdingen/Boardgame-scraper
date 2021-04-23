import logging

import azure.functions as func
import requests
from bs4 import BeautifulSoup


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        page = BeautifulSoup(requests.get(name).content, 'html.parser')
        page.find('section', class_='related products').decompose()
        title = page.find('h1', class_='product_title entry-title').text
        return func.HttpResponse(f"At {name}, the title is {title}")
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
