# importing libraries
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import requests
import pandas as pd
import cx_Oracle   
import socket
import datetime
import bs4
import operator
from Interface import Register, Start, Overview

    
#Start Page
start = Start.launchStart()
register = Register.launchRegister(start)
#Trial1
