# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



                #Использование %:
team1_num = 5
team2_num = 6
Name_team1_num = 'Мастера кода'
print ('"В команде %s '% Name_team1_num,'участников: ',team1_num,'!"')  #"В команде Мастера кода участников: 5 ! "
print('"Итого сегодня в командах участников : %s '% team1_num,'и', team2_num,'!"' )  #"Итого сегодня в командах
                                                                                     # участников: 5 и 6 !"
#Использование format():
score_2 = 42
print('"Команда Волшебники данных решила задач:{}'.format (score_2),'!')  #"Команда Волшебники данных решила задач:
                                                                               # 42 !"
team1_time = 18015.2
print( '"''Волшебники данных решили задачи за {}'.format(team1_time),'с' '!''"') # " Волшебники данных решили задачи
                                                                                 # за 18015.2 с !"
#Использование f-строк:

tasks_total = 82
time_avg = 45.2
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

#"Команды решили 40 и 42 задач.”
print(f'"Команды решили {score_1} и {score_2} задач."')


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else: challenge_result = 'Ничья!'

print(f'"Результат битвы: {challenge_result}"')

#"Сегодня было решено 82 задач, в среднем по 45.2  секунды на задачу!."
print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."')