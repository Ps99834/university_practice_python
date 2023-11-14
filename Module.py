import PySimpleGUI as sg
import Base



def readInputValue(defaultValue, window):
    while True: 
        event, values = window.read()
        if values[0] != '':
            value = values[0]
            break
        if event[0] == sg.WIN_CLOSED:
            value = defaultValue
            break
        else:
            value = defaultValue
            break

    return value

def enterNumberBoundary(default):
    window = sg.Window(Base.windowName, Base.inputBoundaryNumberLayout())

    boundary = int(readInputValue(default, window))

    window.close()
    return boundary

def identUser():
    window = sg.Window(Base.windowName, Base.identLayout)

    name = readInputValue('User', window)

    window.close()
    return name

def enterNumberOfAttempts():
    window = sg.Window(Base.windowName, Base.inputNumberOfAttemptsLayout)

    number = int (readInputValue(Base.attemptPossibleByDefault, window))

    window.close()
    return number

def description(name, minNum = 1, maxNum = 10):
    window = sg.Window(Base.windowName, Base.descriptionLayout(name, minNum, maxNum))

    while True:
        event = window.read()
        if event[0] == 'Play':
            break
        
        if event[0] == sg.WIN_CLOSED:
            break

    window.close()

def readGuessNum():
    window = sg.Window(Base.windowName, Base.guessLayout())
    
    guess = int(readInputValue(-1, window))

    window.close()
    return guess

def windowWaiting(layout, theme = 'DarkGrey5'):
    sg.theme(theme)
    window = sg.Window(Base.windowName, layout)

    while True:
        event = window.read()
        if event[0] == sg.WIN_CLOSED or event[0] == 'Finish':
            break

    window.close()

def attemptFailedWindowDisplaying(attemptPossible, attemptMade):
    window = sg.Window(Base.windowName, Base.attemptFailedDisplayLayout(attemptPossible, attemptMade))

    while True: 
        event = window.read()
        if event[0] == sg.WIN_CLOSED or event[0] == 'Exit':
            attemptPossible = -1
            break

        if event[0] == 'Try again':
            break

    window.close()
    return attemptPossible

def guessing(attemptPossible, number):
    attemptMade = 0

    while attemptMade < attemptPossible:
        guess = readGuessNum()
        attemptMade += 1

        if attemptPossible - attemptMade == 0 and int(guess) != number:
            windowWaiting(Base.failLayout, 'DarkRed1')

        if int(guess) == number:
            windowWaiting(Base.winLayout, 'DarkGreen')
            break

        elif attemptPossible - attemptMade != 0:
            attemptPossible = attemptFailedWindowDisplaying(attemptPossible,attemptMade)