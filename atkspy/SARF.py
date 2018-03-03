class SARF:
    """
    Sarf provides automatic morphological analysis of Arabic words.
    It provides all possible morphological analyses for any given input Arabic word.
    Each analysis consists of the diacritized word and the morphological breakdown of
    the analysis in terms of prefixes, stem, and suffixes.
    The stem is further decomposed into its root and morphological pattern.
    Moreover, each analysis carries the part of speech and a set of morpho-syntactic
    features such as gender, number, transitivity, verb voice, and verb mood.
    """

    def __init__(self, app_id):
        import zeep
        self.__WSDL = "https://atks.microsoft.com/Services/SarfService.svc"
        self.__PORT = "HTTPS_ISarfService"
        self.__client = zeep.Client(wsdl=self.__WSDL, port_name=self.__PORT)
        self.__app_id = app_id

    def AnalyzeToken(self, word, ling_mode):
        """
        :param word: string
        :param ling_mode: LinguisticMode
        ling_mode can take values
            Classical	    0	Default operational mode (ignore direct speech analyses)
            Colloquial	    1	Not used
            Conversational	2	Keeps direct speech analyses (use this to generate all analyses including direct speech analyses)
        :return: ns1:SarfErrorCode, analyses: ns1:ArrayOfSarfAnalysis
        """
        result = self.__client.service.AnalyzeToken(self.__app_id, word, ling_mode)
        return result

    def AnalyzeTokensArray(self, words, ling_mode):
        """
        :param words: array of strings
        :param ling_mode: LinguisticMode
        ling_mode can take values
            Classical	    0	Default operational mode (ignore direct speech analyses)
            Colloquial	    1	Not used
            Conversational	2	Keeps direct speech analyses (use this to generate all analyses including direct speech analyses)
        :return: ns1:ArrayOfSarfErrorCode, analyses: ns1:ArrayOfArrayOfSarfAnalysis
        """
        result = self.__client.service.AnalyzeTokensArray(self.__app_id, words, ling_mode)
        return result

    def DecodeFeatures(self, binary_syntactic_features):
        """
        :param binary_syntactic_features: long
        :return: ns1:SarfErrorCode, detailedFeatures: ns1:MorphoSyntacticFeatures
        """
        result = self.__client.service.DecodeFeatures(self.__app_id, binary_syntactic_features)
        return result

    def EncodeFeatures(self, morpho_syntactic_features):
        """
        :param morpho_syntactic_features: long
        :return: ns1:SarfErrorCode, binarySyntacticFeatures: xsd:long
        """
        result = self.__client.service.EncodeFeatures(self.__app_id, morpho_syntactic_features)
        return result

    def GetAllDerivatives(self, analysis, ignore_affixation):
        """
        :param analysis: sarfAnalysis
        :param ignore_affixation: boolean
        :return: ns1:SarfErrorCode, analyses: ns1:ArrayOfSarfAnalysis
        """
        result = self.__client.service.GetAllDerivatives(self.__app_id, analysis, ignore_affixation)
        return result

    def GetDerivatives(self, analysis, pos, ignore_affixation):
        """
        :param analysis: SarfAnalysis
        :param pos: PartOfSpeech
        :param ignore_affixation: boolean
        :return: ns1:SarfErrorCode, analyses: ns1:ArrayOfSarfAnalysis
        """
        result = self.__client.service.GetDerivatives(self.__app_id, analysis, pos, ignore_affixation)
        return result

    def GetInflections(self, analysis, ling_mode, diacritized):
        """
        :param analysis: SarfAnalysis
        :param ling_mode: LinguisticMode
        ling_mode can take values
            'Classical'	    Default operational mode (ignore direct speech analyses)
            'Conversational'	Keeps direct speech analyses (use this to generate all analyses including direct speech analyses)
        :param diacritized: boolean
        :return: ns1:SarfErrorCode, inflections: ns1:ArrayOfString, totalInflections: xsd:int
        """
        results = self.__client.service.GetInflections(self.__app_id, analysis, ling_mode, diacritized)
        return results

    def GetInflectionsEx(self, analysis, ling_mode, diacritized, max_inflections, start_index):
        """
        :param analysis: SarfAnalysis
        :param ling_mode: LinguisticMode
        ling_mode can take values
            'Classical'	    Default operational mode (ignore direct speech analyses)
            'Conversational'	Keeps direct speech analyses (use this to generate all analyses including direct speech analyses)
        :param diacritized: boolean
        :param max_inflections: int
        :param start_index: int
        :return: ns1:SarfErrorCode, inflections: ns1:ArrayOfString, totalInflections: xsd:int
        """
        result = self.__client.service.GetInflectionsEx(self.__app_id, analysis, ling_mode, diacritized,
                                                        max_inflections, start_index)
        return result

    def GetPlural(self, analysis, ignore_affixation):
        """
        :param analysis: SarfAnalysis
        :param ignore_affixation: boolean
        :return: ns1:SarfErrorCode, analyses: ns1:ArrayOfSarfAnalysis
        """
        result = self.__client.service.GetPlural(self.__app_id, analysis, ignore_affixation)
        return result