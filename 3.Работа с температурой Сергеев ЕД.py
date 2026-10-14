def charac_checker(word): #переделанная функция из командного кода для WORDLE, проверяет, что пользователь ввёл именно число
    cifras = '1234567890.'
    for char in word:
        if char not in cifras: 
            return True
        else:
            return False

grad = None
temp = " "
while grad != "C" and grad != "F" and grad != "c" and grad != "f":
    grad = input("Choose degrees Celsius or Farenheit for initial temperature C/F: ")
    if grad != "C" and grad != "F" and grad != "c" and grad != "f":
        print("!!!Please enter only 'C' for Celcius or 'F' for Farenheit!!!")

while charac_checker(temp):
    temp = input("Enter temperature value in your chosen degrees: ")
    if charac_checker(temp):
        print("!!!Please enter a number for temperature value!!!")
temp = int(temp)

if grad == "C" or grad == "c":
    tempfin = str(temp*(9/5)+32)+"F"
else:
    tempfin = str((temp-32)*(5/9))+"C"
print("Conversion complete: " + tempfin)