#!/bin/bash

CURRENT=`pwd`
LOGROOT=../dataflashlogs
LOGDIR=$LOGROOT/srgbot-log-`date +%Y%m%d-%H%M%S`
echo $LOGDIR

mkdir $LOGDIR
cd $LOGDIR
scp -p erle@10.0.0.1:./APM/logs/* .
ssh -t erle@10.0.0.1 sudo rm ./APM/logs/*
cd $CURRENT
