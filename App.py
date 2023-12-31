import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from aluno import Aluno

class App:
    def __init__(self):
        self.alunos = []
        self.janela = Tk()
        self.janela.geometry("1025x600")
        self.janela.title("Cadastro de Alunos")

        #Label
        self.label_matricula = Label(self.janela, text="Matrícula:", font="Tahoma 12 bold", fg="Blue", padx=5, pady=5)
        self.label_matricula.grid(row=0, column=0, sticky=tkinter.E)

        self.label_nome = Label(self.janela, text="Nome:", font="Tahoma 12 bold", fg="Blue", padx=5, pady=5)
        self.label_nome.grid(row=1, column=0,sticky=tkinter.E)

        self.label_idade = Label(self.janela, text="Idade:", font="Tahoma 12 bold", fg="Blue", padx=5, pady=5)
        self.label_idade.grid(row=2, column=0,sticky=tkinter.E)

        self.label_curso = Label(self.janela, text="Curso:", font="Tahoma 12 bold", fg="Blue",padx=5, pady=5)
        self.label_curso.grid(row=3, column=0,sticky=tkinter.E)

        self.label_nota = Label(self.janela, text="Nota:", font="Tahoma 12 bold", fg="Blue", padx=5, pady=5)
        self.label_nota.grid(row=4, column=0, sticky=tkinter.E)



        #Entry
        self.txt_matricula = Entry(self.janela, font="Tahoma 10", width=27, state=DISABLED)
        self.txt_matricula.grid(row=0, column=1, sticky=tkinter.W)

        self.txt_nome = Entry(self.janela, font="Tahoma 10", width=27)
        self.txt_nome.grid(row=1, column=1, sticky=tkinter.W)

        self.txt_idade = Entry(self.janela, font="Tahoma 10", width=27)
        self.txt_idade.grid(row=2, column=1, sticky=tkinter.W)

        self.txt_nota = Entry(self.janela, font="Tahoma 10", width=27)
        self.txt_nota.grid(row=4, column=1, sticky=tkinter.W)


        #Combobox
        self.cursos = ["Python", "Javascript", "HTML&CSS", "React"]
        self.combo_curso = ttk.Combobox(self.janela, values=self.cursos, width=25, font="Tahoma 10")
        self.combo_curso.grid(row=3, column=1, sticky=tkinter.W)

        #Button
        self.button_adicionar = Button(self.janela, text="Adicionar", font="Tahoma 10 bold", fg="blue",padx=5, pady=5, command=self.cadastrarAluno)
        self.button_adicionar.grid(row=5, column=0)

        self.button_editar = Button(self.janela, text="Editar", font="Tahoma 10 bold", fg="blue", padx=5, pady=5, command=self.editarAluno)
        self.button_editar.grid(row=5, column=1)

        self.button_deletar = Button(self.janela, text="Deletar", font="Tahoma 10 bold", fg="blue", padx=5, pady=5)
        self.button_deletar.grid(row=5, column=2)

        #frame
        self.frame = Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3, sticky=tkinter.EW)
        self.colunas = ['Matrícula','Nome', 'Idade', 'Curso', 'Nota']
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas, show="headings")
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
        self.tabela.bind('<ButtonRelease-1>', self.preencherCampos)
        self.tabela.pack()

        self.janela.mainloop()

    def deletarAluno(self):
        matricula = self.txt_matricula.get()
        for aluno in self.alunos:
            if str(aluno.matricula) == matricula:
                self.alunos.remove(aluno)
        self.listarAlunos()
        self.limparCampos()
        messagebox.showinfo("Sucesso!", "Aluno removido com sucesso!")


    def editarAluno(self):
        matricula = self.txt_matricula.get()
        for aluno in self.alunos:
            if str(aluno.matricula) == matricula:
                aluno.nome = self.txt_nome.get()
                aluno.idade = int(self.txt_idade.get())
                aluno.curso = self.combo_curso.get()
                aluno.nota = float(self.txt_nota.get())
            self.limparCampos()
            self.listarAlunos()
            messagebox.showinfo("Sucesso", "Dados alterados com sucesso!")

    def preencherCampos(self, event):
        self.limparCampos()
        linha_selecionada = self.tabela.selection()[0]
        aluno = self.tabela.item(linha_selecionada)['values']
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.insert(0, str(aluno[0]))
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.insert(0, (aluno[1]))
        self.txt_idade.insert(0, str(aluno[2]))
        self.combo_curso.set(aluno[3])
        self.txt_nota.insert(0, str(aluno[4]))


    def criarAluno(self):
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        curso = self.combo_curso.get()
        nota = float(self.txt_nota.get())
        aluno = Aluno(nome,idade,curso,nota)
        return aluno

    def cadastrarAluno(self):
        aluno = self.criarAluno()
        self.alunos.append(aluno)
        messagebox.showinfo('Sucesso', 'Aluno cadastrado com sucesso!')
        self.limparCampos()
        self.listarAlunos()


    def limparCampos(self):
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.delete(0, END)
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.delete(0, END)
        self.txt_idade.delete(0, END)
        self.combo_curso.set("")
        self.txt_nota.delete(0, END)

    def listarAlunos(self):
        #limpar as linhas da tabela.
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)

        for aluno in self.alunos:
            self.tabela.insert("", END, values=(aluno.matricula, aluno.nome, aluno.idade, aluno.curso, aluno.nota))


if __name__ == "__main__":
    App()


