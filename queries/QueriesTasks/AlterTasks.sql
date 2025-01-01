
UPDATE tarefas SET categoria = %s, descricao = %s, tarefaok = %s
WHERE id = %s
RETURNING (id, 'Alterdado com sucesso!');
