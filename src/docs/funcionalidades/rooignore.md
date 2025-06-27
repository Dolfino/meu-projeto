---
sidebar_label: .rooignore
---

# Usando .rooignore para Controlar Acesso a Arquivos

O arquivo `.rooignore` é um recurso importante para gerenciar a interação do Roo Code com os arquivos do seu projeto. Ele permite especificar arquivos e diretórios que o Roo não deve acessar ou modificar, similar a como `.gitignore` funciona para o Git.

---

## O que é `.rooignore`?

*   **Propósito**: Proteger informações sensíveis, prevenir alterações acidentais em artefatos de build ou arquivos grandes, e definir o escopo operacional do Roo dentro do seu workspace.
*   **Como usar**: Crie um arquivo chamado `.rooignore` no diretório raiz do seu workspace no VS Code. Liste padrões neste arquivo para informar ao Roo quais arquivos e diretórios ignorar.
*   **Escopo**: `.rooignore` afeta tanto as ferramentas do Roo quanto menções de contexto (como anexos `@directory`).

O Roo monitora ativamente o arquivo `.rooignore`. Qualquer alteração que você fizer é recarregada automaticamente, garantindo que o Roo sempre use as regras mais recentes. O próprio arquivo `.rooignore` é sempre implicitamente ignorado, então o Roo não pode alterar suas próprias regras de acesso.

---

## Sintaxe dos Padrões

A sintaxe para `.rooignore` é idêntica à do `.gitignore`. Aqui estão exemplos comuns:

*   `node_modules/`: Ignora todo o diretório `node_modules`.
*   `*.log`: Ignora todos os arquivos terminados em `.log`.
*   `config/secrets.json`: Ignora um arquivo específico.
*   `!important.log`: Uma exceção; o Roo *não* ignorará este arquivo específico, mesmo que exista um padrão mais amplo como `*.log`.
*   `build/`: Ignora o diretório `build`.
*   `docs/**/*.md`: Ignora todos os arquivos Markdown no diretório `docs` e seus subdiretórios.

Para um guia completo sobre a sintaxe, consulte a [documentação oficial do Git sobre .gitignore](https://git-scm.com/docs/gitignore).

---

## Como as Ferramentas do Roo Interagem com `.rooignore`

As regras do `.rooignore` são aplicadas em várias ferramentas do Roo:

### Aplicação Estrita (Leituras e Gravações)

Estas ferramentas verificam diretamente o `.rooignore` antes de qualquer operação de arquivo. Se um arquivo for ignorado, a operação é bloqueada:

*   [`read_file`](/advanced-usage/available-tools/read-file): Não lerá arquivos ignorados.
*   [`write_to_file`](/advanced-usage/available-tools/write-to-file): Não gravará nem criará novos arquivos ignorados.
*   [`apply_diff`](/advanced-usage/available-tools/apply-diff): Não aplicará diffs em arquivos ignorados.
*   [`insert_content`](/advanced-usage/available-tools/insert-content): Não gravará em arquivos ignorados.
*   [`search_and_replace`](/advanced-usage/available-tools/search-and-replace): Não fará busca e substituição em arquivos ignorados.
*   [`list_code_definition_names`](/advanced-usage/available-tools/list-code-definition-names): Não analisará arquivos ignorados para símbolos de código.

### Descoberta e Listagem de Arquivos

*   **Ferramenta [`list_files`](/advanced-usage/available-tools/list-files) e Anexos `@directory`**: Quando o Roo lista arquivos ou quando você usa anexos `@directory`, os arquivos ignorados são omitidos ou marcados com um símbolo 🔒 (veja "Experiência do Usuário" abaixo). Ambos usam a mesma lógica de filtragem.
*   **Detalhes do Ambiente**: Informações sobre seu workspace (como abas abertas e estrutura do projeto) fornecidas ao Roo são filtradas para excluir ou marcar itens ignorados.

### Menções de Contexto

*   **Anexos `@directory`**: O conteúdo do diretório respeita os padrões do `.rooignore`. Arquivos ignorados são filtrados ou marcados com o prefixo `[🔒]` dependendo da configuração `showRooIgnoredFiles`.
*   **Menções de Arquivo Único**: Arquivos ignorados retornam "(Arquivo ignorado por .rooignore)" em vez do conteúdo.

### Execução de Comandos

*   **Ferramenta [`execute_command`](/advanced-usage/available-tools/execute-command)**: Esta ferramenta verifica se um comando (de uma lista predefinida como `cat` ou `grep`) tem como alvo um arquivo ignorado. Se sim, a execução é bloqueada.

---

## Limitações e Escopo Principais

*   **Centrado no Workspace**: As regras do `.rooignore` se aplicam **apenas a arquivos e diretórios dentro da raiz do workspace do VS Code atual**. Arquivos fora deste escopo não são afetados.
*   **Especificidade do [`execute_command`](/advanced-usage/available-tools/execute-command)**: A proteção para `execute_command` é limitada a uma lista predefinida de comandos de leitura de arquivos. Scripts personalizados ou utilitários incomuns podem não ser detectados.
*   **Não é um Sandbox Completo**: `.rooignore` é uma ferramenta poderosa para controlar o acesso a arquivos do Roo por meio de suas ferramentas, mas não cria um sandbox em nível de sistema.

---

## Experiência do Usuário e Notificações

*   **Indicador Visual (🔒)**: Em listagens de arquivos e anexos `@directory`, arquivos ignorados pelo `.rooignore` podem ser marcados com um símbolo de cadeado (🔒), dependendo da configuração `showRooIgnoredFiles` (padrão é `true`).
*   **Mensagens de Ignorar**: Menções de arquivo único retornam "(Arquivo ignorado por .rooignore)" em vez do conteúdo.
*   **Mensagens de Erro**: Se uma operação de ferramenta for bloqueada, o Roo recebe um erro: `"Acesso a [caminho_do_arquivo] está bloqueado pelas configurações do arquivo .rooignore. Você deve tentar continuar a tarefa sem usar este arquivo, ou pedir ao usuário para atualizar o arquivo .rooignore."`
*   **Notificações no Chat**: Você normalmente verá uma notificação na interface de chat do Roo quando uma ação for bloqueada devido ao `.rooignore`.

Este guia ajuda você a entender o recurso `.rooignore`, suas capacidades e limitações atuais, para que você possa gerenciar efetivamente a interação do Roo com sua base de código.
