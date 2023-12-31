text = open("list.txt", "r").readlines()

text.pop(0)

subscriber = text[0].split(" ")
days = text[1].split(" ")

num = []
sorted_array = []
dictionary = {}
sorted_dict = {}

# adds the day and number of subscribers for that day to a dictionary that is unsorted
for x, stuff in enumerate(subscriber):
    dictionary[days[x]] = stuff

# converts all the keys in the unsorted dictionary into int from str
for key, value in dictionary.items():
    new_key = int(key)
    sorted_dict[new_key] = value

# sorts by the days and then adds the subscriber values to an array
sorted_dict = dict(sorted(sorted_dict.items()))
sorted_array.extend(sorted_dict.values())

# this does the math part of subtracting and stuff
for x in range(len(sorted_array) - 1):
    num.append(int(sorted_array[x + 1]) - int(sorted_array[x]))

# adds a + sign in front of positive numbers
for x in range(len(num)):
    if num[x] > 0:
        num[x] = "+" + str(num[x])
    print(num[x])