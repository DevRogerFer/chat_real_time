# Chat em Tempo Real (Cliente-Servidor)

Este projeto é uma aplicação simples de chat em tempo real, construída para demonstrar de forma direta o tráfego de mensagens entre cliente e servidor.

## Objetivo Principal

O objetivo deste projeto não é ser um chat completo de prodção, mas sim mostrar o fluxo básico de comunicação em rede:

- cliente conecta ao servidor
- cliente informa sala e nome
- servidor recebe e redistribui mensagens para os participantes da sala

## Tecnologias Utilizadas

- Python 3
- Socket TCP (`socket`) para comunicação em rede
- Threads (`threading`) para concorrência
- Tkinter para interface grafica do cliente

## Estrutura do Projeto

- `server.py`: inicializa o servidor, gerencia salas em memória e faz o broadcast das mensagens.
- `client.py`: interface gráfica do usuário, conexão com o servidor e envio/recebimento de mensagens.

## Como Executar

1. Inicie o servidor:

```bash
python server.py
```

2. Em outro terminal, inicie um cliente:

```bash
python client.py
```

3. Abra mais instâncias de cliente para simular conversas entre usuários na mesma sala.

## Como Funciona (Resumo)

1. O servidor fica escutando em `localhost:55555`.
2. Ao conectar, o cliente envia nome e sala.
3. O servidor adiciona o cliente na sala correspondente.
4. Toda mensagem recebida é retransmitida para os clientes daquela sala.

## Caracteristicas de Simplicidade

- sem banco de dados
- sem autenticação
- sem criptografia
- sem persistência de histórico

Essas escolhas tornam o código menor e mais fácil de entender para fins de estudo.

## Observação

Este projeto tem foco educacional e de demonstração de conceito (proof of concept). Para uso real em produção, seriam necessários mecanismos de segurança, tratamento robusto de erros e arquitetura mais completa.
