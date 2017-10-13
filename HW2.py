#!/usr/bin/python

from sys import argv

script, name, age, birthmonth = argv

file = open("customers.txt" , "w")

line1 = "your name is %s" % name + "\n"
line2 = "you are %s years old" % age + "\n"
line3 = "Your birthmonth is %s" % birthmonth + "\n"

file.write(line1)
file.write(line2)
file.write(line3)

file.close()

file_input = open("customers.txt")

print file_input.read()
