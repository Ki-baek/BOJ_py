def arr_swap(a, b):
  while a < b:
    arr[a], arr[b] = arr[b], arr[a]
    a += 1
    b -= 1
    
n, m = map(int, input().split())

arr = list(range(1, n + 1))
  
for i in range(m):
  i, j = map(int, input().split())
  
  arr_swap(i - 1, j - 1)

print(*arr)

#____________________상단 코드가 기존 제출했던 방식을 조금 손본것_________________________
#수정 전에는 temp를 이용해서 c 스타일로 swap 했지만 파이썬의 특징을 이용하도록 수정
#____________________하단 코드가 슬라이싱 + reverse() 이용한 방식________________________

n, m = map(int, input().split())

lst = list(range(1, n + 1))
dummy = []

for i in range(m):
  i, j = map(int, input().split())
  
  dummy = lst[i - 1: j]
  dummy.reverse()
  lst[i - 1: j] = dummy

print(*lst)

#________________코드 길이 상으로 하단 코드가 더 길지만 가독성은 더 좋다고 생각해서 슬라이싱 + reverse() 이용한 방식으로 과제 제출____________________