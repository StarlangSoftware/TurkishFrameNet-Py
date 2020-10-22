from xml.dom.minidom import Element
from FrameNet.LexicalUnit import LexicalUnit


class Frame:
    name: str
    lexicalUnits: list

    def __init__(self, name: str, root: Element):
        self.lexicalUnits = []
        self.name = name
        for lexicalUnit in root:
            self.lexicalUnits.append(LexicalUnit(lexicalUnit.attrib["ID"], lexicalUnit))

    def getLexicalUnit(self, index: int) -> LexicalUnit:
        return self.lexicalUnits[index]

    def size(self) -> int:
        return len(self.lexicalUnits)

    def getName(self) -> str:
        return self.name
