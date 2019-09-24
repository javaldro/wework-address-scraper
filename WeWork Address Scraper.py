
# coding: utf-8

# In[ ]:


# Importing Packages
import pycurl
from StringIO import StringIO
import json
import csv
import pandas as pd
from tqdm import tqdm
from pandas.io.json import json_normalize
import requests
from bs4 import BeautifulSoup
import time


# In[ ]:


# Getting the HTML from each WeWork Location
url = 'https://www.wework.com/locations'
response = requests.get(url, params={"search_api_views_fulltext": ""})
soup = BeautifulSoup(response.text, "lxml")
#  note: if this link doesn't work, find the new tag by inspecting one of the city links
locations = soup.find_all("a", {"class":"sl_norewrite marketLink__countryList__F4CBD baseLink__countryList__22den weLink-sc-5sbo5g-0 kbLrON"})


# In[ ]:


# Getting Clean Location Link Stubs
link_stub_list = []
for loc in range(0,len(locations)):
    selector = locations[loc] 
    link_stub = selector['href']
    link_stub_list.append(link_stub)


# In[ ]:


coworking_spaces = []
# Iterating Over Each location
for city in tqdm(link_stub_list):
    delay = 0
    # Trying again if call fails, and therefore space is empty
    space = []
    while len(space) < 1 :
        # Creating dynamic link based on link stub
        url = "https://www.wework.com" + city
        response = requests.get(url, params={"search_api_views_fulltext": ""})
        soup = BeautifulSoup(response.text, "lxml")
        # Test to see if location is coming soon 
        coming_soon = soup.find_all("div", {"class":"ray-tag coming-soon_tag"})
        # Break statement to continue on if the location is coming soon
        if len(coming_soon) > 1:
            print(city + " Coming Soon, Skipped")
            break
        # Getting info from each location (if it doesn't work, inspect inspect the coworking space address update)
        space = soup.find_all("div", {"class":"ray-text--body building-card__address"})
        # Adding a delay to avoid timeouts ; this keeps on growing each time the call fails
        delay = delay +.1
        time.sleep(delay)
    # Appending messy location data to a list of jsons
    coworking_spaces.append(space)


# In[ ]:


# Flattening out the nested list
flat_list = [item for sublist in coworking_spaces for item in sublist]
# Creating list to put cleaned strings in
cleaned_full_address_list = []
cleaned_state_list = []
cleaned_zip_list = []
# Cleaning up addresses to extract the full address, state, and zip
for item in range(0,len(flat_list)):
    messy_address = flat_list[item]
    cleaner_address = str(messy_address).split(">")[1]
    cleaned_address = cleaner_address.split("<")[0]
    state = cleaned_address.split(" ")[-2] 
    zipcode = cleaned_address.split(" ")[-1]
    # Trying to avoid adding international locations; this FAILS is a few locations based on string patters that look like USA 
    if len(zipcode)==5 and len(state)== 2:
        cleaned_state_list.append(state)
        cleaned_zip_list.append(zipcode)
    else:
        cleaned_state_list.append("")
        cleaned_zip_list.append("")
    # Appending the full address to the list
    cleaned_full_address_list.append(cleaned_address)


# In[ ]:


# Converting Lists into a dataframe
address_df = pd.DataFrame(list(zip(cleaned_full_address_list, cleaned_state_list, cleaned_zip_list)), columns =['Full Address', 'State', 'Zip'])


# In[ ]:


# Writing CSV to local directory
address_df.to_csv("WeWork Addresses.csv", encoding = 'utf-8')

