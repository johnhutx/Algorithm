01 位运算、算法是什么、介绍位运算和简单排序

内容：

讲解二进制、位运算

介绍什么是算法

讲解冒泡、选择、插入排序

题目：

实现打印一个整数的二进制

# 给定一个参数N，返回1!+2!+3!+4!+…+N!的结果
memoization, O(N)

# 实现冒泡排序 (bubble sort)
```
# 指针指向数组最右
# 遍历数组，两两对比，每次对比把较大的数右移，直到最大值右移到指针处
# 指针左移，重复第一步，最大值移到指针位置

```

# 实现选择排序 (selection sort)
```
# 指针指向0，开始遍历数组，选择最小值，与0位置交换
# 指针往右移动1，重复第一步直到指针指向数组最后一位
1. min_idx = 0
2. 从 min_idx 到 N-1 遍历数组
3. If arr[min_idx] > arr[i]:
    swap(arr[min_idx], arr[i])
4. min_idx = min_idx + 1
5. Repeat 2 until min_idx = N - 1
```

# 实现插入排序 (insertion sort)

