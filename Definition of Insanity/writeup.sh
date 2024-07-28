#!/bin/bash

# We begin with an ELF file and a file with a long string that we can easily
# recognize as base64. Decoding the string provides another base64 string,
# which provides yet another, and so on. Competitors are free to do it by
# hand, but that will take quite a while. Alternatively, they can write a
# script to do one of two things. Either it can base64-decode it until they
# get a string that begins with lbctf{, or they can reverse-engineer the ELF,
# which will tell them how many times

temp=$(cat out.txt | base64 -d)

for i in `seq 0 50`; do
	temp=$(echo "$temp" | base64 -d)
done
touch decrypted.txt
echo "$temp" > decrypted.txt
