import sys

input = sys.stdin.readline

first = input().strip()
second = input().strip()
first_dic = {chr(i): 0 for i in range(97, 123)}
second_dic = {chr(i): 0 for i in range(97, 123)}


def countSpelling(word, dic):
    for w in word:
        dic[w] += 1
    return dic


def compareDict(dic1, dic2):
    cnt = 0
    for w1, w2 in zip(dic1.values(), dic2.values()):
        cnt += abs(w1 - w2)
    return cnt


print(compareDict(countSpelling(first, first_dic), countSpelling(second, second_dic)))
