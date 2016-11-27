# -*- coding: utf-8 -*-
def divide(a,b):
    return a/b

try:
    c = divide(5,'string')
except ZeroDivisionError:
    print('1두번째 인자는 0이어서는 안됩니다')
except TypeError:
    print('2모든 인자는 숫자여야 합니다')
except:
    print('3음~ 무슨 에러인지 모르겠어요!!')

