#1
#Cat years, Dog years

#def human_years_cat_years_dog_years(human_years):
#    cat = 0
#    dog = 0
#    if human_years == 1:
#        cat = 15
#        dog = 15
#    elif human_years == 2:
#        cat = 24
#        dog = 24
#    else:
#        dog = 5 * (human_years - 2) + 24
#        cat = 4 * (human_years - 2) + 24
#    return [human_years, cat, dog]


#2
#Century From Year

#def century(year):
#    century = year // 100
#    if year % 100 == 0:
#        return century
#    return century + 1



#3
#Third Angle of a Triangle

#def other_angle(a, b):
#    return 180 - (a + b)



#4
#I love you, a little , a lot, passionately ... not at all

#def how_much_i_love_you(nb_petals):
#    phrases = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
#    remainder = nb_petals % len(phrases)
#    return phrases[remainder-1]



#4
#Grader


#def grader(score):
#    if score > 1 or score < 0.6:
#        return "F"
#    elif score >= 0.9:
#        return "A"
#    elif score >= 0.8:
#        return "B"
#    elif score >= 0.7:
#        return "C"
#    elif score >= 0.6:
#        return "D"