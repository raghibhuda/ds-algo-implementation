"""Dynamic Array implementation on Python"""
import ctypes


class DynamicArray(object):
    def __init__(self):
        self.length = 0  # Initial length of the array
        self.capacity = 1  # Initial capacity of the array
        self.array = self.create_array(self.capacity)

    def __len__(self):
        """
        :return: length of the dynamic array
        """
        return self.length

    def __getitem__(self, index):
        """
        :param index:
        :return:element of the given index
        """
        if not (0 <= index < self.length):
            return IndexError("Invalid index")
        return self.array[index]

    def append(self, element):
        """
        Append new element at the end of array
        :param element:
        :return:
        """
        if self.length == self.capacity:
            self.resize(2 * self.capacity)  # Double the capacity of the array if it's reached to it's length
        self.array[self.length] = element
        self.length += 1

    def insert_at(self, element, index):
        """
        Insert an element at a given index
        :param element:
        :param index:
        :return:
        """
        if index < 0 or index > self.length:
            return IndexError("Invalid index")

        if self.length == self.capacity:
            self.resize(2 * self.capacity)
        for i in range(self.length-1, index-1, -1):
            self.array[i+1] = self.array[i]
        self.array[index] = element
        self.length += 1

    def delete_at(self, index):
        """
        Delete element from array on given index
        :param index:
        :return:
        """
        if self.length == 0:
            print("Array is already empty")
            return
        if index < 0 or index > self.length:
            return IndexError("Invalid index")
        if index == self.length - 1:
            self.array[index] = 0
            self.length -= 1
            return
        for i in range(index, self.length-1):
            self.array[i] = self.array[i+1]
        self.array[self.length-1] = 0
        self.length -= 1

    def pop(self):
        """
        Pop out the last element from array
        :return:
        """
        if self.length == 0:
            print("Array is already empty")
        self.array[self.length-1] = 0
        self.length -= 1

    def resize(self, new_capacity):
        """
        Resize the old small array to bigger array so that new elements have enough space to fit in.
        :param new_capacity:
        :return:
        """
        bigger_array = self.create_array(new_capacity)

        for i in range(self.length):
            bigger_array[i] = self.array[i]
        self.array = bigger_array
        self.capacity = new_capacity

    def __str__(self):
        """
        To make array representable
        :return:
        """
        elements = ""
        for i in range(self.length):
            elements = elements + str(self.array[i]) + ","
        elements = "[" + elements[:-1] + "]"
        return elements

    @staticmethod
    def create_array(capacity):
        """
        :param capacity:
        :return: new array object with new capacity
        """
        return (capacity * ctypes.py_object)()


if __name__ == "__main__":
    test_array = DynamicArray()
    test_array.append(23)
    test_array.append(2)
    test_array.append(203)
    test_array.append(3)
    print(len(test_array))
    print(test_array)
