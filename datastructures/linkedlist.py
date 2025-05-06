#Done...Code grade issues.
from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Iterator, Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.count = 0
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        llist = LinkedList(data_type=data_type)
        for item in sequence:
            llist.append(item)
        return llist

    def append(self, item: T) -> None:
        if type(item) != self.data_type:
            raise TypeError("Data is the wrong type")
        node = LinkedList.Node(data=item)

        if self.empty:
            self.head = self.tail = node
        else:
            node.previous = self.tail
            if self.tail:
                self.tail.next = node
            self.tail = node
        self.count +=1

    def prepend(self, item: T) -> None:
       if type(item) != self.data_type:
            raise TypeError("Data is the wrong type")
       new_node = LinkedList.Node(data= item)
       new_node.next = self.head
       if self.head:
           self.head.previous = new_node
       self.head = new_node
       self.count += 1
    def insert_before(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type) or not isinstance(item, self.data_type):
            raise TypeError("Item needs to be the same type")
        travel = self.head
        while travel and travel.data != target:
            travel = travel.next
        if travel is None:
            raise ValueError(f'Target value {target} not found in the linked list :(')
        new_node = LinkedList.Node(data=item, next = travel, previous= travel.previous)
        travel.previous.next = new_node
        travel.previous = new_node
        self.count += 1
        
    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(target, self.data_type) or not isinstance(item, self.data_type):
            raise TypeError("Item needs to be the same type")
        travel = self.head
        while travel and travel.data != target:
            travel = travel.next
        if travel is None:
            raise ValueError(f'Target value {target} not found in the linked list :(')
        new_node = LinkedList.Node(data=item, next = travel.next, previous= travel)
        travel.next.previous = new_node
        travel.next= new_node
        self.count += 1

    def remove(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError("Item needs to be the same type")
        travel = self.head
        while travel and travel.data != item:
            travel = travel.next
        if travel is None:
            raise ValueError(f'Item: {item} not found in the linked list :(')
        if travel is self.head:
            self.pop_front()
            return
        elif travel is self.tail:
            self.pop()
            return
        else:
            travel.next.previous = travel.previous
            travel.previous.next = travel.next
            travel.previous = None
            travel.next = None
        self.count -= 1
        
    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError("Item needs to be the same type")
        travel = self.head
        while item in self:
            self.remove(item)
        

    def pop(self) -> T:
        if self.tail is None:
            raise IndexError('There is no tail to pop')
        data = self.tail.data
        self.count -= 1
        if self.head is not self.tail:
            self.tail = self.tail.previous
            self.tail.next = None
            return data
        else:
            self.clear()
            return data


    def pop_front(self) -> T:
        if self.head is None:
            raise IndexError('There is no head to pop')
        data = self.head.data
        self.count -= 1
        if self.head is not self.tail:
            self.head = self.head.next
            self.head.previous = None
            return data
        else:
            self.clear()
            return data


    @property
    def front(self) -> T:
        if self.head is None:
            raise IndexError('Head is None')
        return self.head.data

    @property
    def back(self) -> T:
        if self.tail is None:
            raise IndexError('Tail is None')

        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
       return self.count

    def clear(self) -> None:
        self.head = self.tail = None
        self.count = 0

    def __contains__(self, item: T) -> bool:
        travel = self.head
        while travel:
            if travel.data == item:
                return True
            travel = travel.next
        return False

    def __iter__(self) -> Iterator[T]:
        self._travel_node = self.head
        return self

    def __next__(self) -> T:
        if self._travel_node is None:
            raise StopIteration
        
        data = self._travel_node.data
        self._travel_node = self._travel_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        travel = self.tail
        while travel:
            yield travel.data
            travel = travel.previous

    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList) or len(other) != len(self):
            return False
        travel_self = self.head
        travel_other = other.head
        while travel_self and travel_other:
            if travel_self.data != travel_other.data:
                return False
            travel_self = travel_self.next
            travel_other = travel_other.next
        return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')