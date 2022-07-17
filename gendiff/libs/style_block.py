# Проверка для блочного типа вывода
def check_value(value):
    if value is None:
        return 'null'
    if str(value) == 'True' or str(value) == 'False':
        return str(value).lower()
    return value


# Модуль приведения блока
def block(data):
    indent = '  '

    def walk(data, round=0, result=''):
        result += '{\n'
        for dif, key, value in sorted(data, key=lambda name: name[1]):
            result += f'  {indent * round}{dif} {key}: '
            if isinstance(value, list):
                result += f'{walk(value, round + 2)}'
                continue
            result += f'{check_value(value)}\n'
        result += f'{indent * round}' + '}\n'
        return result
    return walk(data)
