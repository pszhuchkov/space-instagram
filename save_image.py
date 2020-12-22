import os
import requests
import io
from PIL import Image, UnidentifiedImageError


def download_img(url, images_folder, filename):
    """Download an image and save a thumbnail"""
    response = requests.get(url, verify=False)
    response.raise_for_status()
    save_thumbnail_jpg(response.content, images_folder, filename)


def save_thumbnail_jpg(image_bytes, images_folder, filename):
    extension = 'jpg'
    size = 1080, 1080
    mode = 'RGB'
    try:
        image = Image.open(io.BytesIO(image_bytes))
        rgb_image = image.convert(mode)
        rgb_image.thumbnail(size)
        rgb_image.save(f'{os.path.join(images_folder, filename)}.{extension}')
    except UnidentifiedImageError as e:
        print(f'{e}. Filename {filename}')
