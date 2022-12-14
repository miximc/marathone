# Считается, что Вы знаете, что такое високосный год
# (делится на 4 и не делится на 100 или делится на 400)
# Считается, что Вы знаете, сколько дней в каждом месяце
# Считается известным, что в неделе 7 дней
#
#
# 1. Сегодня вторник, 13-е декабря 2022 года
# Используя только эту информацию вычислить день недели нового года.
# Подсказка: правильный ответ: воскресенье
days = {0:'Среда',
        1:'Четверг',
        2:'Пятница',
        3:'Суббота',
        4:'Воскресенье',
        5:'Понедельник',
        6:'Вторник'}
day_tooday = 13
day_years = 365
num_day = day_years - 31 + day_tooday
day_till = (day_years - num_day) % 7
print(f'Новый год в 2022 году наступает в {days[day_till]}')



# 2. Есть ли годы, начинающиеся с пн? со вт?
# Привести ближайший пример.
# def visokos(year):
#         if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#                 print('Високосный')
#
#         else:
#
#                 print('Не високосный')
v = 2022
year = 2029
ost = (year - v) % 4
a_plus = 0
minus = 0
if v < year and year - v == 1:
    day_till += year - v
elif v < year and 5 >= year - v >= 3:
        day_till += year - v + 1
# elif v < year and year - v == 4:
#         day_till += (year - v + 1)
# elif v < year and year - v == 5:
#         day_till += (year - v + 1)
elif (year - v) % 4 > 0 and year - v > 5:
        day_till += (year - v +2)
elif 3 > ost > 1 and 5 >=
print(f'Новый год в {year} году наступает в {days[day_till%7]}')
# visokos(v)


# 3. В какой день недели Вы родились? Перечислить все свои ДР,
# пришедшиеся на тот же день недели.
# year = 2023
# a_plus = 0
# minus = 0
# if v < year:
#     a_plus += year - v
# if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#     day_years = 366
#     num_day = day_years - 31 + 13
#     till = day_years - num_day
#     if till % 7 == 0:
#         print('НГ во вторник')
#     elif till % 7 == 4:
#         print('НГ в среду!')
# else:
#     till = day_years - num_day
#     if a_plus == 1:
#         if till % 7 == a_plus:
#             print('НГ во среду')
#         elif till % 7 == 1 + a_plus:
#             print('НГ в четверг!')
#         elif till % 7 == 2 + a_plus:
#             print('НГ в пятницу!')
#         elif till % 7 == 3 + a_plus:
#             print('НГ в субботу!')
#         elif till % 7 == 4 + a_plus:
#             print('НГ в воскресенье!')
#         elif till % 7 == 5 + a_plus:
#             print('НГ в понедельник!')
#         elif till % 7 == 0:
#             print('НГ в вторник!')
#     elif a_plus == 3:
#         if till % 7 == 0:
#             print('НГ в четверг!')
#         elif till % 7 == 1:
#             print('НГ в пятницу!')
#         elif till % 7 == 2:
#             print('НГ в субботу!')
#         elif till % 7 == 3:
#             print('НГ в воскресенье!')
#         elif till % 7 == 4:
#             print('НГ в понедельник!')
#         elif till % 7 == 5:
#             print('НГ в вторник!')
#         elif till % 7 == 6:
#             print('НГ в среду!')
#     else:
#         if till % 7 == 0:
#             print('НГ в пятницу!')
#         elif till % 7 == 1:
#             print('НГ в субботу!')
#         elif till % 7 == 2:
#             print('НГ в воскресенье!')
#         elif till % 7 == 3:
#             print('НГ в понедельник!')
#         elif till % 7 == 4:
#             print('НГ в вторник!')
#         elif till % 7 == 5:
#             print('НГ в среду!')
#         elif till % 7 == 6:
#             print('НГ в чертверг!')

