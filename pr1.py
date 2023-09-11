
import math
from typing import Dict


class P1T1:

    @staticmethod
    def run(words: str) -> Dict[str, float]:
        result: Dict[str, float] = {}

        for word in words.split(' '):
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


class P1T2:

    @staticmethod
    def run(operation: str, num_a: float, num_b: float) -> float:
        match operation:
            case '+':
                return num_a + num_b
            case '-':
                return num_a - num_b
            case '*':
                return num_a * num_b
            case '/':
                assert num_b != 0
                return num_a / num_b
            case '//':
                assert num_b != 0
                return num_a // num_b
            case 'abs':
                assert num_b == 0
                return abs(num_a)
            case 'pow':
                return num_a ** num_b
            case _:
                raise Exception


def main():
    print('t1', P1T1.run('0=1.0,2.0 1=3.0,4.0 2=5.0'))
    print('t2', P1T2.run('+', 1.0, 2.0), P1T2.run('/', 4.0, 2.0), P1T2.run('abs', -1.0, 0.0))


if __name__ == '__main__':
    main()

