#!/usr/bin/env python3
"""
Clase ClickTracker para capturar coordenadas de clicks del mouse.
"""

import logging
import threading
import time
from pynput import mouse


class ClickTracker:
    def __init__(self, logger=None):
        """
        Inicializa el tracker de clicks.
        
        Args:
            logger: Logger configurado externamente. Si es None, usa el logger por defecto.
        """
        self.click_count = 0
        self.logger = logger or logging.getLogger(__name__)
        self.listener = None
        self.running = False
        self.timer_thread = None
        
    def on_click(self, x, y, button, pressed):
        """
        Callback que se ejecuta cuando se detecta un click.
        
        Args:
            x, y: Coordenadas del click
            button: Botón presionado
            pressed: True si se presiona, False si se suelta
        """
        if pressed:  # Solo registrar cuando se presiona el botón (no cuando se suelta)
            self.click_count += 1
            coordinates = [int(x), int(y)]
            
            # Determinar qué botón se presionó
            button_name = str(button).replace('Button.', '')
            
            log_message = f"Click {self.click_count} coordenadas: {coordinates} - Botón: {button_name}"
            self.logger.info(log_message)
    
    def start_tracking(self, duration_seconds=None):
        """
        Inicia el seguimiento de clicks.
        
        Args:
            duration_seconds: Si se especifica, el tracking se detendrá después de X segundos.
                            Si es None, el tracking será indefinido hasta Ctrl+C.
        """
        self.running = True
        
        if duration_seconds:
            self.logger.info(f"Iniciando captura de clicks por {duration_seconds} segundos")
            print("=== CLICK TRACKER INICIADO (MODO TEMPORAL) ===")
            print(f"Duración: {duration_seconds} segundos")
            print("El programa se detendrá automáticamente o presiona Ctrl+C")
        else:
            self.logger.info("Iniciando captura de clicks en modo indefinido")
            print("=== CLICK TRACKER INICIADO (MODO INDEFINIDO) ===")
            print("Presiona Ctrl+C para detener el programa")
        
        print("Todos los clicks serán registrados...")
        print("=" * 50)
        
        # Crear listener para el mouse
        self.listener = mouse.Listener(on_click=self.on_click)
        
        try:
            self.listener.start()
            
            # Si hay duración, crear timer
            if duration_seconds:
                self.timer_thread = threading.Timer(duration_seconds, self._timeout_stop)
                self.timer_thread.start()
                self.logger.info(f"Timer iniciado para {duration_seconds} segundos")
            
            # Mantener el programa corriendo
            self.listener.join()
            
        except KeyboardInterrupt:
            self.logger.info("Interrupción por teclado (Ctrl+C) detectada")
            self.stop_tracking()
    
    def _timeout_stop(self):
        """Método interno para detener el tracking por timeout"""
        self.logger.info("Tiempo límite alcanzado - deteniendo captura")
        print(f"\n=== TIEMPO LÍMITE ALCANZADO ===")
        self.stop_tracking()
    
    def stop_tracking(self):
        """Detiene el seguimiento de clicks"""
        if not self.running:
            return
            
        self.running = False
        
        # Cancelar timer si existe
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.cancel()
            self.logger.info("Timer cancelado")
        
        print("\n=== DETENIENDO CLICK TRACKER ===")
        self.logger.info(f"Programa finalizado. Total de clicks registrados: {self.click_count}")
        print(f"Total de clicks registrados: {self.click_count}")
        
        if self.listener:
            self.listener.stop()
    
    def get_click_count(self):
        """Retorna el número total de clicks registrados"""
        return self.click_count
    
    def reset_counter(self):
        """Reinicia el contador de clicks"""
        old_count = self.click_count
        self.click_count = 0
        self.logger.info(f"Contador reiniciado. Clicks anteriores: {old_count}")
        return old_count