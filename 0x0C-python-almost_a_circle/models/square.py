#!/usr/bin/python3
"""The Square module"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """The Square class"""

    def def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y , id)

    def __str__(self):
        return '[{}] ({}) {}/{} - {}'.\
                format(type(self).__name__, self.id, self.x, self.y. self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args:
            if len(args) > 4:
                raise ValueError("Too many positional arguments")
            elif len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.id, self.size = args
            elif len(args) == 3:
                self.id, self.size, self.x = args
            elif len(args) == 4:
                self.id, self.size, self.x, self.y = args
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return ("id": self.id, "size": self.width,
                "x": self.x, "y": self.y)
