# Проверка для строчного типа вывода
def checkp_value(value):
    if value is None:
        return 'null'
    if str(value) == 'True' or str(value) == 'False':
        return str(value).lower()
    if isinstance(value, list):
        return '[complex value]'
    return f"'{value}'"


# Модуль приведения строк
def string(data, plain=[], res=''):  # noqa: C901
    for diff, key, value in sorted(data, key=lambda name: name[1]):
        if diff == ' ' and isinstance(value, list):
            plain.append(key + '.')
            res += string(value, plain)
            plain.pop()
            continue
        elif diff == '-' and sum(data, []).count(key) == 2:
            res += f"{pr}'{''.join(plain)}{key}' {up}{checkp_value(value)}"
            continue
        elif diff == '+' and sum(data, []).count(key) == 2:
            res += f" to {checkp_value(value)}\n"
            continue
        elif diff == '+':
            res += f"{pr}'{''.join(plain)}{key}' {added}{checkp_value(value)}\n"
            continue
        elif diff == '-':
            res += f"{pr}'{''.join(plain)}{key}' {rem}\n"
            continue
    return res


# Константы
comp = '[complex value]'
pr = 'Property '
rem = 'was removed'
up = 'was updated. From '
added = 'was added with value: '
