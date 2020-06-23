import requests
from datetime import datetime
from bs4 import BeautifulSoup

page = requests.get("https://w1.weather.gov/xml/current_obs/KMLU.xml")
#if page.status_code == page.codes.ok:
with open("C:\\Users\\TC\\Desktop\\weather\\KMLU.xml", "w") as xml_write:
    xml_write.write(page.text)
    xml_write.close()
page.close()
#else
 #print("ERROR WITH REQUEST")
	
with open("C:\\Users\\TC\\Desktop\\weather\\KMLU.xml", "r") as read_xml:
    xmldoc = read_xml.read()

soup = 	BeautifulSoup(xmldoc, 'lxml')
now = datetime.now()

observation_time = soup.find("observation_time_rfc822").text
location = soup.find("location").text
temp_f = soup.find("temp_f").text
humidity = soup.find("relative_humidity").text

month = now.strftime("%m/%d/%Y")
hour = now.strftime("%H:%M:%S")
time_string = month + " @ " + hour

html = """<HTML>
Location: {0}<BR />
<!--Condition: Sunny<BR /> -->
Temperature: {1}&deg;F <BR />
Feels Like: N/A<BR />
Dew Point: N/A<BR />
Humidity: {2}%<BR />
Wind: N/A<BR />
Barometer: N/A<BR />
Sunrise: N/A<BR />
Sunset: N/A<BR />
<BR />
<TABLE CELLPADDING='0' CELLSPACING='0'><TR><TD ALIGN='right'>Observed: &nbsp;<br />Downloaded:&nbsp;</TD><TD>{3}
<BR />{4}</TD></TR></TABLE>
</HTML>"""
html_file = html.format(location,temp_f,humidity,observation_time,time_string)
 
with open("C:\\Users\\TC\\Desktop\\weather\\noaa.htm", "w") as htm:
    htm.write(html_file)
    htm.close()
read_xml.close()
 
