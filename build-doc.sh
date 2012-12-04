#!/bin/sh

if [ "$1" == "watch" ]; then
    linkdown all -ws doc_src doc
else
    linkdown all -c doc_src doc
fi
