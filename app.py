# Importing the flask module for the web application
from flask import Flask, render_template, request
# from core import app
import requests
import json
import os
from pprint import pprint

app = Flask(__name__)

# Create a route function and & render the index.html template
@app.route('/home/')
def home():

    return render_template("home.html")    # Modify this line


@app.route('/sport/')
def sport():

    return render_template("sport.html")    # Modify this line


@app.route('/food/')
def food():

    return render_template("food.html")    # Modify this line


@app.route('/news/')
def news():
    

    # url = "https://newsx.p.rapidapi.com/search"

    # querystring = {"limit":"10","skip":"0"}

    # headers = {
    #     "X-RapidAPI-Key": "b8a7c579d7msh0b3b20bd43f9425p13e905jsneab44a0fe9f8",
    #     "X-RapidAPI-Host": "newsx.p.rapidapi.com"
    # }

    # response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)

    # url = "https://bing-news-search1.p.rapidapi.com/news"
    url = "https://bing-news-search1.p.rapidapi.com/news/trendingtopics"

    querystring = {"safeSearch":"Off","textFormat":"Raw"}

    headers = {
        "X-BingApis-SDK": "true",
        "X-RapidAPI-Key": "b8a7c579d7msh0b3b20bd43f9425p13e905jsneab44a0fe9f8",
        "X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
    }

    # Call the API
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()

        #print("\nHeaders:\n")
       # print(response.headers)

       # print("\nJSON Response:\n")
        #pprint(response.json())
    except Exception as ex:
        raise ex

    out_res = json.loads(response.text)
    # response = requests.request("GET", url, headers=headers, params=querystring)
    #print(response.content)
    # print(out_res["_type"], out_res["value"][0]["webSearchUrl"], out_res["value"][1]["webSearchUrl"])
    # # print(response.text)
    # for key, value in out_res.items():
    #     print("Keff")
    #     print(key, value)

    # user = {"name": out_res["_type"], "w": out_res["value"][0]["webSearchUrl"], "e": out_res["value"][1]["webSearchUrl"]}

    url1 = "https://guardianmikilior1v1.p.rapidapi.com/getSections"

    payload1 = "apiKey=%3CREQUIRED%3E&id=%3CREQUIRED%3E"
    headers1 = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "b8a7c579d7msh0b3b20bd43f9425p13e905jsneab44a0fe9f8",
        "X-RapidAPI-Host": "Guardianmikilior1V1.p.rapidapi.com"
    }

    response = requests.get(url1, data=payload1, headers=headers1)

    print(response.text)

    return render_template("news.html", user="user")    # Modify this line

@app.route('/weather/', methods = ['GET', 'POST'])
def weather():

    api_key = "85e8970dd4b1661788ac2882a82ee2a0"
    city = "Madrid"
    country = "Spain"

    # weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}')

    if request.method == 'POST':

        city = request.form['city']
        country = request.form['country']
        api_key = "85e8970dd4b1661788ac2882a82ee2a0"

        # weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}&q={city},{country}&units=imperial')
        weather_url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric')

        weather_data = weather_url.json()
        print('data', weather_data)

        temp = round(weather_data['main']['temp'])
        humidity = round(weather_data['main']['humidity'])
        wind = round(weather_data['wind']['speed'])

        return render_template("weather_result.html", city=city, country=country, temp=temp, humidity=humidity, wind=wind)    # Modify this line
    
    return render_template("weather.html")

#  flask --app sample --debug run


if __name__ == "__main__":
    app.run(debug=True)