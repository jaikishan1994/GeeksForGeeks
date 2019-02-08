# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 03:08:40 2019

@author: v-jaimo
"""

def olcount(sub,string):
    '''
    Returns overlapping count of a givne sub string in a original string
    '''
    count = 0
    l = len(string)
    for i in range(l):
        for j in range(i,l+1):
            if(string[i:j] == sub):
                count += 1
    return count

def minion_game(string):
    #minion game
    string = string.lower()
    vc = 0  #vowels count
    cc = 0  #consonent count

    visited = {}

    chars = set(string)
    for i in chars:
        visited[i] = 0

    for i in range(len(string)):
        if(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u'):
            #vowels count
            if(visited[string[i]] == 0):
                for j in range(i+1,len(string)+1):
                    vc = vc + olcount(string[i:j],string)
                    #print("{0} - {1} --- {2}".format(string[i:j],string.count(string[i:j]),vc))
                #vc = vc + string.count(string[i])
                visited[string[i]] = 1
                #print(vc)
        else:
            #consonant count
            if(visited[string[i]] == 0):
                for j in range(i+1,len(string)+1):
                    cc = cc + olcount(string[i:j],string)
                    #print("{0} - {1} --- {2}".format(string[i:j],string.count(string[i:j]),cc))
                #vc = vc + string.count(string[i])
                visited[string[i]] = 1
                #print(cc)
    if(vc < cc):
        print('Stuart ',cc)
    elif(vc > cc):
        print('Kevin ',vc)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)