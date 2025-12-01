#!/bin/bash
count=$(find /etc -type f 2>/dev/null | wc -l)
echo "Number of regular files in etc: $count"
