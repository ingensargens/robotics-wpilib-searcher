import webbrowser
import requests
from requests_html import HTMLSession
url = 'https://docs.wpilib.org/en/stable/index.html'
base = 'https://docs.wpilib.org/en/stable/docs'
close = '/index.html'
try:
    session = HTMLSession()
    response = session.get(url)
     
except requests.exceptions.RequestException as e:
    print(e)


links = response.html.absolute_links


h = str(input("first: "))
k = str(input('second: '))
link = [base, h, k, close]
oeda = ('/').join(link)
try:
    webbrowser.open(oeda)
    print("success: " + oeda)
except:
    quit