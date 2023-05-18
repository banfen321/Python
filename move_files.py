import os
import shutil

# Путь к папке Downloads
downloads_folder = os.path.join(os.environ["HOME"], "Downloads")



# Словарь с соответствиями расширений и папок назначения
extensions = {
    "txt": os.path.join(os.environ["HOME"], "Documents"),
    "pdf": os.path.join(os.environ["HOME"], "Documents"),

    "odt": os.path.join(os.environ["HOME"], "Documents","Office"),
    "ods": os.path.join(os.environ["HOME"], "Documents","Office"),
    "odp": os.path.join(os.environ["HOME"], "Documents","Office"),
    "odg": os.path.join(os.environ["HOME"], "Documents","Office"),
    "odb": os.path.join(os.environ["HOME"], "Documents","Office"),
    "odf": os.path.join(os.environ["HOME"], "Documents","Office"),
    "doc": os.path.join(os.environ["HOME"], "Documents","Office"),
    "docx": os.path.join(os.environ["HOME"], "Documents","Office"),
    "xlsx": os.path.join(os.environ["HOME"], "Documents","Office"),
    "pptx": os.path.join(os.environ["HOME"], "Documents","Office"),
    "accdb": os.path.join(os.environ["HOME"], "Documents","Office"),

    "fb2": os.path.join(os.environ["HOME"], "Documents","Books"),
    "epub": os.path.join(os.environ["HOME"], "Documents","Books"),
    "mobi": os.path.join(os.environ["HOME"], "Documents","Books"),
    "azw": os.path.join(os.environ["HOME"], "Documents","Books"),
    "djvu": os.path.join(os.environ["HOME"], "Documents","Books"),

    "jpg": os.path.join(os.environ["HOME"], "Pictures"),
    "jpeg": os.path.join(os.environ["HOME"], "Pictures"),
    "png": os.path.join(os.environ["HOME"], "Pictures"),
    "gif": os.path.join(os.environ["HOME"], "Pictures"),
    "bmp": os.path.join(os.environ["HOME"], "Pictures"),
    "tiff": os.path.join(os.environ["HOME"], "Pictures"),
    "webp": os.path.join(os.environ["HOME"], "Pictures"),
    "svg": os.path.join(os.environ["HOME"], "Pictures"),
    "psd": os.path.join(os.environ["HOME"], "Pictures"),
    "ai": os.path.join(os.environ["HOME"], "Pictures"),

    "mp3": os.path.join(os.environ["HOME"], "Music"),
    "wav": os.path.join(os.environ["HOME"], "Music"),
    "aac": os.path.join(os.environ["HOME"], "Music"),
    "flac": os.path.join(os.environ["HOME"], "Music"),
    "ogg": os.path.join(os.environ["HOME"], "Music"),
    "wma": os.path.join(os.environ["HOME"], "Music"),
    "m4a": os.path.join(os.environ["HOME"], "Music"),
    "aif": os.path.join(os.environ["HOME"], "Music"),

    "zip": os.path.join(os.environ["HOME"], "Documents","Archives"),
    "tar": os.path.join(os.environ["HOME"], "Documents","Archives"),
    "gz": os.path.join(os.environ["HOME"], "Documents","Archives"),
    "bz2": os.path.join(os.environ["HOME"], "Documents","Archives"),
    "xz": os.path.join(os.environ["HOME"], "Documents","Archives"),
    "rar": os.path.join(os.environ["HOME"], "Documents","Archives"),
    "7z": os.path.join(os.environ["HOME"], "Documents","Archives"),

    "mp4": os.path.join(os.environ["HOME"], "Videos"),
    "avi": os.path.join(os.environ["HOME"], "Videos"),
    "mkv": os.path.join(os.environ["HOME"], "Videos"),
    "mov": os.path.join(os.environ["HOME"], "Videos"),
    "wmv": os.path.join(os.environ["HOME"], "Videos"),
    "flv": os.path.join(os.environ["HOME"], "Videos"),
    "mpeg": os.path.join(os.environ["HOME"], "Videos"),
    "mpg": os.path.join(os.environ["HOME"], "Videos"),
    "m4v": os.path.join(os.environ["HOME"], "Videos"),
    "webm": os.path.join(os.environ["HOME"], "Videos"),
    "3gp": os.path.join(os.environ["HOME"], "Videos"),

    "iso": os.path.join(os.environ["HOME"], "Documents","Images"),
    "bin": os.path.join(os.environ["HOME"], "Documents","Images"),
    "img": os.path.join(os.environ["HOME"], "Documents","Images"),
    "nrg": os.path.join(os.environ["HOME"], "Documents","Images"),
    "dmg": os.path.join(os.environ["HOME"], "Documents","Images"),

    "py": os.path.join(os.environ["HOME"], "Documents","Scripts"),
    "sh": os.path.join(os.environ["HOME"], "Documents","Scripts"),
    "yaml": os.path.join(os.environ["HOME"], "Documents","Scripts"),
    "json": os.path.join(os.environ["HOME"], "Documents","Scripts"),
    "html": os.path.join(os.environ["HOME"], "Documents","Scripts"),

    "torrent": os.path.join(os.environ["HOME"], "Documents","Torrent_files"),
    "exe": os.path.join(os.environ["HOME"], "Documents","Windows-files"),
}

files = os.listdir(downloads_folder)

# Используется для подсчёта количество перемещённых файлов
movedfile = 0

# Перебор файлов и их перемещение
try:
    for file in files:
        file_path = os.path.join(downloads_folder, file)
        if os.path.isfile(file_path):
            file_extension = file.split(".")[-1].lower()
            if file_extension in extensions:
                destination_folder = extensions[file_extension]
                # Создание папки назначения, если она не существует
                os.makedirs(destination_folder, exist_ok=True)
                destination_path = os.path.join(destination_folder, file)
                shutil.move(file_path, destination_path)
                print(f"Перемещен файл {file} в {destination_folder}")
                if destination_folder is not None:
                    movedfile += 1
    if movedfile == 0:
        print("Файлов для перемещения не найдено")
    else:
        print("Все файлы перемещены.")
    print(f"Количество перемещённых файлов: {movedfile}")
    
except:
    print("Произошла какае-то ошибка на этапе перебора и перемещения файлов, скрипт остановлен!")
    
