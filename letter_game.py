import enchant
import threading
import time 
from itertools import permutations
import sys
import nltk 
from nltk.corpus import words
nltk.download('words')
class countdownLetters:
    def __init__(self,letters:str):
        # Input word
        self.word = None
        self.letters = letters 
        self.combos = []
        self.len1 = 1 
        self.len2 = 1
        self.wrd1 = None 
        self.wrd2 = None
        self.mid = None
        self.first =None 
        self.second = None
        self.dictionary = set(words.words())
        #self.dictionary = enchant.Dict("en_UK")
        start = time.time()
        self.genAllCombo()
        self.getLongRealWord()
        print(self.word)
        print(str(time.time()-start )," Seconds")
    def checkWord(self, word:str):
        return(word in self.dictionary) 
    def genAllCombo(self):
        length = len(self.letters)
        # This generates all possible combos of the letters
        self.combos = [''.join(l) for i in range(length) for l in permutations(self.letters, i+1)]
        print("Combos Generated")
    def getLongRealWord(self):
        self.first = threading.Thread(target = self.readForThread1)
        self.second = threading.Thread(target = self.readForThread2)
        
        self.first.start()
        self.second.start()
       
        self.first.join()
    
        self.second.join()
        if(self.len1 > self.len2):
            self.word = self.wrd1
        else:
            self.word = self.wrd2
    
    def readForThread1(self):
    # Define the end of the range to be half of the list length
        end = len(self.combos)
        strt = 0  # Start from the beginning of the list
        
        # Loop through the first half of the list (from index 0 to half)
        for index in range(strt, int(end / 2)):
            combo = self.combos[index]
            combo_length = len(combo)
            
            if combo_length < self.len2:  # Skip combos that are too short
                continue
            
            # Check if the combo exists in the dictionary
            #if self.dictionary.check(combo):
            if self.checkWord(combo):
                if combo_length > self.len1:  # Only update if a longer combo is found
                    print(f"Updating wrd1 with: {combo}")
                    self.wrd1 = combo  # Update wrd1 instead of wrd2
                    self.len1 = combo_length  # Update len2 with the new length
                
                    
                             
    def readForThread2(self):
        
        end = len(self.combos)
        strt = int((end / 2) + 1)
        
        
        for index in range(strt, end):
            combo = self.combos[index]
            combo_length = len(combo)
           
            
            if combo_length < self.len2:  # Skip too short combos
                continue
            if self.checkWord(combo):
            #if self.dictionary.check(combo):
                if combo_length > self.len2:  # Only update if a longer word is found
                    print(f"Updating wrd2 with: {combo}")
                    self.wrd2 = combo
                    self.len2 = combo_length
                
print(sys.argv[1])
print("Started ")

countDown = countdownLetters(sys.argv[1].lower())

