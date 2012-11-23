text = """Products on order: 
1 x	November Lunch Program - $50.00 
SKU: october
Childs Name: Elliot Steeves
Class: 5
Nov. 5: No lunch
Nov. 6: Gluten Free roll up
Nov. 7: Gluten Free Burrito
Nov. 8: No Lunch
Nov. 9: Gluten Free with chicken
Nov. 12: No lunch
Nov. 13: Gluten Free roll up
Nov. 14: Gluten Free Burrito
Nov. 15: No Lunch
Nov. 16: Gluten Free with chicken
Nov. 19: No lunch
Nov. 20: Gluten Free roll up
Nov. 26: No lunch
Nov. 27: Gluten Free roll up
Nov. 28: Gluten Free Burrito
Nov. 29: No Lunch
Nov. 30: Gluten Free with chicken

1 x	November Lunch Program - $74.75 
SKU: october
Childs Name: Darcie Steeves-TEACHER
Class: 4
Nov. 5: No lunch
Nov. 6: Gluten Free roll up
Nov. 7: Gluten Free Burrito
Nov. 30: Gluten Free with chicken"""

pack_lunches = {}
person = ''

for line in text.split('\n'):
    if line.startswith('Childs Name:'):
        if 'Darcie' in line:
            person = 'Darcie'
        if 'Elliot' in line:
            person = 'Elliot'
        if 'Quinton' in line:
            person = 'Quinton'
    elif 'No ' in line:
        my_date = line.split(':')[0]
        if my_date not in pack_lunches:
            pack_lunches[my_date] = [person]
        else:
            pack_lunches[my_date].append(person)

print pack_lunches


