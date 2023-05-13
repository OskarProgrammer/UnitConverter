
import tkinter as tk #tkinter
from tkinter import ttk 

root=tk.Tk()                                    #stworzenie okna
root.title("Konwerter jednostek!")              #tytul okna
root.configure(background="#755A91")            #ustawienia okna            
root.geometry("600x600+700+150")                #wymiary okna
root.resizable(False,False)                     #mozliwosc modyfikacji wielkosci okna przez uzytkownika 

def przemiana():                                #funkcja przemiany jednostek
    global variable, variable_1                 #potrzebne globalne zmienne do modyfikacji 
    variable.set("")                            #ustawienie combobox na null
    x=float(variable_1.get())                   #przywolanie z okna wartosci float
    y=combobox.get()                            #przywolanie z okna 
    wynik=0                                     #stworzenie int wynik or float
    score=sprawdzenie(y)                        #funkcja sprawdzajaca jaki rodzaj konwersji podano w combobox

    if score==0:
        wynik=round((x*(3.6)),2)
    elif score==1:
        wynik=round((x/(3.6)),2)       
    elif score==2:
        wynik=round(x*0.001,8)
    elif score==3:
        wynik=round(x*1000,2)
    elif score==4:                                  #wszelkie przeliczanie
        wynik=round(x*0.000001,8)
    elif score == 5:
        wynik=round(x*1000000,2)
    elif score == 6:
        wynik=round(x*0.0001,8)
    elif score == 7:
        wynik=round(x*10000,2)

    lista=list[sprawdzenie(y)]                  #listowanie listy od wybranej funkcji
    lista=lista.split(" ")                      #splitowanie 

    variable.set(str(wynik)+" ")                #ustawienie wartosci dla konkretnych okien

    variable_2.set(lista[0])                    #ustawienie wartosci dla konkretnych okien
    variable_3.set(lista[2])                    #ustawienie wartosci dla konkretnych okien   
    #variable.set(x+" m/s")

def sprawdzenie(y):
    return list.index(y)

def czysc():
    global variable,variable_1,variable_2,variable_3
    
    variable.set("")
    variable_1.set("")
    variable_2.set("")
    variable_3.set("")
    
    combobox.set("")

label=tk.Label(root,text="KONWERTER", font='Helvetica 25 bold',bg="#795d96",foreground="#292033",borderwidth=1,relief="groove",justify="center")
label.pack()
label.place(x=195,y=50)

tekst_1=tk.Label(root,text="Co chcesz przeliczyc: ",bg="#755A91",fg="#292033",font=("Helvetica", 15))
tekst_1.pack()
tekst_1.place(x=50,y=260)

variable_1=tk.StringVar();
textbox=tk.Entry(root,textvariable=variable_1,bg="#755A91",width=10,justify="center",fg="#3D2F4D",font=("Helvetica", 15))
textbox.pack()
textbox.place(x=85,y=600/2-3)

####KOLO WYNIKOW 

variable_2=tk.StringVar();
labe_3=tk.Label(root,textvariable=variable_2,bg="#755A91",width=4,justify="center",fg="#3D2F4D",font=("Helvetica", 15))
labe_3.pack()
labe_3.place(x=198,y=600/2-4)

variable_3=tk.StringVar();
labe_2=tk.Label(root,textvariable=variable_3,bg="#755A91",width=4,justify="center",fg="#3D2F4D",font=("Helvetica", 15))
labe_2.pack()
labe_2.place(x=487,y=600/2-4)

tekst_2=tk.Label(root,text="Wynik: ",bg="#755A91",fg="#292033",font=("Helvetica", 15))
tekst_2.pack()
tekst_2.place(x=400,y=260)

variable=tk.StringVar();
label=tk.Label(root,textvariable=variable,width=10,height=1,bg="#755A91",fg="#3D2F4D",font=("Helvetica", 15),borderwidth=1,relief="sunken")
label.pack()
label.place(x=375,y=600/2-3)

button=tk.Button(root,text="Przelicz",width=10,height=1,bg="#755A91",fg="#292033",activebackground='#755A91',font=("Helvetica", 15),command=przemiana)
button.pack()
button.place(x=240,y=350)

button_1=tk.Button(root,text="Czysc okna",width=10,height=1,bg="#755A91",fg="#292033",activebackground='#755A91',font=("Helvetica", 15),command=czysc)
button_1.pack()
button_1.place(x=240,y=400)

button_2=tk.Button(root,text="Wyjdz",width=10,height=1,bg="#755A91",fg="#292033",activebackground='#755A91',font=("Helvetica", 15),command=root.destroy)
button_2.pack()
button_2.place(x=240,y=450)

list=["m/s na km/h","km/h na m/s","dm3 na m3","m3 na dm3","cm3 na m3","m3 na cm3","cm2 na m2","m2 na cm2"]

labeff=tk.Label(root,text="Tryb",font=("Helvetica",15),bg="#755A91",fg="#292033",justify="center",width=10)
labeff.pack()
labeff.place(x=240,y=160)

style=ttk.Style()
style.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': '#755A91',
                                       'fieldbackground': '#755A91',
                                       'background': '#755A91',
                                       'foreground':'#292033',
                                       'selectforeground': '#292033',
                                       }}}
                )
style.theme_create('combostyle1', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': '#604A78',
                                       'fieldbackground': '#604A78',
                                       'background': '#604A78',
                                       'foreground':'#211A29',
                                       'selectforeground': '#211A29',
                                       }}}
                )
style.theme_use("combostyle")

combobox = ttk.Combobox(root, values=list,state="readonly",justify="center",width=10,height=100,font=("Helvetica", 15),foreground="#3D2F4D")
combobox.pack()
combobox.place(x=240,y=200)

def zmiana(event):
    
    if event.type == tk.EventType.Enter:
        style.theme_use("combostyle1")
    elif event.type == tk.EventType.Leave:
        style.theme_use("combostyle")
    else:
        pass

def check(event):
    print(event.widget)
    y=combobox.get()
    lista=list[sprawdzenie(y)]                  #listowanie listy od wybranej funkcji
    lista=lista.split(" ")
    variable_2.set(lista[0])                    #ustawienie wartosci dla konkretnych okien
    variable_3.set(lista[2])
combobox.bind ("<<ComboboxSelected>>",check)
combobox.bind("<Enter>",zmiana)
combobox.bind("<Leave>",zmiana)

###WYNIKI PELNE
sum=tk.Label(root,textvariable=variable,width=15,height=8,bg="#755A91",fg="#3D2F4D",font=("Helvetica", 15),borderwidth=1,relief="sunken",wraplength=150,justify="left")
sum.pack()
sum.place(x=425,y=400)

sum_1=tk.Label(root,textvariable=variable_1,width=15,height=8,bg="#755A91",fg="#3D2F4D",font=("Helvetica", 15),borderwidth=1,relief="sunken",wraplength=150,justify="left")
sum_1.pack()
sum_1.place(x=10,y=400)

root.mainloop()