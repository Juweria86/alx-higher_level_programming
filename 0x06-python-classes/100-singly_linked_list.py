#!/usr/bin/python3
"""defines a node of a singly linked list"""


class Node:
    """represents singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """sets data to avlue
        value: value to be set
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """retrieves next node"""

        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """sets value of next_node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """Initializes the singly linked list"""

        self.head = None

    def __str__(self):
        """prints list"""

        print_lList = ""
        temp = self.head
        while temp:
            print_lList += str(temp.data) + "\n"
            temp = temp.next_node
        return print_lList[:-1]

    def sorted_insert(self, value):
        """insert in a sorted fashion
        Args:
            value: what the value will be on the node
        """
        newnode = Node(value)
        if not self.head:
            self.head = newnode
            return
        if value < self.head.data:
            newnode.next_node = self.head
            self.head = newnode
            return
        temp = self.head
        while temp.next_node and temp.next_node.data < value:
            temp = temp.next_node
        if temp.next_node:
            newnode.next_node = temp.next_node
        temp.next_node = newnode
