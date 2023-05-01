![[Pasted image 20230430040723.png]]

Just another day as a SOC Analyst..

![](https://assets.tryhackme.com/additional/phishing5/main.png)  

A Sales Executive at Greenholt PLC received an email that he didn't expect to receive from a customer. He claims that the customer never uses generic greetings such as "Good day" and didn't expect any amount of money to be transferred to his account. The email also contains an attachment that he never requested. He forwarded the email to the SOC (Security Operations Center) department for further investigation.   

Investigate the email sample to determine if it is legitimate. 

**Tip**: Open the EML file with Thunderbird. 

---

Deploy the machine attached to this task; it will be visible in the split-screen view once it is ready.

If you don't see a virtual machine load then click the Show Split View button.

![](https://assets.tryhackme.com/additional/phishing5/p5-split-view.png)  

Answer the questions below

What is the email's timestamp? (answer format: **mm/dd/yyyy hh:mm**)
06/10/2020 05:58

Who is the email from?
06/10/2020 05:58

What is his email address?
info@mutawamarine.com

What email address will receive a reply to this email? 
info.mutawamarine@mail.com

What is the Originating IP?
192.119.71.157

Who is the owner of the Originating IP? (Do not include the "." in your answer.)
Hostwinds LLC

What is the SPF record for the Return-Path domain?
https://easydmarc.com/tools/spf-lookup?domain=mutawamarine.com
v=spf1 include:spf.protection.outlook.com -all

What is the DMARC record for the Return-Path domain?
https://easydmarc.com/tools/spf-lookup?domain=mutawamarine.com
v=DMARC1; p=quarantine;  fo=1

What is the name of the attachment?
SWT_#09674321____PDF__.CAB

What is the SHA256 hash of the file attachment?
sha256sum SWT_#09674321____PDF__.CAB
2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f

What is the attachments file size? (Don't forget to add "KB" to your answer, **NUM KB**)
https://www.virustotal.com/gui/file/2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f
400.26 KB

What is the actual file extension of the attachment?
https://www.virustotal.com/gui/file/2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f
rar

