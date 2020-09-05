# Alphabet Filter
class LetterFilter:

    def __init__(self, s):
        self.s = s
        
# Answer
    def filter_vowels(self):
        return ''.join(filter(lambda x: not x in set('aeiou'), self.s))

    def filter_consonants(self):    
        return ''.join(filter(lambda x: x in set('aeiou'), self.s))

s = input()
f = LetterFilter(s)
print(f.filter_vowels())
print(f.filter_consonants())
