

INSERT INTO tarefas (id, categoria, descricao, tarefaok) 
  VALUES (%s, %s, %s, %s) 
RETURNING id;
