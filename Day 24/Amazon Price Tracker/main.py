import smtplib
import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage
import os
import ssl
import re

# ---------------------- Making HTTP request to get Website ---------------------- #

URL = 'https://www.amazon.in/JBL-Cancellation-Playtime-Adjustable-Bluetooth/dp/B09HGR1DVC/ref=sr_1_1?_encoding=UTF8' \
      '&_ref=dlx_gate_sd_dcl_tlt_3e4f589c_dt&content-id=amzn1.sym.a532052b-26f3-4811-a261-3b35ffa57237&m' \
      '=A14CZOWI0VEHLG&pd_rd_r=f41d836f-e328-4401-bac6-3ee323692dd7&pd_rd_w=tWHaw&pd_rd_wg=pyNFb&pf_rd_p=a532052b' \
      '-26f3-4811-a261-3b35ffa57237&pf_rd_r=EMMSCXVSVMJJD4WX7KJ4&qid=1677995682&refinements=p_6%3AA14CZOWI0VEHLG&sr=8' \
      '-1 '

parameters = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US"
}
response = requests.get(url=URL, headers=parameters)
data = response.text

# ---------------------- WebScraping using BeautifulSoup ---------------------- #

soup = BeautifulSoup(data, "html.parser")

# Storing Price
price = soup.find(name="span", class_="a-price-whole")
price_at_first = price.text.strip('.')
price_at_first = re.sub(',', '', price_at_first)
price_at_first = int(float(price_at_first))
print(price_at_first)
print(f'The Price of your item is: Rs. {price_at_first}')
current_price = 1000

# ---------------------- Sending Email Using Python ---------------------- #
if current_price < price_at_first:
    # Specifying email details
    sender = "krossquote2@gmail.com"
    password = os.environ["email_password"]
    receiver = "jkpradeep77@gmail.com"

    subject = "Amazon Price Alert!"
    body = f'''Your item is now worth only {current_price}!'''

    # creating email object
    em = EmailMessage()

    em["From"] = sender
    em["To"] = receiver
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, em.as_string())
