import requests
from pathlib import Path
from helpers import download_img, IMAGES_FOLDER


SPACEX_API_LATEST_LAUNCH = 'https://api.spacexdata.com/v4/launches/latest'


def fetch_spacex_last_launch():
    response = requests.get(SPACEX_API_LATEST_LAUNCH)
    response.raise_for_status()
    images_urls = response.json()['links']['flickr']['original']
    for number, url in enumerate(images_urls, 1):
        filename = f'space{number}'
        download_img(url, filename)


if __name__ == '__main__':
    Path(IMAGES_FOLDER).mkdir(exist_ok=True)
    fetch_spacex_last_launch()
