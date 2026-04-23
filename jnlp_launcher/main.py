import tkinter as tk
import sys
from logger_config import setup_logger
from gui import JnlpLauncherApp

def main():
    # Configura o logger global
    logger = setup_logger()

    try:
        root = tk.Tk()
        app = JnlpLauncherApp(root)
        logger.info("Interface gráfica iniciada.")
        root.mainloop()
    except Exception as e:
        logger.exception("Erro fatal na aplicação")
        # Se a GUI não pôde ser iniciada, mostra o erro no console e no log
        print(f"Erro crítico: {e}. Verifique o arquivo de log em %APPDATA%\\JNLPLauncher\\logs\\launcher.log")
        sys.exit(1)

if __name__ == "__main__":
    main()
