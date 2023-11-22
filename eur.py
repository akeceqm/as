import requests
from bs4 import BeautifulSoup
import time


EUR = 'https://www.google.ru/search?q=%D0%B5%D0%B2%D1%80%D0%BE&newwindow=1&sca_esv=584039882&sxsrf=AM9HkKnOkMeP-Wsu5XF9vJzeij8I8BBRHA%3A1700504846380&ei=DqVbZYPkFoynwPAPjIms4Ag&ved=0ahUKEwiDo7qamtOCAxWMExAIHYwEC4wQ4dUDCBA&uact=5&oq=%D0%B5%D0%B2%D1%80%D0%BE&gs_lp=Egxnd3Mtd2l6LXNlcnAiCNC10LLRgNC-MgoQIxiABBiKBRgnMg0QABiABBiKBRixAxhDMg0QABiABBgUGIcCGLEDMgoQABiABBiKBRhDMgoQABiABBiKBRhDMgoQABiABBiKBRhDMgoQABiABBiKBRhDMhEQLhiABBixAxiDARjHARjRAzIKEAAYgAQYigUYQzIKEAAYgAQYigUYQ0ipBVAAWLkDcAB4AZABAJgBXaAB6gKqAQE0uAEDyAEA-AEBwgILEAAYgAQYsQMYgwHCAgUQABiABMICDhAAGIAEGIoFGLEDGIMBwgIIEAAYgAQYsQPiAwQYACBBiAYB&sclient=gws-wiz-serp'


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.660 Safari/537.36"
}

def check_current_euro():
    global balance
    usd_content = requests.get(EUR,headers=headers)
    soup = BeautifulSoup(usd_content.content,'lxml')
    convert = soup.findAll("span",{"class":"DFlfde", "class":"SwHCTb","data-precision":2})
    convert = convert[0].text.strip()
    number = float(convert.replace(",","."))
    return number
