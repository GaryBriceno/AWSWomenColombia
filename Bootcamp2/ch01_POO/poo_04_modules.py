# Modules are python files. The single file in our small program is a module.
# A Package is a collection of modules in a folder.
# We need to tell Python that a folder is a package, to do this, place a file in folder named __init__.py
# As soon as we import a module, any code at the module level is immediately executed.

# To solve this, we should always put out startup code in a function(conventionally called main())
# and only execute that function when we know we are running the module as a script,
# but not when our code is being imported from a different script.


class Point:
    pass


def main() -> None:
    p1 = Point()
    p2 = Point(3, 4)
    print(f'{p1} and {p2}')


if __name__ == "__main__":
    main()

# Every module has a __name__ special variable, that specifies the name of the module
# when it was imported. When the module is executed directly with:
# > python module.py
# it is never imported, so the __name__ is arbitrarily set to the "__main__" string.
