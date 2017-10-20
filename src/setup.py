#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from cx_Freeze import setup, Executable

setup(name = "Menu",
	  version = "0.1",
	  description = "Menu",
	  executables = [Executable("menu.py")],)