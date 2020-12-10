import os
import xml.etree.ElementTree
from FrameNet.Frame import Frame


class FrameNet:

    frames: list

    def __init__(self):
        self.frames = []
        root = xml.etree.ElementTree.parse("../framenet.xml").getroot()
        for frameNode in root:
            frame = Frame(frameNode.attrib["NAME"])
            for childNode in frameNode:
                if childNode.tag == "LEXICAL_UNITS":
                    for lexicalUnit in childNode:
                        frame.addLexicalUnit(lexicalUnit.text)
                elif childNode.tag == "FRAME_ELEMENTS":
                    for frameElement in childNode:
                        frame.addFrameElement(frameElement.text)
            self.frames.append(frame)

    def lexicalUnitExists(self, synSetId: str) -> bool:
        for frame in self.frames:
            if frame.lexicalUnitExists(synSetId):
                return True
        return False

    def getFrames(self, synSetId: str) -> list:
        result = []
        for frame in self.frames:
            if frame.lexicalUnitExists(synSetId):
                result.append(frame)
        return result

    def size(self) -> int:
        return len(self.frames)

    def getFrame(self, index: int) -> Frame:
        return self.frames[index]
