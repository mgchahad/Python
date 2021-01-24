#!/usr/bin/python3
import docker
import git

# Variáveis
image_name = "mchahad/repository/image"

# Coletando ID do commit
repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha[0:7]

# Criando nome da imagem + versão do commit
image_version = image_name + ":" + sha
print("Versão da Imagem: " + image_version)

# Conecta ao Docker utilizando as configurações de socket padrão ou via configuração do seu ambiente
client = docker.from_env()

# Coleta imagem especificada
get_image = client.images.list(image_version)

# Remoção da imagem caso ela exista
if len (get_image):
    print("\nRemovendo imagem...")
    image = get_image[0].tags
    print(f"Imagem: {image}")
    client.images.remove(image[0])
 
# Aplicando build da imagem
print("\nAplicando um novo build...")
client.images.build(path = "./", tag = image_version, nocache = True)

# Efetuando push para Docker Registry
for status in client.images.push(repository = image_name , stream = True):
    print(status)