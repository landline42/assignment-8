class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return str(self.name) + ": " + str(self.number)

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    def __init__(self, size):
        self.size = size
        self.data = [None] * size


    def hash_function(self, key):
        """ Converts a string key into an array index. """
        total = 0

        #Take each character in the string and find their unicode value, then add them to the total
        for char in key:
            total += ord(char)

        return total % self.size  #mod the total and the table size to get the array index


    def insert(self, key, value):
        """ Inserts a new contact into the hash table. """
        #Check input
        if type(key) != str or type(value) != str:
            print("Error: invalid data type")
            return

        #Calculate the index for the key
        index = self.hash_function(key)

        #Fetch the linked list at that index
        current = self.data[index]

        #Check if there are no values at current position
        if self.data[index] is None:
            self.data[index] = Node(key, Contact(key, value))
            return
        
        #Iterate until value of None is reached
        while current:
            #Check for a duplicate
            if current.key == key:
                current.value.number = value
                return

            #Stop when last node is reached
            if current.next is None:
                break

            #Go to next node
            current = current.next

        #Add new node to the end of the list
        current.next = Node(key, Contact(key, value))


    def search(self, key):
        """ Searches for a contact by name. """
        #Check input
        if type(key) != str:
            print("Error: invalid data type")
            return None
        
        #Calculate the index for the key
        index = self.hash_function(key)

        #Fetch the linked list at that index
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None  #Return None if the contact isn't found


    def print_table(self):
        """ Prints the structure of the hash table. """
        print("\n--------------")
        print("Current table:")
        print("--------------")

        #Keep track of the index
        index = 0

        #Iterate through each entry and check if it contains a contact
        for index in range(self.size):
            current = self.data[index]

            #No contact at index
            if current == None:
                print(f"Index {index}: Empty")

            #Contact at index
            else:
                print(f"Index {index}: ", end="")  #Prevent a new line so contacts at the same index appear on the same line

                #Traverse the linked list if there are multiple nodes at one index
                while current:
                    print(f" - {current.value}", end="")  #Print contact info and prevent a new line
                    current = current.next
                
                print() #New line

#Test the functions
table = HashTable(10)
table.print_table()  #Print blank table

#Insert values
table.insert("Sue", "717-555-5555")
table.insert("Sam", "123-456-7890")
table.insert("Bob", "111-111-1111")

table.print_table()

#Search for a value
contact = table.search("Bob")
print("\nSearch result:", contact)

#Search for a contact not in the table
contact = table.search("Nobody")
print("Search result:", contact)

#Invalid search
contact = table.search(1)
print("Search result:", contact)

#Test Collisions
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")
table.print_table()

#Test duplicates
table.insert("Amy", "333-444-5555")

table.print_table()  #Amy's number is now updated

#Try inserting invalid data 
table.insert(1, 4)

