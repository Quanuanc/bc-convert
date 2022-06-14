import re
from io import StringIO
from zipfile import ZipFile

import yaml

from src.bc_convert.converter import DictReaderStrip


class Wechat:
    def __init__(self, input_file, config_file):
        self._input = input_file
        self._config = config_file
        self._read_input()

    def _read_input(self):
        try:
            with open(self._config) as config_f, \
                    ZipFile(self._input) as zip_f:
                config = yaml.load(config_f, Loader=yaml.Loader)
                password = config['password']
                csv_file = zip_f.read(zip_f.namelist()[1], pwd=str.encode(password))
                content = csv_file.decode('utf-8-sig')
                lines = content.split('\n')
                if not re.search(r'微信支付账单明细', lines[0]):
                    raise ValueError('not a wechat csv file')

                print('importing wechat: ')
                content = '\n'.join(lines[16:])
                self._content = content
        except Exception as e:
            print(e)

    def _read_config(self):
        pass

    def parse(self):
        content = self._content
        f = StringIO(content)
        reader = DictReaderStrip(f)
        for row in reader:
            print(row)

    def write(self):
        pass
