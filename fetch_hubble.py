import requests
from pathlib import Path
from urllib.parse import urlparse
from save_image import download_img
from helpers import get_parsed_arguments
from dotenv import load_dotenv


HUBBLE_API_GET_IMAGE = 'http://hubblesite.org/api/v3/image/{}'
HUBBLE_API_GET_IMAGES = 'http://hubblesite.org/api/v3/images'


def fetch_hubble_image(images_folder, image_id):
    response = requests.get(HUBBLE_API_GET_IMAGE.format(image_id))
    response.raise_for_status()
    image_files = response.json()['image_files']
    best_image = image_files[-1]
    scheme = urlparse(HUBBLE_API_GET_IMAGE).scheme
    best_image_url = f"{scheme}:{best_image['file_url']}"
    download_img(best_image_url, images_folder, image_id)


def fetch_hubble_collection(collection_name, images_folder):
    params = {'page': 'all', 'collection_name': collection_name}
    response = requests.get(HUBBLE_API_GET_IMAGES, params=params)
    response.raise_for_status()
    collection_images = response.json()
    for image in collection_images:
        image_id = image['id']
        fetch_hubble_image(images_folder, image_id)


if __name__ == '__main__':
    load_dotenv()
    args = get_parsed_arguments()
    Path(args.images_folder).mkdir(exist_ok=True)
    fetch_hubble_collection(
        args.hubble_collection, args.images_folder
    )
