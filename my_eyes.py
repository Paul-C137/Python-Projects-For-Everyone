#!/usr/bin/env python3
'''Simpson's Slicing Challenge: Lesson: 27'''

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def challenge_function(data):
    eyes = data[2][1] 
    goggles = data[2][0] 
    nothing = data[3] 
    print(f'My {eyes}! The {goggles} do {nothing}!')
	

def main():
    challenge_function(challenge)
	
    a = list(trial[2].keys())[0] #eyes
    b = trial[2]['eyes'] #goggles
    c = trial[3] #nothing
    print(f'My {a}! The {b} do {c}!')
	
    a = nightmare[0]['user']['name']['first'] #eyes
    b = nightmare[0]['kumquat'] #goggles
    c = nightmare[0]['d'] #nothing
    print(f'My {a}! The {b} do {c}!')

main()