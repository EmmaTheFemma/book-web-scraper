from requests_html import HTMLSession # Documentation: https://requests.readthedocs.io/projects/requests-html/en/latest/
from bs4 import BeautifulSoup


def read_and_clean_txt_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Removing newline characters from each line and filtering out empty strings
            lines = [line.strip() for line in lines if line.strip()]
            return lines
    except FileNotFoundError:
        print("File not found.")


def process_lines(lines):
    processed_lines = []
    for line in lines:
        if "-" in line:
            line = line.split("-")[0].strip()
        elif " by " in line:
            line = line.split(" by ")[0].strip()
        # Remove leading and trailing spaces
        line = line.strip()
        
        line = line.replace(".", "")
        line = line.replace(" ", "+")
        line = line.lower()
        
        # Replace special characters
        # TODO: Same as URL encoder??? Can use a URL encoder.
        line = line.replace("#", "%23")
        line = line.replace("'", "%27")
        line = line.replace(":", "%3A")
        line = line.replace("$", "%24")
        line = line.replace("(", "%28")
        line = line.replace(")", "%29")
        line = line.replace(",", "%2C")
    
        processed_lines.append(line)
    return processed_lines

# https://www.youtube.com/watch?v=0hiGp3lF6ig
# TODO: Maybe just use playwright... Might be easier.
# TODO: Find the link with book name???
# TODO: See if I should use selectolax instead of bs4
def find_url(url):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Referer': 'https://www.google.com', # Where we came from
    'DNT': '1' # Do Not Track
}
    session = HTMLSession()
    r = session.get(url, headers=headers)
    r.html.render(sleep=2, keep_page=True, scrolldown=1)

    links = r.html.find('a', containing='reminiscences of a stock operator') # works but not getting the first and likely "best" result.
    print(links[0])

    print("SEARCH RESULTS:")
    search_results = r.html.find('#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section', first=True)
    print(search_results)

    print("First Search Result: ")
    first_search_result = r.html.find('#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(7) > div > div > span > div > div > div > div.puisg-col.puisg-col-4-of-12.puisg-col-8-of-16.puisg-col-12-of-20.puisg-col-12-of-24.puis-list-col-right > div > div > div.a-section.a-spacing-none.puis-padding-right-small.s-title-instructions-style > h2 > a', first=True)
    print(first_search_result)
    print("Absolute Links")
    print(first_search_result.absolute_links)
    link_to_book = first_search_result.absolute_links.pop()
    print("Book URL: ", link_to_book)


def main():
    print("Running main.")
    data_file = "data.txt"
    amazon_url = "https://www.amazon.com/s?k="
    all_names = read_and_clean_txt_file(data_file)
    all_names_cleaned = process_lines(all_names)
    #print(all_names_cleaned)
    temp_count = 0
    for book in all_names_cleaned:
        if temp_count < 1:
            url = amazon_url + book
            print(url)
            find_url(url)
            temp_count += 1

# Makes so main() only runs in this exact file.
if __name__ == '__main__':
    main()