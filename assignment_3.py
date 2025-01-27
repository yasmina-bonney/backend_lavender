sentence = input("What are you doing tomorrow? ")

new_words = sentence.split()

first_word = new_words[0]
last_word= new_words[-1]
first_three_characters = sentence[:3]
last_three_characters = sentence[-3:]
reversed_sentence = sentence[::-1]

print(f"Total length of characters: {len(sentence)}")
print(f"Total lenght of words: {len(new_words)}")
print(f"The first word is: {first_word} \n The last word is: {last_word}")

print(f"The first three characters are: {first_three_characters}")
print(f"The last three characters are: {last_three_characters}")
print(f"The reversed sentence literally: {reversed_sentence}")

print(sentence.upper())
print(sentence.lower())
print(sentence.replace(" ","-")) 