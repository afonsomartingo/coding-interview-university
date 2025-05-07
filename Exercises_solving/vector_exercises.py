"""
Exercises: Implement a Vector (Dynamic Array) in Python

Follow the instructions in each function and class docstring to complete the implementation.
"""

class Vector:
    def __init__(self, initial_capacity=16):
        """
        Initialize the vector with a given initial capacity (default 16).
        If a larger starting number is given, use the next power of 2.
        """
        capacity = 16
        if initial_capacity > 16:
            i = 0
            while 2 ** i < initial_capacity:
                i += 1
            capacity = 2 ** i
        self._capacity = capacity  # capcity of the vector is the next power of 2
        self._size = 0  # number of elements in the vector
        self._data = [0] * self._capacity # initialize the vector with 0s



    def size(self):
        """
        Return the number of items in the vector.
        """
        print(f"The size of the vector is {self._size}")
        return self._size

    def capacity(self):
        """
        Return the current capacity of the vector.
        """
        print(f"The capacity of the vector is {self._capacity}")
        return self._capacity

    def is_empty(self):
        """
        Return True if the vector is empty, False otherwise.
        """
        if self._size == 0:
            return True
        else:
            return False

        pass

    def at(self, index):
        """
        Return the item at the given index. Raise IndexError if out of bounds.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index is out of bounds")
        return self._data[index]
    

    def push(self, item):
        """
        Add an item to the end of the vector, resizing if necessary.
        """
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = item
        self._size += 1

    def insert(self, index, item):
        """
        Insert item at the given index, shifting subsequent elements right.
        Raise IndexError if index is out of bounds.
        """
        if index < 0 or index > self._size:
            raise IndexError("index is out of bounds")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        # Desloca os elementos para a direita
        for i in range(self._size, index, -1): 
            self._data[i] = self._data[i - 1]
        self._data[index] = item
        self._size += 1

    def prepend(self, item):
        """
        Insert item at the beginning of the vector.
        """
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        # Shift elements to the right
        for i in range(self._size, 0, -1):
            self._data[i] = self._data[i - 1]
        self._data[0] = item
        self._size += 1
        

    def pop(self):
        """
        Remove and return the last item. Raise IndexError if empty.
        Resize if size is 1/4 of capacity.
        """
        if self._size == 0:
            raise IndexError("Vector is empty")
        
        item = self._data[self._size - 1]
        self._data[self._size - 1] = 0
        self._size -= 1

        if self._size <= self._capacity / 4:
            self._resize(self._capacity // 2)
        return item

    def delete(self, index):
        """
        Delete item at index, shifting subsequent elements left.
        Raise IndexError if out of bounds.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        for i in range(index, self._size-1):
            self._data[i] = self._data[i+1]
        self._size -= 1

    def remove(self, item):
        """
        Remove all occurrences of item from the vector.
        """
        i = 0
        while i < self._size:
            if self._data[i] == item:
                # Shift elements to the left
                for j in range(i, self._size - 1):
                    self._data[j] = self._data[j + 1]
                self._size -= 1  # Decrement size
            else:
                i += 1  # Only increment if no removal


    def find(self, item):
        """
        Return the index of the first occurrence of item, or -1 if not found.
        """
        pass

    def _resize(self, new_capacity):
        """
        Private method to resize the underlying array to new_capacity.
        """
        pass

# ---
# EXERCISES
# ---

# 1. Implement all methods in the Vector class above.
# 2. Write tests to check the following:
#    - Pushing, popping, inserting, and deleting elements
#    - Automatic resizing (doubling/halving)
#    - Edge cases (empty vector, out-of-bounds access)
# 3. Analyze the time and space complexity of each operation as comments.
# 4. (Bonus) Implement a method to shrink the capacity to fit the current size exactly. 


vec_test = Vector(initial_capacity=20)
vec_test.size()
vec_test.capacity()

print({vec_test.is_empty()})

vec_test.push(42)
print(vec_test.at(0))  # Agora deve funcionar e mostrar 42
