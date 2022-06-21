import sys
def binary_search(element, lst, start = 0, end = None):
    if end == None:
        end = len(lst) - 1
    if start > end:
        return 0

    mid = (start + end) // 2

    if element == lst[mid]:
        return 1
    elif element < lst[mid]:
        end = mid - 1
    elif element > lst[mid]:
        start = mid + 1
    return binary_search(element, lst, start, end)

n = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))
sorted_lst = sorted(n_lst)

m = int(sys.stdin.readline())
m_lst = list(map(int, sys.stdin.readline().split()))

for i in range(len(m_lst)):
    print(binary_search(m_lst[i], sorted_lst), end = " ")

## 답지참고
