from requests_html import HTMLSession

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
def find_url(url):
    session = HTMLSession()
    r = session.get(url)
    r.html.render(sleep=1, keep_page=True, scrolldown=1)
    


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
            temp_count += 1

if __name__ == '__main__':
    main()