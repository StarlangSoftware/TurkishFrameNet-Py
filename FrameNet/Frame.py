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

    def lexicalUnitExists(self, synSetId: str) -> bool:
        for lexicalUnit in self.lexicalUnits:
            if lexicalUnit.getSynSetId() == synSetId:
                return True
        return False

    def getLexicalUnitWithId(self, synSetId: str) -> LexicalUnit:
        for lexicalUnit in self.lexicalUnits:
            if lexicalUnit.getSynSetId() == synSetId:
                return lexicalUnit
        return None

    def removeLexicalUnit(self, synSetId: str):
        for lexicalUnit in self.lexicalUnits:
            if lexicalUnit.getSynSetId() == synSetId:
                self.lexicalUnits.remove(lexicalUnit)
                break

    def getLexicalUnit(self, index: int) -> LexicalUnit:
        return self.lexicalUnits[index]

    def size(self) -> int:
        return len(self.lexicalUnits)

    def getName(self) -> str:
        return self.name
