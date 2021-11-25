from tkinter import*
from PIL import Image, ImageTk
import id
import requests

class myweather:
    def __init__(self, root):
        self.root = root
        self.root.title('ATG Weather APP')
        self.root.geometry('450x500+350+100')
        self.root.config(bg='white')
        
        # ICON #
        self.search_icon=Image.open("icons/search.png")
        self.search_icon=self.search_icon.resize((30, 30), Image.ANTIALIAS)
        self.search_icon=ImageTk.PhotoImage(self.search_icon)

        # TEXT VARIABLE #
        self.var_search = StringVar()

        title = Label(self.root, text = 'Weather App', font = ("Lato", 30, "bold"),bg = "#262626", fg="white").place(x = 0, y = 0, relwidth = 1, height = 60)
        lbl_city = Label(self.root, text = "City Name", font = ("Lato", 15),bg = "#033958", fg="white", anchor="w", padx="10").place(x = 0, y = 60, relwidth = 1, height = 40)
        txt_city = Entry(self.root, textvariable = self.var_search, font = ("Lato", 15),bg = "lightyellow", fg="#262626").place(x = 115, y = 65, width = 250, height = 30)
        btn_search = Button(self.root, cursor = "hand2",bg="#033958", activebackground="#033958" ,bd=0, command = self.get_weather).place(x = 390, y = 65, width = 30, height = 30)

        # RESULTS #
        # self.lbl_city = Label(self.root, text = "City Name", font = ("Lato", 15),bg = "green", fg="white")
        # self.lbl_city.place(x = 0, y = 120, relwidth = 1, height = 30)
        lbl_city = Label(self.root, text = "City Name", font = ("Lato", 15),bg = "green", fg="white").place(x = 0, y = 120, relwidth = 1, height = 30)
        
        # self.lbl_icons = Label(self.root, text = "icons", font = ("Lato", 15),bg = "grey", fg="white")
        # self.lbl_icons.place(x = 0, y = 160, relwidth = 1, height = 100)
        lbl_icons = Label(self.root, text = "icons", font = ("Lato", 15),bg = "grey", fg="white").place(x = 0, y = 160, relwidth = 1, height = 100)
        
        # self.lbl_temp = Label(self.root, text = "temp", font = ("Lato", 15),bg = "orange", fg="white")
        # self.lbl_temp.place(x = 0, y = 270, relwidth = 1, height = 20)
        lbl_temp = Label(self.root, text = "temp", font = ("Lato", 15),bg = "orange", fg="white").place(x = 0, y = 270, relwidth = 1, height = 20)
        
        # self.lbl_wind = Label(self.root, text = "wind", font = ("Lato", 15),bg = "#262626", fg="white")
        # self.lbl_wind.place(x = 0, y = 310, relwidth = 1, height = 20)
        lbl_wind = Label(self.root, text = "wind", font = ("Lato", 15),bg = "#262626", fg="white").place(x = 0, y = 310, relwidth = 1, height = 20)
        
        # self.lbl_error = Label(self.root, text = "Error", font = ("Lato", 15),bg = "red", fg="white")
        # self.lbl_error.place(x = 0, y = 350, relwidth = 1, height = 20)
        lbl_error = Label(self.root, text = "Error", font = ("Lato", 15),bg = "red", fg="white").place(x = 0, y = 350, relwidth = 1, height = 20)

        # FOOTER #
        lbl_footer = Label(self.root, text = "Made  with     ❤️by  Ankit Kumar & Sourav Mukherjee", font = ("Monton", 10),bg = "#033958", fg="white", pady = 10).pack(side = BOTTOM, fill = X)

    # def get_weather(self):
    #     api_key = id.api_key
    #     complete_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={api_key}"
    #     if self.var_search.get() == "":
    #         self.lbl_city.config(text = "")
    #         self.lbl_icons.config(image = "")
    #         self.lbl_temp.config(text = "")
    #         self.lbl_wind.config(text = "")
    #         self.lbl_error.config(text="City Name Required")
    #     else:
    #         result = requests.get(complete_url)
    #         if result: 
    #             json = result.json()
    #             city_name = json["name"]
    #             country = json["sys"]["country"]
    #             icons = json["weather"][0]["icon"]
    #             temp_c = json["main"]["temp"] - 273.15
    #             temp_f = (json["main"]["temp"] - 273.15) * 9/5 + 32
    #             wind = json["weather"][0]["main"]
                
    #             self.lbl_city.config(text = city_name + " | " + country)
    #             # NEW_ICONS #
    #             self.search_icon2 =Image.open(f"icons/{icons}.png")
    #             self.search_icon2 = self.search_icon2.resize((100, 100), Image.ANTIALIAS)
    #             self.search_icon2 = ImageTk.PhotoImage(self.search_icon2)
    #             self.lbl_icons.config(image = self.search_icon2)
    #             deg = u"\N{DEGREE SIGN}"
    #             self.lbl_temp.config(text = str(round(temp_c, 2)) + deg + "C | " + str(round(temp_f, 2)) + deg + "F")
    #             self.lbl_wind.config(text = wind)

    #             self.lbl_error.config(text = "")
    #         else:
    #             self.lbl_city.config(text = "")
    #             self.lbl_icons.config(image = "")
    #             self.lbl_temp.config(text = "")
    #             self.lbl_wind.config(text = "")
    #             self.lbl_error.config(text = "Invalid City Name")

root = Tk()
# obj = myweather(root)
root.mainloop()