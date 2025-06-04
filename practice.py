# #list of dictionary

# people = [
#     {"name":"alice",
#     "age":20,
#     "city":"karachi"
#     },
#     {"name":"john",
#     "age":22,
#     "city":"lahore"
#     },
#     {"name":"ali",
#     "age":25,
#     "city":"pindi"
#     },

# ]

# #accessing each dictionary in the list

# for person in people:
#     print(f"{person["name"]}, {person["age"]},{person["city"]}")


# text = "Hello"
# for index, char in enumerate(text,1):
#     print(f"Character at index {index}: {char}")

#list comprehension:

marks = [20,30,40,50,60]
#normal way
# new_makrs = []

# for x in marks:
#     new_makrs.append(x+2)
# print(new_makrs)


#list comprehension:

new_marks = [x+2 for x in marks] # kia krna ha: kis ke liye krna ha : kaha pay krna a
#print(new_marks)

num = [1,2,3,4,5,6,7,8,9,10]

cube=[x**3 for x in num if x % 2==0]

print(cube)  # [8, 64, 216, 512, 1000]