# organizador_diretorios
Funções para organização e desorganização de diretórios. Ferramenta útil para manter organização de diretórios de download, drivers  e qualquer local onde se trabalhe com diferentes extensões de arquivos. Esse repositório trabalha com decomposição de strings e a biblioteca "OS" permitindo acesso a ferramentas do sistema. Projetado para "WINDOWS";
Para utilizar as funções é necessário instalar a biblioteca OS caso não tenha instalado;
Função organiza_dir(caminho) deve ser chamada para organizar o diretório;
A funão organiza_dir(caminho) aloca cada arquivo em uma pasta correspondente a sua extensão;
Função desorganiza_dir(caminho) deve ser chamada para remover todos os arquivos de dentro das pastas. O intuito é retornar ao estado inicial;
a variável "caminho" necessita que as "\" entre as pastas sejam trocadas por "\\" ou "/". ex:"C:\\User\\Portifólio\\diretoriosAnálise"
