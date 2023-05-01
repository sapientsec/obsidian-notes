![[Pasted image 20230420024319.png]]

# Recon


```bash
┌──(kali㉿kali)-[~]
└─$ nmap -sCV -Pn 10.10.11.209
Starting Nmap 7.93 ( https://nmap.org/ ) at 2023-04-17 12:35 EDT
Nmap scan report for 10.10.11.209
Host is up (0.053s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 94bb2ffcaeb9b182afd789811aa76ce5 (RSA)
|   256 821beb758b9630cf946e7957d9ddeca7 (ECDSA)
|_  256 19fb45feb9e4275de5bbf35497dd68cf (ED25519)
80/tcp open  http    Apache httpd 2.4.54 ((Debian))
|_http-title: The Mail Room
|_http-server-header: Apache/2.4.54 (Debian)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Service detection performed. Please report any incorrect results at [https://nmap.org/submit/](https://nmap.org/submit/ "https://nmap.org/submit/") . Nmap done: 1 IP address (1 host up) scanned in 11.03 seconds
![[Pasted image 20230420024521.png]]

[http://10.10.11.209/](http://10.10.11.209/ "http://10.10.11.209/")

```bash
Added to /etc/hosts
http://10.10.11.209/contact.php
Has an input form
┌──(kali㉿kali)-[~]
└─$ gobuster dir -u http://10.10.11.209/ -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt -t 20 --delay 100ms
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.11.209/
[+] Method:                  GET
[+] Threads:                 20
[+] Delay:                   100ms
[+] Wordlist:                /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Timeout:                 10s
===============================================================
2023/04/17 12:40:42 Starting gobuster in directory enumeration mode
===============================================================
/assets               (Status: 301) [Size: 313] [--> http://10.10.11.209/assets/]
/css                  (Status: 301) [Size: 310] [--> http://10.10.11.209/css/]
/template             (Status: 403) [Size: 277]
/js                   (Status: 301) [Size: 309] [--> http://10.10.11.209/js/]
/javascript           (Status: 301) [Size: 317] [--> http://10.10.11.209/javascript/]
/font                 (Status: 301) [Size: 311] [--> http://10.10.11.209/font/]
Progress: 87623 / 87665 (99.95%)
===============================================================
2023/04/17 12:52:17 Finished
===============================================================
```

Contact Form [http://10.10.11.209/contact.php](http://10.10.11.209/contact.php "http://10.10.11.209/contact.php") (edited)
    [http://10.10.11.209/inquiries/b227c2d4e39f3e2b72d10c99a252b501.html](http://10.10.11.209/inquiries/b227c2d4e39f3e2b72d10c99a252b501.html "http://10.10.11.209/inquiries/b227c2d4e39f3e2b72d10c99a252b501.html")

![[Pasted image 20230420024650.png]]

XSS email=tester%40htb.htb&title=President&message=What+whats+%3Cscript%3Ealert('XSS');%3C/script%3E+doc!+doc%3F

![[Pasted image 20230420024717.png]]

# Getting Shell Access

https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist






# Shell enumeration
look for hidden files with ls -a where you still haven’t and try to find credentials for another 




# SSH Connection




# Basic enumeration 

