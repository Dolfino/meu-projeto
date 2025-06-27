---
sidebar_label: 'Leituras Multiarquivo'
---

# Leituras Concorrentes de Arquivos (Leituras Multiarquivo)

O recurso de Leituras Concorrentes de Arquivos permite que o Roo leia vários arquivos do seu workspace em uma única etapa. Isso melhora significativamente a eficiência ao trabalhar em tarefas que exigem contexto de vários arquivos, pois o Roo pode coletar todas as informações necessárias de uma vez em vez de ler os arquivos um por um.

### Principais Recursos
- Ler até 100 arquivos em uma única solicitação.
- Habilitado por padrão para um fluxo de trabalho mais rápido e simplificado.
- Limite configurável de 1 a 100 arquivos (definir como 1 efetivamente desativa as leituras concorrentes).

---

## Benefícios

-   **Velocidade Aumentada**: Reduz o tempo que o Roo leva para entender seu código, minimizando o número de etapas de ida e volta.
-   **Melhor Contexto**: Permite que o Roo construa um modelo mental mais completo do seu código, levando a respostas mais precisas e relevantes.
-   **Fluxo de Trabalho Aprimorado**: Simplifica tarefas que exigem informações de vários arquivos, tornando você mais produtivo.

---

## Por Que Isso é Importante

**Construção de Contexto Mais Rápida**: Anteriormente, quando o Roo precisava entender seu projeto, você veria várias solicitações como:
- "Posso ler `src/app.js`?" → Você aprova
- "Agora posso ler `src/utils.js`?" → Você aprova
- "E posso ler `src/config.json`?" → Você aprova

**Com leituras concorrentes de arquivos**: O Roo pede uma vez para ler todos os arquivos relacionados juntos, obtendo a visão completa imediatamente e fornecendo assistência melhor e mais rápida.

---

## Como Funciona

Quando você pede ao Roo para realizar uma tarefa que envolve vários arquivos, ele identificará automaticamente os arquivos relevantes e os lerá juntos. Isso é especialmente útil para:

-   Entender a estrutura geral de um componente que está dividido em vários arquivos.
-   Refatorar código que tem dependências em outras partes da base de código.
-   Responder perguntas que exigem um amplo entendimento do seu projeto.

O Roo é instruído a usar esse recurso com eficiência, priorizando os arquivos mais críticos e lendo-os em um único lote. A ferramenta [`read_file`](/advanced-usage/available-tools/read-file) aceita automaticamente vários arquivos em uma única solicitação.

Quando o Roo solicita a leitura de vários arquivos, você verá uma interface de aprovação em lote que exibe:

- Lista de todos os arquivos a serem lidos
- Caminhos dos arquivos com indicadores de intervalo de linhas (se especificado)
- Cabeçalhos de arquivos clicáveis para abrir arquivos no seu editor
- Botões **Aprovar Tudo** e **Negar Tudo** para decisões rápidas

<img src="/img/concurrent-file-reads/concurrent-file-reads-2.png" alt="Interface de aprovação em lote para leitura de vários arquivos" width="600" />

---

## Configuração

Você pode configurar o recurso de Leituras Multiarquivo clicando no ícone <Codicon name="gear" /> e navegando até a seção "Contexto" das configurações.

<img src="/img/concurrent-file-reads/concurrent-file-reads-1.png" alt="Configurações de leituras concorrentes de arquivos mostrando controle deslizante de limite" width="600" />

1.  **Limite de Leituras Concorrentes de Arquivos**:
    *   **Configuração**: `Limite de leituras concorrentes de arquivos`
    *   **Descrição**: Esta configuração determina o número máximo de arquivos que o Roo pode ler em uma única solicitação. O padrão é 5, com um intervalo de 1-100 arquivos. Valores mais altos podem acelerar tarefas envolvendo muitos arquivos pequenos, mas podem usar mais memória. Definir o valor como 1 efetivamente desativa as leituras concorrentes, revertendo para leituras de arquivo único.
