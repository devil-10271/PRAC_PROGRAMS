#!bin/bash

a=$(clear)
echo $a

read -p "enter your marks : " marks

if [[ $marks -ge 90 ]]
then
	echo "your are score very high"

elif [[ $marks -ge 70 ]]
then
	echo "get 70"
else
	echo "you are fail in exam"
fi
