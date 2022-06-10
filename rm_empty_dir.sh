#!/bin/bash

while [ `find ./ -type d -empty `]
do
find ./ -type d -empty  -exec rmdir {} \;
done
