from tkinter import *
from tkinter import ttk
import requests

def get():
    cityName=name.get().strip()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+cityName+"&appid="+'Api Key').json() #Please insert your own api key at place of Api Key to use 
    climate1.config(text=data["weather"][0]["main"])
    temp1.config(text=str(int(data["main"]["temp"]-273.15))+'°C')
    fellTemp1.config(text=str(int(data["main"]["feels_like"]-273.15))+'°C')
    pressure1.config(text=str(data["main"]["pressure"]))
    humidity1.config(text=str(data["main"]["humidity"])+'%')
    description1.config(text=data["weather"][0]["description"])

    

root = Tk()
root.title('Weather App')
root.config(bg='#449DD1')
root.geometry('400x400')
#root.resizable(False,False)



# Heading of the GUI
heading = Label(root,text='Weather App',font=('Arial',32,'bold'),bg='#449DD1')
heading.grid(row=0,column=0,columnspan=2,pady=(10,20),padx=68)

frame = LabelFrame(root,bg='#449DD1',border=0)
frame.grid(row=1,columnspan=2)
lb=Label(frame,text='City Name : ',font =('Arial',16),bg='#449DD1')
lb.grid(row=0,column=0,padx=(2,0))
# Search Box
name = StringVar()
stateList = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","Delhi","Puducherry"]
city = ttk.Combobox(frame,values=stateList,font =('Arial',16),textvariable=name)
city.grid(row=0,column=1,padx=(0,8))

# Things which are to show in app
climate = Label(root,text='Climate:',font =('Arial',12),bg='#449DD1')
temp = Label(root,text='Temprature:',font =('Arial',12),bg='#449DD1')
fellTemp = Label(root,text='Feels Like:',font =('Arial',12),bg='#449DD1')
pressure = Label(root,text='Pressure:',font =('Arial',12),bg='#449DD1')
humidity = Label(root,text='Humidity:',font =('Arial',12),bg='#449DD1')
description = Label(root,text='Weather Description:',font =('Arial',12),bg='#449DD1')

# Placements of showing things
climate.grid(row=4,column=0,pady=2)
temp.grid(row=5,column=0,pady=2)
fellTemp.grid(row=6,column=0,pady=2)
pressure.grid(row=7,column=0,pady=2)
humidity.grid(row=8,column=0,pady=2)
description.grid(row=9,column=0,pady=2)

# Things about to show
climate1 = Label(root,text='',font =('Arial',12),bg='#449DD1',width=20)
temp1 = Label(root,text='',font =('Arial',12),bg='#449DD1',width=20)
fellTemp1 = Label(root,text='',font =('Arial',12),bg='#449DD1',width=20)
pressure1 = Label(root,text='',font =('Arial',12),bg='#449DD1',width=20)
humidity1 = Label(root,text='',font =('Arial',12),bg='#449DD1',width=20)
description1 = Label(root,text='',font =('Arial',12),bg='#449DD1',width=20)

# Placements of about to show things
climate1.grid(row=4,column=1,pady=2)
temp1.grid(row=5,column=1,pady=2)
fellTemp1.grid(row=6,column=1,pady=2)
pressure1.grid(row=7,column=1,pady=2)
humidity1.grid(row=8,column=1,pady=2)
description1.grid(row=9,column=1,pady=2)

#Done butoon to submit
btn = Button(root,text='Done',font =('Arial',15),width=7,command=get)
btn.grid(row=3,column=0,columnspan=2,pady=15)

root.mainloop()