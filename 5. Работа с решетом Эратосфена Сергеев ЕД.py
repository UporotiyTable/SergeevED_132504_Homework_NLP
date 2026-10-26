def charac_checker(word): #функция проверки того, что пользователь написал число
    numbers = '0123456789'
    for char in word:
        if char not in numbers: 
            return False
        else:
            return True
        
while True: #ограничение пользователя от введения некорректных значений
    N = input("Введите число равное или большее 2: ")

    if N == '':
        print('Вам нужно что-то ввести.')

    elif (charac_checker(N) == False):
        print('В вашем числе есть что-то, кроме цифр.')

    elif int(N) < 2:
        print('Ваше число не должно быть меньше 2.')
    else: break

N = int(N)+1 #немного правлю введённое значение под индексацию пайтона

spectr = list(range(2,N)) #ряд чисел для применения решета Эратосфена
for p in spectr: #применение решета Эратосфена
    for k in spectr:
        if k%p == 0 and k != p:
            spectr.remove(k)
        if k==p:
            print(k)

