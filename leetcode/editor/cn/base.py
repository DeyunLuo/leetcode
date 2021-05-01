# coding: utf-8

"""
@file: base.py
@time: 2021/5/1 10:54
"""
import json
import time


def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def readlines(num):
    for line in range(num):
        yield input().strip('\n')


def fun_wrapper(input_nums=1):
    def wrapper(func):
        def inner(*args, **kwargs):
            lines = readlines(input_nums)
            while True:
                try:
                    line = next(lines)
                    input_value = stringToIntegerList(line)
                    start_time = time.time()
                    result = func(*args, input_value)
                    end_time = time.time()
                    # out = integerListToString(result)
                    if result is not None:
                        # print(out)
                        print(result)
                        "Do not return anything, modify nums in-place instead."
                    else:
                        print('out is None')
                    print(f'spend time: {end_time - start_time}')
                except StopIteration:
                    break

        return inner

    return wrapper

# if __name__ == '__main__':
#     main()
