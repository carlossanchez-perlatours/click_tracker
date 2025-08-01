#!/usr/bin/env python3
"""
Configuración centralizada del sistema de logging.
"""

import os
import logging
from datetime import datetime
from pathlib import Path


def setup_logger(name="ClickTracker", log_level=logging.INFO):
    """
    Configura y retorna un logger centralizado para toda la aplicación.
    
    Args:
        name: Nombre del logger
        log_level: Nivel de logging (por defecto INFO)
    
    Returns:
        logging.Logger: Logger configurado
    """
    # Crear directorio logs si no existe
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    # Generar nombre del archivo con timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = logs_dir / f"{timestamp}.log"
    
    # Crear logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Evitar duplicar handlers si ya existe el logger
    if logger.handlers:
        return logger
    
    # Crear handler para archivo
    file_handler = logging.FileHandler(log_filename, encoding='utf-8')
    file_handler.setLevel(log_level)
    
    # Crear handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    
    # Crear formato
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Agregar handlers al logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    # Log inicial
    logger.info(f"Logger configurado. Archivo de log: {log_filename}")
    
    return logger


def get_logger(name="ClickTracker"):
    """
    Obtiene el logger ya configurado o lo configura si no existe.
    
    Args:
        name: Nombre del logger
    
    Returns:
        logging.Logger: Logger configurado
    """
    logger = logging.getLogger(name)
    
    # Si no tiene handlers, configurarlo
    if not logger.handlers:
        return setup_logger(name)
    
    return logger