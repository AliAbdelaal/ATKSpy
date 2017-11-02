class Transliteration:
    """
    Transliteration is the conversion of text from one script to another while preserving
    the same pronunciation. The Transliterator provides translation of named entities,
    such as human and city names, from English to Arabic and vice versa—and conversion of text
    from Romanized Arabic to native Arabic script.
    """

    def __init__(self, app_id):
        import zeep
        self.__WSDL = "https://atks.microsoft.com/Services/TransliteratorService.svc"
        self.__PORT = "HTTPS_ITransliteratorService"
        self.__client = zeep.Client(wsdl=self.__WSDL, port_name=self.__PORT)
        self.__app_id = app_id

    def IsRomanizedArabic(self, text):
        """
        :param text: string
        :return: ns1:TransliteratorErrorCode, isRomanizedArabic: xsd:boolean, confidence: xsd:double
        """
        result = self.__client.service.IsRomanizedArabic(self.__app_id, text)
        return result

    def ReportCandidateSelection(self, word, context, transliteration):
        """
        :param word: string
        :param context: string
        :param transliteration: string
        :return: ns1:TransliteratorErrorCode
        """
        result = self.__client.service.ReportCandidateSelection(self.__app_id, word, context, transliteration)
        return result

    def SuggestMissingTransliteration(self, word, context, transliteration):
        """
        :param word: string
        :param context: string
        :param transliteration: string
        :return: ns1:TransliteratorErrorCode
        """
        result = self.__client.service.SuggestMissingTransliteration(self.__app_id, word, context, transliteration)
        return result

    def TransliterateText(self, in_text, lang_pair):
        """
        :param in_text: string
        :param lang_pair: LanguagePair
        :return: ns1:TransliteratorErrorCode, outText: xsd:string
        """
        result = self.__client.service.TransliterateText(self.__app_id, in_text, lang_pair)
        return result

    def TransliterateWords(self, tokens, lang_pair):
        """
        :param tokens: list of strings
        :param lang_pair: LanguagePair
        :return: ns1:TransliteratorErrorCode, outTokens: ns1:ArrayOfString
        """
        result = self.__client.service.TransliterateWords(self.__app_id, tokens, lang_pair)
        return result
