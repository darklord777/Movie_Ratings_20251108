import csv
import random

# Configuration
num_rows = 10000
genres = ['action', 'comedy', 'drama', 'romance', 'horror', 'sci-fi', 'thriller', 'animation']
years = list(range(1990, 2025))

# Open CSV file for writing
with open('movies.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Genre', 'Year', 'Rating', 'BoxOffice'])
    
    for i in range(1, num_rows + 1):
        title = f'movie{i}'
        genre = random.choice(genres)
        year = random.choice(years)
        rating = round(random.uniform(1.0, 5.0), 1)  # Ratings between 1.0 and 5.0
        box_office = random.randint(5000, 200000)     # Box office in thousands
        writer.writerow([title, genre, year, rating, box_office])

print(f'{num_rows} rows of random movie data written to movies.csv')
