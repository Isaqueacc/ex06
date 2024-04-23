import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

#barra da janela
ctk.set_appearance_mode('dark')
#corpo da janela
janela = ctk.CTk('white')
janela.geometry('600x500')
janela.title('Sistema Escolar v1.0')

#funcão 
def calculo():
    media1 = float(unidade1.get())
    media2 = float(unidade2.get())
    media3 = float(unidade3.get())
    
    result = (media1+media2+media3)/3
    
    if(result >=5):
        resultado.insert(0,f'a média do aluno é de {result:.1f} passou de ano!')
        
    else:
        resultado.insert(0,f'a média do aluno é de {result:.1f} reprovado')
        
#funçao limpar
def limpar():
    unidade1.delete(0,'end')
    unidade2.delete(0,'end')
    unidade3.delete(0,'end')
    resultado.delete(0,'end')
    
#tela inicial
ctk.CTkLabel(janela,text = 'média escolar',font=('arial',22,'bold'),text_color = '#1C1C1C').pack(pady=20)

#1 unidade 1
ctk.CTkLabel(janela,text='1° Unidade', font= ('arial', 18, 'bold'), text_color='#8B2500').pack(pady=5)
unidade1 = ctk.CTkEntry(janela,placeholder_text='Digite o valor da primeira unidade',width=400)
unidade1.pack()

#unidade 2
ctk.CTkLabel(janela,text='2° Unidade', font= ('arial', 18, 'bold'), text_color='#8B2500').pack(pady=5)
unidade2 = ctk.CTkEntry(janela,placeholder_text='Digite o valor da segunda unidade',width=400)
unidade2.pack()

#unidade 3
ctk.CTkLabel(janela,text='3° Unidade', font= ('arial', 18, 'bold'), text_color='#8B2500').pack(pady=5)
unidade3 = ctk.CTkEntry(janela,placeholder_text='Digite o valor da terceira unidade',width=400)
unidade3.pack()
#botão calcular
btn= ctk.CTkButton(janela,text='Calcular', width=150,fg_color='#7A378B',text_color='white',command=calculo)
btn.pack(pady=15)
# otão limpar
btn= ctk.CTkButton(janela,text='limpar', width=150,fg_color='#7A378B',text_color='white',command=limpar)
btn.pack(pady=15)

resultado = ctk.CTkEntry(janela,placeholder_text='resultado',width=400)
resultado.pack()
janela.mainloop()