

import logging
import pathlib
from collections import namedtuple
import argparse

logging.basicConfig(filename='logsHW.log',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

DIRSUBJECT = namedtuple('DIRSUBJECT', ['file_name', 'ext', 'flag', 'name_dir'])


def dir_info(path):
    path = pathlib.Path(path)
    new_list = []
    try:
        for file in path.iterdir():
            if file.is_dir():
                logger.info(f'{file.name} это католог')
            else:
                logger.info(
                    f'файл {file.name} с расширением {file.suffix} лежит в {file.parent}')
            new_list.append(DIRSUBJECT(file.name, file.suffix,
                            file.is_dir(), file.parent))
        return new_list
    except Exception as e:
        logger.error(f'ошибка {e}')


def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default='D:\обучение\python')
    args = parser.parse_args()
    return dir_info(args.dir)


par()
