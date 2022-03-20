#!/bin/bash
# Simple script to restore Termux from a backup file
tar -zvxf $1 -C /data/data/com.termux/files --recursive-unlink --preserve-permissions
