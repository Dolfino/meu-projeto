# new_task

A ferramenta `new_task` cria subtarefas com modos especializados mantendo uma relação pai-filho. Ela divide projetos complexos em partes gerenciáveis, cada uma operando no modo mais adequado para o trabalho específico.

---

## Parâmetros

A ferramenta aceita estes parâmetros:

- `mode` (obrigatório): O slug do modo para iniciar a nova tarefa (ex: "code", "ask", "architect")
- `message` (obrigatório): A mensagem inicial ou instruções para esta nova tarefa

---

## O que faz

Esta ferramenta cria uma nova instância de tarefa com um modo inicial especificado e mensagem inicial. Permite que fluxos complexos sejam divididos em subtarefas com seu próprio histórico de conversa. Tarefas pai são pausadas durante a execução da subtarefa e retomadas quando a subtarefa é concluída, com os resultados transferidos de volta para a tarefa pai.

---

## Quando é usada?

- Para dividir projetos complexos em subtarefas separadas e focadas
- Quando diferentes aspectos de uma tarefa requerem modos especializados distintos
- Quando diferentes fases do trabalho se beneficiam de separação de contexto
- Para organizar fluxos de trabalho de desenvolvimento multifásicos

---

## Principais recursos

- Cria subtarefas com seu próprio histórico de conversa e modo especializado
- Pausa tarefas pai para retomada posterior
- Mantém relações hierárquicas de tarefas para navegação
- Transfere resultados de volta para tarefas pai após conclusão
- Suporta segregação de fluxo de trabalho para projetos complexos
- Permite que diferentes partes de um projeto usem modos otimizados para trabalhos específicos
- Requer aprovação explícita do usuário para criação de tarefas
- Fornece transição clara de tarefas na interface

---

## Limitações

- Não pode criar tarefas com modos que não existem
- Requer aprovação do usuário antes de criar cada nova tarefa
- A interface pode ficar complexa com subtarefas profundamente aninhadas
- Subtarefas herdam certas configurações de workspace e extensão das tarefas pai
- Pode exigir reestabelecimento de contexto ao alternar entre tarefas profundamente aninhadas
- A conclusão da tarefa precisa de sinalização explícita para retornar corretamente às tarefas pai

---

## Como funciona

Quando a ferramenta `new_task` é invocada, segue este processo:

1. **Validação de parâmetros**:
   - Valida os parâmetros obrigatórios `mode` e `message`
   - Verifica se o modo solicitado existe no sistema

2. **Gerenciamento da pilha de tarefas**:
   - Mantém uma pilha de tarefas que rastreia todas as tarefas ativas e pausadas
   - Preserva o modo atual para retomada posterior
   - Define a tarefa pai como pausada

3. **Gerenciamento de contexto da tarefa**:
   - Cria um novo contexto de tarefa com a mensagem fornecida
   - Atribui identificadores únicos taskId e instanceId para gerenciamento de estado
   - Captura dados de telemetria sobre uso da ferramenta e ciclos de vida de tarefas

4. **Troca de modo e integração**:
   - Alterna para o modo especificado com papel e capacidades apropriados
   - Inicializa a nova tarefa com a mensagem fornecida
   - Integra com a paleta de comandos e ações de código do VS Code

5. **Conclusão da tarefa e transferência de resultados**:
   - Quando a subtarefa é concluída, o resultado é passado de volta para a tarefa pai via `finishSubTask()`
   - A tarefa pai é retomada em seu modo original
   - O histórico da tarefa e métricas de uso de tokens são atualizados
   - O evento `taskCompleted` é emitido com dados de performance

---

## Exemplos de uso

- Quando um desenvolvedor front-end precisa arquitetar um novo recurso, implementar o código e documentá-lo, pode criar tarefas separadas para cada fase com resultados fluindo de uma fase para outra.
- Ao depurar um problema antes de implementar uma correção, a tarefa de depuração pode documentar descobertas que são passadas para a tarefa de implementação.
- Ao desenvolver uma aplicação full-stack, designs de esquema de banco de dados de uma tarefa em modo architect informam detalhes de implementação em uma tarefa subsequente em modo code.
- Ao documentar um sistema após implementação, a tarefa de documentação pode referenciar a implementação concluída enquanto usa recursos específicos de documentação.

---

## Exemplos de uso

Criando uma nova tarefa em modo code:
```
<new_task>
<mode>code</mode>
<message>Implementar um serviço de autenticação de usuário com funcionalidades de login, registro e redefinição de senha.</message>
</new_task>
```

Criando uma tarefa de documentação após conclusão da implementação:
```
<new_task>
<mode>docs</mode>
<message>Criar documentação abrangente da API para o serviço de autenticação que acabamos de construir.</message>
</new_task>
```

Dividindo um recurso complexo em planejamento arquitetural e implementação:
```
<new_task>
<mode>architect</mode>
<message>Projetar o esquema do banco de dados e a arquitetura do sistema para nossa nova plataforma de e-commerce.</message>
</new_task>
