from PyQt5.QtWidgets import QApplication #Запуск приложения PyQt5


app = QApplication([]) 
from menu_window import*

from main_window import* #Импорты интерфейса и случайных функций
from random import*
from time import*

class Question(): #Создаёт класс для хранения данных одного вопроса.
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3): #Метод-конструктор, который принимает текст вопроса.
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1   #Сохраняет переданные значения в атрибутах объекта.
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.is_active = True  #Флаг, который можно использовать, чтобы "отключить" вопрос
        self.count_ask = 0 #Счётчики: сколько раз задавался вопрос и сколько раз на него ответили правильно.
        self.count_right = 0
        
    def got_right(self): #Методы класса
        self.count_ask += 1
        self.count_right += 1
    
    def got_wrong(self):
        self.count_ask += 1
        
q1 = Question('Яблуко', 'apple', 'apply', 'pineapple', 'application') #Создание вопросов
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

questions = [q1, q2, q3, q4]

radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] #Список радиокнопок

def new_question(): #Функция показа нового вопроса
    global cur_q
    cur_q = choice(questions) #Выбирает случайный вопрос из списка.
    lb_Question.setText(cur_q.question)
    lb_Corect.setText(cur_q.answer) #Сохраняет правильный ответ в скрытой метке
    
    shuffle(radio_buttons) #Перемешивает порядок кнопок, чтобы правильный ответ был в случайном месте.
    radio_buttons[0].setText(cur_q.answer)
    radio_buttons[1].setText(cur_q.wrong_answer1)
    radio_buttons[2].setText(cur_q.wrong_answer2)
    radio_buttons[3].setText(cur_q.wrong_answer3)
    
    RadioGroup.setExclusive(False) #Снимает выделение со всех кнопок (временно отключая эксклюзивный выбор).
    for button in radio_buttons:
        button.setChecked(False)
    RadioGroup.setExclusive(True)

    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')

def check(): #Функция проверки ответа
    RadioGroup.setExclusive(False)
    for button in radio_buttons:
        if button.isChecked():
            if button.text() == lb_Corect.text():
                cur_q.got_right()
                lb_Result.setText('Вірно!')
            else:
                cur_q.got_wrong()
                lb_Result.setText('Невірно!')
        break
    
    RadioGroup.setExclusive(True)
    RadioGroupBox.hide() #Скрывает варианты ответов и показывает блок с результатом.
    AnsGroupBox.show()
    btn_OK.setText('Наступне питання') #Меняет текст кнопки на "Следующий вопрос"

def click_ok(): #Обработка нажатия кнопки
    if btn_OK.text() == 'Відповісти':
        check()
    else:
        new_question()
def rest():
    win_card.hide()
    n = box_Minutes.value() * 60
    sleep(n)
    win_card.show()



def menu_generation():
    if cur_q.count_ask == 0:
        c = 0
    else:
        c = (cur_q.count_right/cur_q.count_ask)*100

    text = f'Разів відповіли: {cur_q.count_ask}\n' \
           f'Вірних відповідей: {cur_q.count_right}\n' \
           f'Успішність: {round(c, 2)}%'
    lb_statistic.setText(text)
    menu_win.show()
    win_card.hide()
    
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
    
btn_clear.clicked.connect(clear)

def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),
                     le_wrong_ans1.text(), le_wrong_ans2.text(),
                     le_wrong_ans3.text())
    
    questions.append(new_q)
    clear()

btn_add_question.clicked.connect(add_question)
    
def back_menu():
    menu_win.hide()
    win_card.show()


btn_Menu.clicked.connect(menu_generation)
btn_back.clicked.connect(back_menu)


btn_Sleep.clicked.connect(rest)
       
        
btn_OK.clicked.connect(click_ok) #Привязка кнопки и запуск



new_question()





app.exec_() #Запускает главный цикл приложения PyQt5
