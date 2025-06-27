# Utilizando Modos

Modos no Roo Code são personalidades especializadas que adaptam o comportamento do assistente à sua tarefa atual. Cada modo oferece diferentes capacidades, conhecimentos e níveis de acesso para ajudar em objetivos específicos.

:::info Modelos Persistentes
Cada modo lembra o último modelo usado. Ao alternar modos, o Roo seleciona automaticamente esse modelo. Atribua modelos diferentes a modos distintos (ex: Gemini 2.5 Preview para `🏗️ Architect`, Claude Sonnet 3.7 para `💻 Code`) e o Roo alternará entre eles automaticamente.

O modo selecionado persiste entre sessões - o Roo lembra qual modo estava ativo quando você retornar.
:::

---

## Por que Usar Diferentes Modos?

- **Especialização:** Assistência específica para cada tarefa
- **Segurança:** Evita modificações acidentais em arquivos
- **Foco:** Respostas otimizadas para a atividade atual
- **Produtividade:** Transição suave entre planejamento, implementação e depuração

---

## Alternando Entre Modos

Quatro formas de alternar modos:

1. **Menu suspenso:** Clique no seletor à esquerda do campo de entrada

   <img src="/img/using-modes/using-modes.png" alt="Usando o menu suspenso para alternar modos" width="400" />

2. **Comando de barra:** Digite `/architect`, `/ask`, `/debug`, `/code` ou `/orchestrator` no início da mensagem. Isso alterna o modo e limpa o campo.

   <img src="/img/using-modes/using-modes-1.png" alt="Usando comandos de barra para alternar modos" width="400" />

3. **Atalho de teclado:** Use o atalho abaixo conforme seu sistema operacional. Cada pressionamento alterna entre os modos disponíveis.

    | Sistema Operacional | Atalho |
    |---------------------|--------|
    | macOS | ⌘ + . |
    | Windows | Ctrl + . |
    | Linux | Ctrl + . |

4. **Sugestões:** Clique em sugestões de alternância que o Roo oferecer quando apropriado

    <img src="/img/using-modes/using-modes-2.png" alt="Aceitando sugestão de alternância de modo do Roo" width="400" />

---

## Modos Integrados

### Modo Código (Padrão)

| Aspecto | Detalhes |
|---------|----------|
| **Nome** | `💻 Code` |
| **Descrição** | Engenheiro de software especializado em linguagens, padrões e melhores práticas |
| **Acesso** | Acesso completo a todas ferramentas: `read`, `edit`, `browser`, `command`, `mcp` |
| **Indicado Para** | Desenvolvimento, implementação de features e depuração |
| **Recursos** | Sem restrições de ferramentas para tarefas de codificação |

### Modo Perguntar

| Aspecto | Detalhes |
|---------|----------|
| **Nome** | `❓ Ask` |
| **Descrição** | Assistente técnico focado em respostas completas. Menos inclinado a implementar código sem solicitação explícita. |
| **Acesso** | Acesso limitado: `read`, `browser`, `mcp` (não edita arquivos ou executa comandos) |
| **Indicado Para** | Explicações técnicas, exploração de conceitos e aprendizado |
| **Recursos** | Respostas detalhadas com diagramas, sem modificar seu projeto |

### Modo Arquitetura

| Aspecto | Detalhes |
|---------|----------|
| **Nome** | `🏗️ Architect` |
| **Descrição** | Especialista em planejamento e design de sistemas |
| **Acesso** | `read`, `browser`, `mcp` e `edit` restrito (apenas arquivos markdown) |
| **Indicado Para** | Design de sistemas e discussões arquiteturais |
| **Recursos** | Abordagem estruturada desde coleta de informações até planejamento detalhado |

### Modo Depuração

| Aspecto | Detalhes |
|---------|----------|
| **Nome** | `🪲 Debug` |
| **Descrição** | Especialista em solução sistemática de problemas |
| **Acesso** | Acesso completo a todas ferramentas |
| **Indicado Para** | Identificação e correção de bugs complexos |
| **Recursos** | Abordagem metódica: análise, redução de possibilidades e correção com confirmação |

### Modo Orquestrador (Boomerang)

| Aspecto | Detalhes |
|---------|----------|
| **Nome** | `🪃 Orchestrator` |
| **Descrição** | Orquestrador estratégico que divide tarefas complexas e delega a modos especializados. Veja [Tarefas Boomerang](/features/boomerang-tasks). |
| **Acesso** | Sem acesso direto (usa `new_task` para delegar) |
| **Indicado Para** | Gerenciamento de projetos multi-etapas e automação |
| **Recursos** | Usa [`new_task`](/advanced-usage/available-tools/new-task) para delegar subtarefas |

---

## Modos Adicionais

Modos especializados adicionais podem estar disponíveis conforme configuração, incluindo Teste, Engenheiro de Design, Engenheiro de Release, Tradutor, Corretor de Issues, entre outros. Consulte o seletor de modos para a lista completa.

---

## Personalizando Modos

Adapte o comportamento do Roo Code criando ou customizando modos. Defina acesso a ferramentas, permissões de arquivo e instruções específicas. Veja [Documentação de Modos Customizados](/features/custom-modes).

### Grupos de Ferramentas

Cada grupo oferece capacidades específicas:
- **`read`**: Leitura e busca em arquivos
- **`edit`**: Modificação e criação de arquivos
- **`browser`**: Navegação e busca na web
- **`command`**: Execução de comandos no terminal
- **`mcp`**: Interações com servidores MCP

Para detalhes sobre ferramentas, consulte [Documentação de Ferramentas](/advanced-usage/available-tools/tool-use-overview).
