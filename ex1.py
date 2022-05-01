#Exercise 1
dict={"Quixotic":"unrealsitic and impractical", "Grotesque":"repulsive, ugly", "Imperious":"arrogant and domineering", "Ebullient":"cheerful and full of energy", "Nonchalant":"calm and relaxed"}
print(dict.keys())
word=input("Enter the word: ")
_word=word.capitalize()
print("The meaning of",_word,"is",dict[_word])
