def factorial_sum(N):
    ans = 0
    cur = 1
    for i in range(1, N+1):
        cur *= i
        ans += cur
    return ans


if __name__ == '__main__':
    N = 10
    print(factorial_sum(N))
