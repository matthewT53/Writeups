# Access Box:

## Nmap scan:
* The nmap scan reveals the services  
```js
  $ nmap -sS 10.10.10.98
  Results:
    Port 21 -> FTP
    Port 23 -> Telnet
    Port 80 -> Website
```

## FTP:
* The ftp server supports anonymous read logins.
* Login as user "anonymous" and type any password you want.
* Once logged in, there are two folders:
  * Backups:
    * backup.mdb
  * Engineers
    * Access Control.zip
* Use strings on backup.md to obtain the password for the zip file:
  * Should be "access4u@security"
* The zip file contains an outlook data file. You can import it into outlook or use a standard PST viewer to look at the contents.
  * The file reveals that the password to the "security" account is "4Cc3ssC0ntr0ller".

## Telnet:
* Now that we have the password, we can go ahead and telnet into the machine.
* Run:
```js
  $ telnet 10.10.10.98
  User: security
  Password: 4Cc3ssC0ntr0ller
```
* Going to security's desktop folder, there is a file called user.txt which contains the hash.

## Priv escalation:
### Enumeration:
* **Commands used:**
```js
  net users -> Enumerate all users on the system
  net user administrator -> Enumerate permissions for a specific user 
```
* If we enumerate the administrator account, we find that the administrator doesn't require a password.
* This means we can execute commands on the system as the administrator.
* We can use a tool called **runas**.

## Obtaining root.txt:
* The idea is to use the administrator account to copy the root.txt file into a folder that we can access.
* The directory that we are currently in is "c:/users/security".
* To preserve this state, we used the /env switch.
* **Commands used:**
```js
  runas /env /savecred /user:ACCESS\administrator 
  "cmd.exe /K more \"c:/users/Administrator/Desktop/root.txt\" > root.txt"
```

## What I learned:
* To see the owner of all files and directories:
```js
  dir /q
```
