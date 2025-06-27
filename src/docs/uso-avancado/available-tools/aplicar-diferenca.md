# apply_diff

A ferramenta `apply_diff` faz alterações precisas e cirúrgicas em arquivos especificando exatamente qual conteúdo substituir. Ela usa uma estratégia sofisticada para encontrar e aplicar mudanças enquanto mantém a formatação e estrutura adequadas do código.

---

## Parâmetros

A ferramenta aceita estes parâmetros:

- `path` (obrigatório): O caminho do arquivo a ser modificado, relativo ao diretório de trabalho atual.
- `diff` (obrigatório): O bloco de busca/substituição que define as alterações usando um formato específico para a estratégia de diff ativa.
- `start_line` (opcional): Uma dica de onde o conteúdo de busca começa. _Nota: Este parâmetro de nível superior parece não ser usado pela estratégia principal atual, que depende de `:start_line:` dentro do conteúdo diff._
- `end_line` (opcional): Uma dica de onde o conteúdo de busca termina. _Nota: Este parâmetro de nível superior parece não ser usado pela estratégia principal atual._

---

## O que ela faz

Esta ferramenta aplica alterações direcionadas a arquivos existentes usando correspondência aproximada (fuzzy matching) guiada por dicas de números de linha para localizar e substituir conteúdo com precisão. Diferente de uma simples busca e substituição, ela identifica o bloco exato para substituição com base no conteúdo fornecido e nas dicas de localização.

---

## Quando é usada?

- Quando o Roo precisa fazer alterações precisas em código existente sem reescrever arquivos inteiros.
- Ao refatorar seções específicas de código mantendo o contexto ao redor.
- Ao corrigir bugs em código existente com precisão cirúrgica.
- Ao implementar melhorias de recursos que modificam apenas partes específicas de um arquivo.

---

## Principais recursos

- Usa correspondência aproximada (distância de Levenshtein em strings normalizadas) guiada por uma dica `:start_line:`, com limites de confiança configuráveis (tipicamente 0.8-1.0).
- Fornece contexto em torno das correspondências usando `BUFFER_LINES` (padrão 40).
- Realiza uma busca "middle-out" dentro de uma janela de contexto configurável (`bufferLines`) em torno da linha inicial indicada.
- Preserva formatação e indentação do código passivamente substituindo blocos exatos.
- Mostra alterações em uma visualização diff para revisão e edição pelo usuário antes de aplicar.
- Rastreia erros consecutivos por arquivo (`consecutiveMistakeCountForApplyDiff`) para evitar falhas repetidas.
- Valida acesso ao arquivo contra regras `.rooignore`.
- Lida efetivamente com edições multi-linha.

---

## Limitações

- Funciona melhor com seções de código únicas e distintas para identificação confiável.
- O desempenho pode variar com arquivos muito grandes ou padrões de código altamente repetitivos.
- A correspondência aproximada pode ocasionalmente selecionar locais incorretos se o conteúdo for ambíguo.
- Cada estratégia diff tem requisitos de formato específicos.
- Edições complexas podem requerer seleção cuidadosa de estratégia ou revisão manual.

---

## Como funciona

Quando a ferramenta `apply_diff` é invocada, ela segue este processo:

1. **Validação de parâmetros**: Valida os parâmetros obrigatórios `path` e `diff`.
2. **Verificação RooIgnore**: Valida se o caminho do arquivo alvo é permitido pelas regras `.rooignore`.
3. **Análise do arquivo**: Carrega o conteúdo do arquivo alvo.
4. **Encontrando correspondência**: Usa um algoritmo de correspondência aproximada (Levenshtein em strings normalizadas) guiado pela dica `:start_line:` dentro de uma janela de contexto (`BUFFER_LINES`), buscando "middle-out" para localizar o conteúdo alvo com base no limite de confiança.
5. **Preparação da mudança**: Gera as alterações propostas substituindo o bloco identificado.
6. **Interação com o usuário**:
   * Mostra as alterações em uma visualização diff.
   * Permite que o usuário revise e potencialmente edite as alterações propostas.
   * Aguarda aprovação ou rejeição do usuário.
7. **Aplicação da mudança**: Se aprovado, aplica as alterações (potencialmente incluindo edições do usuário) ao arquivo.
8. **Tratamento de erros**: Se ocorrerem erros (ex: falha na correspondência, aplicação parcial), incrementa o `consecutiveMistakeCountForApplyDiff` para o arquivo e relata o tipo de falha.
9. **Feedback**: Retorna o resultado, incluindo qualquer feedback do usuário ou detalhes de erro.

---

## Requisitos de formato Diff

O parâmetro `<diff>` requer um formato específico que suporte uma ou mais alterações em uma única requisição. Cada bloco de alteração requer uma dica de número de linha para o conteúdo original.

* **Requer**: Correspondência exata para o conteúdo do bloco `SEARCH` (dentro do limite de confiança), incluindo espaços em branco e indentação. A dica de número de linha `:start_line:` é obrigatória dentro de cada bloco. A dica `:end_line:` é opcional (mas suportada pelo parser). Marcadores como `<<<<<<<` dentro do conteúdo do arquivo devem ser escapados (`\\`) no bloco SEARCH.

Exemplo de formato para o bloco `<diff>`:

```diff
<<<<<<< SEARCH
:start_line:10
:end_line:12
-------
    // Old calculation logic
    const result = value * 0.9;
    return result;
=======
    // Updated calculation logic with logging
    console.log(`Calculating for value: ${value}`);
    const result = value * 0.95; // Adjusted factor
    return result;
>>>>>>> REPLACE

<<<<<<< SEARCH
:start_line:25
:end_line:25
-------
    const defaultTimeout = 5000;
=======
    const defaultTimeout = 10000; // Increased timeout
>>>>>>> REPLACE
```

---

## Experimental: Edições em múltiplos arquivos (`MULTI_FILE_APPLY_DIFF`)

Uma versão experimental do `apply_diff` permite aplicar alterações em múltiplos arquivos em uma única chamada de ferramenta. Este recurso é ativado pela flag experimental `MULTI_FILE_APPLY_DIFF`.

### Principais recursos do modo experimental

- **Operações multi-arquivo**: Edita múltiplos arquivos em uma única requisição, simplificando tarefas complexas de refatoração.
- **UI de aprovação em lote**: Quando múltiplos arquivos são alvo, uma única UI aparece para o usuário aprovar ou negar todas as alterações de uma vez, ou gerenciar permissões para cada arquivo individualmente.
- **Novo formato XML**: Introduz um novo formato XML mais estruturado usando tags `<args>` e `<file>` para lidar com múltiplas operações.
- **Compatibilidade retroativa**: A ferramenta experimental mantém compatibilidade com o formato legado de parâmetros `path` e `diff` para arquivo único.

### Como funciona (Experimental)

1. **Verificação experimental**: A ferramenta primeiro verifica se o experimento `MULTI_FILE_APPLY_DIFF` está habilitado. Se não estiver, volta para a implementação legada do `apply_diff`.
2. **Análise de parâmetros**: Analisa o novo formato XML `<args>` para identificar todos os arquivos alvo e suas operações diff correspondentes. Também pode lidar com os parâmetros legados `path`/`diff`.
3. **Validação e aprovação**:
   * Valida que todos os arquivos alvo existem e estão acessíveis (não bloqueados por `.rooignore`).
   * Se múltiplos arquivos estão sendo modificados, apresenta um diálogo de **aprovação em lote** para o usuário.
4. **Aplicação do diff**: Para cada arquivo aprovado, aplica os diffs especificados usando o `MultiFileSearchReplaceDiffStrategy`. Esta estratégia pode aplicar múltiplas alterações não sobrepostas a um único arquivo.
5. **Resultados**: Retorna uma mensagem de resultado consolidada resumindo o resultado de todas as operações tentadas.

### Novo formato Diff (Experimental)

O modo experimental usa uma nova estrutura XML dentro da chamada da ferramenta `<apply_diff>`.

- **`<args>`**: Um container para todas as operações de arquivo.
- **`<file>`**: Um bloco para cada arquivo a ser modificado. Contém `<path>` e uma ou mais tags `<diff>`.
- **`<path>`**: O caminho relativo para o arquivo.
- **`<diff>`**: Um bloco contendo a alteração.
    - **`<content>`**: O bloco `SEARCH/REPLACE`.
    - **`<start_line>`**: (Opcional) Uma dica de número de linha.

**Exemplo: Modificando dois arquivos em uma chamada**

```xml
<apply_diff>
  <args>
    <file>
      <path>src/services/auth.service.ts</path>
      <diff>
        <content>
<<<<<<< SEARCH
:start_line:50
-------
    const token_expiration = '15m';
>>>>>>> REPLACE
        </content>
      </diff>
    </file>
    <file>
      <path>src/config/auth.config.ts</path>
      <diff>
        <content>
<<<<<<< SEARCH
:start_line:12
-------
    rateLimit: 5,
=======
    rateLimit: 10,
>>>>>>> REPLACE
        </content>
      </diff>
    </file>
  </args>
</apply_diff>
