# backupcisco
26-06-2019
property of José  Miguel Ferreira

free for use, modifications, and redistributions must include credits to owner.

it makes use of telnetlib, so switches must be telnetable to
it expects username & password in order to extract configurations
it copies running-config to the machine by making use of tftp

How to use:
write list with cisco switches to a text file with name 'cisco_switches.list' with one switch per line.

running backupcisco.py asks for input:


Enter User Name: >? 
username credentials for your cisco switch

Password:
Password for Username

Enable Password:
Cisco's enable password for copy running-config tftp: priviledges

Enter TFTP server ip: >? 
Ip address of the machine where you are executing the code. It will use tftpy to setup a TFTP server on your machine,
where the default folder is 'configs'. All your configurations will be backed up to this location.


What it does:
Parses cisco_switches.list
For each ip in the list, 
    telnets with the defined credentials, and elevates to enabled mode
    Executes copy run tftp://<user defined ip>/configs/<ip of switch>.cfg
