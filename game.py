from random import randint
import random

class Rating:
    rating = 100

p = Rating()

class Bad_review:

    damage = randint(16,23)

e = Bad_review()

class Monthly_revenue:
    revenue = 450000
m = Monthly_revenue()

class Salary:
    salary = 50000
s = Salary()

class Arenda:
    arenda = 150000
a = Arenda()

class Medicines:
    medicines = 50000
d = Medicines()

class Equipment:
    equipment = 100000
q = Equipment()

def menu(p):
    while True:
        print("\n")
        print("0) ПРОЧИТАТЬ ПРАВИЛА ИГРЫ")
        print("*****************")
        print("Главное меню")
        print("1) Отзывы")
        print("2) Посмотреть рейтинг клиники")
        print("3) Открыть список факторов, влияющих на сезонные колебания")
        print("4) РАНДОМНО ВЫЗВАТЬ ФАКТОР, ВЛИЯЮЩИЙ НА СЕЗОННЫЕ КОЛЕБАНИЯ")
        print("5) Оплата аренды помещения")
        print("6) Выплата зарплаты сотрудникам")
        print("7) Закупка медикаментов и оборудования для животных")
        print("8) Посмотреть общую выручку за месяц")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                menu_feedback(p)
            if n == 2:
                menu_rating(p)
            if n == 3:
                seasonal_fluctuations()
            if n == 4:
                randomit()
            if n == 5:
                menu_arenda(m)
            if n == 6:
                menu_salary(m)
            if n == 7:
                menu_purchase(m)
            if n == 8:
                menu_income(m)
            if n == 0:
                rules()

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def seasonal_fluctuations():
    while True:
        print("\n")
        print("Выбирете фактор, чтобы прочитать описание")
        print("Список факторов")
        print("*****************")
        print("1) Время года")
        print("2) Размер доходов потребителей")
        print("3) Конкурент по соседству")
        print("4) Скидки на услуги")
        print("5) Реклама")
        print("6) Рейтинг клиники в интернете")
        print("7) Вернуться в главное меню")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                T_description()
            if n == 2:
                S_description()
            if n == 3:
                K_description()
            if n == 4:
                C_description()
            if n == 5:
                R_description()
            if n == 6:
                RT_description()
            if n == 7:
                menu(p)

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")
            

def menu_rating(p):
    print("Рейтинг клиники")
    print("*****************")

    print(f"Рейтинг на данный момент: {p.rating}")
    if p.rating <= 40:
            print("Низкий рейтинг")
    if p.rating > 40:
            print("Оптимальный рейтинг")
    input("Нажмите Enter для продолжения.")


def menu_income(m):
    print("Общая выручка за месяц")
    print("*****************")

    print(f"Выручка на данный момент: {m.revenue}")
    if m.revenue < 150000:
            print("Работа в убыток")
    if m.revenue > 150000:
            print("Стабильная работа клиники")
    input("Нажмите Enter для продолжения.")


def menu_feedback(p):
        print("**********************")
        print("1) Отрицательный отзыв")
        print("2) Положительный отзыв")
        n = int(input("Введите число: "))
        print("\n")
        if n == 1:

            p.rating -= e.damage
            print(f"Оставлен отрицательный отзыв, текущий рейтинг {p.rating}")

            print("*********************")

        if n == 2:

            p.rating += randint(10,15)

            if p.rating > 100:
                p.rating = 100

            print(f"Оставлен положительный отзыв, текущий рейтинг {p.rating}")

        if p.rating <= 40:
            print("Низкий рейтинг")
        if p.rating > 40:
            print("Оптимальный рейтинг")

        print("******************")

def menu_arenda(m):
    m.revenue = m.revenue - a.arenda
    print("\n")
    print(f"Общая выручка за месяц после оплаты аренды: {m.revenue}")

def menu_salary(m):
    n = int(input("Введите количество сотрудников: "))
    m.revenue = m.revenue - (s.salary * n)
    print("\n")
    print(f"Общая выручка за месяц с учетом выплаты зарплаты сотрудникам: {m.revenue}")

def menu_purchase(m):
    while True:
        print("\n")
        print("1) Закупить медикаменты")
        print("2) Закупить оборудование")
        print("3) Вернуться в главное меню")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                m.revenue = m.revenue - d.medicines
                print(f"Общая выручка за месяц с учетом закупки медикаментов: {m.revenue}")
            if n == 2:
                m.revenue = m.revenue - q.equipment
                print(f"Общая выручка за месяц с учетом закупки оборудования: {m.revenue}")
            if n == 3:
                menu(p)

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def T_description():
    print("В зависимости от времни года, востребованы разные услуги для животных")
    while True:
        print("1) Вернуться к списку факторов")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                seasonal_fluctuations()
            else:
                print("Чего ждем?")

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def S_description():
    print("При снижении доходов клиентов, они реже обращаются в клинику, стараются выбрать недорогостоящие услуги")
    while True:
        print("1) Вернуться к списку факторов")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                seasonal_fluctuations()
            else:
                print("Чего ждем?")

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def K_description():
    print("По соседству с клиникой открылась другая ветеринарная клиника, конкуренция ведет к снижению дохода")
    while True:
        print("1) Вернуться к списку факторов")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                seasonal_fluctuations()
            else:
                print("Чего ждем?")

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def C_description():
    print("Скидки на услуги, востребованные в данный момент")
    while True:
        print("1) Вернуться к списку факторов")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                seasonal_fluctuations()
            else:
                print("Чего ждем?")

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def R_description():
    print("Рекламирование клиники повышает приток клиентов")
    while True:
        print("1) Вернуться к списку факторов")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                seasonal_fluctuations()
            else:
                print("Чего ждем?")

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def RT_description():
    print("Клиенты смотрят рейтинг клиники в интернете и на основе него решают обращаться ли в эту клинику или же нет")
    while True:
        print("1) Вернуться к списку факторов")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                seasonal_fluctuations()
            else:
                print("Чего ждем?")

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def random_vremgoda(m):
    print("Был вызван фактор - Время года")
    print("*****************")
    print("Выбирете время года, чтобы расчитать его влияние на выручку:")
    while True:
        print("1) Лето")
        print("2) Осень")
        print("3) Зима")
        print("4) Весна")
        print("5) Вернуться в главное меню")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                m.revenue = m.revenue - 10000
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 2:
                m.revenue = m.revenue + 10000
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 3:
                m.revenue = m.revenue + 20000
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 4:
                m.revenue = m.revenue + 5000
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 5:
                menu(p)

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")


def random_razmerdoxoda(m):
    print("Был вызван фактор - Размер доходов потребителей")
    print("*****************")
    print("Уменьшились или увеличились доходы потребителей:")
    while True:
        print("1) Увеличились")
        print("2) Уменьшились")
        print("3) Вернуться в главное меню")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                m.revenue = m.revenue + 25000
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 2:
                m.revenue = m.revenue - 25000
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 3:
                menu(p)

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def random_konkurent(m):
    print("Был вызван фактор - Конкурент по соседству")
    print("*****************")
    print("Доход уменьшится в пределах 15000 - 35000")
    m.revenue = m.revenue - randint(15000,35000)
    print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")



def random_skidki(m):
    print("Был вызван фактор - Скидки на услуги")
    print("*****************")
    print("Скидка на услугу делается НА ОДИН МЕСЯЦ в размере 25%")
    print("Выбирете услугу, на которую хотите сделать скидку:")
    while True:
        print("\n")
        print("1) Осмотр животного - цена услуги 1000")
        print("2) Введение лекарственных препаратов - цена услуги 640")
        print("3) Обрезка когтей - цена услуги 300")
        print("4) Очистительная клизма - цена услуги 1500")
        print("5) Вернуться в главное меню")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                v = int(input("Введите количество посетителей за день: "))
                i = (v * (1000/0.25)) * 30
                m.revenue = m.revenue + i
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 2:
                v = int(input("Введите количество посетителей за день: "))
                i = (v * (640/0.25)) * 30
                m.revenue = m.revenue + i
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 3:
                v = int(input("Введите количество посетителей за день: "))
                i = (v * (300/0.25)) * 30
                m.revenue = m.revenue + i
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 4:
                v = int(input("Введите количество посетителей за день: "))
                i = (v * (1500/0.25)) * 30
                m.revenue = m.revenue + i
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 5:
                menu(p)

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def random_rating(m, p):
    print("Был вызван фактор - Рейтинг клиники в интернете")
    print("*****************")
    print("В зависимости от рейтинга в интернете увеличивается или уменьшается приток клиентов")
    print(f"Рейтинг на данный момент: {p.rating}")
    if p.rating <= 40:
            print("Низкий рейтинг")
            m.revenue = m.revenue - 30000
            print(f"Общая выручка за месяц с учетом закупки медикаментов: {m.revenue}")
    if p.rating > 40:
            print("Оптимальный рейтинг")
            m.revenue = m.revenue + 20000
            print(f"Общая выручка за месяц с учетом закупки медикаментов: {m.revenue}")

def random_reklama(m):
    print("Был вызван фактор - Реклама")
    print("*****************")
    print("Дать рекламу 40000, потенциальная выручка при притоке клиентов 60000-65000")
    while True:
        print("1) Дать рекламу")
        print("2) Вернуться в главное меню")

        try:
            n = int(input("Введите число: "))
            print("\n")

            if n == 1:
                m.revenue = m.revenue - 40000 + randint(60000,65000)
                print(f"Общая выручка за месяц с учетом данного фактора: {m.revenue}")
            if n == 2:
                menu(p)

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")

def randomit():
    list = [1, 2, 3, 4, 5, 6]

    if random.choice(list) == 1:
        random_vremgoda(m)
    if random.choice(list) == 2:
        random_razmerdoxoda(m)
    if random.choice(list) == 3:
        random_konkurent(m)
    if random.choice(list) == 4:
        random_skidki(m)
    if random.choice(list) == 5:
        random_rating(m, p)
    if random.choice(list) == 6:
        random_reklama(m)


def rules():
    print("Игра предназначена для расчета общей прибыли за месяц с учетом сезонных колебаний")
    print("Правила:")
    print("1. Зайдите в меню Отзывы, оставьте ряд положительных или ряд отрицательных отзывов, чтобы определить рейтинг клиники в интернете, рейтинг меньший 40 - низкий")
    print("2. Посмотрите рейтинг клиники, все ли вас устраивает?")
    print("3. Откройте список факторов, посмотрите какие факторы могут выпасть в рандомном вызове, и что они означают")
    print("4. Вызовите рандомный фактор, следуйте подсказкам в меню, фактор повлияет на конечную выручку")
    print("5. Вернитесь в главное меню")
    print("7. Выплатите зарплату сотрудникам")
    print("8. Закупите медикаменты и оборудование для животных")
    print("9. ФИНАЛЬНОЕ ДЕЙТВИЕ, посмотрите вашу выручку за месяц, будет указано, работает ли клиника в убыток, или же работа клиники стабильна")
    input("Нажмите Enter для продолжения.")


menu(p)