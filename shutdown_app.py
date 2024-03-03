from tkinter import*
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")

st=Tk()
st.title("Shutdown app")
st.geometry("500x500")
st.config(bg="green")

r_button=Button(st,text="Restart",font=("time new roman",30,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=20,y=20,height=50,width=200)

rt_button=Button(st,text="Restart time",font=("time new roman",30,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=20,y=100,height=50,width=300)

lg_button=Button(st,text="log-out",font=("time new roman",30,"bold"),relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=20,y=200,height=50,width=300)

st_button=Button(st,text="shutdown",font=("time new roman",30,"bold"),relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=20,y=300,height=50,width=300)




st.mainloop()