

class Pic:
    def __init__(self, orien: str, id: int, tags: set):
        __id = id
        __orien = orien
        __tags = tags

    def tags(self):
        return set(self.__tags)

    def id(self) -> int:
        return self.__id
