# Top Movies Scraper

This Python project scrapes the Top 100 Movies of All Time from an archived version of Empire Online’s website and saves them in a text file.

## Features

- Scrapes movie titles using BeautifulSoup and requests
- Reverses the list so it goes from #1 to #100
- Saves results to a file called "movies.txt"

## Skills Used

- Python
- Web scraping (BeautifulSoup, requests)
- File handling

## How to Run

1. Install the required libraries:
   pip install beautifulsoup4 requests

2. Run the script:
   python movie_scraper.py

## Output

The result will be saved in a file named:
movies.txt

Each line will contain one movie title.

## Source

URL: https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/
