# classwork

# Excercise 1

print("")
name = "St. Robert Catholic Highschool"
address = "8101 Leslie St."
city = "Thornhill"
province = "ON"
postal_code = "L3T 7P4"
phone_number = "905-889-4982"

print(name)
print(address)
# print(f"{city}, {province}")
# OR
print("{}, {}".format(city, province))
print(postal_code)
print(phone_number)

print("")
print("OR")
print("")

print("St. Robert Catholic Highschool")
print("8101 Leslie St.")
print("Thornhill, ON")
print("L3T 7P4")
print("905-889-4982")

print("_"*60)

# Excercise 2

print("please enter your name:")

name = input()
print(f"Hello {name}, nice to meet you?")

print(f"{name}, how are you feeling today? (good or bad)")
mood = input()

if mood == "good":
  print("Wow, thats great!")
if mood == "bad":
  print("Its ok, tomorrow will be better!")


print("_"*60)

# Excercise 3

print(f"Hello {name}! I will help you find the area of your room.")
print("What is the width of your room?")
width = input()
width = int(width)
print("Okay. Now what is the length of your room?")
length = input()
length = int(length)

area = length * width
print(f"The area of your room is {area} squre meters")

print("_"*60)

# Excercise 4


print("_"*60)

# Excercise 5

print("What amount of drink containers holding 1L or less are you recycling?")

less_deposit = input()

less_deposit = int(less_deposit)
amount_recieved_for_1L_or_less = less_deposit * 0.10

print("Okay. Now What amount of drink containers holding more than 1L are you recycling?")

more_deposit = input()

more_deposit = int(more_deposit)

amount_recieved_for_more_than_1L = more_deposit * 0.25

total_refund_amount = amount_recieved_for_more_than_1L + amount_recieved_for_1L_or_less

print(f"Your total refund amount is $%.2f"% total_refund_amount)

