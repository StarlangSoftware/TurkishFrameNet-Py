import xml.etree.ElementTree

import pkg_resources

from FrameNet.Frame import Frame


class FrameNet:

    __frames: list

    def __init__(self):
        self.__frames = []
        root = xml.etree.ElementTree.parse(pkg_resources.resource_filename(__name__, 'data/framenet.xml')).getroot()
        for frame_node in root:
            frame = Frame(frame_node.attrib["NAME"])
            for child_node in frame_node:
                if child_node.tag == "LEXICAL_UNITS":
                    for lexical_unit in child_node:
                        frame.addLexicalUnit(lexical_unit.text)
                elif child_node.tag == "FRAME_ELEMENTS":
                    for frame_element in child_node:
                        frame.addFrameElement(frame_element.text)
            self.__frames.append(frame)

    def lexicalUnitExists(self, synSetId: str) -> bool:
        for frame in self.__frames:
            if frame.lexicalUnitExists(synSetId):
                return True
        return False

    def getFrames(self, synSetId: str) -> list:
        result = []
        for frame in self.__frames:
            if frame.lexicalUnitExists(synSetId):
                result.append(frame)
        return result

    def size(self) -> int:
        return len(self.__frames)

    def getFrame(self, index: int) -> Frame:
        return self.__frames[index]
