# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:10:16 2023

@author: jvBra
Organizador de arquivos por diretório em pasta downloads
"""
import os
def organiza_dir(caminho):
    os.chdir(caminho)
    ##ENTRAR EM UM DIRETÓRIO DOWNLOADS E ORGANIZAR A PASTA POR TIPO DE ARQUIVO
    arquivos = os.listdir(caminho)
    list_ext = []
    #LISTANDO ARQUIVOS 
    for arquivo in arquivos:
        extensao = {os.path.splitext(arquivo)[1]}
        extstr = str(extensao)
        limitador_ext = len(extstr)-2
        extfinal = extstr[3:limitador_ext]
        list_ext.append(extfinal)

    lista_diretorios = list(dict.fromkeys((list_ext)))

    #E CRIANDO PASTAS
    for lista in list_ext:
        nome_pasta = str(lista)
        try:
            os.mkdir(nome_pasta)
        except:
            continue


    #MOVER ARQUIVOS PARA RESPECTIVAS PASTAS
    for arquivo in arquivos:
        extensao2 = {os.path.splitext(arquivo)[1]}
        extstr2 = str(extensao2)
        limitador_ext2 = len(extstr2)-2
        extfinal2 = extstr2[3:limitador_ext2]
        os.rename(arquivo,caminho+"\\"+extfinal2+"\\"+arquivo)

def desorganiza_dir(caminho):
    #ACESSO A PASTA E LISTO O DIRETÓRIO
    os.chdir(caminho)
    pastas = os.listdir(caminho)

    #INICIALIZO UM LOOP QUE PASSARÁ POR TUDO DENTRO DO DO DIRETÓRIO DOWNLOADS
    for pasta in pastas:
        #VERIFICO SE É UMA PASTA OU UM ARQUIVO
        if "." in pasta:
            ext_Arq = pasta.split('.')[1]
            print(f"Isso é um arquivo com Extensão: {ext_Arq}")   
        else:
            #CASO FOR PASTA, LISTO TODOS OS ARQUIVOS NO DIRETORIO
            arquivos = os.listdir("C:\\Users\\jvBra\\Downloads\\"+pasta)
            #ACESSO CADA ARQUIVO DENTRO DA PASTA E IREI MOVER PARA DIRETÓRIO DOWNLOAD
            for arquivo in arquivos:
                os.rename(caminho+"\\"+pasta+"\\"+arquivo,caminho+"\\"+arquivo)
            #EXCLUO O DIRETÓRIO QUE FOI LIMPO
            os.rmdir(caminho+"\\"+pasta)

organiza_dir("C:\\Users\\jvBra\\Downloads")