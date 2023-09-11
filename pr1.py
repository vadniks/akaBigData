import fileinput
import math
from typing import Dict, List
import pandas as pd
from sklearn.datasets import fetch_california_housing


# class P1T1: # <done>


class P1T2:

    @staticmethod
    def run(words: str) -> Dict[str, float]:
        result: Dict[str, float] = {}

        for word in words.split(' '):  # type: str
            shape = int(word[0])
            params = word[2:].split(',')

            if len(params) == 1:
                area = P1T2.area(shape, float(params[0]))
            else:
                area = P1T2.area(shape, float(params[0]), float(params[1]))

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


class P1T3:

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


class P1T4:

    @staticmethod
    def run():
        plain_sum = 0
        squares_sum = 0

        print('t4:')

        for x_line in fileinput.input():  # type: str
            line = x_line[:len(x_line) - 1]
            negative = line[0] == '-'

            if negative:
                line = line[1:]

            assert line.isnumeric()
            num = int(line)

            if negative:
                num = -num

            plain_sum += num
            squares_sum += num ** 2

            if plain_sum == 0:
                print('t4', squares_sum)
                break


class P1T5:

    @staticmethod
    def run(n: int) -> List[int]:
        num = 1
        count = 0

        nums: List[int] = []
        for _ in range(1, n + 1):
            nums.append(num)
            count += 1

            if count == num:
                num += 1
                count = 0

        return nums


class P1T6:

    @staticmethod
    def run():
        a = [1,    2,   3,   4,   2,   1,   3,   4,   5,   6,   5,   4,   3,   2]
        b = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
        assert len(a) == len(b)

        result: Dict[str, int] = {}
        for i in range(0, len(b)):  # type: int
            letter = b[i]

            count = result[letter] if letter in result else 0
            count += a[i]

            result.update({letter: count})

        return result


class P1T7_12:

    @staticmethod
    def run():
        data = fetch_california_housing(as_frame=True)
        x_data = data.data

        print('t8:')
        x_data.info()

        print('t9:')
        print(x_data.isna().sum())

        print('t10:')
        print(x_data.loc[(x_data.HouseAge > 50) & (x_data.Population > 2500)])

        print('t11:')
        med_inc = x_data["MedInc"]
        print(med_inc.max(), med_inc.min())

        # print('t12', x_data.apply(pd.DataFrame.mean))  # TODO: not working - f*** it then


class P1T1O:

    @staticmethod
    def run(x_input: str):
        morze = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
            'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
            'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
            'q': '--.-', 'r': '.-.', 's': '…', 't': '-',
            'u': '..-', 'v': '…-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..'
        }

        for word in x_input.split(' '):  # type: str
            count = 0
            last = len(word) - 1

            for char in word:  # type: str
                if char != ' ':
                    print(morze[char.lower()], end='')

                if count < last:
                    print(' ', end='')

                count += 1

            print()


def main():
    # print('t2', P1T2.run('0=1.0,2.0 1=3.0,4.0 2=5.0'))
    # print('t3', P1T3.run('+', 1.0, 2.0), P1T3.run('/', 4.0, 2.0), P1T3.run('abs', -1.0, 0.0))
    # P1T4.run()
    # print('t5', P1T5.run(7))
    # print('t6', P1T6.run())
    # P1T7_12.run()
    P1T1O.run('Ignition sequence start')


if __name__ == '__main__':
    main()

