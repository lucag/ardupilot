#!/bin/sh

FGFS="/Applications/FlightGear.app/Contents/MacOS/fgfs"

nice $FGFS \
    --native-ctrls=socket,in,10,,5502,udp \
    --native-fdm=socket,out,10,,5504,udp \
    --aircraft=Alouette-III \
    --fg-aircraft="$HOME/.fgfs/Aircraft/org.flightgear.fgaddon/Aircraft" \
    --airport=KSFO \
    --geometry=320x240 \
    --bpp=32 \
    --wind=0@0 \
    $*
