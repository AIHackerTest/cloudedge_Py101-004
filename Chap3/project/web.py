# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 19:12:50 2017

@author: think
"""

# import sys
import requests
from requests.exceptions import ConnectionError

from flask import Flask
from flask import render_template
from flask import request
# from flask import url_for

def heweather_query(city):
    weather_url = 'https://free-api.heweather.com/v5/weather'
    payload = {'city': city, 'key': 'a0128998f2944f29974894dc432e74ca'}
    try:
        weather_req = requests.get(weather_url, payload)
        req = weather_req.json()
        # 错误返回值位 {'HeWeather5': [{'status': 'unknown city'}]}
        if req["HeWeather5"][0]["status"] != "ok":
            city_daily_weather = None
            print("未知城市名，请重新输入!")
        else:
            city_daily_weather = {
                    "今日天气":req["HeWeather5"][0]["daily_forecast"][1]["cond"]["txt_d"],
                    "最高温度":req["HeWeather5"][0]["daily_forecast"][1]["tmp"]["max"],
                    "最低温度":req["HeWeather5"][0]["daily_forecast"][1]["tmp"]["min"],
                    "风向":req["HeWeather5"][0]["daily_forecast"][1]["wind"]["dir"],
                    "空气质量":req["HeWeather5"][0]["aqi"]["city"]["qlty"],
                    "PM2.5":req["HeWeather5"][0]["aqi"]["city"]["pm25"]
                    }
    except ConnectionError as e:
        print("网络查询失败！%s" %e)
        city_daily_weather = None
    except KeyError as e:
        print("部分参数查询失败! %s"%e)
        city_daily_weather = None
    return city_daily_weather

app = Flask(__name__)

@app.route('/')
@app.route('/query/')
def web_query():
    webkey = "query"
    city = request.args.get('city', '')
    if city != '':
        city_weather = heweather_query(city)
        if city_weather != None:
            city_history[city] = city_weather
        return render_template("index.html",webkey = webkey,city = city, city_weather = city_weather)
    else:
        return render_template("index.html",webkey = webkey,city = None, city_weather = None)
    
@app.route('/history/',methods=['POST','GET'])
def history():
    webkey = "history"
    print("%s" %(city_history))
    return render_template("index.html",webkey = webkey, city = None, city_weather = None,city_history = city_history,city_help = None)

@app.route('/help/',methods=['POST','GET'])
def web_help():
    webkey = "help"
    print("%s" %(city_help))
    return render_template("index.html", webkey = webkey, city = None, city_weather = None,city_history = city_history,city_help = city_help)


if __name__ == "__main__":
    city_history = {}
    city_help = ""
    app.run()
    
