#!/usr/bin/env python

import random

def arc4random():
	key = random.sample(range(256), 256) # something
	seeds = _RC4PRGA(_RC4keySchedule(key))
	return (seeds[0]<<24)|(seeds[1]<<16)|(seeds[2]<<8)|seeds[3]

def _RC4keySchedule(key):
	sbox = list(range(256))
	x = 0
	keySize = len(key)
	for i in sbox:
		x = (x+i+key[i%keySize])%256
		_swap(sbox, i, x)
	return sbox

def _RC4PRGA(state):
	x, y = 0, 0
	seeds = []
	# Discard first 1536 bytes of the keystream according to RFC4345 as they may reveal information
	# about key used (a set of these keys could reveal information about the source for our key)
	for i in range((1536//4)+4):
		x = (x+1)%256
		y = (y+state[x])%256
		_swap(state, x, y)
		if i >= (1536//4):
			seeds.append(state[(state[x]+state[y])%256])
	return seeds

def _swap(listy, n1, n2):
	listy[n1], listy[n2] = listy[n2], listy[n1]

