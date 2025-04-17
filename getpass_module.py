import getpass

user = getpass.getuser()

while True:
	password = getpass.getpass(f"User Name : {user}\nEnter password : ")

	if password.lower() == 'abcd':
		print ("Welcome!!!",user)
		break
	else:
		print ("The password you entered is incorrect.")
