#!/bin/bash
#HTTP response header for a given URL.
curl -s "$1" | wc -c
