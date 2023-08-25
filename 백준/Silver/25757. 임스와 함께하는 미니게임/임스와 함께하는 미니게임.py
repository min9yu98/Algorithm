import sys

n, g = map(str, sys.stdin.readline().rstrip().split())
n = int(n)
game = {"Y": 1, "F": 2, "O": 3}
st = set()

for _ in range(n):
    person = sys.stdin.readline().rstrip()
    st.add(person)
print(len(st) // game[g])
