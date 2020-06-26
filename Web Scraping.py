# Web Scraping Project
# From Website Booking.com
 Input:
 
 import requests
from bs4 import BeautifulSoup
import argparse
import sqlite3

def database(name):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("CREATE TABLE Hotel(hotel_Name TEXT, hotel_Address TEXT, hotel_Review TEXT, hotel_Price REAL)")
    conn.close()

def upload(info,name):
    conn = sqlite3.connect(name)
    cur = conn.cursor()
    cur.execute("INSERT INTO Hotel Rooms(?,?,?,?)",info)
    conn.commit()
    conn.close()
    
name = 'Hotel3.db'

#database(name)

hotels_url = "https://www.booking.com/searchresults.html?aid=397594&label=gog235jc-1DCAEoggI46AdIM1gDaGyIAQGYATG4ARfIAQzYAQPoAQH4AQKIAgGoAgO4AqD_1vcFwAIB0gIkNTdmZGFhMDEtMGQ0ZC00NWVkLTk1MWYtNGQxNWEyN2MwM2Fh2AIE4AIB&sid=4e3f059fe942f9dc9e4ae9e31f4a7cd5&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Faid%3D397594%3Blabel%3Dgog235jc-1DCAEoggI46AdIM1gDaGyIAQGYATG4ARfIAQzYAQPoAQH4AQKIAgGoAgO4AqD_1vcFwAIB0gIkNTdmZGFhMDEtMGQ0ZC00NWVkLTk1MWYtNGQxNWEyN2MwM2Fh2AIE4AIB%3Bsid%3D4e3f059fe942f9dc9e4ae9e31f4a7cd5%3Bsb_price_type%3Dtotal%26%3B&ss=Hotel+Charring+Cross%2C+Ooty%2C+Garden+Road%2C+Pudumund%2C+Ooty%2C+Tamil+Nadu%2C+India&is_ski_area=&checkin_year=2020&checkin_month=6&checkin_monthday=30&checkout_year=2020&checkout_month=7&checkout_monthday=3&group_adults=2&group_children=0&no_rooms=1&map=1&b_h4u_keep_filters=&from_sf=1&ss_raw=ooty+chering+cross&ac_position=1&ac_click_type=g&dest_id=ChIJ01BuhZK9qDsRktrTYcXsBKs&dest_type=landmark&place_id=ChIJ01BuhZK9qDsRktrTYcXsBKs&place_id_lat=11.4129659&place_id_lon=76.7084544&place_types=lodging%2Cpoint_of_interest%2Cestablishment&search_pageview_id=e0504290d1ce00ec&search_selected=true#map_closed/"

url = requests.get(hotels_url)

Soup = BeautifulSoup(url.content,"html.parser")
all_hotels = Soup.find_all("div", {"class":"sr_item_content sr_item_content_slider_wrapper"})
print(all_hotels)
for hotel in all_hotels:
    hotel = {}
    hotel["name"] = hotel.find("h3", {"class":"sr-hotel__name"}).text
    hotel["address"] = hotel.find("span",{"data-bui-component":"streetAdress"}).text
    try:
        hotel["review"] = hotel.find("span", {"class":"sr-review-score"}).text
    except:
        AttributeError
    hotel["price"] = hotel.find("span", {"class":"bui-price-display"}).text

    info = tuple(hotel.values())
    upload (info,name)

conn  = sqlite3.connect (name)
mac = conn.cursor ()
z = mac.execute ("SELECT * FROM Hotel")

for c in z :
    print (c)

conn.commit ()
conn.close ()

