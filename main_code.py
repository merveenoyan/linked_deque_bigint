# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013

from doubly_linked_base import _DoublyLinkedBase

from linked_stack import *


class LinkedDeque(_DoublyLinkedBase): # note the use of inheritance
  """Double-ended queue implementation based on a doubly linked list."""

  def first(self):
    """Return (but do not remove) the element at the front of the deque.
    Raise Empty exception if the deque is empty.
    """
    if self.is_empty():
      raise Error("Deque is empty")
    return self._header._next._element  # real item just after header



  def last(self):
    """Return (but do not remove) the element at the back of the deque.
    Raise Empty exception if the deque is empty. """
    if self.is_empty():
      raise Error("Deque is empty")
    return self._trailer._prev._element       # real item just before trailer



  def insert_first(self, e):
    """Add an element to the front of the deque."""
    self._insert_between(e, self._header, self._header._next)   # after header



  def insert_last(self, e):
    """Add an element to the back of the deque."""
    self._insert_between(e, self._trailer._prev, self._trailer) # before trailer



  def delete_first(self):
    """Remove and return the element from the front of the deque. 
    Raise Empty exception if the deque is empty. """
    if self.is_empty():
      raise Error("Deque is empty")
    return self._delete_node(self._header._next)   # use inherited method



  def delete_last(self):
    """Remove and return the element from the back of the deque.
    Raise Empty exception if the deque is empty."""
    if self.is_empty():
      raise Error("Deque is empty")
    return self._delete_node(self._trailer._prev) 


######################## Big Int Codes Below ##########################


  def createBigInt(self, s):
    """ takes string input and turns it into deque """
    for item in s:
      self.insert_last(item)
    return self

  def updateBigInt(self, pos, e):
    """ takes bigint (self), index (pos), and element and changes 
    element on index to element taken """
    walk = self._header._next
    i = 0
    #import pdb; pdb.set_trace()
    while walk._next is not None:
      if i == pos:
        walk._element = e
      i = i + 1
      walk = walk._next
    return self


  def equalBigInt(self, s1, s2):

    """ takes two strings, turns them into deque bigints
    and compares if they're equal """

    l1 = LinkedDeque()
    l2 = LinkedDeque()
    b1 = l1.createBigInt(s = s1)
    b2 = l2.createBigInt(s = s2)

    walk1 = b1._header._next
    walk2 = b2._header._next

    equal = 1
    while walk1._next is not None and walk2._next is not None:
      if walk1._element != walk2._element:
        equal = 0
      walk1 = walk1._next
      walk2 = walk2._next

    return equal



  def freeBigInt(self):
    walk = self._header._next
    while walk._next is not None:
      self.delete_last()
    return self


#################### multiply bigint #####################
  
  def multiplyBigInt(self, s1, s2):

    """ 1. take two strings, fill the left with zeros, 
        convert them to Linked Deques
        2. iterate over both in a nested way
        3. multiply each order, keep hand and generate numbers to be summed
        4. sum all the numbers """


    length1 = len(s1)
    length2 = len(s2)
    
    if length1 > length2:
      s2 = s2.zfill(length1)
    elif length2 > length1: 
      s1 = s1.zfill(length2)

    l1 = LinkedDeque()
    l2 = LinkedDeque()

    b1 = l1.createBigInt(s = s1)
    b2 = l2.createBigInt(s = s2)

    walk1 = b1._trailer._prev #iteration starts from units digit
    walk2 = b2._trailer._prev 

    hand = 0

    count_out = 0 #counter of orders of outer loop

    sum_all = 0

    #import pdb;pdb.set_trace()
    while walk1._prev is not None: #first number

      count = 0 #this is to keep which order we are on

      gen_num = 0

      hand = 0

      walk2 = b2._trailer._prev

      while walk2._prev is not None: #second number

        product = int(walk2._element) * int(walk1._element) + int(hand)

        hand = product // 10 # 2 as in 21 to save for later

        order = product - hand*10 # 1 as in 21

        gen_num = gen_num + order * (10 ** count)

        count = count + 1

        walk2 = walk2._prev

      if walk2._prev is None:

        gen_num = gen_num + hand * (10 ** len(s1))

      sum_all = sum_all + gen_num * (10 ** count_out)

      count_out = count_out + 1
    
      walk1 = walk1._prev

    return sum_all
    

################## power   ############

  def power(self, s, p): 
    multiplication = 1
    for _ in range(p):
      multiplication = self.multiplyBigInt(s, str(multiplication))  

    return multiplication



################### subtract bigint ######################

  def substractBigInt(self, s1, s2):

    """ 1. takes two strings
        2. look at their lengths, if one is shorter then pad with 
        zeros for convenience
        3. turns them into deque
        4. substracts them from each other """

    # finds lengths, pads with zeros, does nothing if equal
    l1 = LinkedDeque()
    l2 = LinkedDeque()
    result = LinkedDeque()

    length1 = len(s1)
    length2 = len(s2)
    #import pdb;pdb.set_trace()
    if length1 > length2:

      s2 = s2.zfill(length1)

    elif length2 > length1: 

      s1 = s1.zfill(length2)


    b1 = l1.createBigInt(s = s1)
    b2 = l2.createBigInt(s = s2)


    # initialize loops and hand
    if int(s1) > int(s2):
      walk1 = b1._trailer._prev #iteration starts from units digit
      walk2 = b2._trailer._prev 

    else:
      walk1 = b2._trailer._prev 
      walk2 = b1._trailer._prev 

    hand = 0

    while walk1._prev is not None and walk2._prev is not None:
      #import pdb;pdb.set_trace()

      substract_order = int(walk1._element) - int(walk2._element) + hand

      
      if substract_order < 0:

        value = int(walk1._element) - int(walk2._element) + 10

        hand = -1

      elif substract_order >= 0:

        value = substract_order

        hand = 0

      result.insert_first(e = value)

      walk1 = walk1._prev
      walk2 = walk2._prev

    return result    



################### add bigint #############################
  def addBigInt(self, s1, s2):

    """ 1. takes two strings
        2. look at their lengths, if one is shorter then pad with 
        zeros for convenience
        3. turns them into deque
        4. sums them up """

    # finds lengths, pads with zeros, does nothing if equal

    length1 = len(s1)
    length2 = len(s2)
    
    if length1 > length2:
      s2 = s2.zfill(length1)
    elif length2 > length1: 
      s1 = s1.zfill(length2)


    # turns strings into deques

    l1 = LinkedDeque()
    l2 = LinkedDeque()

    result = LinkedDeque()

    b1 = l1.createBigInt(s = s1)
    b2 = l2.createBigInt(s = s2)

    # initialize loops and hand

    walk1 = b1._trailer._prev #iteration starts from units digit
    walk2 = b2._trailer._prev 

    hand = 0

    while walk1._prev is not None and walk2._prev is not None:

      sum_order = int(walk1._element) + int(walk2._element) + hand #sums for that order

      if sum_order >= 10:

        value = sum_order % 10

        hand = 1

      elif sum_order < 10:

          value = sum_order 

          hand = 0

      result.insert_first(e = value)

      walk1 = walk1._prev
      walk2 = walk2._prev

    if hand == 1:
      result.insert_first(1)

    return result

############## deque bigint into stack for infix-postfix ##########

  def stack_BigInt(self, s):

    # turns bigint deque into stack for operations

    BigInt = self.createBigInt(s)
    stack = LinkedStack()
    walk = BigInt._header._next


    while walk._next is not None:
      stack.push(e = walk._element)
      walk = walk._next
    return stack



  def infix_to_postfix(self, s):

    BigInt = self.createBigInt(s)

    stack = LinkedStack()

    operators = ['-', '+', '*', '/', '(', ')', '^']

    prec_list= {'+':1, '-':1, '*':2, '/':2, '^':3}

    output = '' 

    def isOperand(item):
      if item in "1234567890":
        return True
      else:
        return False


    def isOperator(item):
      if item in "-+*/^":
        return True
      else:
        return False

    postfix = ""

    walk = BigInt._header._next

    #import pdb; pdb.set_trace()

    while walk._next is not None:

      if isOperand(item = walk._element): # check if element is 1234..
        
        postfix += walk._element

      elif isOperator(walk._element): # check if element is +-.. 

        while True:

          try:
            top = stack.top()
          except:
            pass

          if stack.is_empty() or top == "(":
            stack.push(walk._element)
            break

          # check precedences between the element 
          # on top of stack and the current element
          else: 
            item = walk._element  
            prec = prec_list[item]
            prectop = prec_list[top]

            if prec > prectop:
              stack.push(walk._element)
              break
            

            else:
              postfix += stack.pop() 

      elif walk._element == "(":
        stack.push(walk._element)

      elif walk._element == ")":
        char = stack.pop()

        while char != "(":
          postfix+=char
          char=stack.pop()

      walk = walk._next    


    while not stack.is_empty():
      char = stack.pop()
      postfix += char

    return postfix


####################### debug ##########################

  def debug(self):
    print("THIS IS DEBUG FUNCTION")
    walk = self._header._next
    while walk._next is not None:
      print(walk._element)
      walk = walk._next


################### test ##########################

if __name__=="__main__":
  ld = LinkedDeque()
  # test substraction
  s1 = "20"
  s2 = "319"

  result = ld.substractBigInt(s1, s2)
  print(result.debug())

  # test power
  #s1 = "293"
  #s2 = "192"

  #result = ld.power(s1, s2)
  #print(result.debug())


  # test multiplication
  #result = ld.multiplyBigInt(s1, s2)
  #print(result)

  #test infix to post fix
"""
  s3 = "123*(238+3*4)+5"
  ld = LinkedDeque()
  postfix = ld.infix_to_postfix(s3)
  print(postfix)  """

  # check create bigint, freebigint
"""bigint = ld.createBigInt(s3)
  bigint.freeBigInt() 
  print(bigint.debug())"""

  # check update bigint and add bigint
"""ld = LinkedDeque()
  print(b1._header._next._element)
  b1 = b1.updateBigInt(pos = 5, e = 5)
  result = ld.addBigInt(s1, s2)  
  print(result.debug()) """
  # check equal bigint
""" equal = ld.equalBigInt(s1,s2)
    print(equal) """
  