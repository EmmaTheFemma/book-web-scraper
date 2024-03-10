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

## Test
<h2 class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"><a class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal" href="/Reminiscences-Stock-Operator-Edwin-Lefevre-ebook/dp/B09YRCNQHB/ref=sr_1_1?dib=eyJ2IjoiMSJ9.3Xne0AqbS3q-ts7l_NTGuIlGGgNWHmeXHzSfVz0TMW4FbRoS9_TRTqsOVIPi4Hx7Fy5NL4LD0hwX959wLaoNFv_7DS3O47_EqDKmi-LHiTlpoS0ww4zWN8VxHLkMzOCbX4peMimnk6Yo5wPAvLgTlPqso7R6_AHGkk8CeO37V45Jr2a3ap64G1ke_kUdOr9g4-5vmuk-1MysCPuv-6MrOnSzv0ydu8lLUrAKb6LhSi8.36qtYZMPmWCIXm7dwNuVLlMCfHoG6meRnrPbh1Iy2S8&amp;dib_tag=se&amp;keywords=reminiscences+of+a+stock+operator&amp;qid=1710087131&amp;sr=8-1"><span class="a-size-medium a-color-base a-text-normal">Reminiscences of a Stock Operator</span> </a> </h2>

## Installations

Create a venv `python -m venv .venv` //Name the folder whatever you want.

Activate it - Win: `source .venv/Scripts/activate` Mac: `source .venv/bin/activate`

### Requirements

`pip freeze > requirements.txt` - Create the requirements.txt
`pip install -r requirements.txt` - Installs it.