#!/bin/bash 
 
find /var/log -name "*.log" -mtime +7 -exec rm -f {} \; 
 
