import telnetlib
import socket
import time
import subprocess
import sys
import ConfigParser
import re
import os
import platform
import subprocess

print(
 '>>>>>>>>>>>>>>>>>>DSL Modem Watch Dog<<<<<<<<<<<<<<<<<<\n\n+++++++++++++++++ Proudly Wrote By MSS ++++++++++++++++++\n\n---------------------------------------------------------');

if not(os.path.isfile('config.ini')):
	print('Config File \'config.ini\' Not Found.');
	f=open('config.ini','w+')
	f.write('[MODEM]\nMODEM_ADDRESS = "192.168.1.1"\nMODEM_USER=""\nUSER_RECIEVECODE=""\nMODEM_PASSWORD= "12345"\nPASSWORD_RECIVECODE="Password: "\nTELNET_RECIEVE_CODE="> "\nRUN_CODE_1="wan adsl close"\nRUN_CODE_2="wan adsl open"\nEXIT_CODE="exit"\n\n[CONNECTION]\nINTERNET_CHECK_TCP_SERVER="yahoo.com"\nINTERNET_CHECK_TCP_PORT=80\nINTERNET_CHECK_TIME_OUT=2\nINTERNET_CHECK_INTERVAL=10\nBACK_ALIVE_RETRY_MAX=60');
	f.close();
	print('Config File Created From Default Setting !');
	

config = ConfigParser.ConfigParser()
config.read(['config.ini'])
def GetOption(section,option):
	return re.sub(r'^"|"$', '', config.get(section,option))

MODEM_ADDRESS = GetOption("MODEM","MODEM_ADDRESS")
MODEM_USER=GetOption("MODEM","MODEM_USER")
USER_RECIEVECODE=GetOption("MODEM","USER_RECIEVECODE")
MODEM_PASSWORD=GetOption("MODEM","MODEM_PASSWORD")
PASSWORD_RECIVECODE=GetOption("MODEM","PASSWORD_RECIVECODE")
TELNET_RECIEVE_CODE=GetOption("MODEM","TELNET_RECIEVE_CODE")
RUN_CODE_1=GetOption("MODEM","RUN_CODE_1")
RUN_CODE_2=GetOption("MODEM","RUN_CODE_2")
EXIT_CODE=GetOption("MODEM","EXIT_CODE")


INTERNET_CHECK_TCP_SERVER=GetOption("CONNECTION","INTERNET_CHECK_TCP_SERVER")
INTERNET_CHECK_TCP_PORT=int(GetOption("CONNECTION","INTERNET_CHECK_TCP_PORT"))
INTERNET_CHECK_TIME_OUT=int(GetOption("CONNECTION","INTERNET_CHECK_TIME_OUT"))
INTERNET_CHECK_INTERVAL=int(GetOption("CONNECTION","INTERNET_CHECK_INTERVAL"))
BACK_ALIVE_RETRY_MAX=int(GetOption("CONNECTION","BACK_ALIVE_RETRY_MAX"))

def IsInternetAvailible():
  try:
    host = socket.gethostbyname(INTERNET_CHECK_TCP_SERVER)
    s = socket.create_connection((host, INTERNET_CHECK_TCP_PORT), INTERNET_CHECK_TIME_OUT)
    return True
  except:
     pass
  return False

  
def Ping():
	hostname=INTERNET_CHECK_TCP_SERVER
	if platform.system() == "Windows":
		command="ping "+hostname+" -n 1 -w "+str(INTERNET_CHECK_TIME_OUT*1000)
	else:
		command="ping -c 1 " + hostname
	# print command	
	proccess = subprocess.Popen(command, stdout=subprocess.PIPE)
	matches=re.match('.*time=([0-9]+)ms.*', proccess.stdout.read(),re.DOTALL)
	if matches:
		return matches.group(1)
	else: 
		return False


def ResetDSL():
    tn = telnetlib.Telnet(MODEM_ADDRESS)
    if MODEM_USER!="" :
        tn.read_until(USER_RECIEVECODE)
        tn.write(MODEM_USER + "\n")    
    if MODEM_PASSWORD!="" :
        tn.read_until(PASSWORD_RECIVECODE)
        tn.write(MODEM_PASSWORD + "\n")
    tn.read_until(TELNET_RECIEVE_CODE)
    tn.write(RUN_CODE_1+"\n")
    tn.read_until(TELNET_RECIEVE_CODE)
    tn.write(RUN_CODE_2+"\n")
    tn.read_until(TELNET_RECIEVE_CODE)
    tn.write(EXIT_CODE+"\n")
    return

# while True:
	# print Ping()
	# time.sleep(1)
	
State=True
while True:
	State= (Ping())
	if not(State) :
		sys.stdout.flush()
		print('\rInternet Is Not Avialible. Reset Message Is Sending. Wait For Stablizing . . .\n')
		try :
		  ResetDSL()
		except:
		  print('\rFail To Run Telnet Commands!\n')
		  
		ii=0
		while ii<BACK_ALIVE_RETRY_MAX and not(Ping()):
		  sys.stdout.write("\rInternet Is Not Avialible. Internet Check %dth Try" % ii)
		  sys.stdout.flush()
		  time.sleep(1)
		  ii+=1
		  #  time.sleep(90)
		print("\r\n")
	i=INTERNET_CHECK_INTERVAL
	while i>0:
		sys.stdout.write("\rInternet Is Avialible. Recheck In %d Seconds  " % i)
		sys.stdout.flush()
		time.sleep(1)
		i-=1
#print (tn.read_all())

