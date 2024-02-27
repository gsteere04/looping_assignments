number_list = []
duplicate_list = []
while len(number_list) != 5:
    ask_numbers = int(input("Please enter in a number: "))
    number_list.append(ask_numbers)
for num in number_list:
    if number_list.count(num) > 1:
        duplicate_list.append(num)
if len(duplicate_list) < 1:
    print("There are no duplicates.")
else:
    print(duplicate_list) 

    



