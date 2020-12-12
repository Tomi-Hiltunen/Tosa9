import PySimpleGUI as sg

def main():    

    layout = [[sg.Text('Syötä lähtöarvosi')],
              [sg.Text('Arvo ykkönen',size = (25,1)), sg.InputText('',size = (5,1), key = 'Arvo1')],
              [sg.Text('Arvo kakkonen',size = (25,1)), sg.InputText('',size = (5,1), key = 'Arvo2')],
              [sg.Text('Arvo kolmonen',size = (25,1)), sg.InputText('',size = (5,1), key = 'Arvo3')],
              [sg.Text('Arvo nelonen',size = (25,1)), sg.InputText('', size = (5,1),key = 'Arvo4')],
              [sg.Text('Arvo vitonen',size = (25,1)), sg.InputText('',size = (5,1), key = 'Arvo5')],
              [sg.Text('Arvo kutonen',size = (25,1)), sg.InputText('',size = (5,1), key = 'Arvo6')],
              [sg.Text('Arvo seiska',size = (25,1)), sg.InputText('',size = (5,1), key = 'Arvo7')],
              [sg.Submit('OK'), sg.Cancel()]]
                

    window = sg.Window('Hiltunen Engineering Services', layout).finalize()    


    while True:
        event, values = window.read()
        
        if event == 'OK':
            # Haetaan arvot inputkentistä, jotta voidaan syöttää ne parametreinä aliohjelmiin
            try:
                arvo1 = float(values['Arvo1'])
                arvo2 = float(values['Arvo2'])
                arvo3 = float(values['Arvo3'])
                arvo4 = float(values['Arvo4'])
                arvo5 = float(values['Arvo5'])
                arvo6 = float(values['Arvo6'])
                arvo7 = float(values['Arvo7'])
            
            except NameError:
                sg.popup('Kokeileppa nyt tosissas syöttää ne luvut...')

            

            window.Element('Arvo1').Update(value = arvo2)
            window.Element('Arvo2').Update(value = arvo3)
            window.Element('Arvo3').Update(value = arvo4)
            window.Element('Arvo4').Update(value = arvo5)
            window.Element('Arvo5').Update(value = arvo6)
            window.Element('Arvo6').Update(value = arvo7)
            window.Element('Arvo7').Update(value = arvo1)


            #Lähetetään aliohjelmille tietoa ja lasketaan.
            luku = Laskenta1(arvo1, arvo2)

            
            layout2 = [[sg.Text('Tämä on kakkosruutu')],
                       [sg.Text(f'Tässä tapauksessa Arvo1 ja Arvo2 tulos on {luku}')],
                       [sg.Button('OK', key='Tulos_OK'), sg.Cancel()]]
            
            window2 = sg.Window('Tulosruutu', layout2).finalize()
            event2, values2 = window2.read()

            if event2 == 'Tulos_OK' or event2 == 'Cancel':
                window2.close()
            
            
            continue

        elif event == 'Cancel' or event == WIN_CLOSED:
            window.close()
            break



#Esimerkkilasku muutetaan ja palautetaan arvoja:        
def Laskenta1(Arvo1, Arvo2):
    result = Arvo1*Arvo2
    return(result)


 
    


main()
