from requests import Session
from zeep import Client
from zeep.transports import Transport


class Transliteration:
    """
    Transliteration is the conversion of text from one script to another while preserving
    the same pronunciation. The Transliterator provides translation of named entities,
    such as human and city names, from English to Arabic and vice versa—and conversion of text
    from Romanized Arabic to native Arabic script.
    """

    def __init__(self, app_id):
        self._WSDL = "https://atks.microsoft.com/Services/TransliteratorService.svc"
        self._PORT = "HTTPS_ITransliteratorService"
        session = Session()
        session.verify = False
        trasnport = Transport(session=session)
        self._client = Client(wsdl=self._WSDL, port_name=self._PORT, transport=trasnport)
        self._app_id = app_id

    def IsRomanizedArabic(self, text):
        """
        :param text: string
        :return: ns1:TransliteratorErrorCode, isRomanizedArabic: xsd:boolean, confidence: xsd:double
        """
        result = self._client.service.IsRomanizedArabic(self._app_id, text)
        return result

    def ReportCandidateSelection(self, word, context, transliteration):
        """
        :param word: string
        :param context: string
        :param transliteration: string
        :return: ns1:TransliteratorErrorCode
        """
        result = self._client.service.ReportCandidateSelection(self._app_id, word, context, transliteration)
        return result

    def SuggestMissingTransliteration(self, word, context, transliteration):
        """
        :param word: string
        :param context: string
        :param transliteration: string
        :return: ns1:TransliteratorErrorCode
        """
        result = self._client.service.SuggestMissingTransliteration(self._app_id, word, context, transliteration)
        return result

    def TransliterateText(self, in_text, lang_pair):
        """
        :param in_text: string
        :param lang_pair: LanguagePair
        :return: ns1:TransliteratorErrorCode, outText: xsd:string
        """
        result = self._client.service.TransliterateText(self._app_id, in_text, lang_pair)
        return result

    def TransliterateWords(self, tokens, lang_pair):
        """
        :param tokens: list of strings
        :param lang_pair: LanguagePair
        :return: ns1:TransliteratorErrorCode, outTokens: ns1:ArrayOfString
        """
        result = self._client.service.TransliterateWords(self._app_id, tokens, lang_pair)
        return result
