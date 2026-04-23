import logging
import os
import sys
from pathlib import Path

def setup_logger(app_name: str = "JNLPLauncher") -> logging.Logger:
    """
    Configura e retorna um logger que grava em arquivo (dentro de %APPDATA%)
    e também exibe no console (para debug).
    """
    logger = logging.getLogger(app_name)
    logger.setLevel(logging.DEBUG)

    # Diretório de logs seguro no Windows
    log_dir = Path(os.environ.get("APPDATA", os.path.expanduser("~"))) / app_name / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "launcher.log"

    # Formato das mensagens
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Handler para arquivo (sempre ativo)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Handler para console (apenas INFO para não poluir, mas útil em desenvolvimento)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.info(f"Logger iniciado. Arquivo de log: {log_file}")
    return logger
