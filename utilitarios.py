"""
Programa: Funções parar criar diretorios e mover arquivos para elas.
Requisitos: uma função para criar diretorio e uma para mover os arquivos para o diretorio criado.
Ator: Eu inspirado no programa do professor Nelson.
Versão: 0.0.1
Data: 19/09/2022.
"""

import os
import shutil

def criar_dir(nome:str):
    if os.path.exists(nome) == False:
        os.mkdir(nome)
        
def mov_arquivo(arquivos: list):
    for arquivo in arquivos:
        if ".xls" in arquivo:
            shutil.move(arquivo, f"./planilhas/{arquivo}")
        elif ".doc" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")