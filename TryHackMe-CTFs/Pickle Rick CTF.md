# Pickle Rick CTF

The CTF can be found [here](https://tryhackme.com/room/picklerick)

Tuesday, January 10, 2023

![Pickle Rick Image](picklerick-01.png)

This Rick and Morty themed challenge requires you to exploit a webserver to find 3 ingredients that will help Rick make his potion to transform himself back into a human from a pickle.

Deploy the virtual machine on this task and explore the web application: 10.10.50.28

You can also access the web app using the following link: [https://10-10-50-28.p.thmlabs.com](https://10-10-50-28.p.thmlabs.com/) (this will update when the machine has fully started)

----------------------------------------

***Answer the questions below***

What is the first ingredient Rick needs?

What's the second ingredient Rick needs?

What's the final ingredient Rick needs?

---------------------------------------------

So, I begin :)

Note: during this event, I am feeding kids … so I walk away often during scans.

## What is the first ingredient Rick needs?

After opening the site [https://10-10-50-28.p.thmlabs.com](https://10-10-50-28.p.thmlabs.com/) , we see:

![Pickle Rick Image](picklerick-02.png)

Lets view the source for any useful info:

![Pickle Rick Image](picklerick-03.png)

Let look at the robots.txt

![Pickle Rick Image](picklerick-04.png)

I will also run the gobuster while we are at it.

> gobuster dir -u <https://10-10-50-28.p.thmlabs.com> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

![Pickle Rick Image](picklerick-05.png)

Visiting assets gives us the following:

![Pickle Rick Image](picklerick-06.png)

So we/I learn the following:

-   Username: **R1ckRul3s**
-   jQuery v3.3.1
-   Apache 2.4.18
-   Ubuntu
-   Bootstrap v3.4.0
-   A string of **Wubbalubbadubdub**

So now the question is where can we login?

Lets dig a little deeper:

> nmap -sV 10.10.50.28

![Pickle Rick Image](picklerick-07.png)

> gobuster dir -u <https://10-10-50-28.p.thmlabs.com> -x .php,.html,.js,.css -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

![Pickle Rick Image](picklerick-08.png)

I'll inspect the pages we found first, then maybe look at the ssh port.

Sooo, login.php hangs for a while.

Looks like my CTF machine timed out … so I started a new one.

Back to the login page

<https://10-10-106-125.p.thmlabs.com/login.php>

The source was uninteresting.

Lets try what we know:

Use the usrename and the robots.txt string … and that logged us in:

![Pickle Rick Image](picklerick-09.png)

I typed "ls" and it ran:

![Pickle Rick Image](assets/picklerick-010.png)

Lets look at these now:

Sup3rS3cretPickl3Ingred.txt
assets
clue.txt
denied.php
index.html
login.php
portal.php
robots.txt

Oh no!! **cat** does not work.

![Pickle Rick Image](assets/picklerick-011.png)

> pwd
/var/www/html

As I suspected, we are at the root of the site … so I will access them directly via the web server or browser.

-   Sup3rS3cretPickl3Ingred.txt  
    **The first ingredient!!!!!**
-   assets
-   clue.txt  
    Look around the file system for the other ingredient.
-   denied.php  
-   ![Pickle Rick Image](assets/picklerick-012.png)

## What's the second ingredient Rick needs?

Found the first, lets keep going with the clue.txt

I found the second ingredients in Rick's home directory

> ls /home/rick -al

![Pickle Rick Image](assets/picklerick-013.png)

But I can't cat, tac, head or tail it … so I can't see it .. I was trying to copy it to the web root, but it didn't take either.

> cp '/home/rick/second ingredients' /var/www/html/second.txt

Finally, less worked

> less '/home/rick/second ingredients'
**The second ingredient!!!!!**

## What's the final ingredient Rick needs?

Now for the third ingredient:

After digging around and looking for .txt files everywhere … I thought I needed to look deeper … eventually I found it under /root with sudo

> sudo ls /root -al

![Pickle Rick Image](assets/picklerick-014.png)

> sudo ls /root -al

3rd ingredients: **The third ingredient!!!!!**

Whew, done!
