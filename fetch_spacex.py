import requests
from pathlib import Path
from save_image import download_img
from helpers import get_parsed_arguments
from dotenv import load_dotenv


SPACEX_API_LATEST_LAUNCH = 'https://api.spacexdata.com/v4/launches/latest'


def fetch_spacex_last_launch(images_folder):
    response = requests.get(SPACEX_API_LATEST_LAUNCH)
    response.raise_for_status()
    images_urls = response.json()['links']['flickr']['original']
    for number, url in enumerate(images_urls, 1):
        filename = f'space{number}'
        download_img(url, images_folder, filename)


if __name__ == '__main__':
    load_dotenv()
    args = get_parsed_arguments()
    Path(args.images_folder).mkdir(exist_ok=True)
    fetch_spacex_last_launch(args.images_folder)
