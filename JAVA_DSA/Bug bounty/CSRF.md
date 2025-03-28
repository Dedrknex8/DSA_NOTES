# Date 31-07-24 || Rohit Tiwari


## `What is CSRF`

>Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated

- It is done inorder to circumvent the CORS policy in performing other actions

Method: 
- Change filed name etc.


How it work??

> Suppose we have visited a site name xyz.com and there's a change password field and want to change the password of it ...
> it send a post req to https://xyz.com/changepassword=emailaddr

> if we somehow change make the victim to click on the link and change there password  without click on it then worked


## How Does CSRF works ?

- For a sucessfull CSRF to be possible three key condition should be matched 
- A *Relevant Action* : There should be a action within the application that the attacker could take  advantages of like the change-Email action,reset password
- *Cookie based Authentication* : The application should make use  cookies to identify the user who has made the requests. on a http request
- **No unpredictable request parameters.** : The requests that perform the action do not contain any parameters whose values the attacker cannot determine or guess. For example, when causing a user to change their password, the function is not vulnerable if an attacker needs to know the value of the existing password.
