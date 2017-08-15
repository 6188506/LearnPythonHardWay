#-*- coding: utf-8 -*-
x = "There are %d types of people." % 10  #定义一个格式化字符串
binary = "binary"
do_not = "don't"
y = "Those who konw %s and those who %s" % (binary,do_not) #把一个字符串放入另一个字符串

print x
print y

print "I said: %r." % x  #把一个字符串放入另一个字符串
print "I also said: '%s'." % y  #把一个字符串放入另一个字符串

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious  #把一个字符串放入另一个字符串

w = "This is the left side of..."
e = "a string with a right side"

print w + e
