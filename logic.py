# this file contains the logic part of the whole project.
# it contains functions
from tkinter import messagebox


def celsius_fahrenheit(celsius):
    fahrenheit = str(celsius * 9/5 + 32)
    return fahrenheit


def pounds_kilograms(pounds):
    kilogram = str(pounds * 0.45359237)
    return kilogram


def miles_kilometers(miles):
    kilometer = str(miles * 1.609344)
    return kilometer


def millilitres_litres(millilitre):
    litres = str(millilitre * 0.001)
    return litres


if __name__ == '__main__':
    messagebox.showerror('Wrong File!', 'Please run the gui.py file!')
