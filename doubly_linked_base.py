# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013

class _DoublyLinkedBase:
  """A base class providing a doubly linked list representation."""

  #-------------------------- nested _Node class --------------------------
  # nested _Node class
  class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = '_element', '_prev', '_next'            # streamline memory

    def __init__(self, element, prev, next):            # initialize node's fields
      self._element = element                           # user's element
      self._prev = prev                                 # previous node reference
      self._next = next                                 # next node reference

  #-------------------------- list constructor --------------------------

  def __init__(self):
    """Create an empty list."""
    self._header = self._Node(None, None, None)
    self._trailer = self._Node(None, None, None)
    self._header._next = self._trailer                  # trailer is after header
    self._trailer._prev = self._header                  # header is before trailer
    self._size = 0                                      # number of elements

  #-------------------------- public accessors --------------------------

  def __len__(self):
    """Return the number of elements in the list."""
    return self._size

  def is_empty(self):
    """Return True if list is empty."""
    return self._size == 0

  #-------------------------- nonpublic utilities --------------------------

  def _insert_between(self, e, predecessor, successor):
    """Add element e between two existing nodes and return new node."""
    newest = self._Node(e, predecessor, successor)      # linked to neighbors
    predecessor._next = newest
    successor._prev = newest
    self._size += 1
    return newest

  def _delete_node(self, node):
    """Delete nonsentinel node from the list and return its element."""
    predecessor = node._prev
    successor = node._next
    predecessor._next = successor
    successor._prev = predecessor
    self._size -= 1
    element = node._element                             # record deleted element
    node._prev = node._next = node._element = None      # deprecate node
    return element                                      # return deleted element



class LinkedStack:
  """LIFO Stack implementation using a singly linked list for storage."""

  #-------------------------- nested _Node class --------------------------
  class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = '_element', '_next'         # streamline memory usage

    def __init__(self, element, next):      # initialize node's fields
      self._element = element               # reference to user's element
      self._next = next                     # reference to next node

  #------------------------------- stack methods -------------------------------
  def __init__(self):
    """Create an empty stack."""
    self._head = None                       # reference to the head node
    self._size = 0                          # number of stack elements

  def __len__(self):
    """Return the number of elements in the stack."""
    return self._size

  def is_empty(self):
    """Return True if the stack is empty."""
    return self._size == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._head = self._Node(e, self._head)  # create and link a new node
    self._size += 1

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    return self._head._element              # top of stack is at head of list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Empty('Stack is empty')
    answer = self._head._element
    self._head = self._head._next           # bypass the former top node
    self._size -= 1
    return answer

  def pop_second(self):
    """ Removes second element by popping first two elements, keeping the first element somewhere else
    pushes the previous head again"""
    if self._size == 1:
      return Exception("There's only one element in the linked stack")
    self._head._next = self._head._next_next
    self._size-=1
    return second

  def push_second(self, e):
    """ Pushes second element by popping the initial head, then popping the second one,
    then pushing the initial head back"""
    if self._size == 1:
      return Exception("There's only one element in the linked stack")
    first = self.pop()
    self.push(e)
    self.push(first)
    self._size+=1
    return self._head._next._element

  def penultimate(self):
    if self.size <2:
      raise Error("list must be larger than two")
    walk = self._head
    while walk._next_next is not None:
        walk = walk.next
    return walk

  def concatenate_second(self, M):
    walk = self._head
    while walk._next is not None:
      walk = walk._next
      walk._next = M._head
      M._head = None
    return walk

  def find_duplicates(self):

    walk1 = self._head
    walk2 = self._head._next

    if self._size < 2:
      raise Error("The stack has only one element")

    elif self._size < 1:
      raise Error("The stack is empty")

    elif self._size > 1:
      while walk1._next is not None and walk2 is not None:
       #not checking the last element 
        print (walk1._element, walk2._element)

        if walk1._element == walk2._element:
          print ("Duplicate was found")

        if walk2._next is None: #the inner loop is over
          walk1 = walk1._next #update outer loop
          walk2 = walk1._next #restart inner loop
        elif walk2._next:
          walk2 = walk2._next #inner loop continues

      

if __name__=="__main__":
  A = LinkedStack()
  A.push(5)
  A.push(4)
  A.push(3)
  A.push(3)
  A.push(2)
  A.push(1)
  A.find_duplicates()