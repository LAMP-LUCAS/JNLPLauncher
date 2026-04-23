# JNLP Launcher

Aplicação Python para facilitar o lançamento de arquivos Java Web Start (`.jnlp`) através de uma interface gráfica amigável.

## Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação.
- `gui.py`: Camada de interface com o usuário (Tkinter).
- `launcher.py`: Lógica de execução do comando `javaws`.
- `logger_config.py`: Configuração centralizada de logs.
- `tests/`: Testes automatizados (Unitários, Integração, E2E).

## Requisitos de Desenvolvimento

- Python 3.12+
- Java Runtime Environment (JRE) instalado e `javaws` no PATH do sistema.

## Configuração do Ambiente de Desenvolvimento

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
2. Ative o ambiente virtual:
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
3. Instale as dependências:
   ```bash
   pip install -r jnlp_launcher/requirements.txt
   ```

## Executando os Testes

Para rodar os testes unitários e de integração:
```bash
pytest jnlp_launcher/tests
```

## Geração do Executável

Para gerar o arquivo `.exe` para distribuição no Windows:
```bash
pyinstaller --onefile --windowed --name JNLPLauncher jnlp_launcher/main.py
```
O executável será gerado na pasta `dist/`.

## Logs

Os logs da aplicação são salvos em:
`%APPDATA%\JNLPLauncher\logs\launcher.log`
