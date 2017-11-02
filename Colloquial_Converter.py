class Colloquial_Converter:
    """The Colloquial Converter provides translation of Egyptian colloquial text
     into the equivalent Modern Standard Arabic text along with rich mapping information.
      Both Sarf and the Colloquial Morphological Analyzer are used internally to provide the
      final translation."""

    def __init__(self, app_id):
        import zeep
        self.__WSDL = "https://atks.microsoft.com/Services/ColloquialConverterService.svc"
        self.__PORT = "HTTPS_IColloquialConverterService"
        self.__client = zeep.Client(wsdl=self.__WSDL, port_name=self.__PORT)
        self.__app_id = app_id

    def ConvertText(self, in_text):
        """
        :param in_text: string
        :return: ns1:ColloquialConverterErrorCode, outText: xsd:string

        """
        result = self.__client.service.ConvertText(self.__app_id, in_text)
        return result

    def ConvertTextWithDetails(self, in_text):
        """
        :param in_text: string
        :return: ns1:ColloquialConverterErrorCode, outText: xsd:string, words: ns1:ArrayOfColloquialWordMap

        """
        result = self.__client.service.ConvertTextWithDetails(self.__app_id, in_text)
        return result

    def ConvertWord(self, word):
        """
        :param word: string
        :return: ns1:ColloquialConverterErrorCode, translations: ns1:ArrayOfString
        """
        result = self.__client.service.ConvertWord(self.__app_id, word)
        return result

    def SuggestConversion(self, in_text, suggested_text):
        """
        :param in_text: string
        :param suggested_text: string
        :return: ns1:ColloquialConverterErrorCode
        """
        result = self.__client.service.SuggestConversion(self.__app_id, in_text, suggested_text)
        return result
