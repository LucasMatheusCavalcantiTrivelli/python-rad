# Configura o sistema de logging para registrar eventos
# do sistema em um arquivo (sistema.log).

import logging
from logging import Logger, exception, info  # noqa: F401
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("rad_python")
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    arquivo = LOG_DIR / "sistema.log"
    file_handler = logging.FileHandler(arquivo, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)