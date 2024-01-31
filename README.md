# weather-v2
 Python weather update. 

 Weather script that is made forto pull 
Weather data from NOAA website. It was updated with handling 
no internet connection. The program uses the xml data then parsed the data needed for the other program. I uses a scheduler that runs in the background. 

![Html File Genrated by Program](https://tcaviness.github.io/assessts/img/NOAAParsing.png)

~~~
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
~~~

# Out of Date

ZaraRadio has updated its code that the HTM file is no longer usable. 
  
