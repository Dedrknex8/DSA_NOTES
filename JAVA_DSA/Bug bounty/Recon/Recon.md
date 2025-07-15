### Recon is the most important part of bug bounty and in cybersecurity

- In this i will share my own notes for recon with every knowledge i have

1. Certificates/Cert.sh 
 - Certificates, specifically SSL/TLS certificates, are used to verify the identity of websites and servers. When a website is issued a certificate, it's often logged in public Certificate Transparency (CT) logs. These logs are a publicly accessible record of all certificates issued by participating Certificate Authorities (CAs).
 - Cert.sh is a web interface in which a user can query a website for logs in this user can potentialy find subdomains domain name.

Reports: 

```Text
https://systemweakness.com/uncover-hidden-subdomains-using-crt-sh-3f5f3fe704df
https://aswinthambipanik07.medium.com/bug-bounty-recon-part-2-6aa549ba63d5
https://ervinszilagyi.dev/articles/certificate-parsing-with-domain-recon.html
```

# useful Commands

```text
curl -s https://crt.sh\?q\=\.com/&output\=json | jq -r '.[].name_values' | grep -Po '(\w+\.\w+)$'

# Extract domain names
curl -s "https://crt.sh/?q=%.com&output=json" | jq -r '.[].name_value' | tr '\n' ',' | tr ',' '\n' | sort -u | grep -Po '([a-z0-9-]+\.)+[a-z]{2,}'

## Subdomain Enumeration
#Using subfinder to get all domains
subfinder -d example.com -all -recursive > subexample.com.txt

# Alive domains exracted from subfinder
cat subexample.com.txt | httpx-toolkit -ports 80,443,8080,8000,8888 -threads 200 > subexample.coms_alive.txt

# Passive subdomains enumeration
amass enum -passive -d target.com | grep -oE '([a-zA-Z0-9_-]+\.)+target\.com'

# Find subdomains with CIDR or DNS 

amass intel -org "taget.com"
echo <CIDR/IP> | asnmap
```



### Very imp concept 

Active subdomain enumeration means directly interacting with the target 
Passive means using online available data
