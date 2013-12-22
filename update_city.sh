#!/bin/bash

CITIES="北京 天津 上海 杭州 广州 南京 武汉 深圳 长沙 大连 石家庄 大理 苏州"

for city in $CITIES; do
    sed s/KEYWORD/$city/ query.js|mongo > "$city".txt
done

