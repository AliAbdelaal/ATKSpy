class Diacritizer:
    """ The Arabic Automatic Diacritizer component performs vowel restoration on input Arabic text.
     The main objective of the Diacritizer is to insert both missing vowels—diacritics—of the stem
     and the missing vowel for the case ending. """

    def __init__(self, app_id):
        import zeep
        self.__WSDL = "https://atks.microsoft.com/Services/DiacritizerService.svc"
        self.__PORT = "HTTPS_IArabicDiacritizerService"
        self.__client = zeep.Client(wsdl=self.__WSDL, port_name=self.__PORT)
        self.__app_id = app_id

    def Diacritize(self, text, enable_case_ending, enable_quran):
        """
        :param text: string
        :param enable_case_ending: boolean
        :param enable_quran: boolean
        :return: ns1:DiacritizerErrorCode, diacritizedText: xsd:string
        """
        result = self.__client.service.Diacritize(self.__app_id, text, enable_case_ending, enable_quran)
        return result

    def DiacritizeWithTraceInfo(self, text, enable_case_ending, enable_quran, enable_classics):
        """
        :param text: string
        :param enable_case_ending: boolean
        :param enable_quran: boolean
        :param enable_classics: boolean
        :return: ns1:DiacritizerErrorCode, diacritizedText: xsd:string, traceInfo: ns1:ArrayOfWordTraceInfo
        """
        result = self.__client.service.DiacritizeWithTraceInfo(self.__app_id, text, enable_case_ending, enable_quran,
                                                               enable_classics)
        return result

    def ReportWrongDiacritization(self, word, context, suggested_diacritized_word):
        """
        :param word: string
        :param context: string
        :param suggested_diacritized_word: string
        :return: ns1:DiacritizerErrorCode
        """
        result = self.__client.service.ReportWrongDiacritization(self.__app_id, word, context, suggested_diacritized_word)
        return result

    def SuggestDiacritization(self, word, context, suggested_diacritized_word):
        """
        :param word: string
        :param context: string
        :param suggested_diacritized_word: string
        :return: ns1:DiacritizerErrorCode
        """
        result = self.__client.service.SuggestDiacritization(self.__app_id, word, context, suggested_diacritized_word)
        return result
