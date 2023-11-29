import requests
import csv

api_key = '5c31050a'  # Replace with your OMDb API key


movies = []

# Example Vietnamese movie titles
vietnamese_movie_titles = ['The Scent of Green Papaya', 'Cyclo', 'The Vertical Ray of the Sun',
                           'I Served the King of England', 'Norwegian Wood', 'The Third Wife', 'The White Silk Dress',
                           'Furie', 'The Rebel', 'The Little Girl of Hanoi', 'The Buffalo Boy', 'Pao\'s Story',
                           'Bi, Don’t Be Afraid', 'Scent of the Lotus', 'Saigon in the Rain', 'Adrift',
                           'The Moon at the Bottom of the Well', 'Fading Light', 'The Sound of the Violin in My Lai',
                           'The Owl and the Sparrow', 'In the Name of Love', 'Farewell, Berlin Wall',
                           'Dust of the Ground', 'The Pearls of the Far East', 'Floating Lives', 'Clash',
                           'The Housemaid', 'Once Upon a Time in Vietnam', 'Yellow Flowers on the Green Grass']

for movie_title in vietnamese_movie_titles:
    url = f'http://www.omdbapi.com/?apikey={"5c31050a"}&t={movie_title}'
    response = requests.get(url)
    data = response.json()

    if data['Response'] == 'True':
        movie_info = {
            'movie_title': data['Title'],
            'year': data['Year'],
            'stripped_title': movie_title.lower().replace(" ", "_")
        }
        movies.append(movie_info)

# Write movie information to CSV
csv_file_path = 'u.item.csv'
fieldnames = ['movie_title', 'year', 'stripped_title']

with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the movie entries
    writer.writerows(movies)

print(f'The CSV file "{csv_file_path}" has been created.')