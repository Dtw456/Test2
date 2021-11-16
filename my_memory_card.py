#Modules
from random import randint
from random import shuffle
from PyQt5.QtCore import Qt

#Window
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QLabel, QPushButton, QVBoxLayout, QGroupBox, QRadioButton, QHBoxLayout
#class
class Question():
    def __init__(self, question1, right_answer, wrong1, wrong2, wrong3):
        self.question1 = question1
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#questions
q1_list = []
q1_list.append(Question('Где находится Тайвань?', "в Азии", "в Европе", "в Африке", "в Америке"))
q1_list.append(Question("Какая  страна является самой крупной в мире?", 'Россия', "Китай", "США", "Канада"))
q1_list.append(Question ('Cколько республик входило в состав СССР', "15", "25", "20", "10"))
q1_list.append(Question ('Самые высокие горы?', "Гималайские", "Альпийские", "Уральские", "Карпатске"))
q1_list.append(Question('Сколько штатов в составе США?', "50", "48", "52", "35" ))
q1_list.append(Question('В какой стране больше всего населения?', "Китай", "Индия", "США", "Бангладеш"))

app = QApplication([])

main_win = QWidget()
main_win.resize(500,500)

#Buttons
main_win.setWindowTitle('Memory card')
ans_button = QPushButton('Ответить')
question = QLabel('Какой национальности не существует?')
#Group1
AnsGroupBox = QGroupBox('Варианты ответов')
ans0 = QRadioButton('Энцы')
ans1 = QRadioButton('Чулумцы')
ans2 = QRadioButton('Смурфы')
ans3 = QRadioButton('Алеуты')

AnsGroup = QButtonGroup()
AnsGroup.addButton(ans0)
AnsGroup.addButton(ans1)
AnsGroup.addButton(ans2)
AnsGroup.addButton(ans3)

#Lines
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
h_line1 = QHBoxLayout() 
v_line1.addWidget(ans1)
v_line1.addWidget(ans3)
v_line2.addWidget(ans2)
v_line2.addWidget(ans0)
h_line1.addLayout(v_line1)
h_line1.addLayout(v_line2)
AnsGroupBox.setLayout(h_line1)
#Group 2
RightAnsGroup = QGroupBox('Результаты')
write1 = QLabel('Правильно/неправильно')
right_ans = QLabel(' Правильный ответ')
v_line_answers = QVBoxLayout()
v_line_answers.addWidget(write1, alignment= Qt.AlignLeft)
v_line_answers.addWidget(right_ans, alignment= Qt.AlignHCenter)
RightAnsGroup.setLayout(v_line_answers)

#расположение виджетов по лэйаутам и объединение в группу
h_line2 = QHBoxLayout()
h_line3 = QHBoxLayout()
h_line4 = QHBoxLayout()
h_line2.addWidget(question, alignment= Qt.AlignHCenter)
#Привязка групп
h_line3.addWidget(AnsGroupBox)
h_line3.addWidget(RightAnsGroup)
RightAnsGroup.hide()
#Привязка к линиям
h_line4.addStretch(1)
h_line4.addWidget(ans_button, stretch=3)
h_line4.addStretch(1)

main_line = QVBoxLayout()
main_line.addLayout(h_line2, stretch= 3)
main_line.addLayout(h_line3, stretch= 8)
main_line.addStretch(1)
main_line.addLayout(h_line4, stretch= 2)
main_line.addStretch(1)
main_line.setSpacing(5)
main_win.setLayout(main_line)
#Функции
def show_result():
    AnsGroupBox.hide()
    RightAnsGroup.show()
    ans_button.setText("Следующий Вопрос")
def show_question():
    AnsGroupBox.show()
    RightAnsGroup.hide()
    ans_button.setText('Ответить')
    AnsGroup.setExclusive(False)
    ans0.setChecked(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    AnsGroup.setExclusive(True)

answers = [ans0, ans1, ans2, ans3]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question1)
    right_ans.setText(q.right_answer)
    show_question()
def show_correct(res):
    write1.setText(res)
    show_result()
def chek_answers():
    if answers[0].isChecked():
        show_correct("Верно")
        main_win.score+=1
        print('Статистика\n - Всего вопросов:' ,main_win.total, '\n Правильных ответов:' ,main_win.score)
    else:
        if answers[1].isChecked():
            show_correct('Неверно')
            
            print('Ретйтинг:', main_win.score/main_win.total * 100, '%')
        else:
            if answers[2].isChecked():
                show_correct('Неверно')
            else:
                if answers[3].isChecked():
                    show_correct('Неверно')
                    

def next_question():
    main_win.total+= 1
    print('Статистика\n -Всего вопросов:', main_win.total,'\n Правильных ответов:', main_win.score)
    cur_question = randint(0, len(q1_list) - 1)
    q = q1_list[cur_question]
    ask(q)
def click_OK():
    if ans_button.text() == 'Ответить':
        chek_answers()
    else:
        next_question()
ans_button.clicked.connect(click_OK)

main_win.score = 0
main_win.total = 0

next_question()

#final
main_win.show()
app.exec() 
