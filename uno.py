ilosc_poczatkowa = 10
koszt_sztuki = 3
stan = 'y'

while (stan != 'n'):
    if (ilosc_poczatkowa >= 0):
        print('W magazynie znajduje się {} sztuk.'.format(ilosc_poczatkowa))
        print('Koszt jednego elementu to: {}.'.format(koszt_sztuki))

        zamowienie = int(input('Ile sztuk potrzebujesz? Wprowadz ilosc: '))

        test = input('Czy na pewno? Y/N')
        if test is int:
            print('Error! Podana dana to nie string.')
            break

        if zamowienie > ilosc_poczatkowa:
            print('Ilosc zbyt duza.')
            break
        koszt_calkowity = zamowienie * koszt_sztuki
        if (test == 'y'):
            ilosc_koncowa = ilosc_poczatkowa - zamowienie
            if (ilosc_koncowa < 0):
                print('Brak asortymentu.')
                ilosc_koncowa = ilosc_koncowa + zamowienie
                break
            print('Zamowiles {} sztuk, po {}. Calkowity koszt to: {}.'.format(zamowienie, koszt_sztuki, koszt_calkowity))
        else:
            print('Zrezygnowales z zamowienia.')

        print('W magazynie pozostalo: {} sztuk.'.format(ilosc_koncowa))
        ilosc_poczatkowa = ilosc_koncowa
        stan = input('Czy chcesz ponownie dokonać zakupu? Y/N')
    print('Dziekujemy za zakupy. Mielgo dnia.')



