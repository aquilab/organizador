"""
Programa: Organiza arquivos xlsx e doc em suas respectivas pastas.
Requisitos: Analisar uma série de arquivos e mover os arquivos para dadas pastas de acordo com seus formatos.
Ator: Eu inspirado no programa do professor Nelson.
Versão: 0.0.1
Data: 19/09/2022.
"""


import utilitarios
import os
import shutil

def main():
    arquivos = os.listdir()
    for diretorio in ['documentos', 'planilhas']:
        utilitarios.criar_dir(diretorio)
    utilitarios.mov_arquivo(arquivos)
    
if __name__=='__main__':
    main()