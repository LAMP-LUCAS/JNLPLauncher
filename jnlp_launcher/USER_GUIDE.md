# Guia do Usuário - JNLP Launcher

Este guia explica como utilizar o **JNLP Launcher** para abrir suas aplicações Java Web Start.

## O que é o JNLP Launcher?

É uma ferramenta simples que permite selecionar um arquivo `.jnlp` (comumente usado por aplicações do governo, bancos ou sistemas legados) e executá-lo usando o Java instalado no seu computador, sem precisar lidar com o terminal ou comandos complexos.

## Como usar

1. **Abra o aplicativo:** Execute o arquivo `JNLPLauncher.exe`.
2. **Selecione o arquivo:** Clique no botão **"Selecionar .jnlp"**.
3. **Localize seu arquivo:** Na janela que abrir, encontre o arquivo `.jnlp` que deseja executar e clique em "Abrir".
4. **Execute:** Clique no botão **"Executar javaws"**.
5. **Aguarde:** A aplicação Java será iniciada em segundo plano.

## Solução de Problemas

### O botão "Executar javaws" não aparece ou dá erro
Certifique-se de que o **Java (JRE)** está instalado no seu computador. O JNLP Launcher precisa do Java para funcionar.

### Onde encontro os logs de erro?
Se algo der errado, você pode verificar os logs detalhados em:
`%APPDATA%\JNLPLauncher\logs\launcher.log`

Basta colar o caminho acima na barra de endereços do seu Explorador de Arquivos (Windows + E).
