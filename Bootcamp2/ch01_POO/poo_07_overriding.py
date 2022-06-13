from ch01_POO.poo_05_objects_inheritance import Contact


class Friend(Contact):

    def __init__(self, name: str, email: str, phone: str) -> None:
        self.name = name
        self.email = email
        self.phone = phone


class BestFriend(Contact):

    def __init__(self, name: str, email: str, phone: str) -> None:
        # The use of the word super, allow us to execute the original __init__() method
        # This super method could be use in any part of this method
        super().__init__(name, email)
        self.phone = phone


f = BestFriend("Dusty", "Dusty@private.com", "555-1212")

print(Contact.all_contacts)