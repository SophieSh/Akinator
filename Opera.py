import csv

temporary = []
countriespop = []
countriesopera = []
countries = []
opera = []
population = []
opera1 = []
population1 = []
peopleopera = []
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
    del mas[len(mas)-1] #удаляем цифру населения
    countriespop.append(' '.join(mas)) #записываем в список стран с порядком списка населения
    

with open('browser.csv') as d:
    reader1 = csv.reader(d, delimiter=',')
    i = 0
    for row in reader1:
        if i == 0:
            pass
        else:
            countriesopera.append(row[0]) #записываем страны для Opera 
            opera.append(float(row[8])) #записываем процентные данные для стран из списка countriesch
        i+=1
d.close()

for i in range(0,len(countriesopera)):
    countriesopera[i] = countriesopera[i][:len(countriesopera[i])-1] #удаляем пробел в названии стран

    
for i in range(0,len(countriespop)):
    for j in range(0,len(countriesopera)):
        if countriespop[i] == countriesopera[j]:
            countries.append(countriespop[i]) #ищем одинаковые страны
            opera1.append(opera[j]) # записываем процентные данные по Opera
            population1.append(population[i]) #записываем данные по населению

for i in range(0,len(countries)):
    peopleopera.append(int(opera1[i]*population1[i]/100)) #считаем количество человек в каждой стране, использующих Opera

print(sum(peopleopera))
