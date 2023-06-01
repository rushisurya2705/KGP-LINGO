import requests
from bs4 import BeautifulSoup
import json

# url
url="https://wiki.metakgp.org/w/Lingo_of_IIT_Kharagpur"

# Make an HTTP GET request
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Create a dictionary to store the scraped data
all_words_dict={}
all_words_list=[]
for i in soup.find_all("ul"):
    string_=str(i.text)
    if string_[0]!="\n":
        print(string_.split()[0])
        all_words_dict[string_.split()[0]]=str(i.text)
    
all_words_list.append(all_words_dict)

# Write the data to a JSON file
with open('output.json', 'w') as f:
    json.dump(all_words_dict, f, indent=2)
