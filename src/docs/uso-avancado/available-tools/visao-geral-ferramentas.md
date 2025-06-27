# Visão Geral do Uso de Ferramentas

O Roo Code implementa um sistema sofisticado de ferramentas que permite aos modelos de IA interagir com seu ambiente de desenvolvimento de forma controlada e segura. Este documento explica como as ferramentas funcionam, quando são chamadas e como são gerenciadas.

---

## Conceitos Básicos

### Grupos de Ferramentas

As ferramentas são organizadas em grupos lógicos baseados em sua funcionalidade:

| Categoria | Propósito | Ferramentas | Uso Comum |
|----------|---------|-------|------------|
| **Grupo Leitura** | Leitura e exploração do sistema de arquivos | [read_file](/advanced-usage/available-tools/read-file), [list_files](/advanced-usage/available-tools/list-files), [list_code_definition_names](/advanced-usage/available-tools/list-code-definition-names) | Exploração e análise de código |
| **Grupo Busca** | Busca de padrões e semântica | [search_files](/advanced-usage/available-tools/search-files), [codebase_search](/advanced-usage/available-tools/codebase-search) | Encontrar padrões e funcionalidades no código |
| **Grupo Edição** | Modificações no sistema de arquivos | [apply_diff](/advanced-usage/available-tools/apply-diff), [insert_content](/advanced-usage/available-tools/insert-content), [search_and_replace](/advanced-usage/available-tools/search-and-replace), [write_to_file](/advanced-usage/available-tools/write-to-file) | Alterações de código e manipulação de arquivos |
| **Grupo Navegador** | Automação web | [browser_action](/advanced-usage/available-tools/browser-action) | Testes e interação web |
| **Grupo Comandos** | Execução de comandos do sistema | [execute_command](/advanced-usage/available-tools/execute-command) | Execução de scripts, construção de projetos |
| **Grupo MCP** | Integração com ferramentas externas | [use_mcp_tool](/advanced-usage/available-tools/use-mcp-tool), [access_mcp_resource](/advanced-usage/available-tools/access-mcp-resource) | Funcionalidades especializadas através de servidores externos |
| **Grupo Fluxo de Trabalho** | Gerenciamento de modos e tarefas | [switch_mode](/advanced-usage/available-tools/switch-mode), [new_task](/advanced-usage/available-tools/new-task), [ask_followup_question](/advanced-usage/available-tools/ask-followup-question), [attempt_completion](/advanced-usage/available-tools/attempt-completion) | Troca de contexto e organização de tarefas |

### Ferramentas Sempre Disponíveis

Certas ferramentas estão acessíveis independentemente do modo atual:

- [ask_followup_question](/advanced-usage/available-tools/ask-followup-question): Coleta informações adicionais dos usuários
- [attempt_completion](/advanced-usage/available-tools/attempt-completion): Sinaliza conclusão de tarefa
- [switch_mode](/advanced-usage/available-tools/switch-mode): Altera modos operacionais
- [new_task](/advanced-usage/available-tools/new-task): Cria subtarefas

---

## Ferramentas Disponíveis

### Ferramentas de Leitura
Estas ferramentas ajudam o Roo a entender seu código e projeto:

- [read_file](/advanced-usage/available-tools/read-file) - Examina o conteúdo de arquivos
- [list_files](/advanced-usage/available-tools/list-files) - Mapeia a estrutura de arquivos do projeto
- [list_code_definition_names](/advanced-usage/available-tools/list-code-definition-names) - Cria um mapa estrutural do seu código

### Ferramentas de Busca
Estas ferramentas ajudam o Roo a encontrar padrões e funcionalidades no código:

- [search_files](/advanced-usage/available-tools/search-files) - Encontra padrões em múltiplos arquivos usando regex
- [codebase_search](/advanced-usage/available-tools/codebase-search) - Realiza buscas semânticas no código indexado

### Ferramentas de Edição
Estas ferramentas ajudam o Roo a fazer alterações no código:

- [apply_diff](/advanced-usage/available-tools/apply-diff) - Faz alterações precisas no código
- [insert_content](/advanced-usage/available-tools/insert-content) - Adiciona novas linhas sem modificar as existentes
- [search_and_replace](/advanced-usage/available-tools/search-and-replace) - Localiza e substitui texto ou padrões regex em um arquivo
- [write_to_file](/advanced-usage/available-tools/write-to-file) - Cria novos arquivos ou reescreve completamente os existentes

### Ferramentas de Navegador
Estas ferramentas ajudam o Roo a interagir com aplicações web:

- [browser_action](/advanced-usage/available-tools/browser-action) - Automatiza interações no navegador

### Ferramentas de Comando
Estas ferramentas ajudam o Roo a executar comandos:

- [execute_command](/advanced-usage/available-tools/execute-command) - Executa comandos e programas do sistema

### Ferramentas MCP
Estas ferramentas ajudam o Roo a conectar com serviços externos:

- [use_mcp_tool](/advanced-usage/available-tools/use-mcp-tool) - Usa ferramentas externas especializadas
- [access_mcp_resource](/advanced-usage/available-tools/access-mcp-resource) - Acessa fontes de dados externas

### Ferramentas de Fluxo de Trabalho
Estas ferramentas ajudam a gerenciar o fluxo de conversa e tarefas:

- [ask_followup_question](/advanced-usage/available-tools/ask-followup-question) - Obtém informações adicionais
- [attempt_completion](/advanced-usage/available-tools/attempt-completion) - Apresenta resultados finais
- [switch_mode](/advanced-usage/available-tools/switch-mode) - Muda para um modo diferente para tarefas especializadas
- [new_task](/advanced-usage/available-tools/new-task) - Cria uma nova subtarefa

---

## Mecanismo de Chamada de Ferramentas

### Lidando com Tarefas Complexas

Para certas operações complexas que requerem múltiplos passos, o Roo não simplesmente as descobre no momento. Em vez disso, segue planos internos predefinidos para garantir consistência e precisão.

Um exemplo principal é criar um novo servidor MCP, identificado internamente por `create_mcp_server`. **Este identificador não representa uma ferramenta que você verá sendo chamada.** Em vez disso, quando você pede ao Roo para criar um servidor, isso dispara este fluxo de trabalho conhecido e multi-etapas.

Este fluxo específico é iniciado pelo Roo usando sua ferramenta interna `fetch_instructions` (com a tarefa `create_mcp_server`) para recuperar um plano detalhado. Este plano então guia o Roo a fazer chamadas para várias ferramentas padrão e documentadas em sequência, como:

*   [`execute_command`](/advanced-usage/available-tools/execute-command) para executar scripts de configuração (ex: `npx @modelcontextprotocol/create-server`).
*   [`write_to_file`](/advanced-usage/available-tools/write-to-file) ou [`apply_diff`](/advanced-usage/available-tools/apply-diff) para criar ou modificar código e arquivos de configuração do servidor.
*   [`ask_followup_question`](/advanced-usage/available-tools/ask-followup-question) para coletar informações necessárias como chaves de API.
*   Outras ferramentas padrão conforme necessário para passos como determinar locais de arquivos ou atualizar entradas de configuração.

Assim, embora a tarefa geral (como `create_mcp_server`) seja complexa, ela é realizada orquestrando inteligentemente as ferramentas padrão disponíveis em seu ambiente. Esta abordagem permite que o Roo execute operações complexas de forma confiável aproveitando as ferramentas documentadas aqui.

### Quando as Ferramentas São Chamadas

As ferramentas são invocadas sob condições específicas:

1. **Requisitos Diretos de Tarefa**
   - Quando ações específicas são necessárias para completar uma tarefa
   - Em resposta a solicitações do usuário
   - Durante fluxos de trabalho automatizados

2. **Disponibilidade Baseada em Modo**
   - Diferentes modos habilitam diferentes conjuntos de ferramentas
   - Mudanças de modo podem alterar a disponibilidade de ferramentas
   - Algumas ferramentas são restritas a modos específicos

3. **Chamadas Dependentes de Contexto**
   - Baseado no estado atual do workspace
   - Em resposta a eventos do sistema
   - Durante tratamento e recuperação de erros

### Processo de Decisão

O sistema usa um processo multi-etapas para determinar a disponibilidade de ferramentas:

1. **Validação de Modo**
   ```typescript
   isToolAllowedForMode(
       tool: string,
       modeSlug: string,
       customModes: ModeConfig[],
       toolRequirements?: Record<string, boolean>,
       toolParams?: Record<string, any>
   )
   ```

2. **Verificação de Requisitos**
   - Verificação de capacidade do sistema
   - Disponibilidade de recursos
   - Validação de permissões

3. **Validação de Parâmetros**
   - Presença de parâmetros obrigatórios
   - Verificação de tipo de parâmetros
   - Validação de valores

---

## Implementação Técnica

### Processamento de Chamada de Ferramentas

1. **Inicialização**
   - Nome da ferramenta e parâmetros são validados
   - Compatibilidade com o modo é verificada
   - Requisitos são confirmados

2. **Execução**
   ```typescript
   const toolCall = {
       type: "tool_call",
       name: chunk.name,
       arguments: chunk.input,
       callId: chunk.callId
   }
   ```

3. **Tratamento de Resultado**
   - Determinação de sucesso/fracasso
   - Formatação do resultado
   - Tratamento de erros

### Segurança e Permissões

1. **Controle de Acesso**
   - Restrições do sistema de arquivos
   - Limitações de execução de comandos
   - Controles de acesso à rede

2. **Camadas de Validação**
   - Validação específica por ferramenta
   - Restrições baseadas em modo
   - Verificações em nível de sistema

---

## Integração com Modos

### Acesso a Ferramentas Baseado em Modo

As ferramentas são disponibilizadas baseadas no modo atual:

- **Modo Código**: Acesso completo a ferramentas de sistema de arquivos, capacidades de edição de código, execução de comandos
- **Modo Pergunta**: Limitado a ferramentas de leitura, capacidades de coleta de informações, sem modificações no sistema de arquivos
- **Modo Arquitetura**: Ferramentas focadas em design, capacidades de documentação, direitos de execução limitados
- **Modos Personalizados**: Podem ser configurados com acesso específico a ferramentas para fluxos de trabalho especializados

### Mudança de Modo

1. **Processo**
   - Preservação do estado atual do modo
   - Atualização da disponibilidade de ferramentas
   - Mudança de contexto

2. **Impacto nas Ferramentas**
   - Mudança no conjunto de ferramentas
   - Ajustes de permissões
   - Preservação de contexto

---

## Melhores Práticas

### Diretrizes de Uso de Ferramentas

1. **Eficiência**
   - Use a ferramenta mais específica para a tarefa
   - Evite chamadas redundantes de ferramentas
   - Agrupe operações quando possível

2. **Segurança**
   - Valide entradas antes de chamar ferramentas
   - Use as permissões mínimas necessárias
   - Siga as melhores práticas de segurança

3. **Tratamento de Erros**
   - Implemente verificação adequada de erros
   - Forneça mensagens de erro significativas
   - Lide com falhas de forma elegante

### Padrões Comuns

1. **Coleta de Informações**
   ```
   [ask_followup_question](/advanced-usage/available-tools/ask-followup-question) → [read_file](/advanced-usage/available-tools/read-file) → [codebase_search](/advanced-usage/available-tools/codebase-search)
   ```

2. **Modificação de Código**
   ```
   [read_file](/advanced-usage/available-tools/read-file) → [apply_diff](/advanced-usage/available-tools/apply-diff) → [attempt_completion](/advanced-usage/available-tools/attempt-completion)
   ```

3. **Gerenciamento de Tarefas**
   ```
   [new_task](/advanced-usage/available-tools/new-task) → [switch_mode](/advanced-usage/available-tools/switch-mode) → [execute_command](/advanced-usage/available-tools/execute-command)
   ```

---

## Tratamento de Erros e Recuperação

### Tipos de Erros

1. **Erros Específicos de Ferramentas**
   - Falhas na validação de parâmetros
   - Erros de execução
   - Problemas de acesso a recursos

2. **Erros de Sistema**
   - Permissão negada
   - Recurso indisponível
   - Falhas de rede

3. **Erros de Contexto**
   - Modo inválido para a ferramenta
   - Requisitos ausentes
   - Inconsistências de estado

### Estratégias de Recuperação

1. **Recuperação Automática**
   - Mecanismos de repetição
   - Opções alternativas
   - Restauração de estado

2. **Intervenção do Usuário**
   - Notificações de erro
   - Sugestões de recuperação
   - Opções de intervenção manual
