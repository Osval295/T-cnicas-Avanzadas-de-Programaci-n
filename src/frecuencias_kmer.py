#%%
import ast
import pandas as pd


# %%
if __name__ == "__main__":
    # cargar los datos
    fasta = pd.read_csv('../data/output/1.4 samples.tsv', sep='\t',
                        converters={'nombre_seq': ast.literal_eval,
                                    'seq': ast.literal_eval,
                                    'longitud_seq': ast.literal_eval,})
    
# %%

