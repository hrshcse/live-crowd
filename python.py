import populartimes
import calendar
import datetime
import json
import logging
import math
import re
import ssl
import threading
import urllib.request
import urllib.parse
from flask import Flask,render_template,request,Response,json
app = Flask(__name__)

@app.route('/')
def indexMain():
    return render_template('html.html')

@app.route('/hi' , methods = ['POST'])
def indexDisplay():
    #place_id = "ChIJl_ysnknwqzsR5pNLYrwzMi4"
    place_name= request.form['place_name']
    search_url1="https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input="+place_name+"&inputtype=textquery&fields=place_id,formatted_address,name,rating,opening_hours&key=AIzaSyBmhaUoLlGBmfc_92mRRp5fJUDsHYWosx4"

    resp1 = urllib.request.urlopen(urllib.request.Request(url=search_url1, data=None))
    data1 = resp1.read().decode('utf-8').split('/*""*/')[0]
    #print(type(data1))
    data1 = json.loads(data1)
    place_id=data1["candidates"][0]["place_id"]
    #print(type(data1))
    #for g in data1:
    #    if g =="candidates":
    #        place_id=data1[g]["place_id"]


    api_key = "AIzaSyBmhaUoLlGBmfc_92mRRp5fJUDsHYWosx4"
    jsonData = populartimes.get_id(api_key, place_id)
    monday=[]
    tues=[]
    wed=[]
    thurs=[]
    fri=[]
    sat=[]
    sun=[]
    pop=0.404
    print(type(jsonData))

    for i in jsonData:
        # print(i,jsonData[i])
        if i == "coordinates":
            cordiLatitude = jsonData[i]['lat']
            cordiLongitude = jsonData[i]['lng']
            # print(cordiLatitude,cordiLongitude
        if i == 'populartimes':
            pop = jsonData["current_popularity"]
            for j in jsonData[i]:
                if j['name']=='Monday':
                        monday.append(j['data'])
                if j['name']=='Tuesday':
                        tues.append(j['data'])
                if j['name'] == 'Wednesday':
                    wed.append(j['data'])
                if j['name'] == 'Thursday':
                    thurs.append(j['data'])
                if j['name'] == 'Friday':
                    fri.append(j['data'])
                if j['name'] == 'Saturday':
                    sat.append(j['data'])
                if j['name'] == 'Sunday':
                    sun.append(j['data'])
            # print(populartimesPara,len(populartimesPara))
    return render_template("html.html",monday=json.dumps(monday),wed=json.dumps(wed),pop=json.dumps(pop),thurs=json.dumps(thurs),sun=json.dumps(sun),sat=json.dumps(sat),fri=json.dumps(fri),cordiLatitude = json.dumps(cordiLatitude),cordiLongitude=json.dumps(cordiLongitude),tues=json.dumps(tues))

if __name__ == '__main__':
   app.run(debug=True)