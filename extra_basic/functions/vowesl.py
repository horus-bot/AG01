def vowels(n:str):
    vowels = [x for x in n if x in "aeiou" ]
    print(len(vowels))

vowels("swathi")