# In Python, we have two approaches to defining similar things:

# Duck typing: When two class definitions have the same attributes and methods,
# then instances of the two classes have the same protocol and can be used interchangeably.
# We often say, "When I see a bird that walks like a duck and swims like a duck and quacks like a duck,
# I call that bird a duck."

# Inheritance: When two class definitions have common aspects,
# a subclass can share common features of a superclass.
# The implementation details of the two classes may vary, but the classes should be interchangeable
# when we use the common features defined by the superclass.

# Abstract class: they aren't directly useable by themselves, but
# can be used through inheritance to create concrete class.
import abc

# Imagine we are creating a media player with
# third-party plugins.


class Medialoader(abc.ABC):

    @abc.abstractmethod
    def play(self) -> None:
        ...

    @property
    @abc.abstractmethod
    def ext(self) -> str:
        ...


print(Medialoader.__abstractmethods__)


class Wav(Medialoader):
    pass

try:
    x = Wav()
except Exception as e:
    print(str(e))


class Ogg(Medialoader):

    ext = ".ogg"

    def play(self):
        pass


try:
    o = Ogg()
    print(o)
except Exception as e:
    print(str(e))
