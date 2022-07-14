from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


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
