# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())

words = [input().strip() for _ in range(n)]
counts = Counter(words)
print(len(counts))
print(*counts.values())
