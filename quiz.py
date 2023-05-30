from tkinter import *
from tkinter import messagebox
from random import choice

#чтение данных из текстового файла
with open('game_data.txt', encoding='utf-8') as f:
    data = f.readlines()
    copy_of_data = list(data)
    num_of_questions = len(data)
    
def main():
    #окно с результатами
    def window_3():
        global counter
        w3 = Toplevel(window)
        w3.title('Результаты')
        w3.geometry('600x400+10+10')
        Label(w3, text="Результаты", width=36, bg="green",fg="white", font=("ariel", 20, "bold")).place(x=0, y=2)
        Label(w3, text=f'{str(int(counter/num_of_questions * 100))}%', width=16, font=("ariel", 80, "bold"), anchor='w').place(relx=0.05, rely=0.2)
        Label(w3, text=f'{counter}/{num_of_questions} ответов\nправильные.', width=30, font=("ariel", 20, "bold"), anchor='w').place(relx=0.55, rely=0.3)
        w3.resizable(False, False)
        if counter/num_of_questions >= 0.7:
             Label(w3, text='Вы просто настоящий физик и(или) химик!', width=50, font=("ariel", 18, "bold"), anchor='w').place(relx=0.05, rely=0.9)
        else:
             Label(w3, text='Несмотря на недочеты, вы достойно себя показали!', width=50, font=("ariel", 16, "bold"), anchor='w').place(relx=0.04, rely=0.9)
    #Функция преждевременного выхода из игры
    def exit_game():
        global data, copy_of_data
        data = list(copy_of_data)
        main_game.destroy()
        
    #Основная игра           
    def window_2():
        global var, list_of_answs, r_answ, main_game, bA, bB, bC, bD, q_no, q_Label, counter
        counter = 0
        q_no = 1
        main_game = Toplevel(window)
        main_game.title('Второе окно')
        main_game.geometry('1200x800+10+10')
        main_game.resizable(False, False)
        Label(main_game, text="Викторина по физике и химии", width=72, bg="green",fg="white", font=("ariel", 20, "bold")).place(x=0, y=2)
        cur_task = choice(data)
        data.remove(cur_task)
        question = cur_task.split('\t')[0]
        list_of_answs = cur_task.split('\t')[1].split('/')
        q_Label = Label(main_game, text=f'Вопрос {q_no}. {question}', width=75, font=('ariel', 18, 'bold'), anchor= 'w')
        q_Label.place(relx=0.025, rely= 0.2)
         
        for i in list_of_answs: #проверка правильного ответа (правильный ответ задается с восклицательным знаком в конце)
            if i[-1] == '!':
                r_answ = i
                
        var = IntVar(value=4)
        bA = Radiobutton(main_game, variable=var, text=list_of_answs[0].strip('!'), font=("ariel",15), value=0)
        bB = Radiobutton(main_game, variable=var, text=list_of_answs[1].strip('!'), font=("ariel",15), value=1)
        bC = Radiobutton(main_game, variable=var, text=list_of_answs[2].strip('!'), font=("ariel",15), value=2)
        bD = Radiobutton(main_game, variable=var, text=list_of_answs[3].strip('!\n'), font=("ariel",15), value=3)
        bA.place(relx=0.1, rely=0.4)
        bB.place(relx=0.1, rely=0.5)
        bC.place(relx=0.1, rely=0.6)
        bD.place(relx=0.1, rely=0.7)
        Button(main_game, text="Подтвердить", command=next_button, width=10, bg="blue", fg="white", font=("ariel",16,"bold")).place(relx=0.8, rely=0.9)
        Button(main_game, text="Выйти", command=exit_game, width=10, bg="black", fg="white", font=("ariel", 16, "bold")).place(relx=0.8, rely=0.1)

    #В данной функции реализуется переключение вопроса и обновления вариантов ответа при помощи кнопки     
    def next_button():
        
        global list_of_answs, counter, r_answ, q_no, q_Label, main_game, data
        q_no += 1
        if var.get() == list_of_answs.index(r_answ):
            counter += 1
        if not q_no - 1 == num_of_questions:
            cur_task = choice(data)
            data.remove(cur_task)
            question = cur_task.split('\t')[0]
            list_of_answs = cur_task.split('\t')[1].split('/')
            for i in list_of_answs: #проверка правильного ответа (правильный ответ задается с восклицательным знаком в конце)
                if i[-1] == '!':
                    r_answ = i
            
            #Обновление вопроса и вариантов ответа у радиокнопок
            q_Label.config(text=f'Вопрос {q_no}. {question}')
            bA.config(text=list_of_answs[0].strip('!'))
            bB.config(text=list_of_answs[1].strip('!'))
            bC.config(text=list_of_answs[2].strip('!'))
            bD.config(text=list_of_answs[3].strip('!\n'))
            var.set(4)
        else:
            data = list(copy_of_data)
            print(f'{counter} правильных ответов')
            main_game.destroy()
            window_3()
    #функция выхода из приложения 
    def win_close():
        if messagebox.askokcancel('Выход из приложения','Вы действительно хотите выйти из приложения?'):
            window.destroy()
            window.quit()
        
    #Основое окно(меню) 
    pre_window.destroy()
    window = Tk()
    window.title("Главное меню")
    window.geometry('1200x800+10+10')
    window.resizable(False, False)
    window.protocol('WM_DELETE_WINDOW', win_close)
    Label(window, text="Викторина по физике и химии", width=72, bg="green",fg="white", font=("ariel", 20, "bold")).place(x=0, y=2)
    Button(window, text="Начать игру", command=window_2, width=20,bg="blue", fg="white", font=("ariel",16,"bold")).place(rely=0.43, relx=0.38)
    Button(window, text="Выйти", command=win_close, width=20,bg="blue", fg="white", font=("ariel",16,"bold")).place(rely=0.5, relx=0.38)
  
    
#Заставка
pre_window = Tk()
pre_window.state('zoomed')
pre_window.resizable(0,0)
pre_window.title('Заставка')
zastavka = PhotoImage(file='для_заставки.png')
main_text = Label(pre_window, image=zastavka)
main_text.pack(fill=BOTH, expand=True)
icon = PhotoImage(file='icon.png')
pre_window.iconphoto(True, icon)

pre_window.after(3000, main)

mainloop()
