import tkinter as tk
from tkinter import messagebox

def verificar_nota():
    nota_texto = entry_nota.get()#vai pegar a informação
    
    if nota_texto.replace(".","", 1).isdigit():
        nota=float(nota_texto)
    
    
        if nota >= 7:
            resultado = "aprovado"
        elif nota >= 5:
            resultado = "Média"
        else:
            resultado = "recuperação"
   
        messagebox.showinfo("resultado",f"Situação"" {resultado}")
    else:
       messagebox.showerror("erro","Digite um numero válido.")
           
root = tk.Tk()
root.title("Verificação de nota.")
root.geometry("300x200")             
root.configure(bg="#ffff00")   #fundo amarelo claro

#Widgets
tk.label(root, text="Digite a nota do aluno:",bg="#ffff00", fg="black", front=("Arial",11, "bold")).pack(pady=10)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)

tk.Button(root, text="Verificar", coomand=verificar_nota, bg="blue", fg="white", font=("Arial", 11,"bold")).pack(pady=15)
root.mainloop()

def avaliar_nota(nota):
    if nota == 10:
        return "Parabéns, nota máxima!"
    elif 9 <= nota < 10:
        return "Quase perfeito!"
    elif 0 <= nota <= 4.9:
        return "Reprovado com baixa nota."
    else:
        return "Nota fora dos critérios definidos."