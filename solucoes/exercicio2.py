import heapq

def agendaCurso(cursos):
    
    cursos.sort(key=lambda x: x[1])
    
    diaAtual = 0
    filaCurso = []
    
    for duracao, diaFim in cursos:
        
        if diaAtual + duracao <= diaFim:
            diaAtual += duracao
            heapq.heappush(filaCurso, -duracao)  
        elif filaCurso and -filaCurso[0] > duracao:
            diaAtual += duracao + heapq.heappop(filaCurso)
            heapq.heappush(filaCurso, -duracao)
    
    return len(filaCurso)

# Exemplos
cursos1 = [[100,200],[200,1300],[1000,1250],[2000,3200]]
resultado1 = agendaCurso(cursos1)  

cursos2 = [[1,2]]
resultado2 = agendaCurso(cursos2)  

cursos3 = [[3,2],[4,3]]
resultado3 = agendaCurso(cursos3)  

print(resultado1, resultado2, resultado3)
