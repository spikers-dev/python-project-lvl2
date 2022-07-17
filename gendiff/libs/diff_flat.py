from gendiff.libs.diff_parser import load_file
from gendiff.libs.style_block import block
from gendiff.libs.style_plain import string
from gendiff.libs.style_json import json


# Модуль приведения словаря к структурному списку
def flatkey(keys):
    if not isinstance(keys, dict):
        return keys

    def walk(keys, flat=[]):
        for key, value in keys.items():
            if isinstance(value, dict):
                child_flat = []
                walk(value, child_flat)
                flat.append([' ', key, child_flat])
                continue
            flat.append([' ', key, value])
        return flat
    return walk(keys)


def formatter(data, style):
    if style == 'plain':
        return string(data).strip()
    if style == 'json':
        return json(data)
    return block(data).strip()


# Модуль вычисления отличий
def generate_diff(file_path1, file_path2, style=''):  # noqa: C901
    file1 = load_file(file_path1)
    file2 = load_file(file_path2)

    def walk(file1, file2, diff=[]):
        if not isinstance(file1, dict) or not isinstance(file2, dict):
            return []
        for key, value in (file1 | file2).items():
            if key not in file1:
                diff.append(['+', key, flatkey(value)])
                continue
            elif key not in file2:
                diff.append(['-', key, flatkey(value)])
                continue
            elif isinstance(value, dict) and isinstance(file1.get(key), dict):
                child = []
                walk(file1.get(key), file2.get(key), child)
                diff.append([' ', key, child])
                continue
            elif file1.get(key) != file2.get(key):
                diff.append(['-', key, flatkey(file1.get(key))])
                diff.append(['+', key, flatkey(file2.get(key))])
                continue
            diff.append([' ', key, file2.get(key)])
        return diff
    return formatter((walk(file1, file2)), style)


# file1 = 'tests/fixtures/file1_complex.json'
# file2 = 'tests/fixtures/file2_complex.json'

# file3 = 'tests/fixtures/file1.yml'
# file4 = 'tests/fixtures/file2.yml'

# print(generate_diff(file3, file4, 'plain'))
# print(generate_diff(file3, file4, 'json'))

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
