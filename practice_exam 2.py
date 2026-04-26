
"""question 5 PE 2 code"""

# scores= {"alice":85,"bob":60,"charlie":92}

# def organize_by_scores(scores):
#     new = {}
#     new['Pass'] = []
#     new['Fail'] = []
#     for name in scores:
#         if scores[name]>=70:
#             new['Pass'].append(name)
#         else:
#             new['Fail'].append(name)
#     return new

# a= organize_by_scores(scores)
# print(a)





#question 1 E1

# grades = {
# "Alice": {'Math': 90, 'Science': 85, 'English': 95},
# "Bob": {'Math': 92, 'Science': 88, 'English': 95},
# "Charlie": {'Math': 70, 'Science': 75, 'English': 80},
# "David": {'Math': 88, 'Science': 85, 'English': 91}
# }

# def find_top_students(grades):
#     math_best = 0
#     science_best = 0
#     english_best = 0
#     math_p = ''
#     science_p = ''
#     english_p = ''

#     for name in grades:
#         if grades[name]['Math'] >math_best:
#             math_best = grades[name]['Math']
#             math_p = name
#         if grades[name]['Science'] >science_best:
#             science_best = grades[name]['Science']
#             science_p = name  
#         if grades[name]['English'] >english_best:
#             english_best = grades[name]['English']
#             english_p = name 
    
#     new_dict = {
#         "Math":math_p,
#         "Science":science_p,
#         "English":english_p
#     }
#     return new_dict

# result = find_top_students(grades)
# print(result)



# question 4 E1
# def celsius_to_fahrenheit(temps):
# # Fill in missing dictionary comprehension
#     converted_temps = {city: (temp * 9/5) + 32 for city, temp in temps.items()}
#     return converted_temps
# # Test Cases
# city_temps = {"New York": 0, "Los Angeles": 20, "Chicago": -5}
# print(celsius_to_fahrenheit(city_temps))
# #Expected Output: {'New York': 32.0, 'Los Angeles': 68.0, 'Chicago': 23.0}


#question 2 E1
def find_largest(numbers):
    largest = 0
    for num in numbers:
        if largest ==0:
            largest = numbers[0]
        elif num > largest:
            largest = num
    return largest
#Test Case
print(find_largest([-5, -1, -10, -3]))












