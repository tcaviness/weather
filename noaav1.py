__author__ = "Terry Caviness"
__version__ = "1.0"
__data__ = "10-25-23"
__copywrite__ = "2022 copywrite"

"""
Author: Terry Caviness
Date: 7-6-22
Version: 2.0
Descripstion: This is a script that get weather data from NOAA from there xml
then rewrites it to a HTML that Zare Radio can read to make broadcasting on radio.
"""
import os
import requests
import cknet as ck
from datetime import datetime
from bs4 import BeautifulSoup as bs
import time
import schedule as sch
import configparser as ini


def config():
    global fullpath
    global htmlpath
    global fullurl
    config = ini.ConfigParser()
    cwd = os.getcwd()
    config.read_file(open(cwd+'\config.ini'))
    file = config["weather_station"]["station_id"]+".xml"
    htmlfile ="tiempo.htm"
    fullpath = os.path.join(cwd, file)
    htmlpath = os.path.join(cwd, htmlfile)
    url = "https://w1.weather.gov/xml/current_obs/"
    fullurl = url+file
    time.sleep(1)


def make_request():
 if ck.checknet() == True:
    page = requests.get(fullurl, timeout=10)        
    with open(fullpath, "w") as xml_write:
        xml_write.write(page.text)
    page.close()
 else:
        raise Exception("no internet connection. Program did not run.")

def html_parse():
        with open(fullpath, "r") as read_xml:
         xml_doc = read_xml.read()
         soup = bs(xml_doc, 'lxml')
         
         now = datetime.now()
         observation_time = soup.find("observation_time_rfc822").text
         location = soup.find("location").text
         temp_f = soup.find("temp_f").text
         humidity = soup.find("relative_humidity").text
         weather = soup.find("weather").text
         wind = soup.find("wind_string").text
         dew = soup.find("dewpoint_f").text
         bar_in = soup.find("pressure_in").text
         try:
             fl = soup.find("heat_index_f").text
         except Exception:
             fl = "N/A"
             pass
         

         month = now.strftime("%m/%d/%Y")
         hour = now.strftime("%I:%M:%S")
         time_string = month + " @ " + hour        

         file = """<HTML>
        Location: {0}<BR />
        Condition: {1}<BR /> 
        Temperature: {2}&deg;F <BR />
        Feels Like: {3}&deg;F<BR />
        Dew Point: {4}&deg;F<BR />
        Humidity: {5}%<BR />
        Wind: {6}<BR />
        Barometer: {7}<BR />
         <BR />
        <TABLE CELLPADDING='0' CELLSPACING='0'><TR><TD ALIGN='right'>Observed: &nbsp;<br />Downloaded:&nbsp;</TD><TD>{8}
         <BR />{9}</TD></TR></TABLE>
        </HTML>"""
        html_file = file.format(location,weather,temp_f,fl,dew,humidity,wind,bar_in,observation_time,time_string)

        with open(htmlpath, "w") as htm:
             htm.write(html_file)
        

             
if __name__ == "__main__":
  config()
  make_request()
  html_parse()
  sch.every().hour.do(make_request)
  sch.every(30).minutes.do(html_parse)
  sch.every(20).minutes.do(config)
  while True:
    sch.run_pending()
    time.sleep(1)
  