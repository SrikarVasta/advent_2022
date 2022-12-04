from functools import reduce

with open('advent_4.in') as file:
        data = [i for i in file.read().strip().split('\n')]

def get_counting_string(min_num,max_num):
    return reduce(lambda a, b: a +''+ b, map(str, range(min_num, max_num + 1)))

overlaps = 0
exploded_list = []

for item in data:
    split_item =item.split(",")
    left_a, left_b = split_item[0].split("-")
    right_a, right_b = split_item[1].split("-")
   
    left_string = get_counting_string(int(left_a),int(left_b))
    right_string = get_counting_string(int(right_a),int(right_b))
    exploded_list.append((left_string,right_string))

    if left_string in right_string or right_string in left_string:
        overlaps += 1
        
print(overlaps)
# print(exploded_list)
