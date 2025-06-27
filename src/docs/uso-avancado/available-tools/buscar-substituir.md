# search_and_replace

A ferramenta `search_and_replace` localiza e substitui texto dentro de um arquivo, suportando tanto strings literais quanto padrões de expressão regular (regex). Permite substituições direcionadas em múltiplas localizações, opcionalmente dentro de intervalos de linhas específicos.

---

## Parâmetros

### Parâmetros Obrigatórios

- `path`: O caminho relativo (a partir da raiz do workspace) do arquivo a ser modificado.
- `search`: A string de texto ou padrão regex a ser encontrado.
- `replace`: O texto que substituirá as correspondências encontradas.

### Parâmetros Opcionais

- `start_line`: O número da linha (base 1) onde o escopo da busca começa.
- `end_line`: O número da linha (base 1) onde o escopo da busca termina (inclusive).
- `use_regex`: Defina como `"true"` para tratar o parâmetro `search` como um padrão de expressão regular (padrão é `false`).
- `ignore_case`: Defina como `"true"` para realizar uma busca insensível a maiúsculas/minúsculas (padrão é `false`).

---

## Funcionalidade

Esta ferramenta lê o arquivo especificado e executa uma operação de busca-e-substituição baseada nos parâmetros fornecidos. Pode operar em todo o arquivo ou ser restrita a um intervalo específico de linhas. As alterações são apresentadas em uma visualização diff para revisão e aprovação do usuário antes de serem salvas.

---

## Quando usar?

- Ao renomear variáveis, funções ou classes em um arquivo.
- Ao atualizar strings de texto ou valores específicos de forma consistente.
- Ao aplicar alterações padronizadas usando expressões regulares.
- Quando refatorações de código exigem substituição de padrões específicos.
- Ao fazer alterações direcionadas dentro de uma seção definida de um arquivo.

---

## Principais Recursos

- **Busca Flexível**: Suporta tanto texto literal quanto padrões de expressão regular.
- **Controle de Sensibilidade a Maiúsculas/Minúsculas**: Opção para ignorar diferenças de caixa durante a busca.
- **Substituições Escopadas**: Pode limitar substituições a um intervalo específico de linhas (`start_line`, `end_line`).
- **Substituição Global**: Realiza substituições em todo o arquivo (ou intervalo especificado) por padrão.
- **Aprovação Interativa**: Mostra as alterações propostas em uma visualização diff para revisão do usuário.
- **Suporte a Edições do Usuário**: Permite editar o conteúdo proposto diretamente na visualização diff.
- **Rastreamento de Contexto**: Registra a operação de edição do arquivo.
- **Tratamento de Erros**: Verifica parâmetros ausentes, problemas de acesso a arquivos e números de linha inválidos.

---

## Limitações

- **Operação em Arquivo Único**: Opera em apenas um arquivo por vez. Use `search_files` para encontrar padrões em múltiplos arquivos primeiro.
- **Etapa de Revisão**: A aprovação obrigatória via visualização diff adiciona um passo interativo.
- **Complexidade de Regex**: Padrões regex complexos podem exigir construção e teste cuidadosos.

---

## Como Funciona

Quando a ferramenta `search_and_replace` é invocada, segue este processo:

1. **Validação de Parâmetros**: Verifica os parâmetros obrigatórios `path`, `search`, `replace` e valida parâmetros opcionais como números de linha e flags booleanas.
2. **Leitura do Arquivo**: Lê o conteúdo do arquivo alvo especificado por `path`.
3. **Construção do Regex**:
   * Se `use_regex` for `false`, a string `search` é escapada para ser tratada como texto literal.
   * Um objeto `RegExp` é criado com a flag `g` (global) e opcionalmente a flag `i` (ignore case).
4. **Execução da Substituição**:
   * Se `start_line` ou `end_line` forem fornecidos, o conteúdo do arquivo é dividido em linhas, a seção relevante é isolada, a substituição é realizada nessa seção e o conteúdo do arquivo é reconstruído.
   * Se nenhum intervalo de linhas for especificado, a substituição é realizada em toda a string de conteúdo do arquivo.
5. **Interação com Visualização Diff**:
   * Abre o arquivo na visualização diff mostrando o conteúdo original vs. o conteúdo proposto.
   * Atualiza a visualização diff com o resultado da substituição.
6. **Aprovação do Usuário**: Apresenta a alteração via `askApproval`. Reverte se rejeitado.
7. **Salvamento das Alterações**: Se aprovado, salva as alterações (incluindo quaisquer edições feitas pelo usuário na visualização diff).
8. **Rastreamento de Contexto**: Rastreia a edição usando `cline.getFileContextTracker().trackFileContext`.
9. **Relatório de Resultado**: Reporta sucesso (incluindo edições do usuário) ou falha de volta para o modelo de IA.

---

## Exemplos de Uso

Substituição simples de texto em todo o arquivo:

```xml
<search_and_replace>
<path>src/config.js</path>
<search>API_KEY_OLD</search>
<replace>API_KEY_NEW</replace>
</search_and_replace>
```

Substituição com regex insensível a maiúsculas/minúsculas para atualizar chamadas de função:

```xml
<search_and_replace>
<path>src/app.ts</path>
<search>processData\((.*?)\)</search>
<replace>handleData($1)</replace>
<use_regex>true</use_regex>
<ignore_case>true</ignore_case>
</search_and_replace>
```

Substituindo texto apenas entre as linhas 10 e 20:

```xml
<search_and_replace>
<path>README.md</path>
<search>Draft</search>
<replace>Final</replace>
<start_line>10</start_line>
<end_line>20</end_line>
</search_and_replace>
