import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = []

for i in range(n):
    array.append(input().strip())
    
chess = [
    'WBWBWBWB',
    'BWBWBWBW', 
    'WBWBWBWB',
    'BWBWBWBW', 
    'WBWBWBWB',
    'BWBWBWBW', 
    'WBWBWBWB',
    'BWBWBWBW']
    
min_count = 64

for i in range (n - 7):
    for j in range (m - 7):
        count = 0
        
        for row in range (8):
            for col in range(8):
                if array[row + i][col + j] != chess[row][col]:
                    count += 1
                    
        min_count = min(count, min_count, 64 - count)
    
print(min_count)
