# ## IMDb User Reviews Scraper
 # Using panda to create our dataframe
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

# ### Retrieve URLs using IMDbPY package
from imdb import IMDb
import pandas as pd

def get_imdb_url(movies):
    ia = IMDb()
    df = pd.read_csv(movies)
    movie_ids = []
    movie_titles = []
    imdb_urls = []
    # Check if the "title" column exists in the DataFrame
    if 'title' in df.columns:
        # Access and print each element in the "title" column
        titles = df['title']
        for movie_title in titles:
            search_results = ia.search_movie(movie_title)
            movieid = search_results[0].movieID
            movie = ia.get_movie(movieid)
            movie_url = ia.get_imdbURL(movie)

            movie_ids.append(movieid)
            movie_titles.append(movie_title)
            imdb_urls.append(movie_url)
        data = {'movie_id': movie_ids,
                'stripped_title': movie_titles,
                'imdb_url': imdb_urls
                }
        # Build dataframe for each movie to export
        movies_data = pd.DataFrame(data)

        # Save URLs in a CSV file
        movies_data.to_csv(f'data/moviesurl.csv')
csv_file_path = r'C:\Users\msthu\PycharmProjects\pythonProject1\semester5\datascience\u.item.csv'  # Replace with the path to your CSV file
get_imdb_url(csv_file_path)
print("!!!Done retrieving links!!!")



