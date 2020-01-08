# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 00:13:21 2019

@author: LaChandra Ash
"""

def add_word(word, word_count_dict): 
    '''Use key pair to udate word frequency'''
    if word in word_count_dict:
        word_count_dict[word] += 1
    else: word_count_dict[word] = 1
    
import string
def process_line(line, word_count_dict):
    ''' Add lower case words to dictionary by procesing the line'''
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        '''The -- is ignored inside the file'''
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)

def pretty_print(word_count_dict):
    '''Created tuples list, printed highest to lowest word freq'''
    value_key_list=[]
    for key, val in word_count_dict.items():
        value_key_list.append((val,key))
        '''Utilized the sort method'''
    value_key_list.sort(reverse=True)
    '''Sorted value/key list'''
    print('{:11s}{:11s}'.format('Word', 'Count'))
    print('_'*21)
    for val,key in value_key_list:
        print('{:12s} {:<3d}'.format(key,val))
        
def main():
  word_count_dict={}
  gba_file = open('gettysburg.txt', 'r')
  for line in gba_file:
    process_line(line, word_count_dict)
  print('Length of dictionary:', len(word_count_dict))
  pretty_print(word_count_dict)

main()