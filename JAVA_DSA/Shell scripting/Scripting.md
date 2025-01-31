
Command to check supported shells in the system

```shell
┌──(dedrknex㉿R0xt)-[~]
└─$ cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/usr/bin/sh
/bin/bash
/usr/bin/bash
/bin/rbash
/usr/bin/rbash
/bin/dash
/usr/bin/dash
/usr/bin/tmux
/bin/zsh
/usr/bin/zsh
/usr/bin/zsh
```

## Comments in bash

```shell
#!/bin/bash

#This is comment 1
#
<<comment
This is
multi line Commnets
comment

echo "Worked"
```

> Output : `Worked`

## Arrays

```bash
#!/bin/bash

myArray=( 1 2 Name check)

#Array can store multiple data types
echo ${myArray[2]} # To get array

#To print all contents of array

echo ${myArray[*]}

# To get lenght of array

echo "length of array is : ${#myArray[*]}"

#slicing in  array also possible

echo "values from 2-3 ${myArray[*]:2:2}"

#After : 2 {defines where to start} : 2 {how many more want}


```

## Key value pair Arrays

```bash
#!/bin/bash

# How to store key value pair

declare -A  myArray # -A is used to delcare array in name key type
myArray=( [key]=value [name]=Chuck)
echo "get the first value of array by key ${myArray[key]}"
echo "second value by key : ${myArray[name]}"
```


## UserInput

> Taking input in from a user can be done by following

```bash
#!/bin/bash
echo "What is your name?"
read name

echo "Your name is : $name"
```


>Output 

```bash
┌──(dedrknex㉿R0xt)-[~/scirpts]
└─$ ./usrinp.sh
What is your name?
Hello
Your  name is : Hello
```

2. A variation using -p tag to read 

```bash
#!/bin/bash


read -p "What is your name? " name
echo "Your  name is : $name"
```

>Output

```bash
┌──(dedrknex㉿R0xt)-[~/scirpts]
└─$ ./usrinp.sh
What is your name? Hello
Your  name is : Hello
```

## Arithmatic operations

>Arithmatic operation can be accesed by `let` command || `(())` command

# IF else // elif

```bash
#!/bin/bash

read -p "Enter your age : " age

if [[ $age -ge 18 ]]
then
        echo "You're eligible to drive"
elif [[ $age -le 18 ]]
then
        echo "You're not eligible to drive"
else
        echo "You can do whatever you want"

fi
```

```bash
┌──(dedrknex㉿R0xt)-[~/scirpts]
└─$ ./cal.sh
Enter your age : 19
You're eligible to drive
```

#### Remarks
1. make sure of the space b/w brackets
2. after else no then conditon
3. At the end put fi

## Cases

```
#!/bin/bash

echo "Hey Choose an option"

echo "a = To see the current date"

echo "b=see the content of the current dir"

read choice

case $choice in
        a) date;;
        b) ls;;
        *) echo "choose a valid option"

esac
```

output

```
┌──(dedrknex㉿R0xt)-[~/scirpts]
└─$ bash cases.sh
Hey Choose an option
a = To see the current date
b=see the content of the current dir
a
Sat Aug 17 05:10:30 AM IST 2024
```

## Logical operation

> using or and conditional operator

1. In And operator both case should  be true
2. Or any conditon can  be true

```bash
#!/bin/bash

read -p "Enter your age : " age
read -p "Your country: " country
if [[ $age -gt 18 ]] && [[ $country == India ]]
then
        echo "You're eligible to drive"
else
		echo "You're no eligble"
```

## For loops

```bash
┌──(dedrknex㉿R0xt)-[~/scirpts]
└─$ cat loop.sh
#!/bin/bash

for i in 1 2 3 4 6
do
        echo "Number is $i"
done
```

>output

```bash
┌──(dedrknex㉿R0xt)-[~/scirpts]
└─$ bash loop.sh
Number is 1
Number is 2
Number is 3
Number is 4
Number is 6
```

> To wirte loops in a optimize way

```bash
┌──(dedrknex㉿R0xt)-[~/scirpts]
└─$ cat loop.sh
#!/bin/bash

for i in {1..6}
do
        echo "Number is $i"
done
```


## To run a loop from a file

```bash
┌──(dedrknex㉿R0xt)-[~/scirpts]
└─$ cat loopfile.sh
#!/bin/bash

File="/home/dedrknex/scirpts/numbers.txt"

for num in $(cat $File)
do
        echo "Num is $num"
done
```

## while loop

> To read file using while loop

```bash
#!/bin/bash

while read myNum
do
        echo $myNum
done < /home/dedrknex/scirpts/numbers.txt
```

## Function

> Function to call namaste some time

```bash
#!/bin/bash
#
function Welcome {
let count=$1
while [ $count -le 4 ]
do
        echo "Namaste"
        ((count++)) # Double brac beacuse arithmatic operation
done

}
Welcome 0
```

```bash
┌──(dedrknex㉿R0xt)-[~/scirpts]
└─$ bash fun.sh
Namaste
Namaste
Namaste
Namaste
Namaste
```

## special loop like break,continue

> Break is a command to break the loop after required condition met

```<>
#!/bin/bash

# let's start with break loop
#
no=6

for i in {1..6}
do
        #Break the loop if  no is not found
        if [[ $no -eq $i ]]
        then
                echo "No is $i"
                break   #loop will run till it not found 6 in the loop
        fi
        echo "Number found loop $i"
done
```

> Continune is the command that doesn't leave the loop if req met

```<>
#!/bin/bash

#Continue loop will  continue running within loop till requuirement meet


for i in {1..10}
do
        r=$(($i%2))
        if [[ $r -eq 0 ]]
        then
                continue
        fi
        echo "odd num is $i"
done
```

## Some important bash varibales

> This varibales are provided by  bash itslef
> like random and uid etc

1. Random : gives random int b/w 0 and 32767
2. UID: user id of current  user logged in

```bash
┌──(dedrknex㉿R0xt)-[~]
└─$ echo $RANDOM
21121
```

```bash
#!/bin/bash

#here u will use random command to generate a num
#b\w 1 and 6 on a dice

num=$(( $RANDOM%6+1 ))

echo "Num is $num"
```

# Redirection in script

>The redirection is command in bash which is used to save output in a file example `> >>`

# What is /dev/null

> In case if u don't want to print the output of a command on a terminal or written in a file especially the error

> We can use redirect the output to /dev/null

>Example # cd /root &> /dev/null

## TO print the name of a script

```bash
$ vi script.sh

#!/bin/bash

echo "The name of the script is: ${0}"

Output: The name of the script is script.sh
```

## Logging a message

>I f u want to maintain the logging for your script u can use logger in in ur script

> You can find the logs under `/var/logs/messages`
> Example # logger "Hey buddy"

#### TO debug use Set -X at  top of script