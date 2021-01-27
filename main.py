
"""
 Determine if Brackets are Balanced

from stack import Stack


# parent meaning parentheses



def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_parent_balanced(parent_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(parent_string) and is_balanced:
        parent = parent_string[index]
        if parent in "([{":
            s.push(parent)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, parent):
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(is_parent_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_parent_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_parent_balanced("[][]"))


"""
"""
Reverse String

from stack import Stack


def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push((input_str[i]))
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


stack = Stack()

input_str = "!ayneK ot emocleW"
print(reverse_string(stack, input_str))

"""
"""

Conversion of decimal numbers to binary using stack
from stack import Stack
def convert_int_to_bin(dec_num):

    if dec_num == 0:
        return 0
    s = Stack()


    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(convert_int_to_bin(242))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))

print(int(convert_int_to_bin(56),2)==56)

"""

# Singly linked lists and operations

# initializing node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# initializing Linked List

class LinkedList:
    def __init__(self):
        self.head = None

# printing  List

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

# Appending(Inserting) a node at the end of the list

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next =new_node

# Prepending(Inserting a node at the begining of the list)

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head =new_node
#### To investigate further
# Inserting after a node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node doesn't exist.")
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

# Deleting Node by value

    def delete_node(self, key):

        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head =cur_node.next
            cur_node = None
            return
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None


# Deleting Node by position

    def delete_node_at_pos(self, pos):
        if  self.head:
            cur_node = self.head

        if pos == 0:
            self.head = cur_node
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node in None:
            return

        prev.next = cur_node.next
        cur_node = None
# Calculating length of a linked list

    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.delete_node("B")
llist.delete_node("E")

llist.print_list()
llist.insert_after_node(llist.head.next, "D")
print(llist.len_iterative())
# llist.print_list()

