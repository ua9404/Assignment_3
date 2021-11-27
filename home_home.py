class Item:
# encapsulates item state
    __slots__ = ['__name', '__code', '__price']

    def __init__(self, name, code):
        self.__name = name
        self.__code = code
        self.__price = 0

class Home_categories:
# this class is used as the basket for shopping
    __slots__ = ['__garden_options', '__indoor_options', '__bathroom_options', '__base_service']

    def __init__(self, garden_options, indoor_options, bathroom_options):
        self.__garden_options = garden_options
        self.__indoor_options = indoor_options
        self.__bathroom_options = bathroom_options
        self.__base_service = 50

garden_option = {"p": ('3 pack garden flower', 5.0), "l": ('Hanging light wire', 10.0), "b": ('garden bench', 35.0), "n": ('None and Next', 0.0)}
indoor_option = {"t": ('Small table lamp', 5.0), "f": ('City picture frame', 7.0), "r": ('4x5 entry rug', 35.0), "n": ('None and Next (n)', 0.0)}
bathroom_option = {"w": ('Weighing scale', 2.0), "a": ('Towel', 3.0), "y": ('Brush holder', 6.0), "n": ('None and Next (n)', 0.0)}

# The below function prints a welcome address to the users
def print_welcome():
    print("Welcome to Home Ideas Center, where all orders include a new home feeling!")
    print("For your new Home space ... ")

print_welcome()


# The below function will print out the available options for garden decoration
def print_garden_options():
    print("Garden Options: ")
    print(" 3 pack garden flower (p): $5.0 ")
    print(" Hanging light wire (l): $10.0 ")
    print(" garden bench (b): $35.0 ")

print_garden_options()    
