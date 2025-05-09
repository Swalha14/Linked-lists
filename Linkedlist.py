# Node class representing each element in the linked list
class Node:
    def __init__(self, data, next_node=None):
        self.data = data                # Holds the value of the node
        self.next_node = next_node      # Points to the next node in the list

    # Getter for next node
    def get_next(self):
        return self.next_node

    # Setter for next node
    def set_next(self, next_node):
        self.next_node = next_node

    # Getter for data
    def get_data(self):
        return self.data

    # Setter for data
    def set_data(self, data):
        self.data = data


# LinkedList class to manage the list
class LinkedList:
    def __init__(self):
        self.root = None   # Points to the first node (head) of the list
        self.size = 0      # Tracks the number of nodes in the list

    # Returns the number of elements in the list
    def get_size(self):
        return self.size

    # Adds a new node to the beginning of the list
    def add(self, data):
        new_node = Node(data, self.root)  # Create a new node pointing to the current root
        self.root = new_node              # Update root to new node
        self.size += 1                    # Increment size

    # Removes the first node containing the given data
    def remove(self, data):
        current_node = self.root
        previous_node = None

        while current_node:
            if current_node.get_data() == data:
                if previous_node:  # Node is not the root
                    previous_node.set_next(current_node.get_next())
                else:              # Node is the root
                    self.root = current_node.get_next()
                self.size -= 1
                return True  # Data found and removed
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        return False  # Data not found

    # Searches for a node with the given data
    def find(self, data):
        current_node = self.root
        while current_node:
            if current_node.get_data() == data:
                return data  # Data found
            current_node = current_node.get_next()
        return None  # Data not found


# Example usage
my_list = LinkedList()
my_list.add(51)
my_list.add(82)
my_list.add(124)

print("Size =", my_list.get_size())
my_list.remove(82)
print("Size =", my_list.get_size())
print(my_list.remove(124))
print("Size =", my_list.get_size())
print(my_list.find(51))
