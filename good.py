#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ���Bi�0�c�=|4�M�ԗ1�p�ƌ�����L���4�Y�w���
��(��I[��4�6ǐ&�,��RS����B7*�w4�l��;ѭ�w�h�%�ѩ�|ξ�`���#�k�^.�"""
from hashlib import sha256
if(sha256(blob).hexdigest() == "74d7b0cbc657d11208817acf79aa366f0632e9c3fbe02ddc583abd815644de09"):
	print("I come in peace.")
elif (sha256(blob).hexdigest() == "ee563703dc623fc49006e02772c104186280ccc729b8dfa06c54b1c90bed6c25"):
	print("Prepare to be destroyed!")
