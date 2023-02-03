

import PyPDF2

#pre-processing imports here
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import string

## File Location, Import

grimm_url = '/home/aegir/ProgLab/PythonLab/Pytorch/FairytalesByTheBrothersGrimm.txt'
coraline_url = '/home/aegir/ProgLab/PythonLab/Pytorch/Coraline.pdf'
alice_url = '/home/aegir/ProgLab/PythonLab/Pytorch/AlicesAdvanturesInWonderland.txt' 
punct = string.punctuation


#a function to pre process Coraline by Neil Gaiman

def preprocess_coraline(book):
  '''
  param book: url od a PDF book file
  '''
  output = ""
  data = open(book, 'rb')
  data = PyPDF2.PdfFileReader(book)
  npages = data.getNumPages()
  for i in range(npages):
    page_i = data.getPage(i).extractText()
    output += page_i
  output = output[1227:]
  output = output.lower()
  for word in output:
    for char in word:
        if char in punct:
            word = word.replace(char, "")
  remove_punct = "".join([word for word in output if word not in punct])
  processed = word_tokenize(remove_punct)
  print('Coraline database includes {} tokens, and {} unique tokens after editing'.format(len(processed), len(set(processed)))) 
  return processed

coraline = preprocess_coraline(coraline_url)


#a function to pre process Alice's Advantures in Wonderland by Lewis Carroll

def load_alice(text_file, punct, not_a_word):
    '''
    param text_file: url to Project Gutenberg's text file for Alice's Advantures in Wonderland by Lewis Carroll
    param punct: a string of punctuation characters we'd like to filter
    param not_a_word: a list of words we'd like to filter
    '''
    book = open(text_file, 'r')
    book = book.read()
    book = book[715:145060]
    book_edit = re.sub('[+]', '', book)
    book_edit = re.sub(r'(CHAPTER \w+.\s)', '', book)
    words = word_tokenize(book_edit.lower())
    
    word_list = []
    
    # filtering punctuation and non-words
    for word in words:
        for char in word:
            if char in punct:
                word = word.replace(char, "")
        if word not in punct and word not in not_a_word:
            word_list.append(word)

    print('Alice database includes {} tokens, and {} unique tokens after editing'.format(len(word_list), len(set(word_list)))) 
    return word_list

alice = load_alice(alice_url, (punct.replace('-', "") + '’' + '‘'), ['s', '--', 'nt', 've', 'll', 'd'])

def load_fairytales(text_file):
    '''
    param text_file: url to Project Gutenberg's text file for Fairytales by The Brothers Grimm
    '''
    book = open(text_file, encoding='cp1252')
    book = book.read()
    book = book[2376:519859]
    book_edit = re.sub('[(+*)]', '', book)
    words = word_tokenize(book_edit.lower())

    # filtering punctuation inside tokens (example: didn't or wow!)
    for word in words:
        for char in word:
            if char in punct:
                word = word.replace(char, "")

    # filtering punctuation as alone standing tokens(example: \ or ,)
    words = [word for word in words if word not in punct]

    print('Fairytales database includes {} tokens, and {} unique tokens after editing'.format(len(words), len(set(words))))            
    return words

brothers_grimm = load_fairytales(grimm_url)




## Sum of Data

data = coraline + alice + brothers_grimm


## Vocabulary ##

vocab = set(data)
vocab_size = len(data)

len(vocab)

## Word To Index ##

word_to_index = {word: i for i, word in enumerate(vocab)}

#print(word_to_index)


data = [word_to_index[word] for word in data]




## Batch Data ###################################3

batch_size = 5

train_data =[([data[i], data[data+1], data[data+2], data[data+3], data[data+4]], data[data+5]) for i in range (vocab_size-batch_size)]



### Import Torch ###
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import time


embedding_dim = 5

class storyTeller(nn.module):
    def __init__ (self, vocab_size, embedding_dim, batch_size):
        super(StoryTeller, self).__init__()
        self.embedding == n.Embedding(vocab_size, embedding_dim)
        self.linear1 = nn.Linear(batch_size * embedding_dim, 128)
        self.linear2 = nn.Linear(128, 512)
        self.linear3 = nn.Linear(512, vocab_size)

    def forward(self, inputs):
        embeds = self.embedding((inputs).view(1, -1))
        out = F.relu(self.linear1(embeds))
        out = F.relu(self.linear2(embeds))
        out = self.linear3(out)
        log_probs = F.log_softmax(out, dim=1)
        return log_probs

model = StoryTeller(vocab_size, embedding_dim, batch_size)

print(model)



