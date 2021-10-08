import sys
import heapq
numbers = int(input())
if numbers == 0:
    sys.exit()
        
lists = list(map(int,input().split()))

print(lists)

total = 0

while len(lists) > 1:
    first = heapq.heappop(lists)
    second = heapq.heappop(lists)
    total += first + second
    lists = heapq.heappush(lists, total)
print(total)
    
