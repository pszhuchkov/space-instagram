## Космический Инстаграм
### О скриптах
`fetch_spacex.py` - скрипт предназначен для скачивания всех фотографий последнего запуска
космического корабля SpaceX с использованием [API SpaceX](https://github.com/r-spacex/SpaceX-API);  
`fetch_hubble.py` - скрипт предназначен для скачивания всех фотографий указанной коллекции,
которые были получены телескопом Hubble, с использованием [API Hubble](http://hubblesite.org/api/documentation);
`upload_images.py` - скрипт предназначен для загрузки изображений (*.jpg*) из указанной папки в аккаунт социальной
сети Instagram.

### Как установить

1. Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
    ```console
    pip install -r requirements.txt
    ```
2. Для скачивания всех фотографий последнего запуска SpaceX запустить команду:
    ```console
    python fetch_spacex.py
    ```
   По умолчанию фотографии будут размещены в каталоге `images` (при отсутствии будет создан).
3. Для скачивания всех фотографий указанной коллекции, которые были получены телескопом Hubble, 
    запустить команду:
   ```console
    python fetch_hubble.py
    ```
    По умолчанию фотографии будут размещены в каталоге `images` (при отсутствии будет создан). По умолчанию 
    будут скачиваться фотографии из коллекции `spacecraft`. Для выбора другой коллекции 
    требуется в скрипте изменить значение переменной `HUBBLE_COLLECTION`.
4. Для загрузки всех фотографий из каталога `images` в аккаунт социальной сети Instagram:
    * в директории со скриптами создать файл `.env`, и записать в него переменные для доступа в аккаунт
    в следующем формате:
      `IG_LOGIN=<логин в Instagram>`  
      `IG_PASS=<пароль от аккаунта>`
    * запустить команду:
    ```console
    python upload_images.py
    ```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).