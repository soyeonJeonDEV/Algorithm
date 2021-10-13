n = int(input())
trees = list(map(int,input().split()))
node = int(input())
tree = []

for i in range(trees):
    if trees[i]>=0:
        tree[trees[i]] = i

print(tree)