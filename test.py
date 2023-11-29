# ## IMDb User Reviews Scraper

import pandas as pd  # Using panda to create our dataframe
# Import Selenium and its sub libraries
import selenium
from selenium import webdriver
# Import BS4
import requests  # needed to load the page for BS4
from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re
import time
from imdb import IMDb
# ### Retrieve URLs using IMDbPY package
col_names = ['movie_id',
                 'movie_title',
                 'release_date',
                 'video_release_date',
                 'imdb_url',
                 'unknown',
                 'action',
                 'adventure',
                 'animation',
                 'children',
                 'comedy',
                 'crime',
                 'documentary',
                 'drama',
                 'fantasy',
                 'film_noir',
                 'horror',
                 'musical',
                 'mystery',
                 'romance',
                 'sci_fi',
                 'thriller',
                 'war',
                 'western']
movies = pd.read_csv('u.item.csv', sep='|', header=None, names=col_names, encoding='ISO-8859-1')
movies['year'] = movies['movie_title'].astype(str).str.extract('.*\((.*)\).*', expand=False)
movies['stripped_title'] = movies['movie_title'].astype(str).str.replace(r'\s*\(\d+\)$', '')
ia = IMDb()
for index in range(0, len(movies) - 1):
    movie_id = movies['movie_id'][index]
    movie_year = movies['year'][index]
    movie_title = movies['stripped_title'][index]

    # Search for the movie
    search_results = ia.search_movie(movie_title)

print(search_results)
movieid = search_results[0].movieID
print(movieid)
movie = ia.get_movie(movieid)
movie_url = ia.get_imdbURL(movie)
print(movie_url)