import tkinter as tk 
from tkinter import ttk, messagebox
 
class RestaurantOrderManagement:
    def __init__(self,root)
        self.root = root
        self.title("Restaurant Management App")

        self.menu_items = {
            "Fries Meal":2'
            "Lunch Meal":2,
            "Burger meal":3,
            "Pizza meal":3,
            "Cheese Burger":2.5,
            "Drinks":1
        }

        self.exchange_rate = 83
        self.setup_background(root)

        frame = ttk.frame(root)
        frame.place(relx = 0.5, rely = 0.5,anchor = tk.CENTER)

        ttk.Label(frame,text = "Restaurant Order Management",font = ("Arial",20,"bold")).grid(row = 0,
                                                                                              columnspan = 3,
                                                                                              padx = 10,
                                                                                              pady = 10)