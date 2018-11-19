# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 21:30:02 2018
Written by Alex Blackson
ENSEA - FAME Algoritms Course
Last Edited Thursday Mar 8, 2018
"""
import random 

class SkipListNode:
    def __init__(self, label, height):
        self.label = label
        self.next = [None] * height

class SkipList:
    def __init__(self):
        self.head = SkipListNode(None, 0)
        
        
    def findpath(self, label):
        def traverse(currNode, currLevel, nodeList):
            while(True):
                if currNode.next[currLevel] is None or currNode.next[currLevel].label > label:
                    # Checks if on bottom layer, which is just a linked list
                    if currLevel == 0:
                        # Final bottom layer element found
                        return [currNode] + nodeList
                    # Moves down and adds 
                    return traverse(currNode, currLevel - 1, [currNode] + nodeList)
                currNode = currNode.next[currLevel]
            
        #Cannot search an empty list
        if len(self.head.next) == 0: 
            return [self.head]
        return traverse(self.head, len(self.head.next)-1, [])
    
    
    def mem(self, x):
        return len(self.head.next) != 0 and self.findpath(x)[0].label == x        
    
    
    def delete(self, x):
        #Check that node to delete is present before delete operations
        if self.mem(x):
            def findAndDelete(currNode, currLevel):
                while(True):
                    if currNode.next[currLevel] is not None and currNode.next[currLevel].label == x:
                        #Deletes node x by dereferencing it from skip list
                        currNode.next[currLevel] = currNode.next[currLevel].next[currLevel]
                        #Last layer reached, exits 
                        if currLevel == 0:
                            return
                        # Moves down if in an upper layer
                        return findAndDelete(currNode, currLevel - 1)
                      
                    if currNode.next[currLevel] is None or currNode.next[currLevel].label > x:
                        #Moves down 
                        return findAndDelete(currNode, currLevel - 1)
                    #Moves right
                    return findAndDelete(currNode.next[currLevel], currLevel)
                
            findAndDelete(self.head, len(self.head.next)-1)
    
    
    def insert(self, x):
        if self.mem(x):
            return
        
        prevNodes = self.findpath(x)
        
        # Generate height of newNode
        h = 1
        p = 0.5
        r = random.random()
        while r < p:
            h += 1
            p = p * 0.5
        
        newNode = SkipListNode(x, h)
        
        if h > len(self.head.next):
            for i in range(0, len(self.head.next)):
                temp = prevNodes[i].next[i]
                prevNodes[i].next[i] = newNode
                newNode.next[i] = temp 
            for j in range(len(self.head.next), h):
                self.head.next += [newNode]
                newNode.next[j] = None
        else:
            for i in range (0, h):
                temp = prevNodes[i].next[i]
                prevNodes[i].next[i] = newNode
                newNode.next[i] = temp 

l = SkipList()
nodes = [1,4,5,7,8,9,11,16]
for n in nodes:
    l.insert(n)
# Answer to Question 5 in output below
print("Height of Skip List: ", len(l.head.next))