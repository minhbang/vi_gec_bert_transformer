#!/usr/bin/env bash
LOG='evaluation1'

# Input
echo "Fetching input file..."
grep ^S "./output/${LOG}.log" \
 | cut -f2- \
 | sed 's/^\[CLS\] //; s/ \[SEP\]$//; s/ ##//g' \
 | sed 's/ \(.\)$/\1/' \
 > "./output/${LOG}.input.txt"

# Target
echo "Fetching target file..."
grep ^T "./output/${LOG}.log" \
 | cut -f2- \
 | sed 's/ //g' \
 | sed 's/▁/ /g' \
 | sed 's/ $//' \
 > "./output/${LOG}.target.txt"

 # Predict
echo "Fetching predict file..."
grep ^H "./output/${LOG}.log" \
 | cut -f3- \
 | sed 's/ //g' \
 | sed 's/▁/ /g' \
 | sed 's/ $//' \
 > "./output/${LOG}.predict.txt"