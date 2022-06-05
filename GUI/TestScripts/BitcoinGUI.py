import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import requests


root = Tk()
root.title("Crypto Graph TEST")

base_url = "https://api.binance.com"
path = "/api/v3/klines"


def graph():
    r = requests.get(base_url + path, params={"symbol": "BTCUSDT", "interval": "1m"})
    prices = r
    plt.hist(prices, 50)
    plt.show()


my_button = Button(root, text="Graph Button", command=graph)
my_button.pack()


root.mainloop()
