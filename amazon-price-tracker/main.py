from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

EMAIL = "*************"
PASSWORD = "**********"

price_list  = 8300

URL = "https://www.amazon.in/Seagate-Portable-External-Hard-Drive/dp/B07DQ3KW45/ref=sr_1_9?crid=1D4EZ9YWWPDIG&dchild=1&keywords=hard+disk+4tb&qid=1630472087&sprefix=hard%2Caps%2C310&sr=8-9"

headers = {
    "accept-language": "en-US,en;q=0.9",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
}

response = requests.get(URL, headers=headers)
contents = response.text

soup = BeautifulSoup(contents, "lxml")
price = soup.find(name="span", id="priceblock_ourprice").getText()
current_price_ = price.split("₹")[1].split(",")
current_price = "".join(current_price_)

if float(current_price) <= LOWEST_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.login(EMAIL, PASSWORD)
        connection.starttls()
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg="Subject: LOW PRICE ALERT ON HARD-DISK\n\n"
                                                                 f"Seagate 4tb hard-disk at a price of {current_price} only.\n"
                                                                 f"BUY NOW!!\n"
                                                                 f"{URL}")
