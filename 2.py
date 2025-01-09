print('Привіт,як тебе звуть ? \n')
name=input('твоє імя')
print('Приємно, А мене звуть Павло, давай сьогодні пограємо в гру, я задаю тобі питання а ти відповідаешь и заробляешь бали')
correct_answers = 0
wrong_answers = 0
question1= input('Яка столиця України ?\n')


if question1 == 'Київ':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question2= input('Cкільки океанів на землі ?\n')
if question2 == '4':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question3 = input('Найглибша річка в Україні? \n')
if question3 == 'Дніпро':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question4 = input('Скільки днів у тижні \n')
if question4 == '7':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question5=input('Найвища гора у світі \n')
if question5 == 'Еверест':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question6= input('Скільки пальців у людини \n')
if question6 == '20':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question7 = input('Як звуть нашого вчителя ? \n')
if question7 == 'Юлія':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question8 = input('Яку мову програмування ми вивчаємо ?\n')
if question8 == 'Пайтон':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question9 = input('Як звуть нашого президента ? \n')
if question9 =='Володимир Зеленський':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question10 = input('Скільки планет у Сонячній системі? \n')
if question10 =='8':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question11 = input('Який птах не вміє літати, але чудово плаває? \n')
if question11 == 'Пінгвін':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question12 = input('Скільки годин на добу? \n')
if question12 == '24':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1
question13 = input('Якого місяця Новий рік? \n')
if question13 == 'грудень':
    print('Вірно')
    correct_answers += 1
else:
    print('Неправильно')
    wrong_answers += 1

print(f'\nГра завершена! {name}, ти дав(ла) {correct_answers} правильних відповідей і {wrong_answers} неправильних відповідей.')
print('Можем разпочати знов ')