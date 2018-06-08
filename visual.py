import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


class WykresyClass(object):

    '''Klasa rysująca wykresy krzywych pomiarowych geofizyki otworowej.
    Głównym argumentem (obligatoryjnym) jest lista zawierająca dane do przedstawienia na wykresach.
    Klasa pewnie w przyszłosci będzie jeszcze w razie potrzeb rozbudowywana i modyfikowana.

    Argumenty:
    - list:         lista 2D zawierająca na pierwszym miejscu każdego wiersza nazwę pd.DataFrame z którego mają być
                    pobierane dane, a na kolejnych nazwy kolumn z tego pd.DataFrame, które mają być przedstawione na
                    wykresach. Każdy wiersz odpowiada jednemy subplotowi, zaleca się rysowanie do 3 subplotów obok
                    siebie i do 4 krzywych, na każdym subplocie.
                    Przykład:
                    list = [[df1, 'col1', 'col2', 'col3'],
                            [df2, 'col1', 'col2'],
                            [df3, 'col1', 'col3'],
                            [df3, 'col1', 'col2']]

    - fig_size:     tuple określający wielkość wykresu, default: fig_size=(12, 15)

    - save:         określa czy wykres ma zostać zapisany, defaul: save=False. Jeśli chcemy aby kod zapisał wykres,
                    jako arg. save podajemy nazwę pod jaką chcemy zapisać nasz wykres, np. save='wykres_1', nie potrzeba
                    podawać rozszeżenia, klasa zapiszę ho z rozszeżeniem .png

    - x_sale_static: arg. określający, czy wszstkie krzywe na wykresie mają zostać przedstawione w tej samej skali osi
                    x, default: y_sc=False, czyli każda krzywa, będzie miała własną skalę na osi x. Przydatne, przy
                    porównywaniu kilku wariantów tej samej krzywej.

    Klasa nadaje automatycznie kolor krzywej i opisu osi jej odpowiadającej dla podstawowoych krzywych (narazie DT,
    RHOB i NPHI), ta część zostanie w przyszłości rozwinięta.'''

    # inicjalizacja obiektu
    def __init__(self, list, fig_size=(12, 15), save=False, x_scale_static=False):
        self.list = list
        self.fig_size = fig_size
        self.save = save
        self.x_scale_static = x_scale_static

    # na razie jedyna metoda, rysująca wykres
    def rysuj(self):
        fig = plt.figure(figsize=self.fig_size)

        # tworzenie i poruszanie się po kolejnych subplotach, dla poszczególnych wierszy list
        for i in range(len(self.list)):

            ax = plt.subplot(1, len(self.list), i+1)

            # nie potrafię w klasie wygenerować nazwy DataFramu i przypisać go jako tutuł subplota :(
            # name = self.list[i][0].name
            #ax.set_title(name, y=-0.1, fontsize=20)

            # ustawiam limit osi y i nadaje mu dobrze oddający dane spacing
            ax.set_ylim(self.list[i][0].index.max(), self.list[i][0].index.min())
            tick_spacing = 20
            ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

            # opis osi y ma być tylko przy pierwszym z lewej subplocie (wzrasta przejrzystość wykresu)
            if i == 0:
                ax.set_ylabel("DEPT")

            # ustawiam skąd prog. ma pobrać opis osi, jeśli spełnia on określone warunki zostają dla niego nadane od
            # razu limity osi x i kolor krzywej (opisu też docelowo)
            ax.set_xlabel(self.list[i][1])
            if self.list[i][1].upper() == 'RHOB':
                lim = (3, 2)
                ax.set_xlim(lim)
                color = 'b'
            elif self.list[i][1].upper() == 'NPHI':
                lim = (-5, 45)
                ax.set_xlim(lim)
                color = 'g'
            elif self.list[i][1].upper() == 'DT':
                lim = (160, 360)
                ax.set_xlim(lim)
                color = 'r'
            else:
                color = 'k'

            # inicjalizuje krzywą, ustawia grid i kolor opisu krzywej w kolorze krzywej
            crv, = ax.plot(self.list[i][0][self.list[i][1]], self.list[i][0].index, color=color, label=self.list[i][1])
            ax.grid(which='both')
            ax.xaxis.label.set_color(crv.get_color())

            # jeśli w agrumentach założylismy więcej niż jedną kolumnę na subplocie:
            if len(self.list[i]) > 2:
                for j in range(2, len(self.list[i])):

                    # dodajemy dodatkowy zestaw osi z powielającą osią y
                    add = ax.twiny()

                    # jeśli parametr x_scale_static=True, nowopowstałe osie będą miały ten sam zakres i kolor czarny
                    if self.x_scale_static:
                        add.set_xlim(lim)
                        color = 'k'

                    # w przeciwnym wypadku, gdy spełniają pewne warunki, będą miały limity osi i kolory ustalone
                    else:
                        if self.list[i][j].upper() == 'RHOB':
                            lim = (3, 2)
                            add.set_xlim(lim)
                            color = 'b'
                        elif self.list[i][j].upper() == 'NPHI':
                            lim = (-5, 45)
                            add.set_xlim(lim)
                            color = 'g'
                        elif self.list[i][j].upper() == 'DT':
                            lim = (160, 360)
                            add.set_xlim(lim)
                            color = 'r'

                    # dla dodatkowej osi również ustawiamy opis i inicjalizujemy krzywą
                    add.set_xlabel(self.list[i][j])
                    crv, = add.plot(self.list[i][0][self.list[i][j]], self.list[i][0].index, color=color, label=self.list[i][j])
                    add.xaxis.label.set_color(crv.get_color())

                    # każda kolejna oś x z opisem będzie przesunięta w górę o 35 jednostek
                    add.spines['top'].set_position(('outward', 35*(j-1)))

            # przesuwam podziałke i opis głównej osi x na górę, aby zachować kanwę
            ax.xaxis.tick_top()
            ax.xaxis.set_label_position('top')

        # gdy arg. save=True jest spełniony, zapisuję wykres pod nazwą przekazaną argumentowi jako string, z rozszeżeniem .png
        if self.save:
            plt.savefig(self.save+'.png')

        # rysuję wygenerowany i usalony wykres
        plt.show()


