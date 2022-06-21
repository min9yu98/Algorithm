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

n = int(input())
n_lst = list(map(int, input().split()))
sorted_lst = sorted(n_lst)

m = int(input())
m_lst = list(map(int, input().split()))

for i in range(len(m_lst)):
    print(binary_search(m_lst[i], sorted_lst))

## 답지참고