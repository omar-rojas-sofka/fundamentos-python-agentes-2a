from .Agente_taller_15032026 import PseudoAgenteTaller
from .Agente_taller_15032026 import Historial

class agenteAdmin(PseudoAgente):
    def __init__(self, nombre: str = "Athena"):
        ## se invocxa al constructor del padre 
        super().__init__(nombre)

    def gestionar_historial(self, op: str, rol: str) -> str | list[Historial]:
        if op == "all":
            mensaje = f"[{self.nombre}] Historial completo sin gastar tokens de Admnistrador"
            self.registrar_log("historial  - all", rol, mensaje)
            return self.historial_chat
        if op == "clear":
            mensaje = f"[{self.nombre}] Historial borrado  sin gastar tokens de Admnistrador"
            self.registrar_log("historial - clear", rol, mensaje)
            self.historial_chat.clear()
            return mensaje