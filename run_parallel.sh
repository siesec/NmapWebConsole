#!/bin/bash
date
cat ports_file/ports_0-999.txt | parallel -j 100 nmap -sT -Pn -p{} 10.0.2.15 >> output.log 2>&1
date
