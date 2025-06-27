# Instruções Personalizadas

As Instruções Personalizadas permitem que você personalize como o Roo se comporta, fornecendo orientações específicas que moldam respostas, estilo de codificação e processos de tomada de decisão.

:::info Localização dos Arquivos de Instrução
Você pode fornecer instruções personalizadas usando arquivos ou diretórios dedicados dentro do seu workspace. Isso permite melhor organização e controle de versão.

**Instruções para Todo o Workspace:** Aplicam-se a todos os modos no projeto.
*   **Método Preferido: Diretório (`.roo/rules/`)**
    ```
    .
    ├── .roo/
    │   └── rules/          # Regras para todo o workspace
    │       ├── 01-general.md
    │       └── 02-coding-style.txt
    └── ... (outros arquivos do projeto)
    ```
*   **Método Alternativo: Arquivo Único (`.roorules`)**
    ```
    .
    ├── .roorules           # Regras para todo o workspace (arquivo único)
    └── ... (outros arquivos do projeto)
    ```

**Instruções Específicas por Modo:** Aplicam-se apenas a um modo específico (ex: `code`).
*   **Método Preferido: Diretório (`.roo/rules-{modeSlug}/`)**
    ```
    .
    ├── .roo/
    │   └── rules-code/     # Regras para o modo "code"
    │       ├── 01-js-style.md
    │       └── 02-ts-style.md
    └── ... (outros arquivos do projeto)
    ```
*   **Método Alternativo: Arquivo Único (`.roorules-{modeSlug}`)**
    ```
    .
    ├── .roorules-code      # Regras para o modo "code" (arquivo único)
    └── ... (outros arquivos do projeto)
    ```
Os métodos baseados em diretório têm precedência se existirem e contiverem arquivos. Veja [Instruções Nível Workspace](#instruções-nível-workspace) e [Instruções Específicas por Modo](#instruções-específicas-por-modo) para detalhes.
:::

---

## O Que São Instruções Personalizadas?

Instruções Personalizadas definem comportamentos específicos, preferências e restrições além da definição básica de função do Roo. Exemplos incluem estilo de codificação, padrões de documentação, requisitos de teste e diretrizes de fluxo de trabalho.

---

## Configurando Instruções Personalizadas

### Instruções Personalizadas Globais

Estas instruções se aplicam a todos os workspaces e mantêm suas preferências independentemente de qual projeto você está trabalhando.

**Como configurá-las:**

<img src="/img/custom-instructions/custom-instructions.png" alt="Aba Prompts do Roo Code mostrando interface de instruções personalizadas globais" width="600" />
1.  **Abra a Aba Prompts:** Clique no ícone <Codicon name="notebook" /> na barra de menu superior do Roo Code
2.  **Encontre a Seção:** Encontre a seção "Instruções Personalizadas para Todos os Modos"
3.  **Insira as Instruções:** Insira suas instruções na área de texto
4.  **Salve as Alterações:** Clique em "Concluído" para salvar suas alterações

### Instruções Nível Workspace

Estas instruções se aplicam apenas dentro do seu workspace atual, permitindo que você personalize o comportamento do Roo Code para projetos específicos.

#### Instruções para Todo o Workspace via Arquivos/Diretórios

Instruções para todo o workspace se aplicam a todos os modos dentro do projeto atual e podem ser definidas usando arquivos:

*   **Método Preferido: Baseado em Diretório (`.roo/rules/`)**
    *   Crie um diretório chamado `.roo/rules/` na raiz do workspace.
    *   Coloque arquivos de instrução (ex: `.md`, `.txt`) dentro. O Roo Code lê os arquivos recursivamente, anexando seu conteúdo ao prompt do sistema em **ordem alfabética** baseada no nome do arquivo.
    *   Este método tem precedência se o diretório existir e contiver arquivos.
*   **Método Alternativo: Baseado em Arquivo (`.roorules`)**
    *   Se `.roo/rules/` não existir ou estiver vazio, o Roo Code procura por um único arquivo `.roorules` na raiz do workspace.
    *   Se encontrado, seu conteúdo é carregado.

#### Instruções Específicas por Modo

Instruções específicas por modo podem ser definidas de duas maneiras independentes que podem ser usadas simultaneamente:

1.  **Usando a Aba Prompts:**

    <img src="/img/custom-instructions/custom-instructions-2.png" alt="Aba Prompts do Roo Code mostrando interface de instruções personalizadas específicas por modo" width="600" />
    * **Abra a Aba:** Clique no ícone <Codicon name="notebook" /> na barra de menu superior do Roo Code
    * **Selecione o Modo:** Sob o cabeçalho Modos, clique no botão para o modo que deseja personalizar
    * **Insira as Instruções:** Insira suas instruções na área de texto sob "Instruções Personalizadas Específicas por Modo (opcional)"
    * **Salve as Alterações:** Clique em "Concluído" para salvar suas alterações

        :::info Regras Globais de Modo
        Se o modo em si for global (não específico do workspace), quaisquer instruções personalizadas que você definir para ele também se aplicarão globalmente para aquele modo em todos os workspaces.
        :::

2.  **Usando Arquivos/Diretórios de Regras:** Forneça instruções específicas por modo via arquivos:
    *   **Método Preferido: Baseado em Diretório (`.roo/rules-{modeSlug}/`)**
        *   Crie um diretório chamado `.roo/rules-{modeSlug}/` (ex: `.roo/rules-docs-writer/`) na raiz do workspace.
        *   Coloque arquivos de instrução dentro (carregamento recursivo). Os arquivos são lidos e anexados ao prompt do sistema em **ordem alfabética** por nome de arquivo.
        *   Este método tem precedência sobre o método alternativo baseado em arquivo para o modo específico se o diretório existir e contiver arquivos.
    *   **Método Alternativo: Baseado em Arquivo (`.roorules-{modeSlug}`)**
        *   Se `.roo/rules-{modeSlug}/` não existir ou estiver vazio, o Roo Code procura por um único arquivo `.roorules-{modeSlug}` (ex: `.roorules-code`) na raiz do workspace.
        *   Se encontrado, seu conteúdo é carregado para aquele modo.

Instruções da Aba Prompts, do diretório/arquivo específico por modo e do diretório/arquivo para todo o workspace são todos combinados. Veja a seção abaixo para a ordem exata.

---

## Como as Instruções São Combinadas

As instruções são colocadas no prompt do sistema neste formato exato:

```
====
USER'S CUSTOM INSTRUCTIONS

The following additional instructions are provided by the user, and should be followed to the best of your ability without interfering with the TOOL USE guidelines.

[Preferência de Idioma (se definida)]

[Instruções Globais (da Aba Prompts)]

[Instruções Específicas por Modo (da Aba Prompts para o modo atual)]

Instruções Específicas por Modo (de Arquivos/Diretórios):
[Conteúdo dos arquivos em .roo/rules-{modeSlug}/ (se o diretório existir e não estiver vazio)]
[Conteúdo do arquivo .roorules-{modeSlug} (se .roo/rules-{modeSlug}/ não existir ou estiver vazio, e o arquivo existir)]

Instruções para Todo o Workspace (de Arquivos/Diretórios):
[Conteúdo dos arquivos em .roo/rules/ (se o diretório existir e não estiver vazio)]
[Conteúdo do arquivo .roorules (se .roo/rules/ não existir ou estiver vazio, e o arquivo existir)]

====
```

*Nota: A ordem exata garante que instruções mais específicas (nível modo) apareçam antes de instruções mais gerais (workspace-wide), e regras baseadas em diretório tenham precedência sobre métodos alternativos baseados em arquivo dentro de cada nível.*

---

## Regras sobre Arquivos .rules

* **Localização do Arquivo:** O método preferido usa diretórios dentro de `.roo/` (`.roo/rules/` e `.roo/rules-{modeSlug}/`). O método alternativo usa arquivos únicos (`.roorules` e `.roorules-{modeSlug}`) localizados diretamente na raiz do workspace.
* **Arquivos Vazios:** Arquivos de regra vazios ou ausentes são ignorados silenciosamente
* **Cabeçalhos de Origem:** O conteúdo de cada arquivo de regra é incluído com um cabeçalho indicando sua origem
* **Interação de Regras:** Regras específicas por modo complementam regras globais em vez de substituí-las

---

## Exemplos de Instruções Personalizadas

* "Sempre use espaços para indentação, com largura de 4 espaços"
* "Use camelCase para nomes de variáveis"
* "Escreva testes unitários para todas as novas funções"
* "Explique seu raciocínio antes de fornecer código"
* "Foque na legibilidade e manutenibilidade do código"
* "Priorize usar a biblioteca mais comum na comunidade"
* "Ao adicionar novos recursos a sites, garanta que sejam responsivos e acessíveis"

:::tip Dica Profissional: Padrões de Equipe Baseados em Arquivos
Ao trabalhar em ambientes de equipe, usar a estrutura de diretório `.roo/rules/` (e potencialmente diretórios `.roo/rules-{modeSlug}/` para modos específicos) sob controle de versão é a maneira recomendada de padronizar o comportamento do Roo em toda sua equipe. Isso permite melhor organização de múltiplos arquivos de instrução e garante estilo de código consistente, práticas de documentação e fluxos de trabalho de desenvolvimento. O método mais antigo de arquivo `.roorules` ainda pode ser usado, mas oferece menos flexibilidade.
:::

---

## Combinando com Modos Personalizados

Para personalização avançada, combine com [Modos Personalizados](/features/custom-modes) para criar ambientes especializados com acesso específico a ferramentas, restrições de arquivos e instruções personalizadas.
