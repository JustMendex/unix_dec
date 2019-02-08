import crypt

def passwordmatching(cryptedpassword,dictfilelocation):

    dictionaryfile= open(dictfilelocation,'r')

    salt = cryptedpassword[0:2]

    for word in dictionaryfile.readlines():

        word = word.strip('\n')

        endresult = crypt.crypt(word,salt)

        if(cryptedpassword == endresult):

            print "[+] password is: "+word + '\n'

            return

        else:

            print "[-]password not found" + '\n'

    return        

def main():

    print "give the location of the password file "+ '\n'

    passfilelocation =raw_input()

    print "give the location of the dictionary file "+ '\n'

    dictfilelocation =raw_input()

    passwordfile = open(passfilelocation,'r')

    for line in passwordfile.readlines():

    	if ":" in line:

        	username=line.split(':')[0]

        	cryptedpassword =line.split(':')[1].strip()

        	print "[*] Cracking Password For: "+username

        	passwordmatching(cryptedpassword,dictfilelocation)

    	else:

        	cryptedpassword=line.strip()

        	print "[*] Cracking Password For: "+username

        	passwordmatching(cryptedpassword,dictfilelocation)

if __name__ == "__main__":

    main()