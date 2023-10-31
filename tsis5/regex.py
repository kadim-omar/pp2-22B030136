import re
a = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
result = re.match("AC", a)
print(result)
#находит шаблон только в начале строки

a = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
result = re.search("AC", a)
print(result)
#находит первый указанный шаблон

a = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
result = re.findall("AC", a)
print(result)
#находит по шаблону все 

a = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
result = re.split("AC", a, maxsplit= 4)
print(result)
#разбивает элементы по шаблону

a = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
result = re.sub("AC", "CA", a)
print(result)
#одну подстроку заменяет на другую подстроку

a = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
result = re.fullmatch("AC", a)
print(result)
#проверяет подходит ли шаблон на конкретную строчку

s = "2948234823940      ----fsdkfsjdlfs98589358398^7 FSJDOFJSDFJOSffffgggg"
result=re.search(r"f.d", s)
#одна точка одна буква между

result=re.search(r"\d",s)
#выводит любую цифру

result=re.search(r"\D",s)
#любой символ кроме цифры

result=re.search(r"\s",s)
#пробельные символы

result=re.search(r"\S",s)
#НЕ пробельные символы

result=re.search(r"\w",s)
#любая буква, цифра или нижнее подчеркивание

result=re.search(r"\W",s)
#любая НЕ буква, НЕ цифра или НЕ нижнее подчеркивание

result=re.search(r"\bfsdk",s)
#начало или конец любого слова

result=re.search(r"\Bfsdk",s)
#НЕ укажет нам границу слова

result=re.search(r"[fssa]", s)
#диапазон из букв

result=re.search(r"[4-9]", s)
#диапазон из цифр

result=re.search(r"[^4-9]", s)
#диапазон кроме этих цифр

result=re.search(r"F|d", s)
#выбор шаблона что он найдет первее

result=re.search(r"\d{3}",s)
#использование квантификаторов

result=re.search(r"\d{1,3}",s)
#от скольки до скольки повторений 

result=re.search(r"\d{1,}", s)
#не менее чем одно повторение

result=re.search(r"\d{,4}",s)
#не более чем указанное повтрение






