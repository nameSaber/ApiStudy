import json, yaml
from configparser import ConfigParser
from utils.logger import logger


class MyConfigParser(ConfigParser):
    """
    optionxform() ： 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的键 option 自动转为小写的问题
    my_sections() : 重写 RawConfigParser 中的 sections 函数，解决读取ini文件中配置项的键值对问题
    """
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

    def my_sections(self):
        return dict(self._sections)

class ReadFileData:
    """
    读文件:yaml, json, ini
    """
    def __init__(self):
        pass

    def load_yaml(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
        logger.info("读到数据 ==>>  {}".format(yaml_data))
        return yaml_data

    def load_json(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            json_data = json.load(f)
        logger.info("读到数据 ==>>  {} ".format(json_data))
        return json_data

    def load_ini(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="utf-8")
        ini_data = config.my_sections()
        logger.info("读到数据 ==>>  {} ".format(ini_data))
        return ini_data

data = ReadFileData()

