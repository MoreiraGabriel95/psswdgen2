import random
import string
from tkinter import *
from tkinter import ttk
import pyperclip

def generate_password(length, uppercase, numbers, special):
    # define os caracteres possíveis para a senha
    chars = string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if numbers:
        chars += string.digits
    if special:
        chars += string.punctuation

    # gera a senha com os caracteres definidos
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# cria a interface gráfica
root = Tk()
root.title("Gerador de Senhas")
root.configure(bg='black')

# cria widgets para perguntar as opções de senha
length_label = Label(root, text="Quantos caracteres?", fg='white', bg='black')
length_label.pack()
length_entry = Entry(root)
length_entry.pack()

uppercase_var = BooleanVar()
uppercase_check = Checkbutton(root, text="Letras maiúsculas", variable=uppercase_var, fg='white', bg='black', indicatoron=False)
uppercase_check.pack()

numbers_var = BooleanVar()
numbers_check = Checkbutton(root, text="Números", variable=numbers_var, fg='white', bg='black', indicatoron=False)
numbers_check.pack()

special_var = BooleanVar()
special_check = Checkbutton(root, text="Caracteres especiais", variable=special_var, fg='white', bg='black', indicatoron=False)
special_check.pack()

password_label = Label(root, text="", fg='white', bg='black')
password_label.pack()

# adiciona botão para copiar a senha
def copy_button_clicked():
    password = password_label.cget("text")
    if password:
        pyperclip.copy(password)

copy_button = Button(root, text="Copiar senha", command=copy_button_clicked)
copy_button.pack()

# define a função para gerar a senha quando o botão for clicado
def generate_button_clicked():
    length = int(length_entry.get())
    uppercase = uppercase_var.get()
    numbers = numbers_var.get()
    special = special_var.get()
    password = generate_password(length, uppercase, numbers, special)
    password_label.configure(text=password)

generate_button = Button(root, text="Gerar senha", command=generate_button_clicked)
generate_button.pack()

# Altera cor dos checkboxes marcados
style = ttk.Style(root)
style.theme_use('clam')

style.map("TCheckbutton",
          indicatoron=[('selected', '!disabled', 'black'), ('pressed', 'black')],
          background=[('selected', 'yellow'), ('pressed', 'red')],
          foreground=[('selected', 'black'), ('pressed', 'white')])

# inicia a interface gráfica
root.mainloop()
