import pickle
import smtplib

sender = 'bradley7221@gmail.com'
subject = "AAssassins"

with open('info.txt', 'r') as file:
	receivers = pickle.load(file)
	names = pickle.load(file)
	classes = pickle.load(file)
	emailsToNames = pickle.load(file)
	namesToEmails = pickle.load(file)
	emailsToClasses = pickle.load(file)
	targets = pickle.load(file)
	kills = pickle.load(file)

def sendMsg(recipient, text):
	server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("bradley7221@gmail.com", "assassins")
	msg = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (sender, recipient, subject, text)
	server.sendmail(sender, recipient, msg)

def sendWarningEmail(key):
	text = "You have 48 hours to kill %s or you will die. \nglhf" % (emailsToNames[target[key][0]])
	sendMsg(key, text)

def sendDiedTimeEmail(dead):
	text = "You ran out of time, better luck next time :("
	sendMsg(dead, text)

def sendNewTargetEmail(pursuer, newTarget):
	text = "An unfortunate accident has happened to your mark.  As such, your new mark is %s.\nYour classes are still %s.\n\n glhf" % (newTarget, " | ".join(classes[pursuer]))
	sendMsg(pursuer, text)

def sendWinnerEmail(id):
	text = "Wow you win!  Good job."
	sendMsg(id, text)

if len(targets) == 1:
	for x in targets:
		sendWinnerEmail(x)

listKT = []
#deincrement targets
for key in targets.keys():
	timeLeft = targets[key][2]
	victim = targets[key][0]
	pursuer = targets[key][1]

	#if they are at not on their last day
	if timeLeft > 2:
		targets[key] = [victim, pursuer, timeLeft - 1]
		if timeLeft == 3:
			sendWarningEmail(key)
	#They ran out of time :(
	else:
		sendDiedTimeEmail(key)
		targets[pursuer] = [victim, targets[pursuer][1], targets[pursuer][2]]
		listKT.append(pursuer)
		targets[victim] = [targets[victim][0], pursuer, targets[victim][2]]
		del targets[key]

for x in listKT:
	if x in targets:
		targets[x] = [targets[x][0], targets[x][1], 7]
		victim = targets[x][0]
		sendNewTargetEmail(x, victim)

#update file
def produceFiles():
        with open('info.txt', 'w') as file:
                pickle.dump(receivers, file)
                pickle.dump(names, file)
                pickle.dump(classes, file)
                pickle.dump(emailsToNames, file)
		pickle.dump(namesToEmails, file)
                pickle.dump(emailsToClasses, file)
                pickle.dump(targets, file)
		pickle.dump(kills, file)
produceFiles()
