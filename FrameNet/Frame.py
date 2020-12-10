class Frame:
    name: str
    lexicalUnits: list
    frameElements: list

    def __init__(self, name: str):
        self.lexicalUnits = []
        self.frameElements = []
        self.name = name

    def addLexicalUnit(self, lexicalUnit: str):
        self.lexicalUnits.append(lexicalUnit)

    def addFrameElement(self, frameElement: str):
        self.frameElements.append(frameElement)

    def lexicalUnitExists(self, synSetId: str) -> bool:
        return synSetId in self.lexicalUnits

    def getLexicalUnit(self, index: int) -> str:
        return self.lexicalUnits[index]

    def getFrameElement(self, index: int) -> str:
        return self.frameElements[index]

    def lexicalUnitSize(self) -> int:
        return len(self.lexicalUnits)

    def frameElementSize(self) -> int:
        return len(self.frameElements)

    def getName(self) -> str:
        return self.name
