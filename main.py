import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_1_sspa?dchild=1&keywords=macbook+air&qid=1626622192&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFRUElXRDJZSExLN1cmZW5jcnlwdGVkSWQ9QTA2ODI0OTIzQ0VTWTNCNUI5UTNQJmVuY3J5cHRlZEFkSWQ9QTA1MTkzNDlWQ0xJUEo0Nk9DTDcmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice").get_text()
    print(price)

    if price != '₹92,900.00':
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email@email.com', 'password')

    subject = 'price fell down!'
    body = 'check the amazon link https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_1_sspa?dchild=1&keywords=macbook+air&qid=1626622192&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFRUElXRDJZSExLN1cmZW5jcnlwdGVkSWQ9QTA2ODI0OTIzQ0VTWTNCNUI5UTNQJmVuY3J5cHRlZEFkSWQ9QTA1MTkzNDlWQ0xJUEo0Nk9DTDcmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'fromthismail@email.com',
        'tothismail@email.com',
        msg
    )
    print('Email Sent Successfuly!')
    server.quit()

while True:
    check_price()
    time.sleep(60 * 60 * 24)