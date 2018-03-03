class Speller:
    """
    The Speller detects and corrects misspelled words in Arabic text and is designed for
    Modern Standard Arabic. The Speller APIs also enable auto-correction of Common Arabic Mistakes,
    frequent orthographical errors. The main objective of the Speller is to enhance the quality
    of written Arabic text, hence improving the accuracy of the various Arabic text-processing components.
    """

    def __init__(self, app_id):
        import zeep
        self.__WSDL = "https://atks.microsoft.com/Services/SpellerService.svc"
        self.__PORT = "HTTPS_ISpellerService"
        self.__client = zeep.Client(wsdl=self.__WSDL, port_name=self.__PORT)
        self.__app_id = app_id

    def Autocorrect(self, in_text, process_last_word_only):
        """
        :param in_text: string
        :param process_last_word_only: boolean
        :return: ns1:SpellerErrorCode, correctedText: xsd:string
        """
        result = self.__client.service.Autocorrect(self.__app_id, in_text, process_last_word_only)
        return result

    def AutocorrectAndSuggest(self, in_text, process_last_word_only):
        """
        :param in_text: string
        :param process_last_word_only: boolean
        :return: ns1:SpellerErrorCode, correctedText: xsd:string, erroneousWords: ns1:ArrayOfErroneousWord
        """
        result = self.__client.service.AutocorrectAndSuggest(self.__app_id, in_text, process_last_word_only)
        return result

    def AutocorrectAndSuggest2(self, in_text, correction_options, process_last_word_only):
        """
        :param in_text: string
        :param correction_options: SuggestionOption
        :param process_last_word_only: boolean
        :return: ns1:SpellerErrorCode, correctedText: xsd:string, erroneousWords: ns1:ArrayOfErroneousWord
        """
        result = self.__client.service.AutocorrectAndSuggest2(self.__app_id, in_text, correction_options,
                                                              process_last_word_only)
        return result

    def DetectMistakes(self, in_text, process_last_word_only):
        """
        :param in_text: string
        :param process_last_word_only: boolean
        :return: ns1:SpellerErrorCode, erroneousWords: ns1:ArrayOfErroneousWord
        """
        result = self.__client.service.DetectMistakes(self.__app_id, in_text, process_last_word_only)
        return result

    def ReportCorrectionSelection(self, word, context, correction):
        """
        :param word: string
        :param context: string
        :param correction: string
        :return: ns1:SpellerErrorCode
        """
        result = self.__client.service.ReportCorrectionSelection(self.__app_id, word, context, correction)
        return result

    def ReportWronglyDetectedWord(self, word, context):
        """
        :param word: string
        :param context: string
        :return: ns1:SpellerErrorCode
        """
        result = self.__client.service.ReportWronglyDetectedWord(self.__app_id, word, context)
        return result

    def SuggestCorrectionForSpecificWord(self, in_text, word_position, correction_options):
        """
        :param in_text: string
        :param word_position: int
        :param correction_options: SuggestionOption
        :return: ns1:SpellerErrorCode, erroneousWord: ns1:ErroneousWord
        """
        result = self.__client.service.SuggestCorrectionForSpecificWord(self.__app_id, in_text, word_position,
                                                                        correction_options)
        return result

    def SuggestCorrections(self, in_text, correction_options, process_last_word_only):
        """
        :param in_text: string
        :param correction_options: SuggestionOption
        :param process_last_word_only: boolean
        :return: ns1:SpellerErrorCode, erroneousWords: ns1:ArrayOfErroneousWord
        """
        result = self.__client.service.SuggestCorrections(self.__app_id, in_text, correction_options,
                                                          process_last_word_only)
        return result

    def SuggestMissingCorrection(self, word, context, correction):
        """
        :param word: string
        :param context: string
        :param correction: string
        :return: ns1:SpellerErrorCode
        """
        result = self.__client.service.SuggestMissingCorrection(self.__app_id, word, context, correction)
        return result