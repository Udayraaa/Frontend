# How to connect to SQL Database

To preface I only know how to use SSMS so good luck with other things if you use them.

Download SSMS: https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16&redirectedfrom=MSDN

Once in SSMS you should be on a "Connect to Server" screen

Ensure the following:

```Server Type: Database Engine
Server Name: tcp:cis4375.database.windows.net
Authentication: Azure Active Directory - Universal with MFA
User name: [YOUR UH EMAIL]
```
Microsoft should then ask you to sign in 

Press "Connect"

**Boom** you're connected.

_Congratulations~~_

# Database Info
```
serverName = tcp:cis4375.database.windows.net
databaseName = CIS4375TEAM23DB
```

# Run the Website

Open Visual Studio Code
Link GitHub (must have git installed)
Clone repository 
```
git clone https://github.com/Udayraaa/Quantico-Consulting-Site.git
```
Ensure you have python installed (3.12.0) works for sure
Change Directory to the correct location (you can right click on the cloned repo)
```
cd quanticonConsulting
``` 
Install requirements
```
pip install -r requirements.txt
pip install mssql-django 
pip install Pillow 
```
INSTALL ODBC DRIVER 17 (IT HAS TO BE 17, 18 DOESNT WORK)
```
https://go.microsoft.com/fwlink/?linkid=2249004
```
Run Server
```
python3 manage.py runserver
```
test

SiteUser
_Qwerty123

databasename: CIS4375TEAM23DB
servername: cis4375.database.windows.net
user: SiteUser
pass:_Qwerty123


Ensure you have python installed (3.12.0) works for sure

cd quanticonConsulting

pip install -r requirements.txt
pip install mssql-django 
pip install Pillow 

INSTALL ODBC DRIVER 17 (IT HAS TO BE 17, 18 DOESNT WORK)
https://go.microsoft.com/fwlink/?linkid=2249004




