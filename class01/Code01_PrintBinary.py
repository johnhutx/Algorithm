def print_binary(num):
    s = ''
    for i in range(31, -1, -1):
        cur = (num >> i) & 1  # (right shift operation on num and i and bitwise AND with 1)
        s += str(cur)
    print(s)  # s contains 32 bit binary representation of 4(00000000000000000000000000000100)


if __name__ == '__main__':
    # 32位
    num = 212
    print_binary(num)
    # print("{:032b}".format(num))
