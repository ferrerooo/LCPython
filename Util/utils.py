####### 1 string ######

s = 'abc'
print(s)
print(len(s))
print(s[1])
print(s.split('b'))


####### 2 list ######

friends = ['Michael', 'Bob', 'Tracy']
print(len(friends))
friends.append("dd")
friends.insert(1, 'ee')
friends.pop()  # delete the tail element
friends.pop(1) # delete element at index
friends[1] = 'ff' # update value

if ('ann' in friends) :
    pass

if ('ann' not in friends) :
    pass

friends.sort()
friends.sort(reverse=True)

lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x:x[1])
print(lst)

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

####### 4 stack ######

# can be implemented by (1) list (2) Collections.deque (3) queue.LifoQueue
# https://www.geeksforgeeks.org/stack-in-python/

# (1) list
stack = []
stack.append('a')
print(stack.pop())

# (2) collections deque
from collections import deque
stack = deque()
stack.append('a')
stack.append('b')
print(stack.pop())

# (3) queue LifoQueue
from queue import LifoQueue
stack = LifoQueue(maxsize=3)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')
print("Full: ", stack.full())
print("Size: ", stack.qsize())
print(stack.get())
print(stack.get())
print(stack.get())
print("\nEmpty: ", stack.empty())

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

####### 6 map ######

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael']
d['Adam'] = 67
'Thomas' in d
d.get('Thomas')
d.get('Thomas', -1)