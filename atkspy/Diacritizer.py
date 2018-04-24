from requests import Session
from zeep import Client
from zeep.transports import Transport


class Diacritizer:
    """ The Arabic Automatic Diacritizer component performs vowel restoration on input Arabic text.
     The main objective of the Diacritizer is to insert both missing vowels—diacritics—of the stem
     and the missing vowel for the case ending. """

    def __init__(self, app_id):
        self._WSDL = "https://atks.microsoft.com/Services/DiacritizerService.svc"
        self._PORT = "HTTPS_IArabicDiacritizerService"
        session = Session()
        session.verify = False
        trasnport = Transport(session=session)
        self._client = Client(wsdl=self._WSDL, port_name=self._PORT, transport=trasnport)
        self._app_id = app_id

    def Diacritize(self, text, enable_case_ending, enable_quran):
        """
        :param text: string
        :param enable_case_ending: boolean
        :param enable_quran: boolean
        :return: ns1:DiacritizerErrorCode, diacritizedText: xsd:string
        """
        result = self._client.service.Diacritize(self._app_id, text, enable_case_ending, enable_quran)
        return result

    def DiacritizeWithTraceInfo(self, text, enable_case_ending, enable_quran, enable_classics):
        """
        :param text: string
        :param enable_case_ending: boolean
        :param enable_quran: boolean
        :param enable_classics: boolean
        :return: ns1:DiacritizerErrorCode, diacritizedText: xsd:string, traceInfo: ns1:ArrayOfWordTraceInfo
        """
        result = self._client.service.DiacritizeWithTraceInfo(self._app_id, text, enable_case_ending, enable_quran,
                                                               enable_classics)
        return result

    def ReportWrongDiacritization(self, word, context, suggested_diacritized_word):
        """
        :param word: string
        :param context: string
        :param suggested_diacritized_word: string
        :return: ns1:DiacritizerErrorCode
        """
        result = self._client.service.ReportWrongDiacritization(self._app_id, word, context, suggested_diacritized_word)
        return result

    def SuggestDiacritization(self, word, context, suggested_diacritized_word):
        """
        :param word: string
        :param context: string
        :param suggested_diacritized_word: string
        :return: ns1:DiacritizerErrorCode
        """
        result = self._client.service.SuggestDiacritization(self._app_id, word, context, suggested_diacritized_word)
        return result
