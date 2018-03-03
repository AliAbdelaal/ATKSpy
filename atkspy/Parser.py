class Parser:
    """
    The Arabic Parser determines the grammatical structure of Arabic sentences,
    such as which groups of words combine to form phrases and which words are the subject or the object of a verb.
    The Parser relies heavily on the Arabic POS Tagger to identify the correct part of speech for each token
    in an input Arabic sentence, and the Arabic Named-Entity Recognizer to identify named entities in the input
    sentence after it has been corrected using the Arabic Auto-Corrector.
    """

    def __init__(self, app_id):
        import zeep
        self.__WSDL = "https://atks.microsoft.com/Services/ParserService.svc"
        self.__PORT = "HTTPS_IParserService"
        self.__client = zeep.Client(wsdl=self.__WSDL, port_name=self.__PORT)
        self.__app_id = app_id

    def Parse(self, in_text):
        """

        :param in_text: string
        :return: ns1:ParserErrorCode, parseTree: xsd:string, score: xsd:double
        """
        result = self.__client.service.Parse(self.__app_id, in_text)
        return result

    def SuggestParseTree(self, in_text, alternative_parse_tree):
        """
        :param in_text: string
        :param alternative_parse_tree: string
        :return: ns1:ParserErrorCode
        """
        result = self.__client.service.SuggestParseTree(self.__app_id, in_text, alternative_parse_tree)
        return result