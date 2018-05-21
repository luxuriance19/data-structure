# 回溯法
def conflict(state, nextX, n):
    # nextY = n 这里n就是nextY
    for i in range(n):
        if abs(state[i] - nextX) in (0, n-i):
            return True
    return False

# 递归回溯
def backtrace(n,num):
    global locations
    global state
    global tot
    for pos in range(num):
        state[n] = pos
        if not conflict(state, pos, n):
            if n == num - 1:
                s = state.copy()
                locations.append(s)
                tot += 1
            else:
                backtrace(n+1, num)

def queens(num):
    backtrace(0,num)
    print(tot)
    print(locations)



# 非递归回溯
def backtrace_without_recursive(num):
    #backtrace(0, num)
    global locations
    global state
    global tot
    n = 0
    pos = 0
    while n < num:
        while pos < num:
            if not conflict(state, pos, n):
                state[n] = pos
                pos = 0
                break
            else:
                pos += 1

        if state[n] == -1: # 找不到填充位置，回溯
            if n == 0:
                break
            else:
                n -= 1
                pos = state[n] + 1 # 这一步执行因为前面已经遍历到了state[n]中的位置
                state[n] = -1
                continue

        if n == num - 1:
            s = state.copy()
            locations.append(s)
            tot += 1
            pos = state[n]+1
            state[n] = -1
            continue

        n += 1

    print(tot)
    print(locations)

if __name__ == "__main__":
    global locations
    global state
    global tot
    locations = []
    num = 8
    state = [-1 for row in range(num)]
    tot = 0
    backtrace_without_recursive(num)
    locations = []
    state = [-1 for row in range(num)]
    tot = 0
    queens(num)

