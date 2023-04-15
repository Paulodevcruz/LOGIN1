import PySimpleGUI as sg

layout = [
[sg.Text('Usuário')],
[sg.Input(key='usuario')],
[sg.Text('senha')],
[sg.Input(key='senha')],
[sg.Button('login')],
[sg.Text('',key='mensagem')],
]

window = sg.Window('Login',Layout=layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
         break