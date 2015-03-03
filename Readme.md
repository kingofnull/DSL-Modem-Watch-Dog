##What Is It?
Its Python Script Which Observes Internet Connectivity And Reset DSL Line When Internet Is Not Available.
<br />
##Why
DSL Modem Has Kind Of Problem Which They Can't Dial The User/Password On The Line (At Least Mine Does). The Only Way To Problem Is Reset The DSL Line Connection Or Mainly Reset The DSL Modem.
This Script Check The Internet Connection In A Loop And If It Internet Connection Is No Available Connect To The Modem And Run Two Commands To Reset The Line. 
<br />
All Options Are Configurable And Should Be Set In `config.ini`. The Python Script And Win32 Binary Are Available.
<br />
##Configuration
The Following Setting Should Set In `config.ini`
<br />
######MODEM_ADDRESS
Specify The DSL Modem IP Address To Make Telnet Connection.
<br />
######MODEM_USER
Specify The DSL Modem User Name Address To Make Telnet Connection. By Default It's Not Needed And Should Be Empty.
<br />
######USER_RECIEVECODE
Specify The Code That Modem Will Send To Get User Name. By Default It's Not Needed And Should Be Empty.
<br />
######MODEM_PASSWORD
Specify The DSL Modem Password To Make Telnet Connection.
<br />
######PASSWORD_RECIVECODE
Specify The Code That Modem Will Send To Get Password.
<br />
######TELNET_RECIEVE_CODE
Specify The Code That Modem Will Send To Notify It's Ready For Receive Telnet Commands.
<br />
######RUN_CODE_1
Specify The First Telnet Command To Run On Reset Request.
<br />
######RUN_CODE_2
Specify The Second Telnet Command To Run On Reset Request.
<br />
######EXIT_CODE
Specify The Second Telnet Command To Close Connection.
<br />
######INTERNET_CHECK_TCP_SERVER
Specify The Server Which Will Be Used To Check Internet Connectivity.
<br />
######INTERNET_CHECK_TCP_PORT
Specify The Server,s Port Which Will Be Used To Check Internet Connectivity. The Port Should Be Open On TCP.
<br />
######INTERNET_CHECK_TIME_OUT
Specify Internet Check Connection Timeout In Seconds.
<br />
######INTERNET_CHECK_INTERVAL
Specify Normal Internet Check Internal In Seconds.
<br />
######BACK_ALIVE_RETRY_MAX
Specify Maximum Number Of Retry After Reset Line.
<br /><br />
#####Default Configuration As Sample:
```
[MODEM]
MODEM_ADDRESS = "192.168.1.1"
MODEM_USER=""
USER_RECIEVECODE=""
MODEM_PASSWORD= "100604"
PASSWORD_RECIVECODE="Password: "
TELNET_RECIEVE_CODE="> "
RUN_CODE_1="wan adsl close"
RUN_CODE_2="wan adsl open"
EXIT_CODE="exit"

[CONNECTION]
INTERNET_CHECK_TCP_SERVER="yahoo.com"
INTERNET_CHECK_TCP_PORT=80
INTERNET_CHECK_TIME_OUT=2
INTERNET_CHECK_INTERVAL=10
BACK_ALIVE_RETRY_MAX=60
```