# check if the first word is vowel
  # if it is simply add py at the end of the word
# if the first word is a consenant then put it at the very end
  # then add py at the end of the word
# ask user a question and take that sentence and then translate it into
# pig latin

original = input("Please enter a sentence:").strip().lower()
word_list = original.split()
trans_list=[]

for word in word_list:
    if word[0] in "aeiou":
        trans = word + "yay"
        trans_list.append(trans)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
               vowel_pos = vowel_pos+1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons+"ay"
        trans_list.append(new_word)
        

output = " ".join(trans_list)
print(output)


