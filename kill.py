import sys
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

def sendDiedEmail(dead):
	text = "You have been assassinated, better luck next time :("
	sendMsg(dead, text)

def sendNewTargetEmail(pursuer, newTarget):
        text = "Good job on taking care of your target!  Your new mark is %s.\nYour classes are now %s.\n\n glhf" % (emailsToNames[newTarget], " | ".join(classes[pursuer]))
        sendMsg(pursuer, text)

def absorbClasses(victim, pursuer):
	for x in classes[victim]:
		if x not in classes[pursuer]:
			classes[pursuer].append(x)
	#del classes[victim]

def mKill(dead):
	pursuer = targets[dead][1]
	newVictim = targets[dead][0]
	sendDiedEmail(dead)
	absorbClasses(dead, pursuer)
	sendNewTargetEmail(pursuer, targets[dead][0])
	targets[pursuer] = [newVictim, targets[pursuer][1], 7]
	targets[newVictim] = [targets[newVictim][0], pursuer, targets[newVictim][2]]
	kills[pursuer] += 1
	del targets[dead]

mKill(sys.argv[1])

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
