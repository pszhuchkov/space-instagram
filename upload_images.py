import os
from dotenv import load_dotenv
from instabot import Bot
from save_image import IMAGES_FOLDER


def upload_images(images_folder):
    load_dotenv()
    folder_files = os.listdir(images_folder)
    jpg_images = filter(lambda x: x.endswith('.jpg'), folder_files)
    bot = Bot()
    bot.login(
        username=os.getenv('INSTAGRAM_LOGIN'),
        password=os.getenv('INSTAGRAM_PASSWORD')
    )
    for jpg_image in jpg_images:
        filepath = os.path.join(images_folder, jpg_image)
        if os.path.isfile(filepath):
            filename = os.path.splitext(jpg_image)[0]
            bot.upload_photo(filepath, filename)


if __name__ == '__main__':
    upload_images(IMAGES_FOLDER)
