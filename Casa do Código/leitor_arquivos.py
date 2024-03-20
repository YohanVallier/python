import os
for meta_file in os.listdir('/home/yohanvallier/Documentos/Meus Projetos/python/Casa do Código/dados/data/meta-data'):
    print(meta_file)

def extract_entity_name(fillename):
    return fillename.split('.')[0]
