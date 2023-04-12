from flask import Flask
from app import index


def test_index():
	assert index()=="hello"



