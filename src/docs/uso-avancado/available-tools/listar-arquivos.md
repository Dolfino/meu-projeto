# list_files

A ferramenta `list_files` exibe os arquivos e diretórios em um local especificado. Ela ajuda o Roo a entender a estrutura do seu projeto e navegar pela base de código de forma eficiente.

---

## Parâmetros

A ferramenta aceita estes parâmetros:

- `path` (obrigatório): O caminho do diretório para listar conteúdos, relativo ao diretório de trabalho atual
- `recursive` (opcional): Se deve listar arquivos recursivamente. Use `true` para listagem recursiva, `false` ou omita para apenas o nível superior.

---

## O que ela faz

Esta ferramenta lista todos os arquivos e diretórios em um local especificado, fornecendo uma visão geral clara da estrutura do seu projeto. Ela pode mostrar apenas os conteúdos do nível superior ou explorar subdiretórios recursivamente.

---

## Quando é usada?

- Quando o Roo precisa entender a estrutura do seu projeto
- Quando o Roo explora quais arquivos estão disponíveis antes de ler específicos
- Quando o Roo mapeia uma base de código para entender melhor sua organização
- Antes de usar ferramentas mais direcionadas como `read_file` ou `search_files`
- Quando o Roo precisa verificar tipos específicos de arquivos (como arquivos de configuração) em um projeto

---

## Principais recursos

- Lista tanto arquivos quanto diretórios, com diretórios claramente marcados
- Oferece modos de listagem recursiva e não-recursiva
- Ignora inteligentemente diretórios grandes comuns como `node_modules` e `.git` no modo recursivo
- Respeita regras do `.gitignore` no modo recursivo
- Marca arquivos ignorados pelo `.rooignore` com um símbolo de cadeado (🔒) quando `showRooIgnoredFiles` está ativado
- Otimiza o desempenho da listagem usando a ferramenta `ripgrep`
- Ordena resultados para mostrar diretórios antes de seus conteúdos, mantendo uma hierarquia lógica
- Apresenta resultados em um formato limpo e organizado
- Cria automaticamente um mapa mental da estrutura do seu projeto

---

## Limitações

- A listagem de arquivos é limitada a cerca de 200 arquivos por padrão para evitar problemas de desempenho
- O processo subjacente de listagem `ripgrep` tem um timeout de 10 segundos; se excedido, resultados parciais podem ser retornados
- Quando o limite de arquivos é atingido, adiciona uma nota sugerindo usar `list_files` em subdiretórios específicos
- Não foi projetada para confirmar a existência de arquivos que você acabou de criar
- Pode ter desempenho reduzido em estruturas de diretórios muito grandes
- Não pode listar arquivos em diretórios raiz ou home por razões de segurança

---

## Como funciona

Quando a ferramenta `list_files` é invocada, ela segue este processo:

1. **Validação de parâmetros**: Valida o parâmetro obrigatório `path` e o opcional `recursive`
2. **Resolução de caminho**: Converte o caminho relativo para um caminho absoluto
3. **Verificações de segurança**: Previne listagem de arquivos em locais sensíveis como raiz ou home
4. **Varredura de diretórios/arquivos**:
   - Usa a ferramenta `ripgrep` para listar arquivos eficientemente, aplicando um timeout de 10 segundos
   - Usa o módulo `fs` do Node.js para listar diretórios
   - Aplica lógicas diferentes de filtro para modos recursivo e não-recursivo
5. **Filtragem de resultados**:
   - No modo recursivo, ignora diretórios grandes comuns como `node_modules`, `.git`, etc.
   - Respeita regras do `.gitignore` no modo recursivo
   - Lida com padrões do `.rooignore`, ocultando arquivos ou marcando-os com símbolo de cadeado
6. **Formatação**:
   - Marca diretórios com uma barra final (`/`)
   - Ordena resultados para mostrar diretórios antes de seus conteúdos para hierarquia lógica
   - Marca arquivos ignorados com símbolo de cadeado (🔒) quando `showRooIgnoredFiles` está ativado
   - Limita resultados a 200 arquivos por padrão com nota sobre usar subdiretórios
   - Organiza resultados para legibilidade

---

## Formato da listagem de arquivos

Os resultados da listagem incluem:

- Cada caminho de arquivo é exibido em sua própria linha
- Diretórios são marcados com uma barra final (`/`)
- Arquivos ignorados pelo `.rooignore` são marcados com símbolo de cadeado (🔒) quando `showRooIgnoredFiles` está ativado
- Resultados são ordenados logicamente com diretórios aparecendo antes de seus conteúdos
- Quando o limite de arquivos é atingido, uma mensagem aparece sugerindo usar `list_files` em subdiretórios específicos

Exemplo de formato de saída:
```
src/
src/components/
src/components/Button.tsx
src/components/Header.tsx
src/utils/
src/utils/helpers.ts
src/index.ts
...
Listagem de arquivos truncada (mostrando 200 de 543 arquivos). Use list_files em subdiretórios específicos para mais detalhes.
```

Quando arquivos `.rooignore` são usados e `showRooIgnoredFiles` está ativado:
```
src/
src/components/
src/components/Button.tsx
src/components/Header.tsx
🔒 src/secrets.json
src/utils/
src/utils/helpers.ts
src/index.ts
```

---

## Exemplos de uso

- Quando inicia uma nova tarefa, o Roo pode listar os arquivos do projeto para entender sua estrutura antes de mergulhar em códigos específicos
- Quando solicitado a encontrar tipos específicos de arquivos (como todos arquivos JavaScript), o Roo primeiro lista diretórios para saber onde procurar
- Ao fornecer recomendações para organização de código, o Roo examina primeiro a estrutura atual do projeto
- Ao configurar um novo recurso, o Roo lista diretórios relacionados para entender as convenções do projeto

---

## Exemplos de utilização

Listando arquivos do nível superior no diretório atual:
```
<list_files>
<path>.</path>
</list_files>
```

Listando recursivamente todos arquivos em um diretório fonte:
```
<list_files>
<path>src</path>
<recursive>true</recursive>
</list_files>
```

Examinando um subdiretório específico do projeto:
```
<list_files>
<path>src/components</path>
<recursive>false</recursive>
</list_files>
