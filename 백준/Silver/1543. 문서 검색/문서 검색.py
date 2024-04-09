import sys

input = sys.stdin.readline

docs = input().strip()
word = input().strip()

while word in docs:
    docs = docs.replace(word, "!")
print(docs.count("!"))
