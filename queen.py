# 在8×8的棋盘上面放置8个皇后，每个皇后不能位于同样的水平、垂直或对角线位置

# nextX代表下一个皇后的水平位置，nextY代表下一个皇后的垂直位置，state状态为元组的形式
# state的长度是8,因为按照顺序放置皇后，所以每个state的index表示行数，state中间的数表示当前皇后所在的列
# state[0]=3表示第1个皇后在第一行第三列
# nextX代表x坐标，nextY代表Y坐标

import random

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            print("pos",pos)
            print("state", state)
            if len(state) == num-1: #如果说是最后一个皇后
                # state += (pos,)
                print("excute last one")
                yield (pos,) # 一个值的元组的实现，也就是（42,）表示一个元组，否则（42）就是表示42
            else:
                print("state11 ", state+(pos,))
                print("excute others")
                for result in queens(num, state+(pos,)):
                    print("result",result)
                    yield (pos, ) + result

def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. '*(pos)+'X '+'. '*(length-pos-1)
    for pos in solution:
        print(line(pos))

for i in queens(4):
    print(i)

# prettyprint(random.choice(list(queens(8))))