#!/bin/sh
while true; do socat tcp-l:1688,reuseaddr,fork,crlf exec:"/app/blindmaze.py",pty,ctty,echo=0; sleep 10; done
