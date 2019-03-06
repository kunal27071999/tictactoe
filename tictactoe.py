from tkinter import *

tk=Tk()
tk.title("Tic Tac Toe")
#for changing alternet X and O
change = True

#for draw condition
check  =0

#for winner at last button click
abc = True

#for printing X winner
def winner():
     messageVar = Message(tk, text='x is winner')
     messageVar.grid(row=5, column=2)


#for printing O is winner
def winner_1():
     messageVar = Message(tk, text='O is winner')
     messageVar.grid(row=5, column=2)


#for checking winner
def tictactoe(buttons):

     global change
     global check
     global abc

     if buttons["text"] == " " and change == True:
         buttons["text"] = "X"
         change = False
         check=check+1


     elif buttons["text"] == " " and change == False:
          buttons["text"] = "O"
          change = True
          check=check+1



     if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):
          winner()
          abc = False
     elif(button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X'):
          winner()
          abc = False


     elif(button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X'):
          winner()
          abc = False


     elif(button1['text'] =='X' and button5['text'] == 'X' and button9['text'] == 'X'):
          winner()
          abc = False


     elif(button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
          winner()
          abc = False


     elif(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X'):
          winner()
          abc = False


     elif(button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X'):
          winner()
          abc = False


     elif(button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X'):
          winner()
          abc = False


     elif(button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
          winner()
          abc = False


     elif(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
          winner_1()
          abc = False

     if (check == 9 and abc):
          messageVar = Message(tk, text='TIE')
          messageVar.grid(row=5, column=2)

if __name__ == "__main__":



     buttons=StringVar()


     button1 = Button(tk,text=" ", fg='black', height=5, width=8,command= lambda:tictactoe(button1))
     button1.grid(row=1, column=0)

     button2 = Button(tk, text=' ', fg='black', height=5, width=8, command=lambda:tictactoe(button2))
     button2.grid(row=1, column=1)

     button3 = Button(tk, text=' ', fg='black', height=5, width=8, command=lambda:tictactoe(button3))
     button3.grid(row=1, column=2)

     button4 = Button(tk, text=' ', fg='black', height=5, width=8, command=lambda:tictactoe(button4))
     button4.grid(row=2,column=0)

     button5 = Button(tk, text=' ', fg='black', height=5, width=8, command=lambda:tictactoe(button5))
     button5.grid(row=2,column=1)

     button6 = Button(tk, text=' ', fg='black', height=5, width=8, command=lambda:tictactoe(button6))
     button6.grid(row=2,column=2)

     button7 = Button(tk, text=' ', fg='black', height=5, width=8, command=lambda:tictactoe(button7))
     button7.grid(row=3,column=0)

     button8 = Button(tk, text=' ', fg='black', height=5, width=8, command=lambda:tictactoe(button8))
     button8.grid(row=3,column=1)

     button9 = Button(tk, text=' ', fg='black', height=5, width=8, command=lambda:tictactoe(button9))
     button9.grid(row=3,column=2)




     tk.mainloop()