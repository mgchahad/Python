#!/usr/bin/python3
import docker

# Variáveis
image_name = "mchahad:latest"

# Conecta ao Docker utilizando as configurações de socket padrão ou via configuração do seu ambiente
client = docker.from_env()

# Coleta imagem
get_image = client.images.list(image_name)

if len (get_image):
    print("\nRemovendo imagem...")
    image = get_image[0].tags
    print(f"Imagem: {image}")
    client.images.remove(image[0])
 
print("\nAplicando um novo build...")
client.images.build(path = "./", tag = image_name, nocache = True)
    
