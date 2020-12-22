import argparse
import os


def get_parsed_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-if', '--images_folder', help='Каталог с изображениями',
        default=os.getenv('IMAGES_FOLDER', 'images')
    )
    parser.add_argument(
        '-hc', '--hubble_collection', help='Коллекция Hubble',
        default=os.getenv('HUBBLE_COLLECTION', 'spacecraft')
    )
    return parser.parse_args()
