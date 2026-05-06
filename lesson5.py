word = ["sari", "tamar", "tovi", "rut"]
new_word = [i for i in word if len(i) > 3]
print(new_word)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_num = [i if i % 3 == 0 else i*2 for i in num]
print(new_num)
new_num2 = {i: i*2 if i % 2 == 0 else None for i in new_num}
print(new_num2)
str1 = "tamar"
new_str = {i : str1.count(i) for i in str1}
print(new_str)
