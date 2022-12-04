
def find_top_n(array, n):
    top_three=[]
    for _ in range(n):
        max_val = max(array)
        top_three.append(max_val)
        array.remove(max_val)
    return top_three

with open('advent_1.in') as file:
    data = [i for i in file.read().strip().split('\n')]

temp_calories= 0
elf_calories =[]
for i,item in enumerate(data):
    if item == '':
        elf_calories.append(temp_calories) 
        temp_calories=0
    else:
        temp_calories += int(item)
max_value = max(elf_calories)
index = elf_calories.index(max_value)

print(index+1, elf_calories[index],max_value) 

top_n = find_top_n(elf_calories,3)
print(top_n)
print(sum(top_n))


