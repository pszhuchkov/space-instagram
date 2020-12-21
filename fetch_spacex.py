import requests
import os
import io
from pathlib import Path
from PIL import Image


SPACEX_API_LATEST_LAUNCH = 'https://api.spacexdata.com/v4/launches/latest'
IMAGES_FOLDER = 'images'


def download_img(url, filename):
    """Download an image and save a thumbnail"""
    response = requests.get(url, verify=False)
    response.raise_for_status()
    save_thumbnail_jpg(response.content, filename)


def fetch_spacex_last_launch():
    response = requests.get(SPACEX_API_LATEST_LAUNCH)
    response.raise_for_status()
    images_urls = response.json()['links']['flickr']['original']
    for number, url in enumerate(images_urls, 1):
        filename = f'space{number}'
        download_img(url, filename)


def save_thumbnail_jpg(image_bytes, filename):
    extension = 'jpg'
    size = 1080, 1080
    mode = 'RGB'
    try:
        image = Image.open(io.BytesIO(image_bytes))
        rgb_image = image.convert(mode)
        rgb_image.thumbnail(size)
        rgb_image.save(
            os.path.join(IMAGES_FOLDER, '.'.join((filename, extension)))
        )
    except Exception as e:
        print(e)


if __name__ == '__main__':
    Path(IMAGES_FOLDER).mkdir(exist_ok=True)
    fetch_spacex_last_launch()
