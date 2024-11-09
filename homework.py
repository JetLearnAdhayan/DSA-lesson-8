class Queue: 
   def __init__(self):
      self.queue = []

   def enqueue(self, item):
      self.queue.append(item)

   def dequeue(self):
      if len(self.queue) < 1:
         return None 
      return self.queue.pop(0)

   def size(self):
      print("The size of the queue is", len(self.queue))

   def display(self):
      print(self.queue)

   def reverse(self):
      stack = []
      
      while len(self.queue) > 0:
         stack.append(self.dequeue())
      
      while stack:
         self.enqueue(stack.pop())

queuelist = Queue()
queuelist.enqueue(1)
queuelist.enqueue(2)
queuelist.enqueue(3)
queuelist.enqueue(4)
queuelist.enqueue(5)

print("Original Queue:")
queuelist.display()

print("Reversed Queue:")
queuelist.reverse()
queuelist.display()

print("Queue Size:")
queuelist.size()
