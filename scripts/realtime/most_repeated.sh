#!/bin/bash

awk -F, '{print $2}' *repeated_in_tops.csv | sort | uniq -c | sort -nr | head
