
SELECT id, categoria, descricao, tarefaok 
FROM TAREFAS
WHERE id LIKE %s 
  AND categoria ILIKE %s
  AND descricao ILIKE %s
  AND tarefaok = %s
FOR SHARE;
