import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with pd.ExcelFile('dane otworowe.xlsx') as xls:
    L1_df = pd.read_excel(xls, 'L-1')
    K1_df = pd.read_excel(xls, 'K-1')
    O2_df = pd.read_excel(xls, 'O-2')

L1_df.set_index('DEPT', inplace=True)
K1_df.set_index('DEPT', inplace=True)
O2_df.set_index('DEPT', inplace=True)

L1_df = L1_df[['LLS', 'LLD', 'DT', 'RHOB', 'Pe', 'NPHI', 'GR', 'GKUT', 'GRKT', 'POTA',
       'THOR', 'URAN']]
K1_df = K1_df[['LLS', 'LLD', 'DT', 'RHOB', 'Pe', 'NPHI', 'GR', 'GKUT', 'GRKT', 'POTA',
       'THOR', 'URAN']]
O2_df = O2_df[['LLS', 'LLD', 'DT', 'RHOB', 'Pe', 'NPHI', 'GR', 'GKUT', 'GRKT', 'POTA',
       'THOR', 'URAN']]

#wizualizacja trzech wykresów
def trzy_wykresy():

    fig = plt.figure(figsize=(12, 15))
    
    ax_L1 = plt.subplot(1, 3, 1)
    ax_L1.set_title('L-1', y=1.1, fontsize = 20)
    
    add1 = ax_L1.twiny()
    add2 = ax_L1.twiny()
    
    ax_L1.set_ylim(L1_df.index.max(), L1_df.index.min())
    ax_L1.set_xlim(3, 2)
    add1.set_xlim(-5, 45)
    add2.set_xlim(160, 360)
    
    ax_L1.set_ylabel("DEPT")
    ax_L1.set_xlabel("RHOB")
    add1.set_xlabel("NPHI")
    add2.set_xlabel("DT")
    
    crv1, = ax_L1.plot(L1_df['RHOB'], L1_df.index, 'g-', label="RHOB")
    crv2, = add1.plot(L1_df['NPHI'], L1_df.index, 'b-', label="NPHI")
    crv3, = add2.plot(L1_df['DT'], L1_df.index, 'r-', label="DT")
    
    add1.spines['top'].set_position(('outward', 70))
    add2.spines['top'].set_position(('outward', 35))
    ax_L1.xaxis.tick_top()
    ax_L1.xaxis.set_label_position('top')
    
    ax_L1.grid(True)
    
    ax_L1.xaxis.label.set_color(crv1.get_color())
    add1.xaxis.label.set_color(crv2.get_color())
    add2.xaxis.label.set_color(crv3.get_color())
    
    
    ax_K1 = plt.subplot(1,3,2)
    ax_K1.set_title('K-1', y=1.1, fontsize = 20)
    
    add1 = ax_K1.twiny()
    add2 = ax_K1.twiny()
    
    ax_K1.set_ylim(K1_df.index.max(), K1_df.index.min())
    ax_K1.set_xlim(3, 2)
    add1.set_xlim(-5, 45)
    add2.set_xlim(160, 360)
    
    #ax_K1.set_ylabel("DEPT")
    ax_K1.set_xlabel("RHOB")
    add1.set_xlabel("NPHI")
    add2.set_xlabel("DT")
    
    crv1, = ax_K1.plot(K1_df['RHOB'], K1_df.index, 'g-', label="RHOB")
    crv2, = add1.plot(K1_df['NPHI'], K1_df.index, 'b-', label="NPHI")
    crv3, = add2.plot(K1_df['DT'], K1_df.index, 'r-', label="DT")
    
    add1.spines['top'].set_position(('outward', 70))
    add2.spines['top'].set_position(('outward', 35))
    ax_K1.xaxis.tick_top()
    ax_K1.xaxis.set_label_position('top')
    
    ax_K1.grid(True)
    
    ax_K1.xaxis.label.set_color(crv1.get_color())
    add1.xaxis.label.set_color(crv2.get_color())
    add2.xaxis.label.set_color(crv3.get_color())
    
    
    ax_O2 = plt.subplot(1, 3, 3)
    ax_O2.set_title('O-2', y=1.1, fontsize = 20)
    
    add1 = ax_O2.twiny()
    add2 = ax_O2.twiny()
    
    ax_O2.set_ylim(O2_df.index.max(), O2_df.index.min())
    ax_O2.set_xlim(3, 2)
    add1.set_xlim(-5, 45)
    add2.set_xlim(160, 360)
    
    #ax_O2.set_ylabel("DEPT")
    ax_O2.set_xlabel("RHOB")
    add1.set_xlabel("NPHI")
    add2.set_xlabel("DT")
    
    crv1, = ax_O2.plot(O2_df['RHOB'], O2_df.index, 'g-', label="RHOB")
    crv2, = add1.plot(O2_df['NPHI'], O2_df.index, 'b-', label="NPHI")
    crv3, = add2.plot(O2_df['DT'], O2_df.index, 'r-', label="DT")
    
    add1.spines['top'].set_position(('outward', 70))
    add2.spines['top'].set_position(('outward', 35))
    ax_O2.xaxis.tick_top()
    ax_O2.xaxis.set_label_position('top')
    
    ax_O2.grid(True)
    
    ax_O2.xaxis.label.set_color(crv1.get_color())
    add1.xaxis.label.set_color(crv2.get_color())
    add2.xaxis.label.set_color(crv3.get_color())
    
    plt.show()
