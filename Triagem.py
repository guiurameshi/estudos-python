from collections import deque
import time

# Estrutura para armazenar as filas de acordo com o Protocolo de Manchester
filas_hospital = {
    "Vermelho (Emergência)": deque(),
    "Amarelo (Urgente)": deque(),
    "Verde (Pouco Urgente)": deque(),
    "Azul (Não Urgente)": deque()
}

def realizar_triagem(nome, protocolo_cor):
    """Insere o paciente na fila correspondente à sua gravidade."""
    if protocolo_cor in filas_hospital:
        filas_hospital[protocolo_cor].append(nome)
        print(f"🏥 [TRIAGEM] Paciente {nome} classificado com a cor: {protocolo_cor}.")
    else:
        print("❌ Cor de protocolo inválida.")

def chamar_proximo_medico():
    """Chama o próximo paciente respeitando estritamente a prioridade de saúde."""
    for cor, fila in filas_hospital.items():
        if fila:
            paciente = fila.popleft()
            print(f"🩺 [ATENDIMENTO] Médico chama: {paciente} -> Fila: {cor}")
            return
    
    print("✨ [AVISO] Todos os pacientes foram atendidos. Filas vazias!")

# --- SIMULAÇÃO PRÁTICA DO PRONTO-SOCORRO ---
print("--- 🩺 FASE 1: CHEGADA E TRIAGEM DE PACIENTES ---")
realizar_triagem("Ana Silva", "Verde (Pouco Urgente)")
realizar_triagem("Carlos Souza", "Vermelho (Emergência)")
realizar_triagem("Mariana Costa", "Amarelo (Urgente)")
realizar_triagem("José Santos", "Azul (Não Urgente)")
realizar_triagem("Roberto Lima", "Vermelho (Emergência)")

print("\n--- 🩺 FASE 2: INÍCIO DOS ATENDIMENTOS MÉDICOS ---")
for _ in range(6):
    chamar_proximo_medico()
    time.sleep(0.5)