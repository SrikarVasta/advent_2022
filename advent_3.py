import string

# Read in the rucksack contents from the input
rucksack_contents = []

with open("advent_3.in") as input_file:
    for line in input_file:
        rucksack_contents.append(line.strip())

# Create a dictionary to keep track of the counts for each item type
item_type_counts = {}

# Loop through each rucksack and find the common item type
for rucksack in rucksack_contents:
    # Divide the rucksack's contents into two parts, one for each compartment
    compartment1, compartment2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

    # Find the common items between the two compartments
    common_items = set(compartment1) & set(compartment2)

    # Loop through the common items and update the counts in the dictionary
    for item in common_items:
        if item in item_type_counts:
            item_type_counts[item] += 1
        else:
            item_type_counts[item] = 1

# Calculate the sum of the priorities for each item type
sum_of_priorities = 0

for item, count in item_type_counts.items():
    if item.islower():
        # Lowercase item types have priorities 1 through 26
        priority = string.ascii_lowercase.index(item) + 1
    else:
        # Uppercase item types have priorities 27 through 52
        priority = string.ascii_uppercase.index(item) + 27

    # Add the priority to the sum
    sum_of_priorities += priority * count

# Print the sum of the priorities
print(sum_of_priorities)

# Divide the rucksack contents into groups of three
rucksack_groups = [rucksack_contents[i:i+3] for i in range(0, len(rucksack_contents), 3)]

# Create a dictionary to keep track of the counts for each item type
item_type_counts = {}

# Loop through each group of rucksacks and find the common item type
for group in rucksack_groups:
    # Loop through each rucksack in the group and find the common item types
    common_items = set(group[0])
    for rucksack in group[1:]:
        common_items &= set(rucksack)

    # Loop through the common items and update the counts in the dictionary
    for item in common_items:
        if item in item_type_counts:
            item_type_counts[item] += 1
        else:
            item_type_counts[item] = 1

# Calculate the sum of the priorities for each item type
sum_of_priorities = 0

for item, count in item_type_counts.items():
    if item.islower():
        # Lowercase item types have priorities 1 through 26
        priority = string.ascii_lowercase.index(item) + 1
    else:
        # Uppercase item types have priorities 27 through 52
        priority = string.ascii_uppercase.index(item) + 27

    # Add the priority to the sum
    sum_of_priorities += priority * count

# Print the sum of the priorities
print(sum_of_priorities)