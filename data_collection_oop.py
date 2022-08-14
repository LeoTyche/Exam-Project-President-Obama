#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[3]:


class fetch:
    def __init__(self):
        return
    
    ## define the function to extract the speech content
    def extract_text(url):
        headers = {
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
        }
        resp = requests.get(url, headers=headers)
        s = BeautifulSoup(resp.text, "html.parser")
        title = s.title
        text = s.get_text(strip=True)
        return title, text
    
    ## define the function to extract the title of speech
    def title(title):
        title = str(title)
        title = title[title.find("Obama -") + len("Obama -"):title.find("</title>")]
        title = title[:title.find("(transcript-audio-video)")]
        title = title[:title.find("(text-audio-video)")].strip()
        return title

    ## define the function to delete something like cd, pdf ...
    def delet(speech):
        delet = speech[speech.find("transcribed directly from audio]")
                         + len("transcribed directly from audio]"):speech.find(
            "Book/CDs by Michael E. Eidenmuller,")].strip()
        return delet

