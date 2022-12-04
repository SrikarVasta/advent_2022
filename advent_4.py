from functools import reduce

with open('advent_4.in') as file:
        data = [i for i in file.read().strip().split('\n')]

def get_counting_string(min_num,max_num):
    return reduce(lambda a, b: a +','+ b, map(str, range(min_num, max_num + 1)))

overlaps = 0
exploded_list = []
overlaps_2 = 0
for item in data:
    split_item =item.split(",")
    first_start, first_end = split_item[0].split("-")
    second_start, second_end = split_item[1].split("-")
    if int(first_start) <= int(second_start) and int(first_end) >= int(second_end):
        overlaps += 1
    elif int(first_start) >= int(second_start) and int(first_end) <= int(second_end):
        overlaps += 1
    elif int(first_start) >= int(second_start) and  int(first_start) <= int(second_end):
        overlaps_2 += 1
    elif int(second_start) <= int(first_end) and int(first_end) <= int(second_end) :
        overlaps_2 += 1
print(overlaps) #solution 1
print(overlaps+overlaps_2) #solution 2