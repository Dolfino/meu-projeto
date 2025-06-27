# read_file

A ferramenta `read_file` examina o conteúdo de arquivos em um projeto. Permite que o Roo entenda código, arquivos de configuração e documentação para fornecer melhor assistência.

:::info Suporte a Múltiplos Arquivos
Quando o recurso experimental [Leitura Simultânea de Arquivos](/features/concurrent-file-reads) está ativado, esta ferramenta pode ler vários arquivos simultaneamente usando um formato de parâmetro XML aprimorado. Isso melhora significativamente a eficiência para tarefas que requerem análise de vários arquivos relacionados.
:::

---

## Parâmetros

A ferramenta aceita parâmetros em dois formatos dependendo da sua configuração:

### Formato Padrão (Arquivo Único)

- `path` (obrigatório): O caminho do arquivo a ser lido, relativo ao diretório de trabalho atual
- `start_line` (opcional): O número da linha inicial para leitura (indexação baseada em 1)
- `end_line` (opcional): O número da linha final para leitura (base 1, inclusivo)

:::note Formato Legado
Embora os parâmetros de arquivo único (`path`, `start_line`, `end_line`) ainda sejam suportados para compatibilidade, recomendamos usar o formato mais novo `args` para consistência e compatibilidade futura.
:::

### Formato Aprimorado (Múltiplos Arquivos - Experimental)

Quando [Leitura Simultânea de Arquivos](/features/concurrent-file-reads) está ativada, a ferramenta aceita um parâmetro `args` contendo múltiplas entradas de arquivo:

- `args` (obrigatório): Contêiner para múltiplas especificações de arquivo
  - `file` (obrigatório): Especificação de arquivo individual
    - `path` (obrigatório): O caminho do arquivo a ser lido
    - `line_range` (opcional): Especificação de intervalo de linhas (ex: "1-50" ou "100-150")

---

## O Que Faz

Esta ferramenta lê o conteúdo de um arquivo especificado e o retorna com números de linha para fácil referência. Pode ler arquivos inteiros ou seções específicas, e até extrair texto de PDFs e documentos Word.

---

## Quando é Usada?

- Quando o Roo precisa entender a estrutura de código existente
- Quando o Roo precisa analisar arquivos de configuração
- Quando o Roo precisa extrair informações de arquivos de texto
- Quando o Roo precisa ver o código antes de sugerir alterações
- Quando números de linha específicos precisam ser referenciados em discussões

---

## Principais Recursos

- Exibe conteúdo de arquivo com números de linha para fácil referência
- Pode ler porções específicas de arquivos especificando intervalos de linhas
- Extrai texto legível de arquivos PDF e DOCX
- Trunca automaticamente arquivos de texto grandes quando nenhum intervalo de linhas é especificado, mostrando o início do arquivo
- Fornece resumos de métodos com intervalos de linhas para arquivos de código grandes truncados
- Transmite eficientemente apenas os intervalos de linhas solicitados para melhor desempenho
- Facilita a discussão de partes específicas do código com numeração de linhas
- **Suporte a múltiplos arquivos** (experimental): Leia vários arquivos simultaneamente com aprovação em lote

---

## Capacidades com Múltiplos Arquivos (Experimental)

Quando o recurso experimental [Leitura Simultânea de Arquivos](/features/concurrent-file-reads) está ativado, a ferramenta `read_file` ganha capacidades aprimoradas:

### Processamento em Lote

- Leia até 100 arquivos em uma única requisição (configurável, padrão 15)
- Processamento paralelo para melhor desempenho
- Interface de aprovação em lote para consentimento do usuário

### Experiência do Usuário Aprimorada

- Diálogo único de aprovação para múltiplos arquivos
- Opções de substituição individuais por arquivo
- Visibilidade clara de quais arquivos serão acessados
- Tratamento elegante de cenários mistos de sucesso/fracasso

### Eficiência Melhorada

- Reduz interrupções de múltiplos diálogos de aprovação
- Processamento mais rápido através de leitura paralela de arquivos
- Agrupamento inteligente de arquivos relacionados
- Limites de concorrência configuráveis para corresponder às capacidades do sistema

---

## Limitações

- Pode não lidar com arquivos extremamente grandes de forma eficiente sem usar parâmetros de intervalo de linhas
- Para arquivos binários (exceto PDF e DOCX), pode retornar conteúdo não legível por humanos
- **Modo multi-arquivo**: Requer que o recurso experimental esteja ativado e pode ter problemas de estabilidade

---

## Como Funciona

Quando a ferramenta `read_file` é invocada, segue este processo:

1. **Validação de Parâmetros**: Valida o parâmetro obrigatório `path` e parâmetros opcionais
2. **Resolução de Caminho**: Resolve o caminho relativo para um caminho absoluto
3. **Seleção de Estratégia de Leitura**:
   - A ferramenta usa uma hierarquia de prioridade estrita (explicada em detalhes abaixo)
   - Escolhe entre leitura por intervalo, truncamento automático ou leitura completa do arquivo
4. **Processamento de Conteúdo**:
   - Adiciona números de linha ao conteúdo (ex: "1 | const x = 13") onde `1 |` é o número da linha.
   - Para arquivos truncados, adiciona aviso de truncamento e definições de métodos
   - Para formatos especiais (PDF, DOCX), extrai texto legível

---

## Prioridade de Estratégia de Leitura

A ferramenta usa uma hierarquia clara de decisão para determinar como ler um arquivo:

1. **Primeira Prioridade: Intervalo de Linhas Explícito**
   - Se `start_line` ou `end_line` for fornecido, a ferramenta sempre realiza uma leitura por intervalo
   - A implementação transmite eficientemente apenas as linhas solicitadas, tornando-a adequada para processar arquivos grandes
   - Isso tem precedência sobre todas as outras opções

2. **Segunda Prioridade: Truncamento Automático para Arquivos de Texto Grandes**
   - Aplica-se apenas quando **todas** as seguintes condições são atendidas:
     - Nem `start_line` nem `end_line` são especificados.
     - O arquivo é identificado como baseado em texto (não binário como PDF/DOCX).
     - A contagem total de linhas do arquivo excede a configuração `maxReadFileLine` (padrão: 500 linhas).
   - Quando ocorre truncamento automático:
     - A ferramenta lê apenas as *primeiras* `maxReadFileLine` linhas.
     - Anexa um aviso indicando truncamento (ex: `[Mostrando apenas 500 de 1200 linhas totais...]`).
     - Para arquivos de código, também pode anexar um resumo de definições de código fonte encontradas na parte truncada.
   - **Caso Especial - Modo Apenas Definições**: Quando `maxReadFileLine` é definido como `0`, a ferramenta retorna apenas definições de código fonte sem nenhum conteúdo de arquivo.

3. **Comportamento Padrão: Ler Arquivo Inteiro**
   - Se nenhum intervalo explícito for dado nem truncamento automático se aplicar (ex: o arquivo está dentro do limite de linhas, ou é um tipo binário suportado), a ferramenta lê todo o conteúdo.
   - Para formatos suportados como PDF e DOCX, tenta extrair o conteúdo de texto completo.

---

## Exemplos de Uso

Aqui estão vários cenários demonstrando como a ferramenta `read_file` é usada e a saída típica que você pode receber.

### Lendo um Arquivo Inteiro

Para ler o conteúdo completo de um arquivo:

**Entrada:**
```xml
<read_file>
<path>src/app.js</path>
</read_file>
```

**Saída Simulada (para um arquivo pequeno como `example_small.txt`):**
```
1 | This is the first line.
2 | This is the second line.
3 | This is the third line.
```
*(A saída varia com base no conteúdo real do arquivo)*

### Lendo Linhas Específicas

Para ler apenas um intervalo específico de linhas (ex: 46-68):

**Entrada:**
```xml
<read_file>
<path>src/app.js</path>
<start_line>46</start_line>
<end_line>68</end_line>
</read_file>
```

**Saída Simulada (para linhas 2-3 de `example_five_lines.txt`):**
```
2 | Content of line two.
3 | Content of line three.
```
*(A saída mostra apenas as linhas solicitadas com seus números de linha originais)*

### Lendo um Arquivo de Texto Grande (Truncamento Automático)

Ao ler um arquivo de texto grande sem especificar um intervalo de linhas, a ferramenta trunca automaticamente o conteúdo se exceder o limite interno de linhas (ex: 500 linhas).

**Entrada:**
```xml
<read_file>
<path>logs/large_app.log</path>
</read_file>
```

**Saída Simulada (para um arquivo de log de 1500 linhas com limite de 500 linhas):**
```
1 | Log entry 1...
2 | Log entry 2...
...
500 | Log entry 500...

[Mostrando apenas 500 de 1500 linhas totais. Use start_line e end_line para ler intervalos específicos.]
// Opcional: Resumo de definições de código fonte pode aparecer aqui para arquivos de código
```
*(A saída mostra as linhas iniciais até o limite `maxReadFileLine`, mais um aviso de truncamento. Use intervalos de linhas para acesso completo.)*

### Lendo Apenas Definições

Quando `maxReadFileLine` é definido como `0` nas configurações do usuário, a ferramenta retorna apenas definições de código fonte sem conteúdo de arquivo:

**Entrada:**
```xml
<!-- Assumindo que maxReadFileLine está definido como 0 nas configurações do usuário -->
<read_file>
<path>src/services/auth.service.ts</path>
</read_file>
```

**Saída Simulada:**
```xml
<file>
  <path>src/services/auth.service.ts</path>
  <list_code_definition_names>
    class AuthService
      method validateUser
      method generateToken
  </list_code_definition_names>
  <notice>Mostrando apenas 0 de 150 linhas totais. Use start_line e end_line para ler intervalos específicos.</notice>
</file>
```
*(Este modo fornece uma visão geral rápida da estrutura do arquivo sem ler o conteúdo.)*

### Tentando Ler um Arquivo Inexistente

Se o arquivo especificado não existir:

**Entrada:**
```xml
<read_file>
<path>non_existent_file.txt</path>
</read_file>
```

**Saída Simulada (Erro):**
```
Erro: Arquivo não encontrado no caminho 'non_existent_file.txt'.
```

### Tentando Ler um Arquivo Bloqueado

Se o arquivo for excluído pelas regras em um arquivo `.rooignore`:

**Entrada:**
```xml
<read_file>
<path>.env</path>
</read_file>
```

**Saída Simulada (Erro):**
```
Erro: Acesso negado pelas regras do .rooignore
```

---

## Exemplos com Múltiplos Arquivos (Experimental)

Quando o recurso experimental [Leitura Simultânea de Arquivos](/features/concurrent-file-reads) está ativado, você pode ler vários arquivos simultaneamente usando o formato XML aprimorado.

### Lendo Múltiplos Arquivos Completos

Para ler vários arquivos completos de uma vez:

**Entrada:**
```xml
<read_file>
<args>
  <file>
    <path>src/app.ts</path>
  </file>
  <file>
    <path>src/utils.ts</path>
  </file>
  <file>
    <path>src/config.json</path>
  </file>
</args>
</read_file>
```

**Saída Simulada:**
```xml
<files>
  <file>
    <path>src/app.ts</path>
    <content>
      1 | import React from 'react'
      2 | import { Utils } from './utils'
      3 | // ... restante do conteúdo do arquivo
    </content>
  </file>
  <file>
    <path>src/utils.ts</path>
    <content>
      1 | export class Utils {
      2 |   static formatDate(date: Date): string {
      3 |     // ... funções utilitárias
    </content>
  </file>
  <file>
    <path>src/config.json</path>
    <content>
      1 | {
      2 |   "apiUrl": "https://api.example.com",
      3 |   "timeout": 5000
      4 | }
    </content>
  </file>
</files>
```

### Lendo Intervalos de Linhas Específicos de Múltiplos Arquivos

Para ler seções específicas de vários arquivos:

**Entrada:**
```xml
<read_file>
<args>
  <file>
    <path>src/app.ts</path>
    <line_range>1-20</line_range>
    <line_range>45-60</line_range>
  </file>
  <file>
    <path>src/utils.ts</path>
    <line_range>10-25</line_range>
  </file>
</args>
</read_file>
```

**Saída Simulada:**
```xml
<files>
  <file>
    <path>src/app.ts</path>
    <content>
      1 | import React from 'react'
      2 | import { Utils } from './utils'
      ...
      20 | const App = () => {

      45 |   const handleSubmit = () => {
      46 |     // Handle form submission
      ...
      60 |   }
    </content>
  </file>
  <file>
    <path>src/utils.ts</path>
    <content>
      10 |   static formatDate(date: Date): string {
      11 |     return date.toISOString().split('T')[0]
      ...
      25 |   }
    </content>
  </file>
</files>
```

### Lidando com Resultados Mistos (Alguns Arquivos Negados/Bloqueados)

Quando alguns arquivos são aprovados e outros são negados ou bloqueados:

**Entrada:**
```xml
<read_file>
<args>
  <file>
    <path>src/app.ts</path>
  </file>
  <file>
    <path>.env</path>
  </file>
  <file>
    <path>src/secret-config.ts</path>
  </file>
</args>
</read_file>
```

**Saída Simulada:**
```xml
<files>
  <file>
    <path>src/app.ts</path>
    <content>
      1 | import React from 'react'
      2 | // ... conteúdo do arquivo lido com sucesso
    </content>
  </file>
  <file>
    <path>.env</path>
    <error>Acesso negado pelas regras do .rooignore</error>
  </file>
  <file>
    <path>src/secret-config.ts</path>
    <error>Usuário negou acesso ao arquivo</error>
  </file>
</files>
```

### Interface de Aprovação em Lote

Ao solicitar vários arquivos, você verá uma interface de aprovação em lote que permite:

- **Aprovar Tudo**: Conceder acesso a todos os arquivos solicitados
- **Negar Tudo**: Negar acesso a todos os arquivos solicitados
- **Controle Individual**: Substituir decisões para arquivos específicos
- **Pré-visualização de Arquivo**: Clique nos cabeçalhos dos arquivos para abri-los em seu editor

A interface exibe cada caminho de arquivo claramente, facilitando entender o que o Roo deseja acessar antes de conceder permissão.

---

## Compatibilidade com Versões Anteriores

O formato aprimorado multi-arquivo é totalmente compatível com versões anteriores. Solicitações de arquivo único usando o parâmetro `path` continuam funcionando exatamente como antes, independentemente de o recurso experimental estar ativado ou desativado.
