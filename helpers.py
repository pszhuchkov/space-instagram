import os
import requests
import io
from PIL import Image


IMAGES_FOLDER = 'images'


def download_img(url, filename):
    """Download an image and save a thumbnail"""
    response = requests.get(url, verify=False)
    response.raise_for_status()
    save_thumbnail_jpg(response.content, filename)


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
