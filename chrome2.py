import csv

temporary = []
countriespop = []
countriesch = []
countries = []
chrome = []
population = []
chrome1 = []
population1 = []
peoplech = []
mas = []
i = 0
k = 0
with open('population1.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        temporary.append(row[0])#открываем файл, записываем все, что есть во временный список
f.close()        
for i in range(0,len(temporary)):
    temporary[i] = temporary[i][7:]
    mas = temporary[i].split()
    population.append(int(mas[len(mas)-1])) #записываем в список населения
    del mas[len(mas)-1]
    countriespop.append(' '.join(mas)) #записываем в список стран с порядком списка населения
    

with open('browser.csv') as d:
    reader1 = csv.reader(d, delimiter=',')
    i = 0
    for row in reader1:
        if i == 0:
            pass
        else:
            countriesch.append(row[0]) #записываем страны для Chrome 
            chrome.append(float(row[1])) #записываем процентные данные для стран из списка countriesch
        i+=1
d.close()        

for i in range(0,len(countriesch)):
    countriesch[i] = countriesch[i][:len(countriesch[i])-1] #удаляем пробел в названии стран
    
for i in range(0,len(countriespop)):
    for j in range(0,len(countriesch)):
        if countriespop[i] == countriesch[j]:
            countries.append(countriespop[i]) #ищем одинаковые страны
            chrome1.append(chrome[j]) # записываем процентные данные по Chrome
            population1.append(population[i]) #записываем данные по населению
            
for i in range(0,len(countries)):
    peoplech.append(chrome1[i]*population[i]/100) #считаем количество человек в каждой стране, использующих Chrome

max = peoplech[0]
c = 0
for i in range(0,len(peoplech)-1):
    if peoplech[i]>max:
        max = peoplech[i]
        c = i
print(countries[c]) #находим максимум в peoplech, выводим страну, соответсвующую ему 
