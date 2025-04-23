#creating a dictionary
dictionary={}#creating a empty list
while True:#here we are keeping while is true to get loop iterated
    print("1.Add a word")
    print("2.Search for meaning")
    print("3.diplay all words")
    print("4.update meaning")
    print("5.Delete word")
    print("6.exit")
    print("-"*10)
    choice=int(input("enter your choice "))
    if choice==1:
        word=input("enter a word ").lower()#here we storing the word in form of lower case 
        meaning=input("enter a meaning ")
        dictionary[word]=meaning
        print("word added successfully ")
        
    elif choice==2:
        searched_word=input("enter word to search ")
        if searched_word in dictionary:
                print(f"meaning of {searched_word} is {dictionary.get(meaning)}")
        else:
            print("word doesn't exist")
    elif choice==3:
        print(f"displaying all words in dictionary {dictionary}\n")
    elif choice==4:
        want_to_update=input("enter the word that its meaning want to get update")
        if want_to_update in dictionary:
                up_meaning= input(f"give updated meaning to {want_to_update}")
                dictionary[want_to_update]= up_meaning
                print(f" meaning of '{want_to_update}' is {dictionary[want_to_update]}")
        else:
            print("word doesnt exist")
    elif choice==5:
            popping_word=input("enter the word that should remove").lower()
            if popping_word in dictionary:
                dictionary.pop(popping_word)
                print(f"the dictionary after popping the {popping_word}: {dictionary}")
            else:
                print("the given valus is not exist")
    elif choice==6:
        break
    else:
        print("invalid choice. please enter between 1 to6")