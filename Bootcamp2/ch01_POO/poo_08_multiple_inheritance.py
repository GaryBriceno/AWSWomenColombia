from ch01_POO.poo_05_objects_inheritance import Contact


class Emilable:
    email: str


class MailSender(Emilable):

    def send_mail(self, message: str) -> None:\
        print(f"Sending email to {self.name} from {self.email}")

# We wanted to add the functionality to our Contact class
# That allow send emails


class EmailableContact(Contact, MailSender):
    pass


e = EmailableContact("John B", "johnb@sloop.net")
print(Contact.all_contacts)
e.send_mail("Hello, test e-mail here")


# El manejo de la herencia multiple no es sencilla
# Pueden existir metodos con nombre similar,
# O como distinguir a que super clase se esta llamando con el metodo __init__()
