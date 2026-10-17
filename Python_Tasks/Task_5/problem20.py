#Piling Up!
#https://www.hackerrank.com/challenges/piling-up/problem
for _ in range(int(input())):
    n = int(input())
    blocks = list(map(int, input().split()))
    
    left, right = 0, n - 1
    current = float('inf')
    possible = True
    
    while left <= right:
        if blocks[left] >= blocks[right]:
            chosen = blocks[left]
            left += 1
        else:
            chosen = blocks[right]
            right -= 1
            
        if chosen > current:
            possible = False
            break
            
        current = chosen
        
    print("Yes" if possible else "No")
