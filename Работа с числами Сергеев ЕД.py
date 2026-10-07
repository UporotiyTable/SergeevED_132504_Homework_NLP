def charac_checker(word): #переделанная функция из командного кода для WORDLE, проверяет, что пользователь ввёл именно число
    cifras = '1234567890'
    for char in word:
        if char not in cifras: 
            return False
        else:
            return True

newgame = "Y" #Позволяет запустить код заново при желании
while newgame == "Y":
#for i in range(1,100): # для тестирования раcкомментировать эту строку, строку 16, закомментировать строки 9, 10, 12-15
    while True:
        numb = input("Input your NUMBER in range from 1 to 99:")
        if charac_checker(numb) == True and 1 <= int(numb) <= 99:
            break
    #numb = i
    shatter = list(numb) #разделяю число на цифры
    if len(numb) == 2 and numb[1]!="0": #если не десяток, то добавляю ещё ноль, чтобы обозначить первую цифру как десяток
        shatter = shatter[0] + "0" + shatter[1]
    divide = list()
    for i in shatter: #привожу число в подобающую для форматирования запись
        divide.append("{"+i+"}")
    divide = " ".join(divide)
    proces = divide.format("ноль", "один", "два", "три", "четыр", "пять", "шесть", "семь", "восемь", "девять") #форматирую число в запись порядковыми числительными. У "четыре" не хватает окончания исключительно для удобства работы далее, чтобы не писать лишние строчки.
    
    if "ноль" in proces: #начинаю преобразования для десятков и всех чисел, включающих десятки в свою аналитическую запись
        if "один ноль" in proces:
            proces = proces.replace("один ноль", "десять")
        elif "четыр ноль" in proces:
            proces = proces.replace("четыр ноль", "сорок")
        elif "девять ноль" in proces:
            proces = proces.replace("девять ноль", "девяносто")
        elif "ь ноль" in proces:
            proces = proces.replace(" ноль","десят")
        else: proces = proces.replace(" ноль","дцать")
        
    if "десять" in proces and proces != "десять": #со вторым десятком чисел приходится разбираться отдельно
        proces = proces.split() #Делю запись чисел на слова, меняю их местами и склеиваю обратно, чтобы удобнее проводить .replace()
        proces = proces[::-1]
        proces = "".join(proces)
        proces = proces.replace("а", "е") #разбираюсь с частными случаями
        proces = proces.replace("ь", "")
        proces = proces.replace("десят", "надцать")
        
    proces = proces.replace("четыр", "четыре") #если под конец процесса где-то должно остаться слово "четыре", то оно восполняется до этой формы
    
    print(proces)    
    newgame = input("Хотите попробовать снова? Y/N ") #см строку 1

