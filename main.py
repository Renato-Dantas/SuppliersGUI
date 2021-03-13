import PySimpleGUI as sg
from screens import *
from sqlFunctions import *
from functions import *

login, options, searchArea, searchName, insert, info ,info_area= loginScreen(),None, None,None, None, None, None

while True:
    screen, event, values = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED: # Close the window with the X in right corner
        break

# -------------------------------Login Screen------------------------------------------
    elif screen == login and event == 'Start': # if login is true, start the option screen
        login.hide()
        options = optionScreen()
    elif screen == login and event == 'Close': # close de program using a button
        break

    if screen == options and event =='Search for an Application Area': # open the area searching window 
        options.hide()
        searchArea = searchAreaScreen(createListArea())

    elif screen == options and event == 'Search using a Supplier Name': #Open the name searching window
        options.hide()
        names = searchListNames()
        listNames = createNameList(names)
        searchName = searchNameScreen(listNames)

    elif screen == options and event =='Insert a New Supplier': #Open the insert info window
        options.hide()
        insert = insertScreen(createListArea())

#---------------------------------------Search Screen AREA----------------------------------
    if screen == searchArea and event == 'Back': #Come back to the options screen
        searchArea.close()
        options.un_hide()
    elif screen == searchArea and event == 'Search': #Do the area search on the SQL base and return the results on a table
        areaList = createListArea()
        area = values['-AREA-']
        data = searchSqlArea(area)
        if len(data)==0:
            sg.popup('No data Found on This Area', no_titlebar=True, text_color= 'red',font = font)
        else:
            searchArea.close()
            print(data)
            info_area = tableScreen(data)

    elif screen == info_area and event == 'Back':
            info_area.close()
            searchArea = searchAreaScreen(createListArea())
#---------------------------------------Search Screen NAME----------------------------------
    if screen == searchName and event == 'Back':#Come back to the options screen
        searchName.close()
        options.un_hide()

    if screen == searchName and event == 'Search': #Do the name search on the SQL base and return the results on a table
        name = values['-NAME-']
        try:
            data = searchSqlName(name)
            searchName.close()
            info = infoScreen(data[0])
        except:
            sg.popup('You must select a name on the list!', text_color='red')
            searchName = searchNameScreen(listNames)
    
    elif screen == info and event == 'Update':
        data = list(values.values())
        data.append(values['-NAME-'])
        updateData(data)
        info.close()
        newData = searchSqlName(name)
        info = infoScreen(newData[0])
    
    elif screen == info and event == 'Back':
        searchName = searchNameScreen(listNames)
        info.close()

# ------------------------------------INSERT SCREEN------------------------------------
    if screen == insert and event == 'Back':#Come back to the options screen
        insert.close()
        options.un_hide()
    elif screen == insert and event == 'Save': #Save a new supplier on the database

        ID, name, area, city, email, phone1, phone2, link = values['-ID-'],values['-NAME-'], values['-AREA-'], values['-CITY-'], values['-EMAIL-'], values['-PHONE1-'], values['-PHONE2-'], values['-LINK-']

        if ID =='' or name=='' or area=='' or city=='' or email=='' or len(phone1)<8:
            sg.popup('You are trying to insert an incomplete record!\n\n Please complete all required information', font = font, no_titlebar= False, auto_close_duration= 5,text_color='red', auto_close=False)
        else:
            try:
                insertSqlValue(ID,name,area,city,email,phone1, phone2, link)
                sg.popup(title = 'Registered Supplier!',auto_close_duration=5, no_titlebar=True, auto_close=True)
            except:
                sg.popup('You are trying to insert an incomplete record!', font = font, no_titlebar= True,auto_close_duration= 5,text_color='red', auto_close=True)

    elif screen == insert and event == 'Cancel': #Clear all rows on the table
        insert.close()
        insert = insertScreen(createListArea())
# ------------------------------------------------------------------------------------
