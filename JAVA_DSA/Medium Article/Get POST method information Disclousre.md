
Rohit Tiwari / Dedrknex

Today in this article i will show how to get information disclosure bounty in a site .


Domain : target.com

endpoint  :  /api/user

So the domain and endpoint is dummy site and endpoint . While doing my recon i found a js files in it after extracting endpoint i got /api/user/update-User and visiting the endpoint it giving 400
response so i remove /updateme and then send the req got post method not allowed so changes to GET method got the users email id and uuid as response