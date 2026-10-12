# DRILL 2
from pyscript import display, document

def name_finder(e):
    document.getElementById('result').innerHTML = ' '

    first_name = document.getElementById('firstname').value.lower().strip()
    last_name = document.getElementById('surname').value.lower().strip()

    sapphire_club = ['alexa agnote', 'adrianna allas', 'jaena ambata', 'al-makram arbison', 'zoe bueno', 'chase de guzman', 'xyrouz de lara', 'eliana de la cruz', 'franco deocampo', 'leiane gabia', 'helena magsino', 'misha manalo', 'ashley mangondato', 'jacob mendoza', 'sancho mercado', 'david niosco', 'bonnie nubla', 'keane pacaña', 'aisha padua', 'katherine penas', 'zoe reyes', 'cassiopeia rigodon', 'princess sagum', 'aldrich samar', 'antonio soliman', 'frances torculas', 'sebastian uclaray', 'marcus viray']

    candidate_name = first_name + ' ' + last_name
    student_checker = candidate_name in sapphire_club

    display_message = (f'Sorry {candidate_name.title()}, your name is not on the list.',f'Congratulations {candidate_name.title()}! You are now part of the SAPPHIRE 10 Club.')

    display(display_message[student_checker], target='result')

