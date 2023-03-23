from pathlib import Path

# caminho do projeto
caminho_projeto = Path()
print(caminho_projeto)  # relativo
print(caminho_projeto.absolute())  # absoluto

# caminho do arquivo
caminho_arquivo = Path(__file__)
print(caminho_arquivo)

# pasta acima
print(caminho_arquivo.parent)
print(caminho_arquivo.parent.parent)

# nova pasta (novo caminho)
new = caminho_arquivo.parent / 'new'
print(new)

# home
print(Path.home())
print(Path.home() / 'Desktop')

# criando arquivo
arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
arquivo.touch()
print(arquivo)

# escrever no arquivo
arquivo.write_text('Olá, mundo!')
arquivo.write_text('Olá, mundo de novo!')  # sobrescreve

# ler arquivo
print(arquivo.read_text())

# apagar arquivo
arquivo.unlink()

# criar pasta
caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
# caminho_pasta.mkdir()
caminho_pasta.mkdir(exist_ok=True)  # já existe
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

# apgar pasta
# caminho_pasta.rmdir()
# # nãp consegue apagar tudo
# tem que apagar arquivo por arquivo

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    file.touch()

    if file.is_file():  # exists() / is_dir()
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá, mundo\n')
        text_file.write(f'file_{i}.txt')


# from shutil import rmtree
def rmtree(root, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)
