import os
import numpy as np
import pandas as pd
from glob import glob


def seleccionar_especies_random(input, random_size=4):
    np.random.seed(0)
    return np.random.choice(np.unique(df['species']), size=4)

if __name__ == '__main__':
    # selección
    df = pd.read_csv(
        '../data/input/1. Datos iniciales/Supplememtary_Table_1.csv',
        low_memory=False)
    lista_especies = list(seleccionar_especies_random(
        '../data/input/1. Datos iniciales/Supplememtary_Table_1.csv', 4))
    print(selected_species := '\n'.join(lista_especies))
    os.makedirs('../data/output', exist_ok=True)
    with open('../data/output/1.1 especies_seleccionadas.txt', 'w') as f:
        f.write(selected_species)
        
    # filtrado general
    df = df[df['species'].isin(lista_especies)]
    df.to_csv('../data/output/1.2 especies_filtradas.csv', index=False)
    
    # metadatos
    lista_fna = []
    acc = []
    for ii in glob('../0. Proyecto/Data_forTAP/*.fna'):
        for en,jj in enumerate(df['accession']):
            if ii.split('/')[-1].startswith(jj):
                lista_fna.append(ii)
                acc.append(en)
    df_fna = pd.DataFrame(lista_fna, columns=['fna'])
    # Dominio, filo, clase, orden, familia, género y especie.
    meta = df.iloc[acc]['gtdb_taxonomy'].str.split(';')
    
    