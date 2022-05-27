#!/bin/bash
mkdir $(printf "%02x " {0..255})

for dir in */
do
  touch "$dir/.gitkeep"
done




