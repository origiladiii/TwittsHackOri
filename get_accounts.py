import requests
from bs4 import BeautifulSoup


def get_twitter_handles(url='https://pressgallery.house.gov/member-data/members-official-twitter-handles'):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check for a valid response
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all text content on the page
        text_content = soup.stripped_strings

        # Filter out those strings that contain the "@" sign indicating a Twitter handle
        # And remove the "@" sign from the handle
        handles = [string.replace("@", "") for string in text_content if "@" in string]
        for handle in handles:
            print(handle)
        return handles
    else:
        print(f'Failed to retrieve the page: {response.status_code}')
        return None


def get_names_from_txt(file_path='names.txt'):

    with open(file_path, 'r') as file:
        names_list = [line.strip() for line in file]

    return names_list


if __name__ == "__main__":
    get_twitter_handles(url='https://en.wikipedia.org/wiki/List_of_most-followed_Twitter_accounts')