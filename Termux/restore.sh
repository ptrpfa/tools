#!/bin/bash
# Simple script to restore Termux from a backup file
# Usage ./restore.sh <file path>
tar -zxvf $1 -C /data/data/com.termux/files --recursive-unlink --preserve-permissions
