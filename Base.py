import PySimpleGUI as sg

sg.theme('DarkGrey5')
windowName ='Guess number game'
attemptPossibleByDefault = 3
firstNumberBoundaryNumber = 1
SecondNumberBoundaryNumber = 10
                               
inputNumberOfAttemptsLayout = [ [sg.Text('Enter number of attempts')],
                                [sg.InputText('')],
                                [sg.Button('Submit')] ]
             
winLayout = [ [sg.Text('You are right, well done!')],
              [sg.Button('Finish')] ]

failLayout = [ [sg.Text('Game over!')],
               [sg.Button('Finish')] ]

identLayout = [ [sg.Text('Hi, what is your name?'), sg.InputText('')],
                [sg.Button('Submit')] ]

def inputBoundaryNumberLayout():
    return [ [sg.Text('Type number for boundary')],
            [sg.InputText('')],
            [sg.Button('Next')] ]          

def descriptionLayout(name, minNum = 1, maxNum = 10):
    return [ [sg.Text('Let\'s play, {0}, I have guessed the number between {1} to {2}.'.format(name, minNum, maxNum))],
        [sg.Button('Play')] ]

def guessLayout(): 
    return [ [sg.Text('Can you guess which one?')],
        [sg.InputText('')],
        [sg.Button('Submit')] ]

def attemptFailedDisplayLayout(attemptPossible, attemptMade):
    return [ [sg.Text('Unfortunately NO')],
          [sg.Text('You still have {0} attempts'.format(attemptPossible - attemptMade))],
          [sg.Button('Try again'), sg.Button('Exit')] ]