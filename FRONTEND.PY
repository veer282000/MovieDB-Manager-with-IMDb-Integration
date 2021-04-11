##frontend
from tkinter import *
import tkinter.messagebox
import BACKEND
class Movie:

    def __init__(self,root):
        self.root =root
        self.root.title("Movie Database Management System")
        self.root.geometry("1300x800+0+0")
        self.root.config(bg="cadet blue")

        MovieID = StringVar()
        MovieName = StringVar()
        ReleaseDate = StringVar()
        Director = StringVar()
        Cast = StringVar()
        BoxOfficeCollection = StringVar()
        Duration = StringVar()
        Rating = StringVar()
# --------------------------------------FUNCTIONS-------------------------------------------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("Movie Database Management Systems", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        def clearData():
            self.txtMovieID.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtDirector.delete(0, END)
            self.txtCast.delete(0, END)
            self.txtBoxOfficeCollection.delete(0, END)
            self.txtAdr.delete(0, END)
            self.txtRating.delete(0, END)
        def addData():
            if(len(MovieID.get())!=0):
                dbbackend.addStdRec(MovieID.get(), MovieName.get(), ReleaseDate.get() , Director.get() ,Cast.get(), BoxOfficeCollection.get(), Duration.get(), Rating.get())
                Movielist.delete(0, END)
                Movielist.insert(END, (MovieID.get(), MovieName.get(), ReleaseDate.get(), Director.get(), Cast.get(), BoxOfficeCollection.get(), Duration.get(), Rating.get()))

        def DisplayData():
            Movielist.delete(0,END)
            for row in dbbackend.viewData():
                Movielist.insert(END, row, str(""))

        def MovieRec(event):
            global sd
            searchStd= Movielist.curselection()[0]
            sd = Movielist.get(searchStd)

            self.txtMovieID.delete(0, END)
            self.txtMovieID.insert(END, sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sd[2])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sd[3])
            self.txtDirector.delete(0, END)
            self.txtDirector.insert(END, sd[4])
            self.txtCast.delete(0, END)
            self.txtCast.insert(END, sd[5])
            self.txtBoxOfficeCollection.delete(0, END)
            self.txtBoxOfficeCollection.insert(END, sd[6])
            self.txtAdr.delete(0, END)
            self.txtAdr.insert(END, sd[7])
            self.txtRating.delete(0, END)
            self.txtRating.insert(END, sd[8])

        def DeleteData():
            if(len(MovieID.get())!=0):
                dbbackend.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            Movielist.delete(0,END)
            for row in dbbackend.searchData(MovieID.get(), MovieName.get(), ReleaseDate.get() , Director.get() ,Cast.get(), BoxOfficeCollection.get(), Duration.get(), Rating.get()):
                Movielist.insert(END, row, str(""))

        def update():
            if (len(MovieID.get()) != 0):
                dbbackend.deleteRec(sd[0])
            if (len(MovieID.get()) != 0):
                dbbackend.addStdRec(MovieID.get(), MovieName.get(), ReleaseDate.get(), Director.get(), Cast.get(), BoxOfficeCollection.get(),Duration.get(), Rating.get())
                Movielist.delete(0, END)
                Movielist.insert(END, (MovieID.get(), MovieName.get(), ReleaseDate.get(), Director.get(), Cast.get(), BoxOfficeCollection.get(), Duration.get(), Rating.get()))
#--------------------------------------Frames-----------------------------------------------------------------------__________________________________________________________
        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=56,pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP,fill=X)
        self.lblTit = Label(TitFrame ,font=('times new roman',35,'bold'),text="Movie Database Management System",bg="Ghost White")
        self.lblTit.grid()
        ButtonFrame =Frame(MainFrame,bd=2,width=1350,height=70,padx=19,pady=10,bg="Brown",relief =RAISED)
        ButtonFrame.pack(side=BOTTOM,ipadx=20)
        DataFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=0, pady=0,relief=RIDGE,bg="cadet blue")
        DataFrame.pack(side=BOTTOM,ipadx=10,ipady=5,padx=0)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=750, height=70, padx=15,relief=RIDGE,bg="Yellow", font=('times new roman',26,'bold'),text="MOVIE INFORMATION:\n")
        DataFrameLEFT.pack(side=LEFT,fill =BOTH)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=500, height=70, relief=RIDGE,bg="Ghost White",font=('times new roman',26,'bold'),text="MOVIE DETAILS:\n")
        DataFrameRIGHT.pack(side=RIGHT,fill =BOTH,ipadx=20,ipady=20)
#--------------------------------entries-------------------------------------------------------------------------------------------------
        self.lblMovieID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="MOVIE ID:",padx=2,pady=2,bg="Ghost White")
        self.lblMovieID.grid(row=0,column=0,sticky=W)
        self.txtMovieID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=MovieID, width=30)
        self.txtMovieID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="MOVIE NAME:", padx=2, pady=2,bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=MovieName, width=30)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="RELEASE DATE:", padx=2, pady=2,bg="Ghost White")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=ReleaseDate, width=30)
        self.txtSna.grid(row=2, column=1)

        self.lblDirector = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="DIRECTOR:", padx=2, pady=2,bg="Ghost White")
        self.lblDirector.grid(row=3, column=0, sticky=W)
        self.txtDirector = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Director, width=30)
        self.txtDirector.grid(row=3, column=1)

        self.lblCast = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="CAST:", padx=2, pady=2,bg="Ghost White")
        self.lblCast.grid(row=4, column=0, sticky=W)
        self.txtCast = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Cast, width=30)
        self.txtCast.grid(row=4, column=1)

        self.lblBoxOfficeCollection = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="BOX-OFFICE COLLECTION:", padx=2, pady=2,bg="Ghost White")
        self.lblBoxOfficeCollection.grid(row=5, column=0, sticky=W)
        self.txtBoxOfficeCollection = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=BoxOfficeCollection, width=30)
        self.txtBoxOfficeCollection.grid(row=5, column=1)

        self.lblAdr = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="DURATION:", padx=2, pady=2,bg="Ghost White")
        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Duration, width=30)
        self.txtAdr.grid(row=6, column=1)

        self.lblRating = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="CRITIC-RATING(OUT OF 5):", padx=2, pady=2,bg="Ghost White")
        self.lblRating.grid(row=7, column=0, sticky=W)
        self.txtRating = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Rating, width=30)
        self.txtRating.grid(row=7, column=1)
#--------------------------------------scroll bar and list box----------------------------------------------------------------------------
        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')


        Movielist = Listbox(DataFrameRIGHT,width=50,height=15 ,font=('times new roman', 10, 'bold'),yscrollcommand=scrollbar.set)

        Movielist.bind('<<ListboxSelect>>',MovieRec)
        Movielist.grid(row=0, column=0, padx=1,pady=1)
        scrollbar.config(command=Movielist.yview)
#--------------------------------------buttons-----------------------------------------------------------------------------------------------------------
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddData.grid(row=0, column =0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, text="Search", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4,command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)

if __name__=='__main__':
    root = Tk()
    application = Movie(root)
    root.mainloop()
