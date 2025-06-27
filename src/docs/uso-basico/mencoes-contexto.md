# Menções de Contexto

Menções de contexto são uma forma poderosa de fornecer informações específicas ao Roo Code sobre seu projeto, permitindo tarefas mais precisas e eficientes. Use menções para referenciar arquivos, pastas, problemas e commits Git. As menções começam com o símbolo `@`.

<img src="/img/context-mentions/context-mentions.png" alt="Visão geral de menções de contexto mostrando o menu suspenso com símbolo @" width="600" />

*Visão geral das menções de contexto mostrando o menu suspenso na interface de chat.*

---

## Tipos de Menções

<img src="/img/context-mentions/context-mentions-1.png" alt="Exemplo de menção de arquivo mostrando conteúdo sendo referenciado com @" width="600" />

*Menções de arquivo incluem código diretamente na conversa para referência e análise.*

| Tipo | Formato | Descrição | Exemplo de Uso |
|------|---------|-----------|----------------|
| **Arquivo** | `@/caminho/arquivo.ts` | Inclui conteúdo do arquivo no contexto | "Explique a função em @/src/utils.ts" |
| **Pasta** | `@/caminho/pasta` | Inclui conteúdo de todos os arquivos na pasta (não recursivo) | "Analise o código em @/src/components" |
| **Problemas** | `@problems` | Inclui diagnósticos do painel Problems do VS Code | "@problems Corrija todos os erros" |
| **Terminal** | `@terminal` | Inclui último comando e saída do terminal | "Corrija os erros mostrados em @terminal" |
| **Commit Git** | `@a1b2c3d` | Referencia commit específico por hash | "O que mudou no commit @a1b2c3d?" |
| **Mudanças Git** | `@git-changes` | Mostra alterações não commitadas | "Sugira mensagem para @git-changes" |
| **URL** | `@https://exemplo.com` | Importa conteúdo de websites | "Resuma @https://docusaurus.io/" |

### Menções de Arquivo

<img src="/img/context-mentions/context-mentions-1.png" alt="Exemplo de menção de arquivo mostrando conteúdo com numeração de linhas" width="600" />

*Menções de arquivo incluem código com numeração de linhas para referência precisa.*
| Capacidade | Detalhes |
|------------|---------|
| **Formato** | `@/caminho/arquivo.ts` (sempre comece com `/` da raiz) |
| **Fornece** | Conteúdo completo com numeração de linhas |
| **Suporta** | Arquivos texto, PDF e DOCX (com extração de texto) |
| **Funciona em** | Solicitações iniciais, respostas e mensagens |
| **Limitações** | Arquivos muito grandes podem ser truncados |

### Menções de Pasta

<img src="/img/context-mentions/context-mentions-2.png" alt="Exemplo de menção de pasta mostrando conteúdo de diretório" width="600" />

*Menções de pasta incluem conteúdo de todos os arquivos no diretório.*
| Capacidade | Detalhes |
|------------|---------|
| **Formato** | `@/caminho/pasta` (sem barra final) |
| **Fornece** | Conteúdo de todos os arquivos no diretório |
| **Inclui** | Arquivos texto não-binários (não recursivo) |
| **Melhor para** | Fornecer contexto de múltiplos arquivos |
| **Dica** | Considere limites de contexto para pastas grandes |

### Menção Problems

<img src="/img/context-mentions/context-mentions-3.png" alt="Exemplo de menção problems mostrando painel do VS Code" width="600" />

*Menções problems importam diagnósticos diretamente do painel Problems.*
| Capacidade | Detalhes |
|------------|---------|
| **Formato** | `@problems` |
| **Fornece** | Todos os erros e avisos do painel Problems |
| **Inclui** | Caminhos, linhas e mensagens de erro |
| **Organiza** | Problemas agrupados por arquivo |
| **Melhor para** | Corrigir erros sem cópia manual |

### Menção Terminal
<img src="/img/context-mentions/context-mentions-4.png" alt="Exemplo de menção terminal mostrando saída de comando" width="600" />

*Menções terminal capturam saída recente para depuração.*

| Capacidade | Detalhes |
|------------|---------|
| **Formato** | `@terminal` |
| **Captura** | Último comando e sua saída completa |
| **Preserva** | Estado do terminal (não limpa) |
| **Limitação** | Limitado ao conteúdo visível no buffer |
| **Melhor para** | Depurar erros de build ou analisar saída |

### Menções Git

<img src="/img/context-mentions/context-mentions-5.png" alt="Exemplo de menção commit mostrando detalhes sendo analisados" width="600" />

*Menções Git fornecem detalhes de commits para análise contextual.*
| Tipo | Formato | Fornece | Limitações |
|------|---------|---------|------------|
| **Commit** | `@a1b2c3d` | Mensagem, autor, data e diff completo | Só funciona em repositórios Git |
| **Mudanças** | `@git-changes` | `git status` e diff de alterações | Só funciona em repositórios Git |

### Menções URL
<img src="/img/context-mentions/context-mentions-6.png" alt="Exemplo de menção URL mostrando conteúdo web convertido" width="600" />

*Menções URL importam conteúdo web convertido para Markdown.*

| Capacidade | Detalhes |
|------------|---------|
| **Formato** | `@https://exemplo.com` |
| **Processa** | Usa navegador headless para buscar conteúdo |
| **Limpa** | Remove scripts, estilos e elementos de navegação |
| **Saída** | Converte conteúdo para Markdown |
| **Limitação** | Páginas complexas podem não converter perfeitamente |

---

## Como Usar Menções

1. Digite `@` no campo de chat para abrir sugestões
2. Continue digitando para filtrar ou use setas para navegar
3. Selecione com Enter ou clique
4. Combine múltiplas menções: "Corrija @problems em @/src/component.ts"

O menu sugere automaticamente:
- Arquivos abertos recentemente
- Pastas visíveis
- Commits Git recentes
- Palavras-chave especiais (`problems`, `terminal`, `git-changes`)
- **Todos arquivos abertos** (ignorando configurações de filtro)

Pastas como `node_modules`, `.git`, `dist` e `out` são filtradas automaticamente para reduzir ruído.

---

## Comportamentos Importantes

### Interações com Arquivos Ignorados

| Comportamento | Descrição |
|--------------|-----------|
| **Ignora `.rooignore`** | Menções de arquivos/pastas ignoram `.rooignore` |
| **Ignora `.gitignore`** | Menções de arquivos/pastas ignoram `.gitignore` |
| **Respeita Git** | Menções Git (`@git-changes`, `@commit`) respeitam `.gitignore` |

