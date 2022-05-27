#!/bin/bash
mkdir $(printf "%02x " {0..255})

for dir in */
do
  mkdir $(printf "$dir/%02x " {0..255})
done
