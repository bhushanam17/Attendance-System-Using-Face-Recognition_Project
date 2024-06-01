from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

#SEARCH BUTTON IN STUDENT PAGE
#UPDATE BUTTON IN ATTENDANCE PAGE
#CREATE LOGIN PAGE
class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")

        #first image
        img=Image.open(r"Images\face.jpg")
        img=img.resize((500,130), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)


        #second image
        img1=Image.open(r"Images\MUJ.jpg")
        img1=img1.resize((500,130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)


        #third image
        img2=Image.open(r"Images\doneby.png")
        img2=img2.resize((500,130), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)


        #bg image
        img3=Image.open(r"Images\final.jpg")
        img3=img3.resize((1530,710), Image.LANCZOS) 
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        
        title_lbl=Label(bg_img, text="FACE RECOGNITION ATTENDANCE SOFTWARE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        #student button
        img4=Image.open(r"Images\student_icon.jpg")
        img4=img4.resize((220,220), Image.LANCZOS) 
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1=Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1_1.place(x=200, y=300, width=220, height=40)


        #detect face button
        img5=Image.open(r"Images\face_recog_icon2.jpg")
        img5=img5.resize((220,220), Image.LANCZOS) 
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img, image=self.photoimg5, cursor="hand2", command=self.face_data)
        b1.place(x=650, y=100, width=220, height=220)

        b1_1=Button(bg_img, text="Face Detector", command=self.face_data, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1_1.place(x=650, y=300, width=220, height=40)


        #attendance button
        img6=Image.open(r"Images\attendance_icon.jpg")
        img6=img6.resize((220,220), Image.LANCZOS) 
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img, image=self.photoimg6, cursor="hand2", command=self.attendance_data)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1=Button(bg_img, text="Attendance", cursor="hand2", command=self.attendance_data,
         font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1_1.place(x=1100, y=300, width=220, height=40)


        #train face button
        img7=Image.open(r"Images\train_data_icon.jpg")
        img7=img7.resize((220,220), Image.LANCZOS) 
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.train_data)
        b1.place(x=200, y=400, width=220, height=220)

        b1_1=Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1_1.place(x=200, y=600, width=220, height=40)


        #photos button
        img8=Image.open(r"Images\photos_icon.png")
        img8=img8.resize((220,220), Image.LANCZOS) 
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.open_img)
        b1.place(x=650, y=400, width=220, height=220)

        b1_1=Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1_1.place(x=650, y=600, width=220, height=40)


        #exit button
        img9=Image.open(r"Images\exit_icon.jpg")
        img9=img9.resize((220,220), Image.LANCZOS) 
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.iExit)
        b1.place(x=1100, y=400, width=220, height=220)

        b1_1=Button(bg_img, text="Exit", cursor="hand2", command=self.iExit, font=("times new roman", 15, "bold"), bg="white", fg="black")
        b1_1.place(x=1100, y=600, width=220, height=40)
             


    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return


        #=================Function buttons=================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_System(root)
    root.mainloop()


    