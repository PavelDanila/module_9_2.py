first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
first_result = [len(x) for x in first_strings if len(x) > 5]
print(first_result)

second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
second_result = [x + y for x in first_strings for y in second_strings if len(tuple(x)) == len(tuple(y))]
print([tuple(second_result)])

third_strings = first_strings + second_strings
third_result = {str(x): len(y) for x in third_strings for y in third_strings if len(x) % len(y) == 0}
print(third_result)