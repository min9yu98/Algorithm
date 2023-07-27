n = int(input())
s = input()
dic = {"A": 0, "B": 0}

for i in s:
    if i == "A":
        dic["A"] += 1
    else:
        dic["B"] += 1
if dic["A"] == dic["B"]:
    print("Tie")
else:
    print("A" if dic["A"] > dic["B"] else "B")