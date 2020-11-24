import unittest

from FrameNet.FrameElement import FrameElement


class FrameElementTest(unittest.TestCase):

    def test_FrameElement(self):
        frameElement = FrameElement("Agent$TUR10-0100230")
        self.assertEqual("Agent", frameElement.getFrameElementType())
        self.assertEqual("TUR10-0100230", frameElement.getId())
        self.assertEqual("Agent$TUR10-0100230", frameElement.__str__())


if __name__ == '__main__':
    unittest.main()
