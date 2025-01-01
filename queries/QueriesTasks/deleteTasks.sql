
DELETE FROM tarefas
WHERE id = %s
RETURNING (id, 'Deletado com sucesso!');
