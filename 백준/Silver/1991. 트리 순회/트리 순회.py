import sys

input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(n):
    a, b, c = input().strip().split()
    tree[a] = [b, c]


def preorder(node):
    if node != '.':
        print(node, end='')
    if tree[node][0] != '.':
        preorder(tree[node][0])
    if tree[node][1] != '.':
        preorder(tree[node][1])


def inorder(node):
    if tree[node][0] != '.':
        inorder(tree[node][0])
    if node != '.':
        print(node, end='')
    if tree[node][1] != '.':
        inorder(tree[node][1])


def postorder(node):
    if tree[node][0] != '.':
        postorder(tree[node][0])
    if tree[node][1] != '.':
        postorder(tree[node][1])
    if node != '.':
        print(node, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
