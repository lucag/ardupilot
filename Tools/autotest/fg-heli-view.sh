#!/bin/sh

nice fgfs \
    --native-fdm=socket,in,10,,5503,udp \
    --native-fdm=socket,out,10,,5501,udp \
    --aircraft=Alouette-III \
    --fg-aircraft="$HOME/.fgfs/Aircraft/org.flightgear.fgaddon/Aircraft" \
    --airport=KSFO \
    --geometry=1920x1080 \
    --bpp=32 \
    --wind=0@0 \
    $*
