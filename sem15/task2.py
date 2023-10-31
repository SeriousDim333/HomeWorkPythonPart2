

import argparse
import logging

logging.basicConfig(filename='logsHW.log',
                    encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def triangle(side_A, side_B, side_C):
    try:
        side_A = int(side_A)
        side_B = int(side_B)
        side_C = int(side_C)
    except Exception as e:
        logger.error(
            f'ошибка {e} стороны треугольника {side_A},{side_B},{side_C} должны быть числами')

    if side_A < 0 or side_B < 0 or side_C < 0:
        logger.error(
            f'стороны треугольника {side_A},{side_B},{side_C} не могут быть отрицательными')
    elif side_A > side_B+side_C or side_B > side_A+side_C or side_C > side_A+side_B:
        logger.error(
            f'треугольника со сторонами {side_A},{side_B},{side_C} не существует')
    else:
        if side_A == side_B == side_C:
            logger.info(
                f'треугольника со сторонами {side_A},{side_B},{side_C} равносторонний')
        elif side_A == side_B or side_A == side_C or side_B == side_C:
            logger.info(
                f'треугольника со сторонами {side_A},{side_B},{side_C} равнобедренный')
        else:
            logger.info(
                f'треугольника со сторонами {side_A},{side_B},{side_C} разносторонний')


def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--side_A', default=1)
    parser.add_argument('-b', '--side_B', default=1)
    parser.add_argument('-c', '--side_C', default=1)
    args = parser.parse_args()
    return triangle(args.side_A, args.side_B, args.side_C)


par()
