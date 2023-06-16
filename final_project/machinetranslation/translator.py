""" akjdf """
from deep_translator import MyMemoryTranslator

def e2f(text):
    """ akjdf """
    translated = MyMemoryTranslator(source='english', target='french').translate(text)
    return translated

def f2e(text):
    """ akjdf """
    translated = MyMemoryTranslator(source='french', target='english').translate(text)
    return translated
