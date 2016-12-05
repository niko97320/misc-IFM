#!/bin/bash

output=$1

grep "^ENERGY" $output | awk '{print $11}'
