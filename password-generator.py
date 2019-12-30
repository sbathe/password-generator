#!/usr/bin/env python3
import random
from pathlib import Path
class generate_password:
    def __init__(self, num_words=4):
        self.connector = '-'
        self.transcodes = {
               'e': '3',
               'i': '1',
               'j': '1',
               'l': '1',
               'o': '0',
               'r': '2',
               's': '5',
               't': '7'
            }
        self.wordlist = open(str(Path.home())+'/bin/large_word_list.txt').readlines()
        self.num_words = num_words

    def getword(self):
        # get 2 words from our wordlist
        return self.wordlist[random.randint(0,len(self.wordlist))].strip()

    def getwordarray(self):
        words = list()
        for w in range(0,self.num_words):
            words.append(self.getword())
        return words

    def capitalize_one(self, words=[]):
        w = random.randint(0,len(words)-1)
        words[w] = words[w].capitalize()
        return words

    def numberize_one(self, words=[]):
        w = random.randint(0,len(words)-1)
        numberized = 0
        for k in self.transcodes.keys():
          if k in words[w]:
              words[w] = words[w].replace(k,self.transcodes[k],1)
              numberized = 1
              break
        return (numberized, words)

    def generate(self):
        words = self.getwordarray()
        #print(words)
        self.capitalize_one(words)
        numbered = 0
        while not numbered:
            numbered, words = self.numberize_one(words)
        return self.connector.join(words)

    def getmany(self, num_passwords=5):
        passwords = list()
        for c in range(num_passwords):
            passwords.append(self.generate())
        return passwords

if __name__ == "__main__":
    gp = generate_password()
    for p in gp.getmany():
        print(p)
