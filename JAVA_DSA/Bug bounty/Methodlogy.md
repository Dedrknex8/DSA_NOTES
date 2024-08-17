
# date 04-08-24 || Rohit Tiwari

> This is just a compilation of what i learned from bug bounty writeups and came with a statergy to go with when hunting for bug bounty

## Recon

### Submoain Enumeration
 
 -  Assetfinder
 - crt.sh
 - Subdomains .txt
### Find working Subdomains
 - httpx
 - httprobe
### Run automatic scanner like
- Nikto
- Nmap
- Nuclie
### Find non tech on site

- wapplayzer
### Find known bugs using this automated  tools
a) Subdomain Takeover

- [Subzy](https://github.com/PentestPad/subzy?source=post_page-----0e7eda23d324--------------------------------)

b) Broken link hijacking

- [Social Hunter](https://github.com/utkusen/socialhunter?source=post_page-----0e7eda23d324--------------------------------)

c) XSS

- [ParamSpider](https://github.com/devanshbatham/ParamSpider?source=post_page-----0e7eda23d324--------------------------------)

d) Open redirect 

- Use paramSpider

## Screenshorts

Then I use the tool aquatone for getting a screenshot of all the subdomains

- [AquaTone](https://github.com/michenriksen/aquatone?source=post_page-----0e7eda23d324--------------------------------)

## Urls 

Find urls in the site using tools like

- Waybacks annd gau
- [ ]  `Command ` cat alivesubs.txt | waybackurls | tee -a urls.txt
- Find alive tools using httprobe
  - [ ] cat urls.txt | httprobe | tee -a aliveurls.txt

-  Then I search for keywords on the urls found like config,ini,admin using grep command
- [ ] cat aliveurls.txt | grep config


### For refernce visite the site below

https://infosecwriteups.com/what-to-do-after-choosing-a-target-part-01-bug-bounty-0e7eda23d324



