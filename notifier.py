import datetime #for reading present date
import time
import requests #for retreiving coronavirus data from web
from plyer import notification #for getting notification on your PC

#let there is no data initially
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    #if the data is not fetched due to lack of internet
    print("Please! Check your internet connection")

