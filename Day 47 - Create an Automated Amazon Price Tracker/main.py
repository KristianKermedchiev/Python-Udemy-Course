from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://appbrewery.github.io/instant_pot/'

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, 'html.parser')
price = float(soup.find(class_="a-offscreen").get_text()[1::])

# ====================== Send an Email ===========================

# Get the product title
title = soup.find(id="productTitle").get_text().strip()

# Set the price below which you would like to get a notification
BUY_PRICE = 70

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    # ====================== Use environment variables ===========================

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )