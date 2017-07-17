## list comprehension  to get even
even_numbers = [i for i in range(1,15) if i%2==0]
print (even_numbers)
print("%%%%%%%%%%%%%%%")
## list voiwels
letters =["a", "c","i","o","p","P"]
find_vowels = [i for i in letters if i.lower() not in "aeiou"]
print(find_vowels)
print("%%%%%%%%%%%%%%%")
# advance list comprehension
statement= ["the" , "quick" , "brown" , "fox" , "jumps" , "the" , "dog"]
ans = [[w.upper(), w.lower(), len(w)] for w in statement if w[0]  not in "tf"] 
print(ans)
