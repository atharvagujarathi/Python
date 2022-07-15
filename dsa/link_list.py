#  dyanamic data structures made up of nodes.
# data in a linked list is not stored in a contigous memory locations.
#  insertion and deletion is easier in a linked list.
#  it can be used in a abstract data types like stack, queue, link.

# Disadvantages = 
#  some extra memory locations are required.
#  efficient random access is not possible.

# Types = 
#  1. single linked list
#  2. double linked list
#  3. circular linked list
#  4. sorted linked list
#  5. linked list with header node


#  1. Single linked list =


# code for starting node is None or empty.

# class Node:
#     def __init__(self, value):
#         self.info = value
#         self.link = None

# class singleLinkList:
#     def __init__(self):
#         self.start: None 

      




class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

# code for display the list.        

class singleLinkList:
    def __init__(self):
        self.start = None


    def display_list(self):
        if self.start is None:
            print("list is empty")
            return
        else:
            print("List is : ")
            p = self.start
            while p is not None:
                print(p.info , " ", end=" ")
                p = p.link
            print()  

# code for count nodes.
    def count_nodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("the number of nodes is", n)


# code for search a nodes.
    def search_node(self, x):
        position = 1
        p = self.start
        while p is not None:
            if position == x:
                print(x, " is a position ", position)
                return True
                position += 1
                p = p.link
            else:
                print(x, "do not found in the list")
                return False    











list = singleLinkList()

# list.create_list()

while True:
    print("1. Display list.")
    print("2. count nodes in the list.")
    print("3. search node in the list")

    option = int(input("Enter your choice"))

    if option == 1:
        list.display_list()
    elif option == 2:
        list.count_nodes()
    elif option == 3:
        data = int(input("enter the number to be searched"))
        list.search_node(data)  

        

                   

