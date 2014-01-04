#!/usr/bin/python

def main(text):
    '''parse text for lunch order
    return pretty markdown formatted lunch listing by day'''
    
    delim_start = 'Student Date    Lunch   Price\n'
    delim_end = '    Subtotal:'
    price = '5.00'
    
    content = text.split(delim_start)[1].split(delim_end)[0]

    lunches = content.split(price)[:-1]
    lunches = [a.strip() for a in lunches]

    pretty = []

    for lunch in lunches:
        name, grade_day, date_menu, option = lunch.split('\n')
        date, menu = date_menu.split('    ')
        pretty.append('%s %s %s %s' % (date, name, menu, option))

    pretty.sort()

    return '\n'.join(pretty)


