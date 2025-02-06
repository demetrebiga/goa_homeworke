def convert_and_join(int_list):
    str_list = [str(num) for num in int_list]
    return " ".join(str_list)
numbers = [1, 2, 3, 4, 5]
result = convert_and_join(numbers)
print(result)

#codewars


#1

#Jenny's secret message

#def greet(name):
#    if(name == "Johnny"):
#            return "Hello, my love!"
#    return "Hello, " + name + "!"



#2

#Reversed Words

#def reverse_words(s):
#    words = s.split(' ')
#    reverse_words = words[::-1]
#    return ' '.join(reverse_words)



#3

#Number of People in the Bus

#def number(bus_stops):
#    return sum(on-off for on, off in bus_stops)



#4

#Get the mean of an array


#def get_average(marks):
#    avg = sum(marks) / len(marks)
#    return int(avg)



#5

#Remove exclamation marks


#def remove_exclamation_marks(s):
#    z = s.replace("!", "")
#    return z



#6

#Transportation on vacation


#def rental_car_cost(d):
#    cost_per_day = 40
#    total_cost = d * cost_per_day
#
#    if d >= 7:
#        total_cost -= 50
#    elif d >= 3:
#        total_cost -= 20
#
#    return total_cost