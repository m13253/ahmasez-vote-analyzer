#!/bin/bash

while true
do
    date
    curl -o res-`date +%s`.html -A 'Mozilla/5.0 ahmasez-vote-analyzer (this program gets vote result to make a chart and DOES NOT affect vote. +https://github.com/m13253/ahmasez-vote-analyzer )' --compressed -m 60 'http://www.ahmasez.cn/System/sys0_inc_voteresult.asp?VoteID=16&TxtVis=1' &
    sleep 10m
done
