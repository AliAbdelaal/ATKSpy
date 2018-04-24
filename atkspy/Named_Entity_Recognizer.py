from requests import Session
from zeep import Client
from zeep.transports import Transport


class Named_Entity_Recognizer:
    """
    The Arabic Named Entity Recognizer (ANER) detects and classifies named entities in Arabic text.
    It classifies them into three categories: persons, locations, and organizations.
    It also provides a character index at which the named entity is located in the original text.

    ANER is adopting hybrid deterministic/probabilistic approaches for detecting and classifying named entities.
    The user can use the appropriate ANER setup per call, but using all the components provides the best quality.
    Processing article by article instead of sentence by sentence provides more contextual information,
    which contributes to higher detection and classification accuracy.

    ANER uses the Speller component to enhance the quality of the Arabic text before the named-entity-detection phase.
    The detection/classification accuracy depends on the quality of the input Arabic text.
    The user has the option to select between them depending on the error rate of the
    input text: Auto-Corrector for low error rate and Speller for high error rate.
    """

    def __init__(self, app_id):
        self._WSDL = "https://atks.microsoft.com/Services/ANERService.svc"
        self._PORT = "HTTPS_IANERService"
        session = Session()
        session.verify = False
        trasnport = Transport(session=session)
        self._client = Client(wsdl=self._WSDL, port_name=self._PORT, transport=trasnport)
        self._app_id = app_id

    # TODO :: build the options part
    def GetArabicNamedEntities(self, arabic_text, options=None):
        """
        :param arabic_text: string
        :param options: list of strings can take values of the following:
        'UseAllComponents' , 'UseAutoCorrector', 'UseSpeller'
        example : options = ['UseAllComponents']
        :return: ns1:NERErrorCode, namedEntities: ns1:ArrayOfNamedEntity
        """
        if options is None:
            options = ['UseAllComponents']
        result = self._client.service.GetArabicNamedEntities(self._app_id, arabic_text, options)
        return result

    def ReportWronglyDetectedNamedEntity(self, named_entity, context, wrong_named_entity):
        """
        :param named_entity: string
        :param context: string
        :param wrong_named_entity: string
        :return: ns1:NERErrorCode
        """

    def SuggestMissingNamedEntity(self, named_entity, context, named_entity_type):
        """
        :param named_entity: string
        :param context: string
        :param named_entity_type: string
        :return: ns1:NERErrorCode
        """
        result = self._client.service.SuggestMissingNamedEntity(self._app_id, named_entity, context, named_entity_type)
        return result
