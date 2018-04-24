from requests import Session
from zeep import Client
from zeep.transports import Transport


class Parser:
    """
    The Arabic Parser determines the grammatical structure of Arabic sentences,
    such as which groups of words combine to form phrases and which words are the subject or the object of a verb.
    The Parser relies heavily on the Arabic POS Tagger to identify the correct part of speech for each token
    in an input Arabic sentence, and the Arabic Named-Entity Recognizer to identify named entities in the input
    sentence after it has been corrected using the Arabic Auto-Corrector.
    """

    def __init__(self, app_id):
        self._WSDL = "https://atks.microsoft.com/Services/ParserService.svc"
        self._PORT = "HTTPS_IParserService"
        session = Session()
        session.verify = False
        trasnport = Transport(session=session)
        self._client = Client(wsdl=self._WSDL, port_name=self._PORT, transport=trasnport)
        self._app_id = app_id

    def Parse(self, in_text):
        """

        :param in_text: string
        :return: ns1:ParserErrorCode, parseTree: xsd:string, score: xsd:double
        """
        result = self._client.service.Parse(self._app_id, in_text)
        return result

    def SuggestParseTree(self, in_text, alternative_parse_tree):
        """
        :param in_text: string
        :param alternative_parse_tree: string
        :return: ns1:ParserErrorCode
        """
        result = self._client.service.SuggestParseTree(self._app_id, in_text, alternative_parse_tree)
        return result