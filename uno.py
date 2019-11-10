ilosc_poczatkowa = 10
koszt_sztuki = 3
kolejny = 'y'

import os

while (kolejny != 'n'):
    if (ilosc_poczatkowa >= 0):
        print('W magazynie znajduje się {} sztuk.'.format(ilosc_poczatkowa))
        print('Koszt jednego elementu to: {}.'.format(koszt_sztuki))

        zamowienie = int(input('Ile sztuk potrzebujesz? Wprowadz ilosc: '))
        test = input('Czy na pewno? Y/N')


        ilosc_koncowa = ilosc_poczatkowa - zamowienie
        koszt_calkowity = zamowienie * koszt_sztuki
        if (ilosc_koncowa < 0):
            print('Brak asortymentu.')
            break
        if (test == 'y'):
            print('Zamowiles {} sztuk, po {}. Calkowity koszt to: {}.'.format(zamowienie, koszt_sztuki, koszt_calkowity))
        else:
            print('Zrezygnowales z zamowienia.')

        print('W magazynie pozostalo: {} sztuk.'.format(ilosc_koncowa))
        ilosc_poczatkowa = ilosc_koncowa
        kolejny = input('Czy chcesz ponownie dokonać zakupu? Y/N')
        os.system("clear")



