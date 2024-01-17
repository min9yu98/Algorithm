import sys
input = sys.stdin.readline

b, c, d = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
bev = list(map(int, input().split()))

origin_price = sum(burger) + sum(side) + sum(bev)

burger.sort(reverse=True)
side.sort(reverse=True)
bev.sort(reverse=True)

lt = min(len(burger), len(side), len(bev))
raw_sum_price = sum(burger[:lt]) + sum(side[:lt]) + sum(bev[:lt])
discount_price = int(raw_sum_price * 0.9) + sum(burger[lt:]) + sum(side[lt:]) + sum(bev[lt:])

print(origin_price)
print(discount_price)
