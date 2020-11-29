class FrameElement(object):

    __frameElementType: str
    __frame: str
    __id: str

    def __init__(self, frameElement: str):
        """
        A constructor of FrameElement class which takes frameElement string which is in the form of frameElementType$id
        and parses this string into frameElementType and id. If the frameElement string does not contain '$' then the
        constructor return a NONE type frameElement.

        PARAMETERS
        ----------
        frameElement : str
            Argument string containing the argumentType and id
        """
        if "$" in frameElement:
            self.__frameElementType = frameElement[0:frameElement.index("$")]
            self.__frame = frameElement[frameElement.index("$") + 1:frameElement.rindex("$")]
            self.__id = frameElement[frameElement.rindex("$") + 1:]
        else:
            self.__frameElementType = "NONE"

    def initWithId(self, frameElementType: str, frame: str, _id: str):
        """
        Another constructor of FrameElement class which takes frameElementType and id as inputs and initializes corresponding
        attributes

        PARAMETERS
        ----------
        frameElementType : str
            Type of the argument
        _id : str
            Id of the argument
        """
        self.__frameElementType = frameElementType
        self.__frame = frame
        self.__id = _id

    def getFrameElementType(self) -> str:
        """
        Accessor for frameElementType.

        RETURNS
        -------
        str
            frameElementType.
        """
        return self.__frameElementType

    def getFrame(self) -> str:
        """
        Accessor for frame.

        RETURNS
        -------
        str
            frame.
        """
        return self.__frame

    def getId(self) -> str:
        """
        Accessor for id.

        RETURNS
        -------
        str
            id.
        """
        return self.__id

    def __str__(self) -> str:
        """
        __str__ converts an Argument to a string. If the frameElementType is "NONE" returns only "NONE", otherwise
        it returns frameElement string which is in the form of frameElementType$id

        RETURNS
        -------
        str
            string form of argument
        """
        if self.__frameElementType == "NONE":
            return self.__frameElementType
        else:
            return self.__frameElementType + "$" + self.__frame + "$" + self.__id
