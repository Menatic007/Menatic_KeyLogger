# Menatic KeyLogger

![Python Version](https://img.shields.io/badge/python-3.x-blue?style=flat&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=flat&logo=linux)
![GitHub](https://img.shields.io/github/license/Menatic007/Menatic-SubDominator?style=flat-square)
![GitHub](https://img.shields.io/github/repo-size/Menatic007/Menatic-SubDominator)
![GitHub](https://img.shields.io/github/forks/Menatic007/Menatic-SubDominator?style=flat-square)
![GitHub](https://img.shields.io/github/stars/Menatic007/Menatic-SubDominator?style=social)


![unknown](https://user-images.githubusercontent.com/102872534/187035669-18b1ca0a-4d86-4a35-88ec-71f6ed561008.png)


## **Description**

Menatic Keylogger is a fully undetectable malware that will capture all keystrokes from a victim machine and use discord webhooks to transfer these keystrokes to the attacker machine, without causing anything suspicious to take place that in-turn will trigger most anti-virus softwares. Discord webhooks will be considered as normal discord traffic, thus blends away our malicious activities even from network firewalls. 

  - **All user logins and passwords**
  - **Bank passwords**
  - **social media account passwords**
  - **Emails sent to people**
  - **Complete reconaissance of the victims day to day activities**
  - **Bypasses Windows Defender**

## Disclaimer !!!

<p>The exploits and malware built on this respository are mainly for POC and Educational purposes only. The developer is in no way responsible for any sort of misuse of tools and exploits or spreading of malware from this respository.</p>


## Prerequisites

*From the standard libraries.*
* datetime
* threading 
* Timer 
* os 

*Not from the standard libraries.*
* discord-webhooks 
* keyboard
## Installation


<code>

- git clone https://github.com/Menatic007/Menatic_KeyLogger.git
  
- cd Menatic_KeyLogger
  
- pip3 install -r requirements.txt

- Installation done, as simple as that.
  
</code> 


## Usage

First make a discord server or use an existing one.

Create a seperate channel for this program.

Get your webhook url for that particular channel, if you dont know how to, there are many you tube videos. 

Open the script with a text editor and paste the url under `discord_webhooks_url` on line 11.



<code>

To run this on the victim machine in the form of a python script do the following on the victim machine:

- python3 menatickeylogger.py

To run this on the victim machine in the form of a .exe file, do the following before sending it to the victim:

- pyinstaller <**full_path_to_script**> --onefile --noconsole

You should find your executable in the dest folder. You can now run the exe file in the victim machine.

Make your own changes to the file for it to gain persistence, we will not be covering that in detail because this is only a **Proof of Concept**

</code>



## Built With

* **Python 3.10.5** - [https://www.python.org/](https://www.python.org/)

## Points to Note:

- You can also change the time of how fast you want to receive keystrokes on your discord server by changing the `time_to_send_logs` option, the unit of time being used is seconds.

