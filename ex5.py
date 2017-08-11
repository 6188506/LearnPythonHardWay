# -*- coding: utf-8 -*-
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_height_cm = round(74*2.54) # cm
my_weight = 180 # lbs
my_weight_kg = round(180*0.45) # kg
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about  %s." % my_name
print "He's %d inches (%d cm) tall." %(my_height,my_height_cm)
print "He's %d pounds (%d kg) heavy" %(my_weight,my_weight_kg)
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair" % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d ,%d, and %d I get %d." %(my_age,my_height,my_weight,my_age+my_height+my_weight)

