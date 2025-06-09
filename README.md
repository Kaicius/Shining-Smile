# Projeto de uma Clínica de Odontologia

### Este projeto foi desenvolvido como trabalho final da turma de Desenvolvimento de Sistemas da escola SENAI Morvan Figueiredo em 2024.
__________________________________
## 💡 Sobre o projeto
O sistema foi desenvolvido para a gestão de uma clínica de odontologia, incorporando diversas funcionalidades. Durante dois anos de curso, novas experiências foram adquiridas no desenvolvimento de códigos ao longo dos semestres. No início do 4º semestre, o projeto foi iniciado e, ao final desse mesmo semestre, foi concluído e apresentado.
__________________________________
## ⚙️ Requisitos
Para ver os requisitos clique no link abaixo:
<br><br>
[Requisitos](https://github.com/Kaicius/Shining-Smile/blob/main/Requirements.txt)
__________________________________
## 🛠️ Tecnologias utilizadas
#### - Django: Framework principal para backend.
#### - HTML, CSS e JavaScript: Para a criação de interfaces interativas e responsivas.
#### - Bootstrap: Para estilização e design.
#### - SQLite: Banco de dados para armazenar informações de usuários e consultas.
#### - Django-Allauth: Ultilizado para fazer o login, cadastro, reset de senha e login com Google
__________________________________
## 🚀 Funcionalidades principais
### Agendamento de consultas:

#### - Pacientes podem agendar consultas diretamente pelo sistema.
#### - Restrições para evitar conflitos de horário.
#### - Sistema de geração automática de credencial para médicos.

### Gestão de usuários:

#### - Separação de perfis: administrador, médicos e pacientes.
#### - Permissões distintas para cada tipo de usuário.
__________________________________
## 📚 Como executar o projeto

### Clone este repositório:

``` git clone https://github.com/Kaicius/Shining-Smile.git ```

### Instale as dependências:

``` pip install -r requirements.txt ```

### Execute as migrações para configurar o banco de dados:

``` python manage.py migrate ```

### Inicie o servidor:

``` python manage.py runserver ```

### Acesse o sistema no navegador pelo endereço: http://127.0.0.1:8000

## Para fazer o login do google funcionar acesse o [console](https://console.cloud.google.com/projectselector2/apis/credentials?hl=pt-br&authuser=4&supportedpurview=project) crie a credencial e a tela de permissão OAuth e substitua os campos nas settings.py
