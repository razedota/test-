#вопрос как зовут?
print('Привіт,як тебе звуть ?')
#ввести имя
name=input('Введіть імя')
#вопрос от бота
print(f'Мені дуже приємно,{name},мене звуть бот Богдан,давай пограем в гру,я загадую рандомне число від 1 до 10 а ти повинен вгадати його')
#импортировал рандомные числа
import random
# генерируем случайное целое число в диапазоне от a до b
secret_number = random.randint(1, 10)
print('Я загадав рандомне число від 1 до 10. Вгадай')
#игровой цикл
while True:
    try:
        # ввод числа игрока
        guess =int(input('Введіть число'))
        # проверка диапазона
        if guess < 1 or guess > 10:
            print('Введи число від 1 до 10')
            continue
        # проверка на правильность
        if guess == secret_number:
            print('Молодець ти вгадав')
            break
        else:
            print('Неправильно')
            # проверка некорректного ввода
    except ValueError:
        print("Будь ласка, введи ціле число.")
#конец)
print("Гра завершена!")
print('Вам понравилась игра ?')
