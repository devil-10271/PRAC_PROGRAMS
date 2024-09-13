#!usr/bin/bash

a=(shail 2 , 4 , , , , 5 ,)
echo "${a[*]}"

echo "${#a[0]}"

echo "${a[*]:0:2}"

b+=(1 2 33)

echo "${b[*]}"
