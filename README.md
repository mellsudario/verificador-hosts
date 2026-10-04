# Verificador de Hosts

Script em Python que lê uma lista de hosts (IPs ou domínios) de um arquivo de texto e verifica, usando `ping`, quais deles estão online ou offline. No final, mostra um resumo com a contagem.

## Requisitos

- Python 3 instalado (testado com Python 3.14)
- Windows (o script usa `ping -n`, que é o formato do Windows)
- Conexão com a internet para testar hosts externos
- Nenhuma biblioteca extra: só usa módulos que já vêm com o Python


## Como executar

1. Clone o repositório:

```
git clone https://github.com/SEU-USUARIO/verificador-hosts.git
```

2. Entre na pasta do projeto:

```
cd verificador-hosts
```

3. Rode o script:

```
python verificador.py
```

Importante: execute o comando dentro da pasta do projeto, porque o script procura o `hosts.txt` na pasta onde está rodando.

## Exemplo de saída

```
[ONLINE]  127.0.0.1
[ONLINE]  8.8.8.8
[ONLINE]  google.com
[OFFLINE] 192.0.2.1

Resumo: 3 online, 1 offline
```

O endereço `192.0.2.1` é reservado para documentação e nunca responde, então ele serve de exemplo de host offline.


## Branches

- `main`: versão estável do projeto.
- `feature/resumo`: branch onde foi desenvolvido o resumo de hosts online e offline (já incorporada à `main`).
