from flask import Flask,render_template 
#pip install Flask
from bs4 import BeautifulSoup  #pip install bs4
import requests  #pip install requests

app = Flask(__name__) #initiate flask app
@app.route('/', methods=['GET', 'POST']) #route for the home page
def index():

    url = "https://www.businesstoday.in/technology/news"
    req = requests.get(url)
    soup = BeautifulSoup(req.text,'html.parser')
    # print(soup.prettify())
    # print(soup.find_all("div", class_="widget-listing", limit=6))
    outerdata = soup.find_all("div", class_="widget-listing", limit=7)

    finalNews = ""

    for data in outerdata:
        news = data.div.div.a["title"]
        finalNews += "\u2022 " + news + "\n"

    return render_template("index.html", News=finalNews)


