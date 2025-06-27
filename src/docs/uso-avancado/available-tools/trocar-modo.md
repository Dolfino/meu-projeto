# switch_mode

A ferramenta `switch_mode` permite que o Roo alterne entre diferentes modos operacionais, cada um com capacidades especializadas para tipos específicos de tarefas. Isso permite transições perfeitas entre modos como Code, Architect, Ask ou Debug quando a tarefa atual requer diferentes especialidades.

---

## Parâmetros

A ferramenta aceita estes parâmetros:

- `mode_slug` (obrigatório): O slug do modo para o qual alternar (ex: "code", "ask", "architect")
- `reason` (opcional): O motivo para alternar modos, fornecendo contexto para o usuário

---

## Funcionalidade

Esta ferramenta solicita uma mudança de modo quando a tarefa atual seria melhor tratada pelas capacidades de outro modo. Mantém o contexto enquanto ajusta o foco e os conjuntos de ferramentas disponíveis do Roo para corresponder aos requisitos da nova fase da tarefa.

---

## Quando é usado?

- Ao transicionar da coleta de informações para implementação de código
- Ao mudar de codificação para arquitetura ou design
- Quando a tarefa atual requer capacidades disponíveis apenas em um modo diferente
- Quando é necessária expertise especializada para uma fase específica de um projeto complexo

---

## Principais recursos

- Mantém continuidade de contexto entre transições de modo
- Fornece raciocínio claro para recomendações de mudança de modo
- Requer aprovação do usuário para todas as mudanças de modo
- Aplica restrições de grupo de ferramentas específicas para cada modo
- Adapta-se perfeitamente à disponibilidade de ferramentas com base no modo selecionado
- Funciona com modos padrão e personalizados
- Exibe a mudança de modo e o raciocínio na interface
- Usa formatação XML para especificação de parâmetros
- Gerencia restrições de tipo de arquivo específicas para certos modos

---

## Limitações

- Não pode alternar para modos que não existem no sistema
- Requer aprovação explícita do usuário para cada transição de modo
- Não pode usar ferramentas específicas de um modo até que a mudança seja concluída
- Aplica um atraso de 500ms após a mudança de modo para permitir que a alteração entre em vigor
- Alguns modos têm restrições de tipo de arquivo (ex: modo Architect só pode editar arquivos markdown)
- A preservação de modo para retomada aplica-se apenas à funcionalidade `new_task`, não a mudanças gerais de modo

---

## Como funciona

Quando a ferramenta `switch_mode` é invocada, segue este processo:

1. **Validação da solicitação**:
   - Valida que o modo solicitado existe no sistema
   - Verifica se o parâmetro `mode_slug` foi fornecido e é válido
   - Confirma que o usuário já não está no modo solicitado
   - Garante que o parâmetro `reason` (se fornecido) está formatado corretamente

2. **Preparação para transição de modo**:
   - Empacota a solicitação de mudança de modo com o motivo fornecido
   - Apresenta a solicitação de mudança para aprovação do usuário

3. **Ativação do modo (após aprovação do usuário)**:
   - Atualiza a interface para refletir o novo modo
   - Ajusta as ferramentas disponíveis com base na configuração do grupo de ferramentas do modo
   - Aplica o prompt e comportamento específicos do modo
   - Aplica um atraso de 500ms para permitir que a mudança entre em vigor antes de executar a próxima ferramenta
   - Aplica quaisquer restrições de arquivo específicas do modo

4. **Continuação**:
   - Prossegue com a tarefa usando as capacidades do novo modo
   - Mantém o contexto relevante da interação anterior

---

## Associação a grupos de ferramentas

A ferramenta `switch_mode` pertence ao grupo de ferramentas "modes", mas também está incluída na lista de ferramentas "sempre disponíveis". Isso significa:

- Pode ser usada em qualquer modo, independentemente dos grupos de ferramentas configurados
- Está disponível junto com outras ferramentas principais como `ask_followup_question` e `attempt_completion`
- Permite transições de modo a qualquer ponto em um fluxo de trabalho quando os requisitos da tarefa mudam

---

## Estrutura do modo

Cada modo no sistema tem uma estrutura específica:

- `slug`: Identificador único para o modo (ex: "code", "ask")
- `name`: Nome de exibição para o modo (ex: "Code", "Ask")
- `roleDefinition`: A função especializada e capacidades do modo
- `customInstructions`: Instruções opcionais específicas do modo que orientam o comportamento
- `groups`: Grupos de ferramentas disponíveis para o modo com restrições opcionais

---

## Capacidades dos modos

Os modos principais fornecem estas capacidades especializadas:

- **Modo Code**: Focado em tarefas de codificação com acesso total a ferramentas de edição de código
- **Modo Architect**: Especializado em design de sistema e planejamento de arquitetura, limitado a editar apenas arquivos markdown
- **Modo Ask**: Otimizado para responder perguntas e fornecer informações
- **Modo Debug**: Equipado para diagnóstico sistemático de problemas e resolução

---

## Modos personalizados

Além dos modos principais, o sistema suporta modos personalizados específicos do projeto:

- Modos personalizados podem ser definidos com grupos de ferramentas específicos habilitados
- Podem especificar definições de função e instruções personalizadas
- O sistema verifica os modos personalizados primeiro antes de recorrer aos modos principais
- Definições de modos personalizados têm precedência sobre modos principais com o mesmo slug

---

## Restrições de arquivo

Diferentes modos podem ter restrições específicas de tipo de arquivo:

- **Modo Architect**: Só pode editar arquivos com extensão `.md`
- Tentativas de editar tipos de arquivo restritos resultam em um `FileRestrictionError`
- Essas restrições ajudam a impor a separação adequada de preocupações entre modos

---

## Exemplos de uso

- Ao discutir um novo recurso, o Roo alterna do modo Ask para o modo Architect para ajudar a projetar a estrutura do sistema.
- Após concluir o planejamento de arquitetura no modo Architect, o Roo alterna para o modo Code para implementar os recursos projetados.
- Ao encontrar bugs durante o desenvolvimento, o Roo alterna do modo Code para o modo Debug para solução sistemática de problemas.

---

## Exemplos de uso

Alternando para o modo Code para implementação:
```
<switch_mode>
<mode_slug>code</mode_slug>
<reason>Need to implement the login functionality based on the architecture we've discussed</reason>
</switch_mode>
```

Alternando para o modo Architect para design:
```
<switch_mode>
<mode_slug>architect</mode_slug>
<reason>Need to design the system architecture before implementation</reason>
</switch_mode>
```

Alternando para o modo Debug para solução de problemas:
```
<switch_mode>
<mode_slug>debug</mode_slug>
<reason>Need to systematically diagnose the authentication error</reason>
</switch_mode>
```

Alternando para o modo Ask para informações:
```
<switch_mode>
<mode_slug>ask</mode_slug>
<reason>Need to answer questions about the implemented feature</reason>
</switch_mode>
