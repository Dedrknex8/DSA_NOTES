# Project 01

> Here in this project i have created a simple bash script to check if a site is alive or down by using ping command and taking site name through user input

```<>
#!/bin/bash

read -p "Which site you want to ping? "  site

ping -c 1 $site
sleep 5s

if [[ $? -eq 0 ]] # this will check the status of the  site
then
        echo "Successfully connected to  $site"
else
        echo "Can't ping the site"
fi
```

