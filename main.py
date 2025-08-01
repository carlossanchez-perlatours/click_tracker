#!/usr/bin/env python3
"""
Script principal para ejecutar el tracker de clicks.
"""

import sys
import signal
import argparse
from logger_config import setup_logger
from click_tracker import ClickTracker


# Variable global para el tracker (necesaria para el signal handler)
tracker_instance = None


def signal_handler(signum, frame):
    """Manejador de señales para cierre limpio del programa"""
    print("\nSeñal de interrupción recibida...")
    if tracker_instance:
        tracker_instance.stop_tracking()
    sys.exit(0)


def parse_arguments():
    """
    Parsea los argumentos de línea de comandos.
    
    Returns:
        argparse.Namespace: Argumentos parseados
    """
    parser = argparse.ArgumentParser(
        description="Capturador de clicks del mouse con logging",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python main.py                    # Modo indefinido (Ctrl+C para parar)
  python main.py --seconds 30       # Captura por 30 segundos
  python main.py --seconds 120      # Captura por 2 minutos
        """
    )
    
    parser.add_argument(
        '--seconds', 
        type=int, 
        metavar='X',
        help='Duración en segundos para la captura. Si no se especifica, será indefinida.'
    )
    
    return parser.parse_args()


def validate_arguments(args):
    """
    Valida los argumentos proporcionados.
    
    Args:
        args: Argumentos parseados
        
    Returns:
        bool: True si los argumentos son válidos
    """
    if args.seconds is not None:
        if args.seconds <= 0:
            print("Error: El número de segundos debe ser mayor que 0")
            return False
        elif args.seconds > 86400:  # 24 horas
            print("Advertencia: Duración muy larga (>24 horas). ¿Estás seguro?")
            response = input("Continuar? (s/N): ").lower().strip()
            if response not in ['s', 'si', 'sí', 'y', 'yes']:
                return False
    
    return True


def main():
    """Función principal del programa"""
    global tracker_instance
    
    # Parsear argumentos de línea de comandos
    args = parse_arguments()
    
    # Validar argumentos
    if not validate_arguments(args):
        return 1
    
    # Configurar el logger centralizado
    logger = setup_logger("ClickTracker")
    
    # Configurar manejador de señales para Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        logger.info("=== INICIANDO APLICACIÓN DE CAPTURA DE CLICKS ===")
        
        # Log del modo de ejecución
        if args.seconds:
            logger.info(f"Modo: Temporal ({args.seconds} segundos)")
        else:
            logger.info("Modo: Indefinido (hasta Ctrl+C)")
        
        # Crear instancia del tracker con el logger compartido
        tracker_instance = ClickTracker(logger=logger)
        
        # Iniciar el tracking según el modo
        tracker_instance.start_tracking(duration_seconds=args.seconds)
        
    except KeyboardInterrupt:
        logger.info("Interrupción por teclado detectada en main")
        print("\nPrograma interrumpido por el usuario")
    except Exception as e:
        logger.error(f"Error inesperado: {e}", exc_info=True)
        print(f"Error al ejecutar el programa: {e}")
        return 1
    finally:
        logger.info("=== FINALIZANDO APLICACIÓN ===")
    
    return 0


if __name__ == "__main__":
    exit(main())