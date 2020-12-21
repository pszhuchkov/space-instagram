import requests
import os
import io
from pathlib import Path
from urllib.parse import urlparse
from PIL import Image


HUBBLE_API_GET_IMAGE = 'http://hubblesite.org/api/v3/image/{}'
HUBBLE_API_GET_IMAGES = 'http://hubblesite.org/api/v3/images'
HUBBLE_COLLECTION = 'spacecraft'
IMAGES_FOLDER = 'images'


def download_img(url, filename):
    """Download an image and save a thumbnail"""
    response = requests.get(url, verify=False)
    response.raise_for_status()
    save_thumbnail_jpg(response.content, filename)


def fetch_hubble_image(image_id):
    response = requests.get(HUBBLE_API_GET_IMAGE.format(image_id))
    response.raise_for_status()
    image_files = response.json()['image_files']
    best_image = image_files[-1]
    scheme = urlparse(HUBBLE_API_GET_IMAGE).scheme
    best_image_url = f"{scheme}:{best_image['file_url']}"
    filename = f"{image_id}"
    download_img(best_image_url, filename)


def fetch_hubble_collection(collection_name):
    params = {'page': 'all', 'collection_name': collection_name}
    response = requests.get(HUBBLE_API_GET_IMAGES, params=params)
    response.raise_for_status()
    collection_images = response.json()
    for image in collection_images:
        image_id = image['id']
        fetch_hubble_image(image_id)


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
    fetch_hubble_collection(HUBBLE_COLLECTION)
