import os

for i in os.walk("allimages/"):
    lista_immagini = i[2]

placeholder_lista = list()
for i in range(1, 4501):
    name = 'face-'+str(i)+'.png'
    placeholder_lista.append(name)

def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

output_lista = Diff(lista_immagini, placeholder_lista)

f = open('file_to_remove.txt', 'w')

for i in output_lista:
    f.write('rm ./glasses-or-no-glasses/faces-spring-2020/faces-spring-2020/'+i+' ; ')
