# Date 31-07-24 || Rohit Tiwari


## `What is CSRF`

>Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated

Method: 
- Change filed name etc


How it work??

> Suppose we have visited a site name xyz.com and ther's a change password field and want to change the password of it ...
> it send a post req to https://xyz.com/changepassword=emailaddr

> if we somehow change make the victim to click on the link and change there password  without click on it then worked