SIMPLE_STRING = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


LOADED_FILE1 = {"host": "hexlet.io",
                "timeout": 50,
                "proxy": "123.234.53.22",
                "follow": False
                }

ERROR_MSG01 = "[Errno 2]"
ERROR_MSG02 = 'while parsing a block mapping'
ERROR_MSG03 = 'load_file() missing'
