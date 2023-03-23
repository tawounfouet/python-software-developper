

import requests
from bs4 import BeautifulSoup

import time
import csv
import pandas as pd


def book_details(single_book_url,  parser = "lxml"):
    """
    Collect book details from the given book url
       
    single_book_url:
    parser : default parser
    """
    res = requests.get(single_book_url, parser)
    res.encoding = "utf-8"
    
    html_text = res.text
    soup = BeautifulSoup(html_text)
    
    book_availability = soup.find_all("table", class_="table table-striped")[0].findAll('tr')[5].td.text
    book_rating = soup.find_all("div", class_="col-sm-6 product_main")[0].findAll('p')[2].get('class')[1]
    book_upc = soup.find_all("table", class_="table table-striped")[0].findAll('tr')[0].td.text
    book_category = soup.find_all("ul", class_="breadcrumb")[0].findAll('a')[2].text
    book_title = soup.find_all("div", class_="col-sm-6 product_main")[0].h1.text
    book_price = soup.find_all("div", class_="col-sm-6 product_main")[0].p.text.lstrip("Â")
    book_desc = soup.find_all("p")[3].text
    book_img_link =  soup.find_all("div", class_="item active")[0].img['src']
    full_book_img_link = "http://books.toscrape.com/" + book_img_link.lstrip("../../../")
        

    book_infos = {
        'book_upc': book_upc,
        'book_category': book_category,
        "book_title": str(book_title),
        "book_price": book_price,
        "book_rating": book_rating,
        'book_availability': book_availability,
        "book_description": str(book_desc),
        "book_img_link": full_book_img_link,
    }
    
    return book_infos

    