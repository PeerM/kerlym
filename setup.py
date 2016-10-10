#!/usr/bin/env python3
import os
from setuptools import setup, find_packages
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "KeRLym",
    version = "0.0.2",
    author = "Tim O'Shea",
    author_email = "tim.oshea753@gmail.com",
    description = ("Keras Reinforcement Learners for Gym."),
    license = "MIT",
    keywords = "keras reinforcement learning gym",
    url = "http://www.kerlym.com",
    packages = find_packages(), #['kerlym'], #'kerlym/dqn', 'kerlym/a3c'
    long_description = read('README.md'),
    scripts = ['bin/kerlym'],
)
