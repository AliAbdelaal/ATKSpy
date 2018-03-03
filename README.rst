Microsoft ATKS python Package
===============================

a python package that supports SOAP interface to communicate with the Microsoft ATKS 

What is the ATKS
==================

The Arabic Toolkit Service ([ATKS](https://www.microsoft.com/en-us/research/project/arabic-toolkit-service-atks/?from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fprojects%2Fatks%2F)) offers a set of APIs for basic processing of written Arabic language. The Toolkit is designed to help the Arabic developer by providing high-quality Arabic NLP APIs which eases the burden of building the low-level language processing functionality and allows developers and researchers to focus more on higher-level functionality and on the applications’ level. The ATKS provides a rich set of APIs as SOAP Web Services, and covering the basic language processing operations through the following components:

* [Colloquial to Arabic Converter](https://www.microsoft.com/en-us/research/project/colloquial-to-arabic-converter/)

> The Colloquial Converter provides translation of Egyptian colloquial text into the equivalent Modern Standard Arabic text along with rich mapping information. Both Sarf and the Colloquial Morphological Analyzer are used internally to provide the final translation.

* [Diacritizer](https://www.microsoft.com/en-us/research/project/diacritizer/)

> The automatic Diacritizer component performs vowel restoration on input Arabic text. The main objective of the Diacritizer is to insert both missing vowels—diacritics—of the stem and the missing vowel for the case ending.

* [Named Entity Recognizer (NER)](https://www.microsoft.com/en-us/research/project/named-entity-recognizer-ner/)

> The Named Entity Recognizer (NER) detects and classifies named entities in Arabic text. It classifies them into three categories: persons, locations, and organizations. It also provides a character index at which the named entity is located in the original text.

* [Parser](https://www.microsoft.com/en-us/research/project/parser/)

> The Parser determines the grammatical structure of Arabic sentences, such as which groups of words combine to form phrases and which words are the subject or the object of a verb. The Parser relies heavily on the Arabic POS Tagger to identify the correct part of speech for each token in an input Arabic sentence, and the Arabic Named-Entity Recognizer to identify named entities in the input sentence after it has been corrected using the Arabic Auto-Corrector.

* [Part of Speech Tagger](https://www.microsoft.com/en-us/research/project/part-of-speech-pos-tagger/)

> The Part of Speech (POS) Tagger is responsible for identifying the correct part of speech for each token of any given Arabic sentence. The POS Tagger relies heavily on the Morphological Analyzer to extract the relevant morpho-syntactic features for the input words. The POS Tagger also relies on the Auto-Corrector to correct input text. 

* [SARF](https://www.microsoft.com/en-us/research/project/sarf-morphological-analyzer/)

> Sarf provides automatic morphological analysis of Arabic words. It provides all possible morphological analyses for any given input Arabic word. Each analysis consists of the diacritized word and the morphological breakdown of the analysis in terms of prefixes, stem, and suffixes. The stem is further decomposed into its root and morphological pattern. Moreover, each analysis carries the part of speech and a set of morpho-syntactic features such as gender, number, transitivity, verb voice, and verb mood.

* [Speller](https://www.microsoft.com/en-us/research/project/speller/)

> The Speller detects and corrects misspelled words in Arabic text and is designed for Modern Standard Arabic. The Speller APIs also enable auto-correction of Common Arabic Mistakes, frequent orthographical errors. The main objective of the Speller is to enhance the quality of written Arabic text, hence improving the accuracy of the various Arabic text-processing components.

* [Transliterator](https://www.microsoft.com/en-us/research/project/transliterator/)

> Transliteration is the conversion of text from one script to another while preserving the same pronunciation. The Transliterator provides translation of named entities, such as human and city names, from English to Arabic and vice versa—and conversion of text from Romanized Arabic to native Arabic script.

requirements
============

* python3
* [Zeep](http://docs.python-zeep.org/en/master/) module
* Microsoft ATKS Account with [login credentials](https://www.microsoft.com/en-us/research/project/arabic-toolkit-service-atks/?from=http%3A%2F%2Fresearch.microsoft.com%2Fen-us%2Fprojects%2Fatks%2F)
> you will need to wait for the mail from Microsoft team with the App ID of yours

How to use it
=============

this library is so simple to use, you just need your app id and you're ready to go

see this example of using the Parser module 

```python
from ATKSpy import Parser
parser = Parser(app_id)
text = "عشان اصحى بدري لازم انام بدري"
print(parser.Parse(text))
```

```raw
>>> Forcing soap:address location to HTTPS
>>> {
>>>     'ParseResult': 'Success',
>>>     'parseTree': '(TOP (S (NP (NNS عشان) (ADJP (ADJP (NNP اصحى)) (PP (PREP ب) (NNP دري)))) (ADJP (JJ لازم) (VP (VBP أنام) (NP (PRT (PREP ب)) (NNP دري))))))',
>>>     'score': 0.05979948927458925
>>> }
```

it's so straight forward !!

after login with your Microsoft account you can then navigate the ATKS modules specs for specific argument values that are not standard (e.x:the SARF module has many non string nor boolean attributes)

you can check the official documentation of all the modules at [Microsoft ATKS Site](http://atks.microsoft.com/Help/) 