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


global fullpath
global htmlpath
cwd = os.getcwd()
file = "KMLU.xml"
htmlfile ="noaa.htm"
fullpath = os.path.join(cwd, file)
htmlpath = os.path.join(cwd, htmlfile)
time.sleep(1)


def make_request():
 if ck.checknet() == True:
    page = requests.get("https://w1.weather.gov/xml/current_obs/KMLU.xml", timeout=10)        
    with open(fullpath, "w") as xml_write:
        xml_write.write(page.text)
    page.close()
 else:
        print("no internet connection")

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
       #  fl = soup.find("heat_index_f").text
         dew = soup.find("dewpoint_f").text
         bar_in = soup.find("pressure_in").text
         

         month = now.strftime("%m/%d/%Y")
         hour = now.strftime("%H:%M:%S")
         time_string = month + " @ " + hour

         file = """<HTML>
        Location: {0}<BR />
        Condition: {1}<BR /> 
        Temperature: {2}&deg;F <BR />
        Feels Like: N/A&deg;F<BR />
        Dew Point: {3}&deg;F<BR />
        Humidity: {4}%<BR />
        Wind: {5}<BR />
        Barometer: {6}<BR />
         <BR />
        <TABLE CELLPADDING='0' CELLSPACING='0'><TR><TD ALIGN='right'>Observed: &nbsp;<br />Downloaded:&nbsp;</TD><TD>{7}
         <BR />{8}</TD></TR></TABLE>
        </HTML>"""
        html_file = file.format(location,weather,temp_f,dew,humidity,wind,bar_in,observation_time,time_string)

        with open(htmlpath, "w") as htm:
             htm.write(html_file)

             
if __name__ == "__main__":
  
  make_request()
  html_parse()
  

