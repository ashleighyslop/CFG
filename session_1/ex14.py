from sys import argv

script, user_name = argv
prompt ='>'

print "Hi %s, I'm the %s script" % (user_name, script)
print "I'd like to ask you a few questions."
print "Where do you live %s?" % (user_name)
lives = raw_input(prompt)

print"what type of computer do you have %s" % (user_name)
computer = raw_input(prompt)

print """oh so you live in %r and
have a %r computer""" % (lives, computer)
