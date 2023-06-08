#from classes.gerenciarS3 import GerenciarS3
#controla_s3 = GerenciarS3('aulanoitealexis1')
#controla_s3.lista_arquivos()
#diretorio_destino = '/home/ec2-user/environment/aulas3/aulaclasse/arquivos'
#nome_arquivo = 'log.png'
#controla_s3.download_arquivo(nome_arquivo, diretorio_destino)

from classes.menugerenciadorS3 import MenuGerenciadorS3
nome_bucket = "aulanoitealexis1"
menu = MenuGerenciadorS3(nome_bucket)
menu.executar()
