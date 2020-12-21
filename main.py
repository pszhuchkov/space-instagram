import requests
import os
from pathlib import Path
from urllib.parse import urlparse


SPACEX_API_LATEST_LAUNCH = 'https://api.spacexdata.com/v4/launches/latest'
HUBBLE_API_GET_IMAGE = 'http://hubblesite.org/api/v3/image/{}'
HUBBLE_API_GET_IMAGES = 'http://hubblesite.org/api/v3/images'
HUBBLE_COLLECTION = 'spacecraft'
IMAGES_FOLDER = 'images'


def download_img(url, filename):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(os.path.join(IMAGES_FOLDER, filename), 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    response = requests.get(SPACEX_API_LATEST_LAUNCH)
    response.raise_for_status()
    images_urls = response.json()['links']['flickr']['original']
    for number, url in enumerate(images_urls, 1):
        extension = get_extension(url)
        filename = f'space{number}.{extension}'
        download_img(url, filename)


def fetch_hubble_images(image_id):
    response = requests.get(HUBBLE_API_GET_IMAGE.format(image_id))
    response.raise_for_status()
    image_files = response.json()['image_files']
    best_image = image_files[-1]
    scheme = urlparse(HUBBLE_API_GET_IMAGE).scheme
    best_image_url = f"{scheme}:{best_image['file_url']}"
    extension = get_extension(best_image_url)
    filename = f"{image_id}.{extension}"
    download_img(best_image_url, filename)


def fetch_hubble_collection(collection_name):
    params = {'page': 'all', 'collection_name': collection_name}
    response = requests.get(HUBBLE_API_GET_IMAGES, params=params)
    response.raise_for_status()
    collection_images = response.json()
    for image in collection_images:
        image_id = image['id']
        fetch_hubble_images(image_id)
        print(f"{image_id} обработано")


def get_extension(url):
    extension = url.split('.')[-1]
    return extension


if __name__ == '__main__':
    Path(IMAGES_FOLDER).mkdir(exist_ok=True)
    fetch_spacex_last_launch()
    fetch_hubble_collection(HUBBLE_COLLECTION)

