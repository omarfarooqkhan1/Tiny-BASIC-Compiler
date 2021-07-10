import sys
import subprocess

from MyLexer import *
from MyParser import *
from MyEmitter import *

from tkinter import *
import tkinter.scrolledtext as tkst


# This function will get called everytime the user presses "Compile" button
def compile_Click():
    input = codeInput.get("1.0", 'end')
    st.delete("1.0", "end")
    cCode.delete("1.0", "end")
    codeOutput.delete("1.0", "end")
    lexer = Lexer(input)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)
    parser.parse()  # Start the parser.
    st.insert(INSERT, "Symbol Table:\n\n-> Variables:\n")
    if len(parser.symbols) > 1:
        st.insert(END, parser.symbols)
    else:
        st.insert(END, "No variables declared!\n")
    if len(parser.labelsDeclared) > 1:
        st.insert(END, "\n-> Labels:\n")
        st.insert(END, parser.labelsDeclared)
    else:
        st.insert(END, "\n-> Labels:\nNo labels declared!\n")
    cCode.insert(INSERT, emitter.header)
    cCode.insert(END, emitter.code)
    emitter.writeFile()  # Write the output to file.
    subprocess.call(["gcc", "out.c"])
    codeOutput.insert(INSERT, subprocess.getoutput("a.exe"))
    messagebox.showinfo("Success", "Compilation Successful!")


root = Tk()
root.geometry('1000x500')
root.configure(background='#FFFFFF')
root.title('Tiny BASIC Compiler')

Label(root, text='Source code in BASIC', bg='#F0F8FF',
      font=('arial', 12, 'normal')).place(x=30, y=45)

codeInput = tkst.ScrolledText(root, width=25, height=20, bd=5, relief='groove')
codeInput.pack()
codeInput.place(x=30, y=76)


# This is the section of code which creates the a label
Label(root, text='Symbol Table', bg='#F0F8FF', font=(
    'arial', 12, 'normal')).place(x=275, y=45)


# This is the section of code which creates a text input box
st = tkst.ScrolledText(root, width=23, height=20, bd=5, relief='groove')
st.pack()
st.place(x=275, y=76)


# This is the section of code which creates the a label
Label(root, text='Translated Code in C', bg='#F0F8FF',
      font=('arial', 12, 'normal')).place(x=500, y=45)


# This is the section of code which creates a text input box
cCode = tkst.ScrolledText(
    root, width=25, height=20, bd=5, relief='groove')
cCode.pack()
cCode.place(x=500, y=76)


# This is the section of code which creates the a label
Label(root, text='Code Output', bg='#F0F8FF', font=(
    'arial', 12, 'normal')).place(x=750, y=45)


# This is the section of code which creates a text input box
codeOutput = tkst.ScrolledText(
    root, width=25, height=20, bd=5, relief='groove')
codeOutput.pack()
codeOutput.place(x=750, y=76)

# This is the section of code which creates a button
Button(root, text='Compile', bg='#F0F8FF', font=(
    'arial', 12, 'normal'), command=lambda: compile_Click()).place(x=450, y=425)

root.mainloop()
