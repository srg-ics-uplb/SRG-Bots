#!/bin/bash

LOGROOT=.
LOGDIR=srgbot-log-`date +%Y%m%d-%H%M%S`
echo $LOGDIR

mkdir log-$DATE
cd $LOGDIR
scp -p erle@10.0.0.1:./APM/logs/* .
ssh erle@10.0.0.1 rm ./APM/logs/*
cd ..
