#!/bin/bash
# Simple script to restore Termux from a backup file
tar -zxf $1 -C /data/data/com.termux/files --recursive-unlink --preserve-permissions
