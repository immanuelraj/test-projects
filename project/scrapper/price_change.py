import requests
from bs4 import BeautifulSoup
import smtplib
import time


def check_price():
    URL = 'https://www.flipkart.com/samsung-6-2-kg-monsoon-feature-fully-automatic-top-load-grey/p/itmewa2xkfkeq9cz?pid=WMNEWA2XKFSHQZZG&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_8_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_8_na_na_pr&lid=LSTWMNEWA2XKFSHQZZGDYJV2I&fm=SEARCH&iid=en_sKWwZMaFqF4X4oss1Ch3xnjHNHpXBYjXt0wcCWE0rvgu8BbRgR2Hww2I5RN5rf3209ry0kNEJYAzNmHUxYXcYA%3D%3D&ppt=sp&ppn=sp&ssid=y5v0kkov5c0000001574512841523&qH=bcadf718d561cab9'
    headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(attrs="_1vC4OE _3qQ9m1").get_text()
    cancerted_price = float(price[1:7].replace(',',''))
    if cancerted_price < 12000:
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    print "hi"
    server.login('immanuel@wwstay.com', 'fmocsvbjdjyqbskn')
    subject = 'Price has changed'
    body = 'Check the link for more: https://www.flipkart.com/samsung-6-2-kg-monsoon-feature-fully-automatic-top-load-grey/p/itmewa2xkfkeq9cz?pid=WMNEWA2XKFSHQZZG&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_8_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_8_na_na_pr&lid=LSTWMNEWA2XKFSHQZZGDYJV2I&fm=SEARCH&iid=en_sKWwZMaFqF4X4oss1Ch3xnjHNHpXBYjXt0wcCWE0rvgu8BbRgR2Hww2I5RN5rf3209ry0kNEJYAzNmHUxYXcYA%3D%3D&ppt=sp&ppn=sp&ssid=y5v0kkov5c0000001574512841523&qH=bcadf718d561cab9'
    msg ='Subject: {}\n\n{}'.format(subject, body)
    server.sendmail('immanuel@wwstay.com','immanuel@wwstay.com',msg)
    print "Mail has been sent"
    server.quit()

while(True):
    check_price()
    time.sleep(86400)