#! /usr/bin/python
# filename: ex5.py

'''
This exercise is only to let you know that you could make strings have 
variables in them. You embed variables inside a string by using specialized
format sequences and then put the var at the end
'''

def main():
  my_name = 'Kinnin Yung'
  my_age = 25 # not a lie
  my_height = 178 # cm
  my_weight = 180 # lb
  my_eyes = 'Black'
  my_teeth = 'White'
  my_hair = 'Black'

  print "Let's talk about %s." % my_name
  print "He's %d cm tall." % my_height
  print "He's %d pounds heavy." % my_weight
  print "Actually that's not too heavy."
  print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
  print "His teeth are usually %s depending on the coffee." % my_teeth

  print "If I add %d, %d, and %d I get %d." % (my_age, my_height, \
          my_weight, my_age + my_height + my_weight)


if __name__ == '__main__':
  main()
