#!/usr/bin/python

from sys import exit

prompt = ">"

def start():
	print "You wake up late and have a bunch of stuff to do"
	print "Do you keep [sleeping] or [wakeup]"

	next = raw_input(prompt)

	if next == "sleeping":
		sleeping()
	elif next == "wakeup":
		wakeup()
	else:
		done("You have blown off all responsibilities for the day, NICE!")
def done(why):
	print why
	exit(0)

def sleeping():
	print "You continue sleeping and then never wake up!! You are in a virtual world!"
	print "\n when you finally realize you are still alive what do you do?"

	run = True

	while True:
		next = raw_input(prompt)
		print next
		if next == "walk around" or next == "run around" or next == "explore":
			run = false
			print "You are now discivering new things in the new world"
		elif next == "hide":
			dead("You hide and dont know what to do and die of starvation"
		elif next == "look":
			print "You see a portal that looks like the earth"
		elif next == "continue" or "cont":
			if run == True:
				dead("You try to run but you have no where to go"
			elif run == False:
				chamber()

def portal():
	print "You have reached the portal and see the world you used to live in, but you have some options"
	print "There are three options to choose from Option [1] [2] [3]"

	options = ["You are staying here and starting a new life", "You get to go back home like nothing happened", "When you get back you will be greeted by scientists about your virtual world experience"]

	pick = int(raw_input(prompt))
	
	print "You choose option number %d and you receive %s" % (pick, chests[pick-1])
	raw_input("Thank you for playing my game press any key to exit")
	

def wakeup():
	print "You wake up and face the reality and do the responsibilities you have to do"
	raw_input("press any key to return")
	start()

start()



