# insert_content

A ferramenta `insert_content` adiciona novas linhas de conteúdo em um arquivo existente sem modificar o conteúdo original. É ideal para inserir blocos de código, entradas de configuração ou linhas de log em locais específicos.

---

## Parâmetros

A ferramenta aceita estes parâmetros:

- `path` (obrigatório): O caminho relativo (a partir da raiz do workspace) do arquivo onde o conteúdo será inserido.
- `line` (obrigatório): O número da linha (base 1) *antes* da qual o conteúdo será inserido. Use `0` para anexar o conteúdo ao final do arquivo.
- `content` (obrigatório): O conteúdo de texto a ser inserido.

---

## Funcionamento

Esta ferramenta lê o arquivo alvo, identifica o ponto de inserção especificado pelo parâmetro `line` e insere o `content` naquela localização. Se `line` for `0`, o conteúdo é adicionado ao final. As alterações são apresentadas em uma visualização de diff para aprovação do usuário antes de serem salvas.

---

## Quando usar?

- Para adicionar novas declarações de import no início de um arquivo
- Para inserir novas funções ou métodos em código existente
- Para adicionar blocos de configuração em arquivos de settings
- Para anexar entradas de log ou registros de dados
- Para adicionar qualquer bloco de texto multilinha sem alterar linhas existentes

---

## Principais recursos

- **Inserção direcionada**: Adiciona conteúdo precisamente no número de linha especificado ou anexa ao final
- **Preserva conteúdo existente**: Não modifica ou deleta linhas originais do arquivo
- **Aprovação interativa**: Mostra as inserções propostas em uma visualização de diff, exigindo aprovação explícita do usuário
- **Suporte a edições**: Permite editar o conteúdo proposto diretamente na visualização de diff antes da aprovação final
- **Tratamento de números de linha**: Interpreta corretamente o parâmetro `line` (base 1 ou 0 para anexar)
- **Rastreamento de contexto**: Registra a operação de edição para gerenciamento de contexto
- **Tratamento de erros**: Verifica parâmetros faltantes, números de linha inválidos e problemas de acesso a arquivos

---

## Limitações

- **Apenas inserção**: Não pode substituir ou deletar conteúdo existente. Use `apply_diff` ou `search_and_replace` para modificações.
- **Requer arquivo existente**: O arquivo alvo especificado por `path` deve existir.
- **Etapa de revisão**: A aprovação obrigatória via visualização de diff adiciona um passo interativo.

---

## Como funciona

Quando a ferramenta `insert_content` é invocada, segue este processo:

1. **Validação de parâmetros**: Verifica os parâmetros obrigatórios `path`, `line` e `content`. Valida se `line` é um inteiro não negativo.
2. **Leitura do arquivo**: Lê o conteúdo do arquivo alvo especificado por `path`.
3. **Cálculo do ponto de inserção**: Converte o parâmetro `line` (base 1) para um índice base 0 para processamento interno (`-1` para anexar).
4. **Inserção de conteúdo**: Usa um utilitário interno (`insertGroups`) para mesclar as linhas originais com o novo `content` no índice calculado.
5. **Interação com diff view**:
   - Abre o arquivo na visualização de diff (`cline.diffViewProvider.open`)
   - Atualiza a visualização com o conteúdo proposto (`cline.diffViewProvider.update`)
6. **Aprovação do usuário**: Apresenta a mudança via `askApproval`. Reverte se rejeitado.
7. **Salvamento das alterações**: Se aprovado, salva as mudanças usando `cline.diffViewProvider.saveChanges`.
8. **Rastreamento de contexto**: Registra a edição usando `cline.getFileContextTracker().trackFileContext`.
9. **Tratamento de edições**: Se o usuário editou o conteúdo na visualização de diff, reporta o conteúdo final mesclado.
10. **Relatório de resultado**: Reporta sucesso (incluindo edições do usuário) ou falha de volta para o modelo de IA.

---

## Exemplos de uso

Inserindo declarações de import no início de um arquivo (`line: 1`):

```xml
<insert_content>
<path>src/utils.ts</path>
<line>1</line>
<content>
// Add imports at start of file
import { sum } from './math';
import { parse } from 'date-fns';
</content>
</insert_content>
```

Anexando conteúdo ao final de um arquivo (`line: 0`):

```xml
<insert_content>
<path>config/routes.yaml</path>
<line>0</line>
<content>
- path: /new-feature
  component: NewFeatureComponent
  auth_required: true
</content>
</insert_content>
```

Inserindo uma função antes da linha 50:

```xml
<insert_content>
<path>src/services/api.js</path>
<line>50</line>
<content>
async function fetchUserData(userId) {
  const response = await fetch(`/api/users/${userId}`);
  if (!response.ok) {
    throw new Error('Failed to fetch user data');
  }
  return response.json();
}
</content>
</insert_content>
