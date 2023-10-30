def menorIntervalo(j, n):
   contador_tarefa = [0] * 26

   for tarefa in j:
      contador_tarefa[ord(tarefa) - ord('A')] += 1

   max_frequencia = max(contador_tarefa)
   num_max_frequencia_tasks = contador_tarefa.count(max_frequencia)

   min_time = (max_frequencia - 1) * (n + 1) + num_max_frequencia_tasks

   return max(min_time, len(j))


# Exemplos
j = ["A","A","A","B","B","B"]
n1 = 2
resultado1 = menorIntervalo(j, n1)  

j = ["A","A","A","B","B","B"]
n2 = 0
resultado2 = menorIntervalo(j, n2)  

j = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n3 = 2
resultado3 = menorIntervalo(j, n3)  

print(resultado1, resultado2, resultado3)
