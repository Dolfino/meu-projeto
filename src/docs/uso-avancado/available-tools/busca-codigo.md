# codebase_search

:::warning Funcionalidade Experimental
A ferramenta `codebase_search` faz parte do recurso experimental [Codebase Indexing](/features/experimental/codebase-indexing). Este recurso está em desenvolvimento ativo e pode sofrer alterações significativas em versões futuras. Requer configuração adicional incluindo um provedor de embeddings e banco de dados vetorial.
:::

A ferramenta `codebase_search` realiza buscas semânticas em todo o seu código usando embeddings de IA. Diferente de buscas tradicionais baseadas em texto, ela compreende o significado das consultas e encontra código relevante mesmo quando as palavras-chave exatas não coincidem.

---

## Parâmetros

A ferramenta aceita estes parâmetros:

- `query` (obrigatório): Consulta em linguagem natural descrevendo o que você está procurando
- `path` (opcional): Caminho do diretório para limitar o escopo da busca a uma parte específica do código

---

## Funcionalidade

Esta ferramenta busca no código indexado usando similaridade semântica ao invés de correspondência exata de texto. Ela encontra blocos de código relacionados conceitualmente à sua consulta, mesmo que não contenham as palavras exatas pesquisadas. Os resultados incluem trechos de código relevantes com caminhos dos arquivos, números de linha e escores de similaridade.

---

## Quando é usada?

- Quando o Roo precisa encontrar código relacionado a funcionalidades específicas no projeto
- Ao procurar padrões de implementação ou estruturas de código similares
- Ao buscar tratamento de erros, autenticação ou outros padrões conceituais
- Ao explorar bases de código desconhecidas para entender como funcionalidades são implementadas
- Ao encontrar código relacionado que pode ser afetado por mudanças ou refatorações

---

## Principais Características

- **Compreensão Semântica**: Encontra código por significado ao invés de correspondência exata de palavras-chave
- **Busca Transversal**: Pesquisa em todo o código indexado, não apenas em arquivos abertos
- **Resultados Contextuais**: Retorna trechos de código com caminhos de arquivo e números de linha para fácil navegação
- **Pontuação de Similaridade**: Resultados classificados por relevância com escores de similaridade (escala 0-1)
- **Filtro de Escopo**: Parâmetro opcional para limitar buscas a diretórios específicos
- **Classificação Inteligente**: Resultados ordenados por relevância semântica à sua consulta
- **Integração com UI**: Resultados exibidos com syntax highlighting e links de navegação
- **Otimizado para Performance**: Busca vetorial rápida com limites configuráveis de resultados

---

## Requisitos

Esta ferramenta só está disponível quando o recurso experimental Codebase Indexing está configurado:

- **Recurso Ativado**: Codebase Indexing deve estar habilitado nas configurações experimentais
- **Provedor de Embeddings**: Chave da API OpenAI ou configuração Ollama necessária
- **Banco de Dados Vetorial**: Instância Qdrant rodando e acessível
- **Status do Índice**: Código deve estar indexado (status: "Indexed" ou "Indexing")

---

## Limitações

- **Funcionalidade Experimental**: Parte do sistema experimental de indexação de código
- **Requer Configuração**: Depende de serviços externos (provedor de embeddings + Qdrant)
- **Dependência do Índice**: Só pesquisa em blocos de código indexados
- **Limite de Resultados**: Máximo de 50 resultados por busca para manter performance
- **Limiar de Similaridade**: Só retorna resultados acima do escore 0.4
- **Limite de Tamanho**: Arquivos abaixo de 1MB que foram indexados com sucesso
- **Suporte a Linguagens**: Eficácia depende do suporte do Tree-sitter

---

## Como Funciona

Quando a ferramenta `codebase_search` é invocada, segue este processo:

1. **Validação de Disponibilidade**:
   - Verifica se o CodeIndexManager está disponível e inicializado
   - Confirma que a indexação está habilitada nas configurações
   - Checa se a indexação está configurada corretamente (chaves API, URL Qdrant)
   - Valida se o estado atual do índice permite buscas

2. **Processamento da Consulta**:
   - Pega sua consulta em linguagem natural e gera um vetor de embedding
   - Usa o mesmo provedor de embeddings configurado para indexação (OpenAI ou Ollama)
   - Converte o significado semântico da consulta em uma representação matemática

3. **Execução da Busca Vetorial**:
   - Busca no banco de dados vetorial Qdrant por embeddings de código similares
   - Usa similaridade de cosseno para encontrar os blocos de código mais relevantes
   - Aplica o limiar mínimo de similaridade (0.4) para filtrar resultados
   - Limita resultados a 50 correspondências para performance ideal

4. **Filtragem por Caminho** (se especificado):
   - Filtra resultados para incluir apenas arquivos dentro do caminho especificado
   - Usa comparação normalizada de caminhos para filtragem precisa
   - Mantém classificação de relevância dentro do escopo filtrado

5. **Processamento e Formatação de Resultados**:
   - Converte caminhos absolutos para relativos ao workspace
   - Estrutura resultados com caminhos de arquivo, intervalos de linha, escores de similaridade e conteúdo do código
   - Formata para consumo por IA e exibição na UI com syntax highlighting

6. **Formato de Saída Duplo**:
   - **Saída para IA**: Formato de texto estruturado com consulta, caminhos de arquivo, escores e trechos de código
   - **Saída para UI**: Formato JSON com syntax highlighting e capacidades de navegação

---

## Melhores Práticas para Consultas

### Padrões Eficazes

**Bom: Conceitual e específico**
```xml
<codebase_search>
<query>autenticação de usuário e validação de senha</query>
</codebase_search>
```

**Bom: Focado em funcionalidade**
```xml
<codebase_search>
<query>configuração de pool de conexões com banco de dados</query>
</codebase_search>
```

**Bom: Orientado a problemas**
```xml
<codebase_search>
<query>tratamento de erros para requisições API</query>
</codebase_search>
```

**Menos eficaz: Muito genérico**
```xml
<codebase_search>
<query>função</query>
</codebase_search>
```

### Tipos de Consulta que Funcionam Bem

- **Descrições Funcionais**: "processamento de upload de arquivo", "lógica de validação de email"
- **Padrões Técnicos**: "implementação do padrão singleton", "uso do método factory"
- **Conceitos de Domínio**: "gerenciamento de perfil de usuário", "fluxo de processamento de pagamentos"
- **Componentes de Arquitetura**: "configuração de middleware", "scripts de migração de banco de dados"

---

## Escopo por Diretório

Use o parâmetro opcional `path` para focar buscas em partes específicas do código:

**Busca em módulos API:**
```xml
<codebase_search>
<query>middleware de validação de endpoint</query>
<path>src/api</path>
</codebase_search>
```

**Busca em arquivos de teste:**
```xml
<codebase_search>
<query>padrões de configuração de dados mockados</query>
<path>tests</path>
</codebase_search>
```

**Busca em diretórios específicos:**
```xml
<codebase_search>
<query>gerenciamento de estado de componente</query>
<path>src/components/auth</path>
</codebase_search>
```

---

## Interpretação de Resultados

### Escores de Similaridade

- **0.8-1.0**: Correspondências altamente relevantes, provavelmente exatamente o que você procura
- **0.6-0.8**: Boas correspondências com forte similaridade conceitual
- **0.4-0.6**: Potencialmente relevantes mas podem requerer revisão
- **Abaixo de 0.4**: Filtrados como muito diferentes

### Estrutura do Resultado

Cada resultado inclui:
- **Caminho do Arquivo**: Caminho relativo ao workspace do arquivo contendo a correspondência
- **Score**: Escore de similaridade indicando relevância (0.4-1.0)
- **Intervalo de Linhas**: Números de linha inicial e final do bloco de código
- **Trecho de Código**: O conteúdo real do código que correspondeu à consulta

---

## Exemplos de Uso

- Ao implementar nova funcionalidade, o Roo busca por "middleware de autenticação" para entender padrões existentes antes de escrever novo código.
- Ao debugar um problema, o Roo busca por "tratamento de erros em chamadas API" para encontrar padrões relacionados no código.
- Ao refatorar código, o Roo busca por "padrões de transação de banco de dados" para garantir consistência em todas as operações.
- Ao se familiarizar com novo código, o Roo busca por "carregamento de configuração" para entender como a aplicação é inicializada.

---

## Exemplos de Uso

Buscando código relacionado a autenticação em todo o projeto:
```xml
<codebase_search>
<query>lógica de login e autenticação de usuário</query>
</codebase_search>
```

Encontrando código relacionado a banco de dados em diretório específico:
```xml
<codebase_search>
<query>conexão com banco de dados e execução de queries</query>
<path>src/data</path>
</codebase_search>
```

Procurando padrões de tratamento de erros em código API:
```xml
<codebase_search>
<query>respostas HTTP de erro e tratamento de exceções</query>
<path>src/api</path>
</codebase_search>
```

Buscando utilitários de teste e configurações mock:
```xml
<codebase_search>
<query>configuração de teste e criação de dados mockados</query>
<path>tests</path>
</codebase_search>
```

Encontrando código de configuração e ambiente:
```xml
<codebase_search>
<query>variáveis de ambiente e configuração da aplicação</query>
</codebase_search>
