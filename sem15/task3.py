
import argparse
import logging

logging.basicConfig(filename='logsHW.log',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def check_digit(digit):
    try:
        digit = int(digit)
    except Exception as e:
        logger.error(
            f'ошибка {e} введите число, а не {digit}')
        
    for i in range(2, int(digit**0.5)):
        if digit % i == 0:
            logger.info(f'число {digit} непростое')
            break
    else:
        logger.info(f'число {digit} простое')

def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--digit', default=1)
    args = parser.parse_args()
    return check_digit(args.digit)


par()