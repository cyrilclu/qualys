#!/bin/bash

workdir=$(dirname $(readlink -f $0))
tmpdir=$workdir/.tmp
if [ -d $tmpdir ]; then
    rm -rf $tmpdir/*
else
    mkdir -p $tmpdir
fi

j2 $workdir/logstash.conf.j2 $workdir/logstash.yml > $tmpdir/logstash.conf
