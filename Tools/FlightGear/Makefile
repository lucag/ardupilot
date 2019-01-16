#!/usr/bin/make
#
# Requires GNU Make
#

OS		:=	$(shell uname)

ifeq ($(OS),Darwin)
CC		:=	cc
#CC		:=	c++
CFLAGS		:=	-std=c99
LDFLAGS		:=
endif

ifeq ($(OS),Linux)
CC		:=	cc
#CFLAGS		:=	-std=c99 -D_XOPEN_SOURCE=600
#CFLAGS		:=	-D_XOPEN_SOURCE=600
LDFLAGS     	:=	-lpthread -lm
endif

CFLAGS		+=	-I./c_library_v1 -I../../libraries -I/usr/include
SRCS		:=	FGShim.c

FGShim:		$(SRCS)
	$(CC) -o $@ $(SRCS) $(CFLAGS) $(LDFLAGS)


clean:
	rm -f FGShim *~
