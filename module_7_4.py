'''team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
'''
team1_num = int(input('Ввести кол-во участников команды Мастера кода: '))
team2_num = int(input('Ввести кол-во участников команды Волшебники данных: '))
score_1 = int(input('Ввести количество решённых задач командой Мастер кода: '))
score_2 = int(input('Ввести количество решённых задач комндой Волшебники данных: '))
team1_time = float(input('Ввести время команды Мастер кода: '))
team2_time = float(input('Ввести время команды Волшебники данных: '))

print(' ')
print(' ')
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'


#использование %
print('В команде Мастера кода участников: %d' %team1_num)
print('Итого сегодня в командах участников: %d и %d !' %(team1_num, team2_num))

#использование format()
print('Команда Волшебники данных решила задач: {0}'.format(score_2))
print("Волшебники данных решили задачи за {0} с !".format(team2_num))

#использование f-строк
print(f'Команды решили {score_1} и {score_2} задач')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')