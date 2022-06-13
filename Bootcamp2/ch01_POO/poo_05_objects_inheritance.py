# Inheritance allow us to create "is-a" relationships between two o more classes
# abstracting common logic into superclasses and extending the superclass with
# specific details in each subclass.

# Basic inheritance
# Inheriting from buil-in types
# Multiple inheritance
# Polymorphism and duck typing

# In python every class are subclasses of the special built-in class named Object.
from typing import List


class MySubClass(object):
    pass


class AnotherSubClass:
    pass


class Contact:

    # Class variable
    all_contacts: List["Contact"] = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return(
            f"{self.__class__.__name__} ("
            f"{self.name!r}, {self.email!r} )"
        )


contact_01 = Contact("Dusty", "dusty@example.com")
contact_02 = Contact("Steve", "steve@example.com")

print(Contact.all_contacts)

# We have Contacts that are a suppliers too
# Suppliers make an order, however a Contact couldn't make and order.


class Supplier(Contact):

    def order(self, order: "Order") ->None:
        print(f"To send the order {order} to {self.name}")

