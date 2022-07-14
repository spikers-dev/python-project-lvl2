from yaml import load
from yaml import CLoader as Loader


# BEGIN
# Загружаем файл
def load_file(file):
    # В случае проблем с путём к файлу
    # обработать его здесь
    # pyyaml обрабатывает и json файлы,
    # смысла обрабатывать разные расширения нет!!!
    try:
        return load(open(file), Loader=Loader)
    except Exception as error:
        return error
