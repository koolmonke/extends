from extends import __version__
from extends import extends


def test_version():
    assert __version__ == '0.3.0'


def test_extension():
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age

    @extends(Person)
    def print(self: Person) -> str:
        return f'{self.name}, {self.age} years old.'

    assert Person('Alice', 22).print() == 'Alice, 22 years old.'
