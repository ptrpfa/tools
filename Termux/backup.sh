#!/bin/bash
# Simple script to create a Termux backup
# Usage: ./backup.sh <file name>
tar -zvcf /storage/downloads/$1.tar.gz -C /data/data/com.termux/files ./home ./usr
