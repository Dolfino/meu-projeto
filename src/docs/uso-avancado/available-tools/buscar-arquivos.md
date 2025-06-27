# search_files

A ferramenta `search_files` realiza buscas por expressões regulares (regex) em múltiplos arquivos dentro do workspace do seu projeto. Por questões de segurança, não pode buscar fora do diretório atual do workspace. Ela ajuda o Roo a localizar padrões de código, texto ou outros conteúdos específicos em toda a base de código, com resultados contextuais.

---

## Parâmetros

A ferramenta aceita estes parâmetros:

- `path` (obrigatório): O caminho do diretório onde buscar, relativo ao diretório atual do workspace. A busca é limitada ao workspace.
- `regex` (obrigatório): O padrão de expressão regular para buscar (usa sintaxe de regex do Rust)
- `file_pattern` (opcional): Padrão glob para filtrar arquivos (ex: '*.ts' para arquivos TypeScript)

---

## Funcionalidade

Esta ferramenta busca em arquivos de um diretório especificado usando expressões regulares, mostrando cada correspondência com o contexto ao redor. É como ter um poderoso recurso de "Buscar em Arquivos" que funciona em toda a estrutura do projeto.

---

## Quando é usada?

- Quando o Roo precisa encontrar onde funções ou variáveis específicas são usadas
- Quando o Roo ajuda com refatoração e precisa entender padrões de uso
- Quando o Roo precisa localizar todas as instâncias de um padrão de código específico
- Quando o Roo busca texto em múltiplos arquivos com capacidade de filtragem

---

## Principais características

- Busca em múltiplos arquivos em uma única operação usando Ripgrep de alta performance
- Mostra o contexto ao redor de cada correspondência (1 linha antes e depois)
- Filtra arquivos por tipo usando padrões glob (ex: apenas arquivos TypeScript)
- Fornece números de linha para fácil referência
- Usa padrões regex poderosos para buscas precisas
- Limita automaticamente a saída a 300 resultados com notificação
- Trunca linhas maiores que 500 caracteres com marcador "[truncated...]"
- Combina inteligentemente correspondências próximas em blocos únicos para melhor legibilidade

---

## Limitações

- Funciona melhor com arquivos de texto (não é eficaz para arquivos binários como imagens)
- Performance pode diminuir em bases de código extremamente grandes
- Usa sintaxe de regex do Rust, que pode diferir levemente de outras implementações de regex
- Não pode buscar dentro de arquivos compactados ou arquivados
- O tamanho padrão do contexto é fixo (1 linha antes e depois)
- Pode exibir tamanhos de contexto variáveis quando correspondências estão próximas devido ao agrupamento de resultados
- Por segurança, as buscas são estritamente limitadas ao workspace atual e não podem acessar diretórios pai ou outros locais no sistema de arquivos.

---

## Como funciona

Quando a ferramenta `search_files` é invocada, segue este processo:

1. **Validação de parâmetros**: Valida os parâmetros obrigatórios `path` e `regex`
2. **Resolução de caminho**: Converte o caminho relativo para absoluto
3. **Execução da busca**:
   - Usa Ripgrep (rg) para busca de texto de alta performance
   - Aplica filtro de padrão de arquivo se especificado
   - Coleta correspondências com contexto ao redor
4. **Formatação de resultados**:
   - Formata resultados com caminhos de arquivo, números de linha e contexto
   - Exibe 1 linha de contexto antes e depois de cada correspondência
   - Estrutura a saída para fácil legibilidade
   - Limita resultados a no máximo 300 correspondências com notificação
   - Trunca linhas maiores que 500 caracteres
   - Combina correspondências próximas em blocos contíguos

---

## Formato dos resultados

Os resultados da busca incluem:

- Caminhos relativos dos arquivos para cada arquivo correspondente (prefixado com #)
- Linhas de contexto antes e depois de cada correspondência (1 linha por padrão)
- Números de linha alinhados em 3 espaços seguidos por ` | ` e o conteúdo da linha
- Uma linha separadora (----) após cada grupo de correspondências

Exemplo de formato de saída:
```
# rel/path/to/app.ts
 11 |   // Alguma lógica de processamento aqui
 12 |   // TODO: Implementar tratamento de erros
 13 |   return processedData;
----

# Mostrando os primeiros 300 de 300+ resultados. Use uma busca mais específica se necessário.
```

Quando ocorrem correspondências próximas umas das outras, são mescladas em um único bloco em vez de mostradas como resultados separados:

```
# rel/path/to/auth.ts
 13 | // Algum código aqui
 14 | // TODO: Adicionar validação adequada
 15 | function validateUser(credentials) {
 16 |   // TODO: Implementar rate limiting
 17 |   return checkDatabase(credentials);
----
```

---

## Exemplos de uso

- Quando solicitado a refatorar uma função, o Roo primeiro busca todos os lugares onde a função é usada para garantir mudanças abrangentes.
- Ao investigar bugs, o Roo busca por padrões similares para identificar problemas relacionados em toda a base de código.
- Ao abordar dívida técnica, o Roo localiza todos os comentários TODO no projeto.
- Ao analisar dependências, o Roo encontra todas as importações de um módulo específico.

---

## Exemplos de utilização

Buscando comentários TODO em todos os arquivos JavaScript:
```
<search_files>
<path>src</path>
<regex>TODO|FIXME</regex>
<file_pattern>*.js</file_pattern>
</search_files>
```

Encontrando todos os usos de uma função específica:
```
<search_files>
<path>.</path>
<regex>function\s+calculateTotal</regex>
<file_pattern>*.{js,ts}</file_pattern>
</search_files>
```

Buscando um padrão específico de importação em todo o projeto:
```
<search_files>
<path>.</path>
<regex>import\s+.*\s+from\s+['"]@components/</regex>
</search_files>
