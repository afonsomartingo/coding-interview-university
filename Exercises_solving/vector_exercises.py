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
        self._capacity = capacity
        self._size = 0
        self._data = [None] * self._capacity  # Initialize with None instead of 0

    def size(self):
        """
        Return the number of items in the vector.
        """
        return self._size

    def capacity(self):
        """
        Return the current capacity of the vector.
        """
        return self._capacity

    def is_empty(self):
        """
        Return True if the vector is empty, False otherwise.
        """
        return self._size == 0

    def at(self, index):
        """
        Return the item at the given index. Raise IndexError if out of bounds.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
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
            raise IndexError("Index out of bounds")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        # Shift elements right
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = item
        self._size += 1

    def prepend(self, item):
        """
        Insert item at the beginning of the vector.
        """
        self.insert(0, item)

    def pop(self):
        """
        Remove and return the last item. Raise IndexError if empty.
        Resize if size is 1/4 of capacity.
        """
        if self.is_empty():
            raise IndexError("Vector is empty")
        item = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if self._size <= self._capacity // 4 and self._capacity > 16:
            self._resize(self._capacity // 2)
        return item

    def delete(self, index):
        """
        Delete item at index, shifting subsequent elements left.
        Raise IndexError if out of bounds.
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        # Shift elements left
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if self._size <= self._capacity // 4 and self._capacity > 16:
            self._resize(self._capacity // 2)

    def remove(self, item):
        """
        Remove all occurrences of item from the vector.
        """
        write_index = 0
        for read_index in range(self._size):
            if self._data[read_index] != item:
                self._data[write_index] = self._data[read_index]
                write_index += 1
        for i in range(write_index, self._size):
            self._data[i] = None
        removed_count = self._size - write_index
        self._size = write_index
        if self._size <= self._capacity // 4 and self._capacity > 16:
            self._resize(self._capacity // 2)
        return removed_count

    def find(self, item):
        """
        Return the index of the first occurrence of item, or -1 if not found.
        """
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1

    def _resize(self, new_capacity):
        """
        Private method to resize the underlying array to new_capacity.
        """
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def __str__(self):
        """
        Return a string representation of the vector.
        """
        return f"Vector(size={self._size}, capacity={self._capacity}, data={self._data[:self._size]})"

# Test code
if __name__ == "__main__":
    # Create a vector and test operations
    vec = Vector(initial_capacity=20)
    print(f"Empty vector: {vec}")
    print(f"Is empty? {vec.is_empty()}")
    
    # Test push
    vec.push(10)
    vec.push(20)
    vec.push(30)
    print(f"After pushing 10, 20, 30: {vec}")
    
    # Test insert
    vec.insert(1, 15)
    print(f"After inserting 15 at index 1: {vec}")
    
    # Test find
    print(f"Find 20: index {vec.find(20)}")
    print(f"Find 99: index {vec.find(99)}")
    
    # Test remove
    vec.remove(20)
    print(f"After removing 20: {vec}")
    
    # Test pop
    popped = vec.pop()
    print(f"Popped value: {popped}")
    print(f"After pop: {vec}")

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
vec_test.push(12)  # This will work since it adds to the end
vec_test.insert(0, 15)
vec_test.find(0)


print({vec_test.is_empty()})

vec_test.push(42)
print(vec_test.at(0))  
