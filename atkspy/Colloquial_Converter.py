from requests import Session
from zeep import Client
from zeep.transports import Transport


class Colloquial_Converter:
    """The Colloquial Converter provides translation of Egyptian colloquial text
     into the equivalent Modern Standard Arabic text along with rich mapping information.
      Both Sarf and the Colloquial Morphological Analyzer are used internally to provide the
      final translation."""

    def __init__(self, app_id):
        self._WSDL = "https://atks.microsoft.com/Services/ColloquialConverterService.svc"
        self._PORT = "HTTPS_IColloquialConverterService"
        session = Session()
        session.verify = False
        trasnport = Transport(session=session)
        self._client = Client(wsdl=self._WSDL, port_name=self._PORT, transport=trasnport)
        self._app_id = app_id

    def ConvertText(self, in_text):
        """
        :param in_text: string
        :return: ns1:ColloquialConverterErrorCode, outText: xsd:string

        """
        result = self._client.service.ConvertText(self._app_id, in_text)
        return result

    def ConvertTextWithDetails(self, in_text):
        """
        :param in_text: string
        :return: ns1:ColloquialConverterErrorCode, outText: xsd:string, words: ns1:ArrayOfColloquialWordMap

        """
        result = self._client.service.ConvertTextWithDetails(self._app_id, in_text)
        return result

    def ConvertWord(self, word):
        """
        :param word: string
        :return: ns1:ColloquialConverterErrorCode, translations: ns1:ArrayOfString
        """
        result = self._client.service.ConvertWord(self._app_id, word)
        return result

    def SuggestConversion(self, in_text, suggested_text):
        """
        :param in_text: string
        :param suggested_text: string
        :return: ns1:ColloquialConverterErrorCode
        """
        result = self._client.service.SuggestConversion(self._app_id, in_text, suggested_text)
        return result
