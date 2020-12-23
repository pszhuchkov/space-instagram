import os
from dotenv import load_dotenv
from instabot import Bot
from helpers import get_parsed_arguments


def upload_images(images_folder):
    if os.path.exists(images_folder):
        bot = Bot()
        bot.login(
            username=os.getenv('INSTAGRAM_LOGIN'),
            password=os.getenv('INSTAGRAM_PASSWORD')
        )
        folder_files = os.listdir(images_folder)
        jpg_images = filter(lambda x: x.endswith('.jpg'), folder_files)
        for image in jpg_images:
            filepath = os.path.join(images_folder, image)
            if os.path.isfile(filepath):
                filename = os.path.splitext(image)[0]
                try:
                    bot.upload_photo(filepath, filename)
                finally:
                    try:
                        os.remove(
                            f'{os.path.join(images_folder, image)}.REMOVE_ME'
                        )
                    except FileNotFoundError:
                        os.remove(os.path.join(images_folder, image))
    else:
        print('The directory does not exist')


if __name__ == '__main__':
    load_dotenv()
    args = get_parsed_arguments()
    upload_images(args.images_folder)
