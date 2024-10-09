#Варіант 17
#17. Ввести з клавіатури три цілих числа (a, b, c). Визначити, 
#чи є вони трійкою Піфагора (с^2 = а^2 + b^2 або а^2=b^2+с^2 або b^2=а^2+с^2 ).
# Відповідь вивести в вигляді повідомлення. Результат роботи програми повинен відповідати
# показаному в прикладах
from babel import Locale

def readFromFile(filename):
    #зчитуємо з файула
    try:
        with open(filename, 'r') as file:
            a = int(file.readline())
            b = int(file.readline())
            c = int(file.readline())
            interfaceLanguage = file.readline().strip()
            languageName = getLanguageName(interfaceLanguage)
            return a, b, c, languageName

    except FileNotFoundError:
        return "Файл не знайдено";
    except ValueError:
        return "Помилка при зчитуванні файлу"

def writeToFile(filename, a, b, c, interfaceLanguage):
    try:
        with open(filename,'w') as outfile:
            outfile.write(str(a) + "\n")
            outfile.write(str(b) + "\n")
            outfile.write(str(c) + "\n")
            outfile.write(interfaceLanguage + "\n")
        return "Файл успішно записано під назвою " + filename
    except IOError:
        return "Помилка запису у файл"


def isPythagoreanTriple(a, b, c):
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        return "f(a,b,c) = Так, це трійка Піфагора"
    else:
        return "f(a,b,c) = Ні, це не трійка Піфагора"

def getLanguageName(interfaceLanguage):
    try:
        locale = Locale(interfaceLanguage)
        return locale.get_display_name()
    except ValueError:
        return "Невідомий код мови"


# Основна функція
def main():
    print("Зчитування файлу...")      
    dataFromFile = readFromFile("./MyData.txt")  
     # Якщо зчитування файлу повернуло рядок (наприклад, "Файл не знайдено" або помилка)
    if isinstance(dataFromFile, str):
        print("Результат: " + dataFromFile)
        print("Створимо новй файл")
        print("Введіть три цілих числа")
        try:
            a = int(input("a = "))
            b = int(input("b = "))
            c = int(input("c = "))
            interfaceLanguage = str(input("Введіть мову інтерфейсу (Наприклад uk, en) = ")).strip()
            print(f"Ви ввели: a = {a}, b = {b}, c = {c}, Мова інтерфейсу: {interfaceLanguage}")
            result = writeToFile("./MyData.txt", a, b, c, interfaceLanguage)
            print(result)
        except ValueError:
            print("Ви ввели не ціле число")
            return
    else:
        a, b, c, languageName = dataFromFile
        print(f"Зчитані дані: a = {a}, b = {b}, c = {c}, Мова інтерфейсу: {languageName}")
        print( isPythagoreanTriple(a,b,c))
    

        

if __name__ == "__main__":
    main()