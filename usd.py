import requests
from bs4 import BeautifulSoup



USD = 'https://www.google.ru/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&newwindow=1&sca_esv=584039882&sxsrf=AM9HkKmeFID61NaZRTXpT4QqIxkuUXkVmQ%3A1700503345667&source=hp&ei=MZ9bZarBJoG8wPAP-N2B4Ak&iflsig=AO6bgOgAAAAAZVutQVOMSf3zyQYHznlOyHe-GZO_vV6C&ved=0ahUKEwjqnezOlNOCAxUBHhAIHfhuAJwQ4dUDCAo&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&gs_lp=Egdnd3Mtd2l6IgzQtNC-0LvQu9Cw0YAyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEC4YgAQYsQMYgwEyCxAAGIAEGLEDGIMBMg4QABiABBiKBRixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBSPoGUABYowVwAHgAkAEAmAFfoAGRBKoBATa4AQPIAQD4AQHCAhEQLhiABBixAxiDARjHARjRA8ICBRAAGIAEwgIIEAAYgAQYsQPCAgUQLhiABA&sclient=gws-wiz'


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.660 Safari/537.36"
}

def check_current_dollar():
    usd_content = requests.get(USD,headers=headers)

    soup = BeautifulSoup(usd_content.content,'lxml')

    convert = soup.findAll("span",{"class":"DFlfde", "class":"SwHCTb","data-precision":2})
    convert = convert[0].text.strip()
    number = float(convert.replace(",","."))
    return number

