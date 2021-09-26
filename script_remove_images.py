#support script used for creating a shell command to remove images not correct

import os

#put in a directory the cleaned dataset
for i in os.walk("allimages/"):
    lista_immagini = i[2]

placeholder_lista = list()
for i in range(1, 4501):
    name = 'face-'+str(i)+'.png'
    placeholder_lista.append(name)

#detect which images are in the original dataset but not in the cleaned
def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

output_lista = Diff(lista_immagini, placeholder_lista)

#write into a file shell command to remove images that are in the original dataset but not in the cleaned
f = open('file_to_remove.txt', 'w')

for i in output_lista:
    f.write('rm ./glasses-or-no-glasses/faces-spring-2020/faces-spring-2020/'+i+' ; ')
