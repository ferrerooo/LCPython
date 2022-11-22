
####### 3 queue ######

# can be achieved by (1) list, (2) collections.deque (3) queue.Queue 
# https://www.geeksforgeeks.org/queue-in-python/

# (1) list
queue = []
queue.append('a')
queue.append('b')
print(queue.pop(0))

# (2) collections.deque
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print(q.popleft())
print(q.pop())
q.appendleft('c')
print(q)

# (3) queue.Queue
from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())

# minHeap & maxHeap
from heapq import heappop, heappush, heapify
# Creating empty heap
heap = []
heapify(heap)
# Adding items to the heap using heappush
# function by multiplying them with -1
heappush(heap, -1 * 10)
heappush(heap, -1 * 30)
heappush(heap, -1 * 20)
heappush(heap, -1 * 400)
# printing the value of maximum element
print("Head value of heap : " + str(-1 * heap[0]))
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print((-1*i), end=" ")
print("\n")
element = heappop(heap)
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(-1 * i, end = ' ')

####### 5 set ######

# Python has no built-in TreeSet, TreeMap like Java does

s = set([1, 2, 3]) # set的原理和dict一样，所以，同样不可以放入可变对象as key. Try to add a list, and see error
s = set([1, 1, 2, 2, 3, 3]) # 重复元素在set中自动被过滤
s.add(4)
s.remove(4)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2

if (1 in s):
    pass


######## 7 control flow ########

#for name in names:
#    print(name)

#row0_reverse = [1 - val for val in grid[0]]

#for idx, x in enumerate(xs):
#    print(idx, x)


#################################

import sys;

print(sys.maxsize);
print(-sys.maxsize - 1);

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()

print(type(range(9)))
print(type(list(range(9))))