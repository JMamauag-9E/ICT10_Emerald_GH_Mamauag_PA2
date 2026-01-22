# if-elif-else statement
from pyscript import display, document


#def Julias_answer(e):
    #document.getElementById('output').innerHTML = ' '

    #response = document.getElementById('input1').value.lower()

    #if response == 'yes':
        #display(f'K will be her valentine.', target='output')
    #elif response == 'no':
        #display(f'Womp womp.', target='output')
    #elif response == 'maybe':
        #display(f'', target='output')
    #else:
        #display(f'I AM THE WALRUS! GOO GOO GOO JOOB!', target='output')

def students_classification(e):
    document.getElementById('result').innerHTML = ' '

    classification = float(document.getElementById('number1').value)

    if classification >= 95:
        display(f'Bergamo 1: EXCELLENT!', target='result')
    elif classification >= 91:
        display(f'Bergamo 2: Nice one!', target='result')
    elif classification >= 86:
        display(f'Bergamo 3: Good.', target='result')
    elif classification >= 75:
        display(f'Perugia 1: Better luck next time.', target='result')
    elif classification >= 0:
        display(f'Perugia 2: Failed.', target='result')