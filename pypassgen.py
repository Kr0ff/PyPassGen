#!/usr/bin/python
#Author: Seph0ra
#Date: 4/09/2018
#Version: 1.0v

print "---------------------------------------"
print " ___      ___             ___          "
print "| _ \_  _| _ \__ _ ______/ __|___ _ _  "
print "|  _/ || |  _/ _` (_-<_-< (_ / -_) ' \ "
print "|_|  \_, |_| \__,_/__/__/\___\___|_||_|"
print "    |__/                               "
print "---------------------------------------"
print "\n"



import random

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
passlength = input('Length of your password: ')
passgen = ''


for pas in range(passlength):
    passwd = random.randrange(len(chars))
    passgen = passgen + chars[passwd]

print passgen
