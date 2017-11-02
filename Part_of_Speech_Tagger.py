class Part_of_Speech_Tagger:
    """
    The Part of Speech (POS) Tagger is responsible for identifying the correct part of speech for each token
    of any given Arabic sentence.
    The POS Tagger relies heavily on the Morphological Analyzer to extract the relevant morpho-syntactic
    features for the input words.
    The POS Tagger also relies on the Auto-Corrector to correct input text.
    """

    def __init__(self, app_id):
        import zeep
        self.__WSDL = "https://atks.microsoft.com/Services/POSTaggerService.svc"
        self.__PORT = "HTTPS_IPOSTaggerService"
        self.__client = zeep.Client(wsdl=self.__WSDL, port_name=self.__PORT)
        self.__app_id = app_id

    def ReportWrongTag(self, word, context):
        """
        :param word: string
        :param context: string
        :return: ns1:POSTaggerErrorCode
        """
        result = self.__client.service.ReportWrongTag(self.__app_id, word, context)
        return result
    def SuggestTag(self, word, context, suggested_tag):
        """
        :param word: string
        :param context: string
        :param suggested_tag: string
        :return: ns1:POSTaggerErrorCode
        """
        result = self.__client.service.SuggestTag(self.__app_id, word, context, suggested_tag)
        return result
    def TagText(self, text, auto_correct):
        """
        :param text: string
        :param auto_correct: boolen
        :return: ns1:POSTaggerErrorCode, taggedWords: ns1:ArrayOfTaggedWord
        """
        result = self.__client.service.TagText(self.__app_id, text, auto_correct)
        return result

    def TagWords(self, words):
        """
        :param words: list of strings
        :return: ns1:POSTaggerErrorCode, taggedWords: ns1:ArrayOfString
        """
        result = self.__client.service.TagWords(self.__app_id, words)
        return result
