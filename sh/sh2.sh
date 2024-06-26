#!/bin/bash
s=0
# for ((i=1; i<=100;i++)); do
# for i in {1..100}; do
for i in $(seq 1 100); do
  s=$(($s + $i))
done

echo "1+2+...+100 = $s"
