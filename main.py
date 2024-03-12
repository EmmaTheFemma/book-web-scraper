from requests_html import HTMLSession # Documentation: https://requests.readthedocs.io/projects/requests-html/en/latest/
# from bs4 import BeautifulSoup # Maybe I should use selectolax instead of bs4
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
    'Accept-Language': 'en-GB,en;q=0.5',
    'Referer': 'https://www.google.com', # Where we came from
    'DNT': '1' # Do Not Track
}


def only_keep_numbers(input_string):
    # Use a list comprehension to keep only numeric characters
    numbers_only = ''.join(char for char in input_string if char.isdigit())
    return numbers_only


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
def find_url(url):
    print("Starting: find_url()")
    session = HTMLSession()
    r = session.get(url, headers=headers)
    r.html.render(sleep=2, keep_page=True, scrolldown=1)

    #links = r.html.find('a', containing='reminiscences of a stock operator') # works but not getting the first and likely "best" result.
    #print(links[0])

    print("SEARCH RESULTS:")
    search_results = r.html.find('#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section', first=True)
    print(search_results)

    print("First Search Result: ")
    first_search_result = r.html.find('#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(7) > div > div > span > div > div > div > div.puisg-col.puisg-col-4-of-12.puisg-col-8-of-16.puisg-col-12-of-20.puisg-col-12-of-24.puis-list-col-right > div > div > div.a-section.a-spacing-none.puis-padding-right-small.s-title-instructions-style > h2 > a', first=True)
    print(first_search_result)

    print("Image")
    image = r.html.find('#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(7) > div > div > span > div > div > div > div.puisg-col.puisg-col-4-of-12.puisg-col-4-of-16.puisg-col-4-of-20.puisg-col-4-of-24.puis-list-col-left > div > div.s-product-image-container.aok-relative.s-text-center.s-image-overlay-grey.puis-image-overlay-grey.s-padding-left-small.s-padding-right-small.puis-flex-expand-height.puis.puis-v2v5pwx3nl8aar2aoxf0782v1pf > div > span > a > div > img', first=True)
    #image = image[0]

    # TODO: Get the alt text.

    all_images = []
    image_alt = ""
    if image and 'alt' in image.attrs:
        image_alt = image.attrs['alt']
        print("ALT:")
        print(image_alt)
    else:
        print("No 'alt' attribute found in the image element.")

    if image and 'srcset' in image.attrs:
        srcset_values = image.attrs['srcset'].split(',')
        # Extract each URL from the srcset values
        for srcset_value in srcset_values:
            src_url = srcset_value.split()[0]
            print(src_url)
            all_images.append(src_url)
    print(all_images)
    link_to_book = first_search_result.absolute_links.pop()
    print("Book URL: ", link_to_book)

    result = {
        'url': link_to_book,
        'image': all_images[-1],
        'alt': image_alt,
    }

    print("END: find_url()")
    return result


def get_pages(url):
    print("Starting: find_url()")
    session = HTMLSession()
    r = session.get(url, headers=headers)
    r.html.render(sleep=2, keep_page=True, scrolldown=1)

    title_element = r.html.find('#productTitle', first=True)
    title = title_element.text

    author_elements  = r.html.find('span.author.notFaded > a')
    authors = [author.text for author in author_elements ]
    # TODO: Need to format the authors so it looks great! like this: Author name, Author name two.
    # Maybe remove anything that dosen't have (author) next to it?
    print(authors)


    pages = r.html.find('#rpi-attribute-book_details-ebook_pages > div.a-section.a-spacing-none.a-text-center.rpi-attribute-value > span > a > span', first=True)
    print(pages.text)
    only_pages = only_keep_numbers(pages.text)
    #r.html.find('', first=True)
    result = {
        'title': title,
        'authors': authors,
        'pages': only_pages
    }
    return result


def remove_trailing_comma(text):
    # Check if the text ends with a comma
    if text.endswith(','):
        # Remove the trailing comma
        text = text[:-1]
    return text


def main():
    print("Running main.")
    markdown_file = "text.md"
    data_file = "data.txt"
    amazon_url = "https://www.amazon.com/s?k="
    all_names = read_and_clean_txt_file(data_file)
    all_names_cleaned = process_lines(all_names)
    #print(all_names_cleaned)
    temp_count = 0
    markdown_content = "--- ---\n\n"
    for book in all_names_cleaned:
        #if temp_count < 1:
            url = amazon_url + book
            print(url)
            result_one = find_url(url)
            result_two = get_pages(result_one["url"])
            markdown_content += "## " + result_two["title"] + "\n"

            author_formatted = ""
            for author in result_two["authors"]:
                author_formatted += author + ","
            author_formatted = remove_trailing_comma(author_formatted)

            # TODO: Add image

            markdown_content += '<img loading="lazy" src="' + result_one["image"] + '" alt="' + result_one["alt"] + '">\n'
            markdown_content += "- Author: " + author_formatted + "\n"
            markdown_content += "- Pages: " + result_two["pages"] + "\n"
            
            #temp_count += 1
            print(markdown_content)

            with open(markdown_file, 'w') as file: # Write the entire Markdown content to the file
                file.write(markdown_content)

# Makes so main() only runs in this exact file.
if __name__ == '__main__':
    main()