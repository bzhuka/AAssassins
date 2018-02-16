import smtplib
import random
import pickle

#Davey modifies this at the start to "randomize" the game
#Choose a number that's not a factor of the total number players
#You can't change this number halfway through
randomNum = 5
sender = 'bradley7221@gmail.com'
tempR = "ktlam99@gmail.com grace.jf.lily@gmail.com reidmasaki20@gmail.com jerryklai@gmail.com Wenxinfan98@gmail.com iywu11@gmail.com Stev1612@gmail.com Sun.amanda26@gmail.com josephyu612@gmail.com jt.whirlpoolgalaxy@gmail.com jason.sean.liu@gmail.com reine.naka@gmail.com leung.jasonh@gmail.com lpham127@gmail.com Hannah.h.liu98@gmail.com jenlin5368@gmail.com rebekah.park.12@gmail.com imakawakami@gmail.com hannah.pham@gmail.com joshuayu12@gmail.com aw123abc@gmail.com jnwidjaja@gmail.com jlam1999@g.ucla.edu markdong413@yahoo.com notwdjw@gmail.com byronc@ucla.edu jeremiah.fan@gmail.com sydneyk98@gmail.com ryan.k.cheng@gmail.com Gsukarto@gmail.com jeffrey7221@gmail.com debcheng3@gmail.com ethankato@g.ucla.edu Kayleesiu24@gmail.com nwtsai@gmail.com Kristee.song@gmail.com michelle.chungg@gmail.com kimberlyh.hoops31@gmail.com lollipoplinz@gmail.com jey.truong@gmail.com biviana_lie@outlook.com siow98@ucla.edu jrmashita@ucla.edu nney78@gmail.com Isabelchu123@gmail.com jordan@leongfamily.us zhangannie0@gmail.com mandiahn@yahoo.com yeokts@gmail.com timothyli97@gmail.com nicklin369@gmail.com li.tina.grace@gmail.com"
receivers = tempR.split()
tempN = "Katie Grace Reid Jerry Lulu Ingrid Steven Amanda Joseph JonathanTse JasonLiu Reine JasonLeung Lam HannahLiu Jennifer Rebekah Scott HannahPham JoshYu Angela JoshuaWidjaja Jlam Mark Davey Byron Jeremy SydneyK Ryan Griffin Jeffrey Deborah EthanKato Kaylee Nathan Kristee Michelle Kimberly Lindsey Jenny Bivi Leo JOel Nateney Isabel Jordan Annie Mandi Steffi Timothy Nick Tina"
names = tempN.split()
tempC = "Apothecary Apothecary Archer Archer Archer Archer Archer Archer Archer Mage Archer Archer Archer Mage Mage Mage Mage Mage Mage Mage Mage Mage Mage Mage Ninja Ninja Ninja Ninja Ninja Ninja Ninja Ninja Ninja Ninja Rogue Rogue Rogue Rogue Rogue Rogue Sorceror Sorceror Sorceror Sorceror Sorceror Sorceror Sorceror Sorceror Sorceror Sorceror Sorceror Sorceror"
tempClasses = tempC.split()
classes = {}
emailsToNames = {}
namesToEmails = {}
emailsToClasses = {}
targets = {}
kills = {}
totalNumPlayers = len(names)
for i in range(totalNumPlayers):
	classes[receivers[i]] = [tempClasses[i]]
	emailsToNames[receivers[i]] = names[i]
	namesToEmails[names[i]] = receivers[i]
	emailsToClasses[receivers[i]] = tempClasses[i]
	targets[receivers[i]] = [receivers[(i + randomNum) % totalNumPlayers], receivers[(i - randomNum) % totalNumPlayers], 7]
	kills[receivers[i]] = 0

subject = "AAssassins"

def sendInitialEmails():	
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.login("bradley7221@gmail.com", "assassins")
	for i in range(totalNumPlayers):
		text = "Greetings %s\nYour target is %s.  Your class is %s.\nglhf\n" % (names[i], emailsToNames[targets[receivers[i]][0]], tempClasses[i])
		msg = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (sender, receivers[i], subject, text)
		server.sendmail(sender, receivers[i], msg)

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
#sendInitialEmails()
produceFiles()
