# coding=utf-8

import pysynth_b

test = (('e4', 4), ('e4', 8), ('g4', 8),
        ('a4', 8), ('c5', 8), ('c5', 8), ('a4', 8), 
        ('g4', 4), ('g4', 8), ('a4', 8),
        ('g4', 2),
        ('e4', 4), ('e4', 8), ('g4', 8),
        ('a4', 8), ('c5', 8), ('c5', 8), ('a4', 8), 
        ('g4', 4), ('g4', 8), ('a4', 8),
        ('g4', 2),
        ('g4', 4), ('g4', 4),
        ('g4', 4), ('e4', 8), ('g4', 8),
        ('a4', 4), ('a4', 4),
        ('g4', 2),
        ('e4', 4), ('d4', 8), ('e4', 8),
        ('g4', 4), ('e4', 8), ('d4', 8),
        ('c4', 4), ('c4', 8), ('d4', 8),
        ('c4', 2)
        )

pysynth_b.make_wav(test, fn = "茉莉花.wav")
