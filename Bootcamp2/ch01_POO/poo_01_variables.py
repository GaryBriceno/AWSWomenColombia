# Todo en python es un Objeto
# Todo objeto esta definido para ser la instancia de una clase.

# Instancia del objeto str
name = "Gary"
print(type(name))

# Una variable es una referencia a un objeto
my_variable = "Python"
print("instancia de str:", type(my_variable))

my_variable = 1
print("instancia de int:", type(my_variable))


def odd(n):
    return n % 2 != 0


# The hints consume storage, they have no runtime impact
# They are optionals
# It helps to understand your code
def typing_odd(n: int) -> bool:
    return n % 2 != 0


print(odd(10))
print(typing_odd(10))
# The mypy tool is commonly used to check the hints for consistency.

