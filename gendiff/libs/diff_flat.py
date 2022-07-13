from json import load


# BEGIN
# Загружаем файл
def load_file(file):
    # В случае проблем с путём к файлу
    # обработать его здесь
    return load(open(file))


# Модуль приведения строки
def to_block(data):
    result = '{\n'
    for dif, key, value in sorted(data, key=lambda name: name[1]):
        result += f'  {dif} {key}: {str(value).lower()}\n'
    result += '}'
    return result


# Модуль вычисления отличий плоских файлов
def generate_diff(file_path1, file_path2):
    file1 = load_file(file_path1)
    file2 = load_file(file_path2)
    diff = []
    for key in file1 | file2:  # under 3.9 use {**file1, **file2}
        if key not in file1:
            diff.append(['+', key, file2.get(key)])
            continue
        elif key not in file2:
            diff.append(['-', key, file1.get(key)])
            continue
        elif file1.get(key) != file2.get(key):
            diff.append(['-', key, file1.get(key)])
            diff.append(['+', key, file2.get(key)])
            continue
        diff.append([' ', key, file2.get(key)])
    return to_block(diff)
# END
# {                                   {
#   "host": "hexlet.io",                "timeout": 20,
#   "timeout": 50,                      "verbose": true,
#   "proxy": "123.234.53.22",           "host": "hexlet.io"
#   "follow": false                    }
# }


# Диф строится на основе того как файлы изменились относительно
# друг друга, ключи выводятся в алфавитном порядке.

# gendiff filepath1.json filepath2.json
# {
#   - follow: false
#     host: hexlet.io
#   - proxy: 123.234.53.22
#   - timeout: 50
#   + timeout: 20
#   + verbose: true
# }

# Отсутствие плюса или минуса говорит о том, что ключ есть в обоих файлах,
# и его значения совпадают. Во всех остальных ситуациях значение по ключу
# либо отличается, либо ключ есть только в одном файле. В примере выше ключ
# timeout есть в обоих файлах, но имеет разные значения, proxy находится
# только в file1.json, а verbose только в file2.json.
