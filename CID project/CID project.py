import csv
from tkinter.ttk import *
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter
from PIL import ImageTk, Image

                        ### interface ###

root = Tk()
root.config(bg="light blue")
root.title("CID LAB")
root.geometry("400x650")
                      ###image###

canvas = tkinter.Canvas(root, width=500, height=250)
canvas.pack()
img = Image.open("G:\\CID project\\dna-image-over-hand.jpg")
resized_image = img.resize((650, 450))
converted_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(200, 50, anchor=CENTER, image=converted_image)

                    ###end of image###



                   ###welcome_message###
greetlabel=Label(root, text="WELCOME TO THE CID LAB", fg="black", bg="light blue", font=("Arial", 20, "bold"))
greetlabel.pack()
                    ###DNA_SUSPECT_LABEL###
DNAsuspectsLabel = Label(root, text="Enter DNA Sequence of the criminal", fg="black", bg="light blue")
DNAsuspectsLabel.pack()
DNAsuspectsEntry = Entry(root)
DNAsuspectsEntry.pack()


# criminal_seq1 = "CCCCGGTTAA"

def test_50_precent():

    criminal_seq = DNAsuspectsEntry.get()
    l = ["CAAGCTTCGATCCCTTGA", "ATCGGCTACCCCGATTTTTT", "ATTTCGGACCCCGTAAAAA", "ATATATACCCCGGTTCCC","GCCATCGACCCCGGTTAA"]

    criminal_seq_temp = criminal_seq[0:5]
    criminal_seq_temp2 = criminal_seq[5:10]
    for pos in range(len(l)):
        if criminal_seq_temp in l[pos]:
            result_label1 = Label(text="the criminal's sequence matches 50% with:" + str(l[pos]), bg="light blue")
            result_label1.pack()
        elif criminal_seq_temp2 in l[pos]:
            result_label1 = Label(text="the criminal's sequence matches 50% with:" + str(l[pos]), bg="light blue")
            result_label1.pack()
        else:
            result_label = Label(text="The criminal sequence mismatches with:"+ str(l[pos]), bg="light blue")
            result_label.pack()
button1 = Button(root, text="50%", command=test_50_precent, bg="white")
button1.pack()

def test_75_precent():
    criminal_seq2=DNAsuspectsEntry.get()
    ll = ["CAAGCTTCGATCCCTTGA", "ATCGGCTACCCCGATTTTTT", "ATTTCGGACCCCGTAAAAA", "ATATATACCCCGGTTCCC","GCCATCGACCCCGGTTAA"]
    criminal_seq_temp = criminal_seq2[0:8]
    criminal_seq_temp2 = criminal_seq2[2:10]


    for pos in range(len(ll)):
      if criminal_seq_temp in ll[pos]:
         result_label2 = Label(text="the criminal's sequence matches 75% with:" + str(ll[pos]),bg="light blue")
         result_label2.pack()
      elif criminal_seq_temp2 in ll[pos]:
         result_label2 = Label(text="the criminal's sequence matches 75% with:" + str(ll[pos]),bg="light blue")
         result_label2.pack()
      else:
         result_label2 = Label(text="the criminal's sequence matches 75% with:" + str(ll[pos]),bg="light blue")
         result_label2.pack()

mybuttom2=Button(root,text="75%",command=test_75_precent,bg="white")
mybuttom2.pack()


def test_100_precent( ):
    criminal_seq3=DNAsuspectsEntry.get()
    lll= ["CAAGCTTCGATCCCTTGA", "ATCGGCTACCCCGATTTTTT", "ATTTCGGACCCCGTAAAAA", "ATATATACCCCGGTTCCC","GCCATCGACCCCGGTTAA"]
    criminal_seq_temp= criminal_seq3[0:10]
    for pos in range(len(lll)):
       if criminal_seq_temp in lll[pos]:
           result_label3 = Label(text="the criminal is:" + str(lll[pos]),bg="light blue")
           result_label3.pack()
       else:
           result_label3 = Label(text="mismatch sequence" + str(lll[pos]),bg="light blue")
           result_label3.pack()


mybuttom3=Button(root,text="100%",command=test_100_precent,bg="white")
mybuttom3.pack()




root.mainloop()