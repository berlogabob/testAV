# -*- coding: utf-8 -*-
my_file = open(raw_input('Введи имя файла\n->'), "w")
print 'имя файла ', my_file.name
print "В каком режиме файл открыт: ", my_file.mode