import telnetlib
import getpass

user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

device_list = ["Isi Ip Disini seperti disamping","192.168.99.2",
			   "192.168.99.3","192.168.99.4"]

for host in device_list:
	print "Configuring %s" % (host)
	tn = telnetlib.Telnet(host)

	tn.read_until("Username: ")
	tn.write(user + "\n")
	if password:
		tn.read_until("Password: ")
		tn.write(password + "\n")

	tn.write("Isi Command disini \n")

	print tn.read_all()
