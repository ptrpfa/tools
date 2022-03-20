#!/bin/bash
# Simple script to create a Termux backup
# Usage: ./backup.sh <file path>.tar.gz
tar -zcvf $1.tar.gz -C /data/data/com.termux/files ./home ./usr
