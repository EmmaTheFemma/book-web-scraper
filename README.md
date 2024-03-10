# book-web-scraper
To get full name of books, the pages, year, whatever.


## TODO
- Read a txt file, with newline as delimiter.

- Lowercase them, remove all characters (and remove "by author??")
- Create a url "Book Name" = https://www.amazon.com/s?k=book+name  %23=#, %27=', %3=:
- Get the URL from the first result with the exact name "Book Name"
- Go to that URL
- Get full name of book
- Get all authors (Author)
- Get "230 Pages", maybe use regex to find it? Or under "Print length"

- write to a markdown file
- create ## for each book name
- create a "- Author: {AuthorName}"
- create a "- Pages: {AmountOfPages}"
- create a "- Year: {YearOfPublishing}"


## Installations

Create a venv `python -m venv .venv` //Name the folder whatever you want.

Activate it - Win: `source .venv/Scripts/activate` Mac: `source .venv/bin/activate`

### Requirements

`pip freeze > requirements.txt` - Create the requirements.txt
`pip install -r requirements.txt` - Installs it.