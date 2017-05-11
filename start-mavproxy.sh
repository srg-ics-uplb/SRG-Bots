#!/bin/bash
#for use if there is no tablet
mavproxy.py --master udp:10.0.0.2:6000 --out 127.0.0.1:14550 --out 127.0.0.1:14551
#for use if there is a tablet
mavproxy.py --master udp:10.0.0.2:6000 --out 10.0.0.3:14550 --out 127.0.0.1:14551
