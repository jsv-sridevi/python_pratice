#using break and continue statements
words=['word1','word2','continue','word3','break','word4']
for word in words:
    if word=='break':#if the word is equal to break string than it goes into the true block code
        break #here the iteration of word variable stops because of break
    elif word=='continue':#if the word is equal to continue string than it goes into the true block code
        continue#here the current iterated word is skipped moves to next iteration
    else:#else statement for if and elif if the word didnt match to these statement than it comes to else
        print(f"{word} is word")#here it prints remaining words
print(word)#it prints last iterated value