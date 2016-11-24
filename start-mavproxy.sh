#!/bin/bash
mavproxy.py --master udp:10.0.0.2:6000 --out 10.0.0.3:14550 --out 127.0.0.1:14551
