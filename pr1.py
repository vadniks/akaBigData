import math
import sys
from typing import Dict


class P1T1:

    @staticmethod
    def run() -> Dict[str, float]:
        """reads the program arguments, expects the following pattern: 0=1.0,2.0 1=3.0,4.0 2=5.0"""
        result: Dict[str, float] = {}
        for word in sys.argv[1:]:  # 0=1.0,2.0
            shape = int(word[0])
            params = word[2:].split(',')

            if len(params) == 1:
                area = P1T1.area(shape, float(params[0]))
            else:
                area = P1T1.area(shape, float(params[0]), float(params[1]))

            result.update(area)
        return result

    @staticmethod
    def area(shape: int, *params: float) -> Dict[str, float]:
        match shape:
            case 0:
                assert len(params) == 2
                return {'triangle': params[0] * params[1] / 2}
            case 1:
                assert len(params) == 2
                return {'rectangle': params[0] * params[1]}
            case 2:
                assert len(params) == 1
                return {'circle': math.pi * params[0] ** 2}
            case _:
                raise Exception


def main():
    print(P1T1.run())


if __name__ == '__main__':
    main()
