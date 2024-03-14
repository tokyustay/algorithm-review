from collections import deque

queue = deque() # 큐.스택 구현 라이브러리(시간복잡도 효율적)

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(4)
queue.append(5)
queue.popleft()
queue.append(6)

print(queue)
queue.reverse()
print(queue)