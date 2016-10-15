# -*- coding: utf-8 -*-

usinp = (raw_input('-> '))#ввод имени, открываемого файла
#print "user input: ", type(usinp)
len_usinp = len(str(usinp))
#print type(len_usinp)
#замена разширения файла
extension = '.CSV'

#usinp[-4:len_usinp]#если оставить разширение, которое было

usinp_e = usinp[0:-4] + 'e' + extension 
print usinp_e


s = open(usinp).read()#прочитали исходный файл


#блок замен
s = s.replace('"', '')#удаляем кавычки
s = s.replace('sec', '"sec"')#удаляем кавычки
s = s.replace('mA', '"mA"')#удаляем кавычки
s = s.replace('mV', '"mV"')#удаляем кавычки


s = s.replace('    ', '\t')#меняем запятую на точкуу
#s = s.replace(',', '.')#меняем запятую на точкуу
#s = s.replace('\n', ', ')#замена новой строки на запятую
#s = s.replace(',', '\t')#замена запятой символом табуляции
s = s.replace('.', ',')#замена точки заятой

#создаем новый файл для записывания в него изменений
f = open(usinp_e, 'w')#открыли файл (создали)
f.write(s)#записали
f.close()#закрыли