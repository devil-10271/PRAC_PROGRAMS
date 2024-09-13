#!/bin/bash

clear

echo "a -------> pwd"
echo "b -------> ls"
echo ""
read marks

case $marks in 
	a)
		pwd;;
	b)
		ls;;
	*)
		clear;;
esac

