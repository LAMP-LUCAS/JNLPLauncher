import subprocess
import logging
import os
from pathlib import Path

# Obtém o logger configurado para este módulo
logger = logging.getLogger("JNLPLauncher.launcher")

def launch_jnlp(file_path: str) -> bool:
    """
    Executa 'javaws <arquivo.jnlp>'.
    Retorna True se o processo foi iniciado com sucesso, False caso contrário.
    Todos os erros são registrados no log.
    """
    path = Path(file_path)

    # Verificações iniciais
    if not path.exists():
        logger.error(f"Arquivo não encontrado: {file_path}")
        return False

    if path.suffix.lower() != ".jnlp":
        logger.warning(f"Extensão inesperada: {path.suffix}. Continuando, mas pode não funcionar.")

    # Verifica se o javaws está disponível no PATH
    try:
        # No Windows, 'where' é mais confiável; usamos 'javaws' diretamente
        subprocess.run(["javaws", "-help"], capture_output=True, check=False, timeout=5)
    except FileNotFoundError:
        logger.critical("javaws não encontrado no PATH. Instale o Java Runtime Environment (JRE).")
        return False
    except Exception as e:
        logger.error(f"Erro ao verificar javaws: {e}")

    # Comando a executar
    cmd = ["javaws", str(path.absolute())]
    logger.info(f"Executando: {' '.join(cmd)}")

    try:
        # Popen sem esperar – o javaws será executado em segundo plano
        subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True  # desvincula do terminal (Windows)
        )
        logger.info(f"javaws iniciado com sucesso para {path.name}")
        return True
    except Exception as e:
        logger.exception("Falha ao iniciar o javaws")
        return False
