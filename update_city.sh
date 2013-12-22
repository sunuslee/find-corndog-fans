#!/bin/bash

CITIES="北京 天津 上海 杭州 广州 南京 武汉 深圳"

for city in $CITIES; do
    sed s/KEYWORD/$city/ showtj.js|mongo > "$city".txt
done

