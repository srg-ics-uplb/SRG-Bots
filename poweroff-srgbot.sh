#!/bin/bash
echo "Shutting down SRG-Bot."
echo "You can cut the power once the board starts beeping."
echo ""
ssh erle@10.0.0.1 sudo poweroff
