name = input('Дайте кличку коту: ')
print('теперь',name, "будет кличкой кота")
want = input('Ваш кото хочет есть: ')
if want == 'Да' or 'Покормить':
    print(name, 'Поел')
elif want == 'Нет' or 'Не кормить':
    print("Вы бессердесен и кот остаося голодать")
sleep = input("Ваш кот лёг на вас: ")
if sleep == 'Заснуть гладя его':
    print("Вы выспались без проблем")
breakfast = input('Ваш кот хочет поесть: ')
if breakfast == 'Дать корма':
    print(name ,'Поел корма')
elif breakfast == 'Дать молока':
    print(name ,'полакал')