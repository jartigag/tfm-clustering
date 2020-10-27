#!/bin/bash

mkdir -p ../tmp
for f in $1; do
    column -tnes, $f > ../tmp/$f
done
