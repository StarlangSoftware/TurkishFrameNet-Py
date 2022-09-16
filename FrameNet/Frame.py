class Frame:
    __name: str
    __lexical_units: list
    __frame_elements: list

    def __init__(self, name: str):
        self.__lexical_units = []
        self.__frame_elements = []
        self.__name = name

    def addLexicalUnit(self, lexicalUnit: str):
        self.__lexical_units.append(lexicalUnit)

    def addFrameElement(self, frameElement: str):
        self.__frame_elements.append(frameElement)

    def lexicalUnitExists(self, synSetId: str) -> bool:
        return synSetId in self.__lexical_units

    def getLexicalUnit(self, index: int) -> str:
        return self.__lexical_units[index]

    def getFrameElement(self, index: int) -> str:
        return self.__frame_elements[index]

    def lexicalUnitSize(self) -> int:
        return len(self.__lexical_units)

    def frameElementSize(self) -> int:
        return len(self.__frame_elements)

    def getName(self) -> str:
        return self.__name

    def __repr__(self):
        return f"{self.__name} {self.__lexical_units} {self.__frame_elements}"
