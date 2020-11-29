from xml.dom.minidom import Element


class LexicalUnit:

    synSetId: str
    frameElements: list

    def __init__(self, id: str, root: Element):
        self.frameElements = []
        self.synSetId = id
        for element in root:
            self.frameElements.append(element.text)

    def getSynSetId(self) -> str:
        return self.synSetId

    def size(self) -> int:
        return len(self.frameElements)

    def getFrameElements(self) -> list:
        return self.frameElements
