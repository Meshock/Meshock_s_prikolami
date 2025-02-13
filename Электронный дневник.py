import random
#список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# Сортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам
# цикл по ученикам
for student in students: # 1 итерация: student = 'Александра'
    students_marks[student] = {} # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes: # 1 итерация: class_ = 'Математика'
        # цикл по предметам
        marks = [random.randint(1,5) for i in range(3)] # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks # students_marks['Александра']['Математика'] = [5, 5, 5]
        # выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
    {students_marks[student]}''')

print('''Список команд:
        1. Добавить оценку ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести оценки по всем ученикам
        4. Выход из программы''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        # 2. Выводим средний балл по всем предметам по каждому ученику
        print('2. Выводим средний балл по всем предметам по каждому ученику')
        print()
        # Цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценорк по прдмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # Выводим среднй балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
                print()
    elif command == 3:
        # Вывести оценки по всем ученикам
        print('3. Выводим оценки по всем ученикам')
        print()
            # Выводим словарь с оценками
            # Цикл по ученикам
        for student in students:
            print(student)
            # Цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
                print()
# Выход из программы
    elif command == 4:
        print('4. Выход из программы')
        break
    else:
        print('Неверная команда')