def kar(kare):
    baste = {"کار" : kare,
    "انجام" : False
    }
    faaliat.append(baste)
    with open("text.txt", "a") as fil:
          fil.write(kare + "\n")
def namaysh(faaliat):
    if len(faaliat) == 0:
        print("کاری موجود نیست")
    else:
        for shomare, i in enumerate(faaliat):
            print("=" * 10)
            print(shomare + 1, "-", i["کار"])
            print("=" * 10)
def delit(delit1):
    pida_shod = False
    for bshmar, i in enumerate(faaliat):
        if delit1 == bshmar + 1:
            faaliat.remove(i)
            print("حذف شد")
            pida_shod = True
            break
    if not pida_shod:
      print("این کار یافت نشد")
    with open("text.txt", "w") as fil:
           for i in faaliat:
                 fil.write(i["کار"] + "\n")
faaliat = []
with open("text.txt", "a"):
    pass
    
with open("text.txt", "r") as fil:
    for i in fil:
        vazeyat, kare = i.strip().split("|")

        if vazeyat == "1":
            anjam = True
        else:
            anjam = False

        faaliat.append({
            "کار": kare,
            "انجام": anjam
        })
import tkinter as tk
panjerh = tk.Tk()
panjerh.title("مدریت کارها")
panjerh.geometry("500x400")
matn = tk.Label(panjerh, text="سلام رفیق، برنامه مدیریت کارها",
justify="right",
anchor="e")
matn.pack()
kadr = tk.Entry(panjerh, width=30)
kadr.pack(pady=10)
def azafe():
    kare = kadr.get()
    kar(kare)
    list_karha.insert(
    tk.END,
    f"{len(faaliat)} - {kare}")
    kadr.delete(0,tk.END)
def hazf():
    entekhab = list_karha.curselection()
    if not entekhab:
        return
    shomare = entekhab[0]
    list_karha.delete(shomare)
    faaliat.pop(shomare)
    with open("text.txt", "w") as fil:
        for i in faaliat:
            fil.write(i["کار"] + "\n")
def tik():
    entekhab = list_karha.curselection()
    if not entekhab:
        return
    shomare = entekhab[0]
    faaliat[shomare]["انجام"] = not faaliat[shomare]["انجام"]
    list_karha.delete(shomare)
    if faaliat[shomare]["انجام"]:
        list_karha.insert(shomare, f"OK {shomare + 1} - {faaliat[shomare]['کار']}")
    else:
        list_karha.insert(shomare, f"{shomare + 1} - {faaliat[shomare]['کار']}")
    with open("text.txt", "w") as fil:
          for i in faaliat:
              if i["انجام"]:
                 fil.write("1|" + i["کار"] +"\n")
              else:
                 fil.write("0|" + i["کار"] + "\n")
dokme = tk.Button(panjerh, text = "افزودن", command=azafe)
dokme.pack()
list_karha = tk.Listbox(panjerh, width=40, height=10)
list_karha.pack(pady=10)
for shomare, i in enumerate(faaliat):
    if i["انجام"]:
        list_karha.insert(tk.END, f"OK {shomare + 1} - {i['کار']}")
    else:
        list_karha.insert(tk.END, f"{shomare + 1} - {i['کار']}")
dokme_hazf = tk.Button(panjerh, text="حذف", command=hazf)
dokme_hazf.pack()
dokme_tik = tk.Button(panjerh, text="تیک",
command=tik)
dokme_tik.pack()
panjerh.mainloop()