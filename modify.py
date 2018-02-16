import pickle

with open('info.txt', 'r') as file:
        receivers = pickle.load(file)
        names = pickle.load(file)
        classes = pickle.load(file)
        emailsToNames = pickle.load(file)
        namesToEmails = pickle.load(file)
        emailsToClasses = pickle.load(file)
        targets = pickle.load(file)
        kills = pickle.load(file)


classes['Isabelchu123@gmail.com'] = ['Mage']

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

