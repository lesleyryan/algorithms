#! /usr/bin/env python
# Implementation of Circular Linked List Detection
# Use two iterators to traverse list. First iterator (tortoise) increments by one
# node.  Second iterator (hare) increments by two.  If there is a loop, than the
# second iterator will lap the first iterator and both will meet.

class Node:
  def __init__ (self, data=None, next=None):
    self.data = data;
    self.next = next;

  def __str__(self):
    return str(self.data);

def hasLoop(node):
  tortoise = hare = node
  
  # Keep iterating as long as there is a loop.  No loop if the last node points
  # to None 
  while(tortoise.next != None and hare.next != None and hare.next.next != None):
    tortoise = tortoise.next;
    hare = hare.next.next;
    print "tortoise: %d hare: %d" % (tortoise.data, hare.data)
    if ( tortoise == hare ):
      print "Loop found."
      return 

  print "No loop found."

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node1

hasLoop(node1)
