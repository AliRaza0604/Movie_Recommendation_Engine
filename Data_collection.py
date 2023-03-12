import csv
import requests

# Add your API key here
API_KEY = '451462f77232d087fe0723ebb4ffd55b'

# Define the base URL for the API requests
BASE_URL = f'https://api.themoviedb.org/3'

# Define the endpoint for retrieving popular movies
POPULAR_MOVIES_ENDPOINT = f'{BASE_URL}/movie/popular'

# Define the parameters for the API request
params = {
    'api_key': API_KEY,
    'language': 'en-US',
    'page': 1
}

# Send the API request
response = requests.get(POPULAR_MOVIES_ENDPOINT, params=params)

# Parse the JSON response
data = response.json()

# Extract the movie data from the JSON response
movies = data['results']

# Open a CSV file for writing
with open('dataset/movies.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Title', 'Release Date', 'Synopsis',
                    'Poster Image', 'Rating'])

    # Write the movie data to the CSV file
    for movie in movies:
        title = movie['title']
        release_date = movie['release_date']
        synopsis = movie['overview']
        poster_image = movie['poster_path']
        rating = movie['vote_average']

        writer.writerow([title, release_date, synopsis, poster_image, rating])

print('Done!')
