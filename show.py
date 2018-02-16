import pickle
import sys

with open('info.txt', 'r') as file:
        receivers = pickle.load(file)
        names = pickle.load(file)
        classes = pickle.load(file)
        emailsToNames = pickle.load(file)
	namesToEmails = pickle.load(file)
        emailsToClasses = pickle.load(file)
        targets = pickle.load(file)
	kills = pickle.load(file)

#print len(names)
strlist = []
if 'all' in sys.argv:
	for x in sorted(names):
		mStr = '%-15s' % (x,)
	       	mStr += '| Email: %-28s' % (namesToEmails[x],)
              	mStr += '| Kill Count: %-4s' % (str(kills[namesToEmails[x]]),)
		strlist.append(mStr)
else:
	for x in targets.keys():
		mStr = '%-15s' % (emailsToNames[x],)
		if 'e' in sys.argv:
			mStr += '| Email: %-28s' % (x,)
		if 't' in sys.argv:
			mStr += '| Target: %-15s' % (emailsToNames[targets[x][0]],)
		if 'p' in sys.argv:
			mStr += '| Pursuer: %-15s' % (emailsToNames[targets[x][1]],)
		if 'kt' in sys.argv:
			mStr += '| Kill Timer: %-4s' % (str(targets[x][2]),)
		if 'kc' in sys.argv:
			mStr += '| Kill Count: %-4s' % (str(kills[x]),)
		if 'c' in sys.argv:
                        mStr += '| Classes: ' + str(classes[x])
		strlist.append(mStr)	

if 'count' in sys.argv:
	print len(targets)

for x in sorted(strlist):
	print x
