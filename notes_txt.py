#для начала скопируй сюда интерфейс "Умных заметок" и проверь его работу

#затем запрограммируй демо-версию функционала
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog, QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout
import json
app = QApplication([])

# notes = {
#     "Инструкция": {
#         "текст": "Добро пожаловать",
#         "тэги": ["инструкция", "полезное"]
#     }
# }

notes = []





notes_win = QWidget()
notes_win.setWindowTitle('умные заметки')
notes_win.resize(900, 600)

list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')

b_n_c = QPushButton('Создать заметку')
b_n_d = QPushButton('Удалить заметку')
b_n_s = QPushButton('Сохранить заметку')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('введите тег...')
field_text = QTextEdit()
b_t_a = QPushButton('Добавить к заметке')
b_t_d = QPushButton('Открепить от заметки')
b_t_s = QPushButton('Искать заметки по тегу')
list_tegs = QListWidget() 
list_tegs_label = QLabel('Список тегов')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col1.addWidget(field_text)

col2 = QVBoxLayout()
col2.addWidget(list_notes_label)
col2.addWidget(list_notes)
row1 = QHBoxLayout()

row1.addWidget(b_n_c)
row1.addWidget(b_n_d)
row2 = QHBoxLayout()
row2.addWidget(b_n_s)

col2.addLayout(row1)
col2.addLayout(row2)
col2.addWidget(list_tegs_label)
col2.addWidget(list_tegs)
col2.addWidget(field_tag)
row3 = QHBoxLayout()
row3.addWidget(b_t_a)
row3.addWidget(b_t_d)
row_4 = QHBoxLayout()
row_4.addWidget(b_t_s)

col2.addLayout(row3)
col2.addLayout(row_4)

layout_notes.addLayout(col1, stretch = 2)
layout_notes.addLayout(col2, stretch = 1)
notes_win.setLayout(layout_notes)

def show_note():
    key = list_notes.selectedItems()[0].text()
    for note in notes:
        if note[0] == key:
            field_text.setText(note[1])
            list_tegs.clear()
            list_tegs.addItems(note[2])


def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Добавить заметку", "Название заметки:")
    if ok and note_name != "":
        note = [note_name, '', []]
        notes.append(note)
        list_notes.addItem(note[0])
        list_tegs.addItems(note[2])
        with open(str(len(notes)-1)+".txt", 'w', encoding='utf-8') as file:
            file.write(note[0]+'\n')

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        index = 0
        for note in notes:
            if note[0] == key:
                note[1] =field_text.toPlainText()
                with open(str(index)+".txt", "w", encoding='utf-8') as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            index += 1
            
list_notes.itemClicked.connect(show_note)
b_n_c.clicked.connect(add_note)
b_n_s.clicked.connect(save_note)




notes_win.show()

name = 0

note = []
while True:
    filename = str(name)+".txt"
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                note.append(line)
        tags = note[2].split(' ')
        note[2] = tags

        notes.append(note)
        note = []
        name += 1
    except IOError:
        break

for note in notes:
    list_notes.addItem(note[0])
                

app.exec_()