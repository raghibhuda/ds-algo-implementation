"""
Singly liked list implementation on Python3
"""


class Node(object):
    """
    Sample node object which receives a value (number, strings etc)
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    """
    Primarily initiated linked list object head will be none
    """
    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        """
        :return: String representation of the linked list
        ex: 1-->2-->3-->None
        """
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(current_node.value)
            current_node = current_node.next
        nodes.append('None')

        return '-->'.join(map(str, nodes))

    def insert_node_at_beginning(self, node):
        """
        Receive a node object and put it to as the head of the liked list
        :param node:
        :return:
        """
        node.next = self.head
        self.head = node

    def insert_node(self, node):
        """
        Receive a node object and put it at the end of the liked list
        :param node:
        :return:
        """
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node


if __name__ == '__main__':
    linked_list = LinkedList()
    second_node = Node(4)
    third_node = Node(6)
    linked_list.insert_node(second_node)
    linked_list.insert_node(third_node)
    new_node = Node(78)
    linked_list.insert_node_at_beginning(new_node)
    print(repr(linked_list))
