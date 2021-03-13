import PySimpleGUI as sg 
global font, titleFont
font = 'Segoe 12 bold'
titleFont = 'Segoe 15 bold'
sg.theme('Darkblue')
# Tela de inicialização do programa
def loginScreen():
    layout = [
        [sg.Text('User:', pad = (50,15), font= font), sg.Input(key = 'user', size= (25,1), justification= 'center', focus= True, border_width=3)],
        [sg.Text('Password:', pad = (30,0), font= font), sg.Input(key= 'password',password_char='*', size = (25,1), justification= 'center', pad = (0,5),border_width=3)],
        [sg.Button('Start', pad = (20,50), size=(10,1), font= font, border_width=5), sg.Button('Close', pad  = (0,50), size= (10,1), font = font, border_width=5)]
    ]
    return sg.Window('Login', layout,size = (500,230), element_justification='c',icon='logo.ico', finalize= True,grab_anywhere=True)

# Tela para escolher opções entre consulta ou registro de fornecedores
def optionScreen():
    layout = [
        [sg.Text('Please choose an option', pad = (0,15),font= titleFont)],
        [sg.Button('Search for an Application Area', pad= (20,5), size = (40,1), font = font)],
        [sg.Button('Search using a Supplier Name', pad= (20,5), size = (40,1), font = font)],
        [sg.Button('Insert a New Supplier', pad= (20,5), size = (40,1), font = font)]
    ]
    return sg.Window('Options', layout, size=(400,200), element_justification='c', icon='logo.ico', finalize= True,grab_anywhere=True)

# Tela de consulta - tipo de produto
def searchAreaScreen(areaList):
    layout = [
        [sg.Text('Please choose the field area to search', font = titleFont, pad = (0,10))],
        [sg.Combo(areaList, font= font, pad = (0,10), size = (40,1), background_color='black', text_color='white', key= '-AREA-', default_value='Choose an option', )],
        [sg.Button('Search', pad = (20,30), font = font, size = (10,1),border_width=(5)), sg.Button('Back', pad = (0,30), font = font, size = (10,1),border_width=(5))]
    ]
    return sg.Window('Search', layout, size = (500,200), element_justification = 'c', icon = 'logo.ico', finalize = True,grab_anywhere=True)

# Tela de consulta - por nome
def searchNameScreen(namelist):
    layout = [
        [sg.Text('Please choose a supplier name to search', font = titleFont, pad = (0,10))],
        [sg.Combo(namelist, font= font, pad = (0,10), size = (40,1), background_color='black', text_color='white', key= '-NAME-', default_value='Choose an option')],
        [sg.Button('Search', pad = (20,30), font = font, size = (10,1),border_width=(5)), sg.Button('Back', pad = (0,30), font = font, size = (10,1),border_width=(5))]
    ]
    return sg.Window('Search', layout, size = (500,200), element_justification = 'c', icon = 'logo.ico', finalize = True,grab_anywhere=True)

# Tela de registro - inserir novo registro de fornecedor
def insertScreen(function):
    border, pad, size = 5, (50,5,40,5), (5,1)
    layout = [
        [sg.Text('Supplier information',font= titleFont, pad = (190,20), size = (50,1), justification='c')],
        [sg.Text('ID:', pad = pad, size= size, font = font), sg.Input(justification= 'c', size= (50,1), key= '-ID-')],
        [sg.Text('Name:', pad = pad, size= size, font = font), sg.Input(justification= 'c', size= (50,1), key= '-NAME-')],
        [sg.Text('Area:', pad = (50,5,20,5), size= (5,1), font = font), sg.Combo(function, size= (50,1), key = '-AREA-', default_value='Choose an option')],
        [sg.Text('City:', pad = pad, size= size, font = font), sg.Input(justification= 'c', size= (50,1), key = '-CITY-')],
        [sg.Text('Email:', pad = pad, size= size, font = font), sg.Input(justification= 'c', size= (50,1), key= '-EMAIL-')],
        [sg.Text('Phone 1:', pad = pad, size= size, font = font), sg.Input(justification= 'c', size= (50,1), key='-PHONE1-')],
        [sg.Text('Phone 2:', pad = pad, size= size, font = font), sg.Input(justification= 'c', size= (50,1), key = '-PHONE2-', default_text='*',)],
        [sg.Text('Link:', pad = pad, size= size, font = font), sg.Input(justification= 'c', size= (50,1), key = '-LINK-')],
        [sg.Button('Save', pad = ((80,0),0), size=(10,1), border_width=5, font = font), sg.Button('Back',pad = ((80,0),0), size=(10,1), border_width= 5, font = font), sg.Button('Cancel',pad = ((80,0),30), size=(10,1), border_width=5, font = font)]
    ]
    return sg.Window('Insert', layout, size = (650,450), element_justification = 'l', icon = 'logo.ico', finalize = True,grab_anywhere=True, margins=(2,2))

# Tela de update - para modificar valores no registro de um fornecedor
def updateScreen():
    layout = [
        [sg.Text('UPDATING SUPPLIER')]
    ]
    return sg.Window('Update', layout, size = (400,200), element_justification = 'c', icon = 'logo.ico', finalize = True,grab_anywhere=True)

# Tela para exibição das informações do fornecedor
def infoScreen(data):
    border, pad, size = 5,((70,0),5),(5,1)
    layout = [
        [sg.Text('Supplier Information', pad =(190,20), font = titleFont, size = (20,1), justification= 'c')],
        [sg.Text('ID:', font = font, pad = pad, size = size),sg.Input(data[0], font = font, size=(40,1), border_width= border, justification='c',key='-ID-')],
        [sg.Text('Name:', font = font, pad = pad, size = size),sg.Input(data[1], font = font, size=(40,1), border_width= border, justification='c', key= '-NAME-')],
        [sg.Text('Area:', font = font, pad = pad, size = size),sg.Input(data[2], font = font, size=(40,1), border_width= border ,justification='c', key = '-AREA-', disabled = True, disabled_readonly_background_color = 'black', disabled_readonly_text_color = 'white')],
        [sg.Text('City: ', font = font, pad = pad, size = size),sg.Input(data[3], font = font,  size=(40,1), border_width= border,justification='c', key = '-CITY-')],
        [sg.Text('Email: ', font = font, pad = pad, size = size),sg.Input(data[4], font = font,  size=(40,1), border_width= border,justification='c', key= '-EMAIL-')],
        [sg.Text('Phone 1: ', font = font, pad = pad, size = size),sg.Input(data[5], font = font,  size=(40,1), border_width= border,justification='c', key='-PHONE1-')],
        [sg.Text('Phone 2: ', font = font, pad = pad, size = size),sg.Input(data[6], font = font,  size=(40,1), border_width= border,justification='c',key='-PHONE2-')],
        [sg.Text('Link:', font = font, pad = pad, size = size),sg.Input(data[7], font = font,  size=(40,1), border_width= border,justification='c',key='-LINK-')],
        [sg.Button('Update', font = font, border_width=5, pad = ((180,40),40), size = (10,1)), sg.Button('Back', font = font, border_width=5, pad = (0,0), size = (10,1))]
    ]
    return sg.Window('Search', layout, size = (600,500), element_justification = 'l', icon = 'logo.ico', finalize = True,grab_anywhere=False, margins=(1,1))

#Screen with the area table seach result
def tableScreen(data):
    data = data
    header = ['ID','Name','Area', 'City', 'Email','Phone #1','Phone #2','Link']

    layout = [
        [sg.Text('Report Area Information', font = titleFont,justification='c')],
        [sg.Table(values = data, headings=header, auto_size_columns=True, justification='c',vertical_scroll_only=False,  font = font, header_font=titleFont, num_rows=20)],
        [sg.Button('Back', size=(10,1), border_width=5, font = font)]
    ]

    return sg.Window('Table',layout, size = (1050,600), element_justification='c', border_depth=2, finalize= True, icon= 'logo.ico')


