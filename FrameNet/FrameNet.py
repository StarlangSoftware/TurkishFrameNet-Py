import os
import xml.etree.ElementTree
from FrameNet.Frame import Frame


class FrameNet:

    frames: list

    def __init__(self, directory="../Frames/"):
        self.frames = []
        for r, d, f in os.walk(directory):
            for file in f:
                root = xml.etree.ElementTree.parse(os.path.join(r, file)).getroot()
                self.frames.append(Frame(file, root))

    def size(self) -> int:
        return len(self.frames)

    def getFrame(self, index: int) -> Frame:
        return self.frames[index]
