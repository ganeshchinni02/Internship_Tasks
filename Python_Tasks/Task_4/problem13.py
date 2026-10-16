# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set(map(int, input().split()))
n2 = int(input())
set_b = set(map(int, input().split()))

symmetric_diff = set_a.symmetric_difference(set_b)

for val in sorted(symmetric_diff):
    print(val)
