
- Authentication is the process of verifying the identity of a user or client. Websites are potentially exposed to anyone who is connected to the internet. This makes robust authentication mechanisms integral to effective web security.
- There are mainly three 3 types of Authentication:
	1. knowledge Factor : Is like something we know password or question to security question 
	2. Possesion Factor : The physical factor such as token or RFID card 
	3. Inherence Factor : Something we do like biometric

## Difference between Authentication & Authorization ?

- Authentication is the process of verifying that a user is who they claim to be. Authorization involves verifying whether a user is allowed to do something.

## How do this occur ?

- There are mainly 3 factors 
  a. Weak mechanism against bruteforce attacks
	b. Poor mechanism allow authentication implementaion that allow hacker to bypass easily

## Impact of authentication?

- Depending on the factor authentication mainly it is high impact


## Vulnerabilities in password-based login

For websites that adopt a password-based login process, users either register for an account themselves or they are assigned an account by an administrator. This account is associated with a unique username and a secret password, which the user enters in a login form to authenticate themselves.


![[../Networking/assests/Pasted image 20250616201329.png]]


In this scenario, the fact that they know the secret password is taken as sufficient proof of the user's identity. This means that the security of the website is compromised if an attacker is able to either obtain or guess the login credentials of another user.

This can be achieved in a number of ways. The following sections show how an attacker can use brute-force attacks, and some of the flaws in brute-force protection. You'll also learn about the vulnerabilities in HTTP basic authentication.

- Mainly types are :
- Bruteforce attacks
- Bruteforce username
- Bruteforce password
- username enumeration

While attempting to brute-force a login page, you should pay particular attention to any differences in:

- **Status codes**: During a brute-force attack, the returned HTTP status code is likely to be the same for the vast majority of guesses because most of them will be wrong. If a guess returns a different status code, this is a strong indication that the username was correct. It is best practice for websites to always return the same status code regardless of the outcome, but this practice is not always followed.
- **Error messages**: Sometimes the returned error message is different depending on whether both the username AND password are incorrect or only the password was incorrect. It is best practice for websites to use identical, generic messages in both cases, but small typing errors sometimes creep in. Just one character out of place makes the two messages distinct, even in cases where the character is not visible on the rendered page.
- **Response times**: If most of the requests were handled with a similar response time, any that deviate from this suggest that something different was happening behind the scenes. This is another indication that the guessed username might be correct. For example, a website might only check whether the password is correct if the username is valid. This extra step might cause a slight increase in the response time. This may be subtle, but an attacker can make this delay more obvious by entering an excessively long password that the website takes noticeably longer to handle.
-  *Suppose we have given two user one is valid and another one is invalid with wrong password any when we logged in there will be a time difference in response time *