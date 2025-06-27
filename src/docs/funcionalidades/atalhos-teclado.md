---
sidebar_label: Navegação por Teclado
---

# Navegação por Teclado

A interface do Roo Code suporta navegação por teclado e atalhos para agilizar seu fluxo de trabalho e reduzir a dependência de interações com o mouse.

---

## Comandos de Teclado Disponíveis

O Roo Code oferece comandos de teclado para melhorar seu fluxo de trabalho. Esta página foca no comando `roo.acceptInput`, mas aqui está uma referência rápida de todos os comandos de teclado:

| Comando | Descrição | Atalho Padrão |
|---------|-------------|-----------------|
| `roo.acceptInput` | Enviar texto ou aceitar a sugestão principal | Nenhum (configurável) |
| `roo.focus` | Focar na caixa de entrada do Roo | Nenhum (configurável) |
| Setas Cima/Baixo | Navegar pelo histórico de prompts | Integrado |

### Principais Benefícios dos Comandos de Teclado

* **Interface Orientada por Teclado**: Enviar texto ou selecionar o botão de sugestão principal sem interação com o mouse
* **Melhor Acessibilidade**: Essencial para usuários com limitações de mobilidade ou desconforto com o uso do mouse
* **Compatibilidade com Vim/Neovim**: Suporta transições perfeitas para desenvolvedores vindos de ambientes centrados no teclado
* **Eficiência no Fluxo de Trabalho**: Reduz a alternância de contexto entre teclado e mouse durante tarefas de desenvolvimento

---

## Comando roo.acceptInput

O comando `roo.acceptInput` permite enviar texto ou aceitar sugestões com atalhos de teclado em vez de clicar em botões ou pressionar Enter na área de entrada.

### O Que Ele Faz

O comando `roo.acceptInput` é um comando de envio de entrada de propósito geral. Quando acionado, ele:

- Envia seu texto ou entrada de imagem atual quando na área de entrada de texto (equivalente a pressionar Enter)
- Clica no botão principal (primeiro) quando botões de ação estão visíveis (como botões de confirmação/cancelamento ou qualquer outro botão de ação)

### Guia Detalhado de Configuração

#### Método 1: Usando a Interface do VS Code

1. Abra a Paleta de Comandos (`Ctrl+Shift+P` ou `Cmd+Shift+P` no Mac)
2. Digite "Preferências: Abrir Atalhos de Teclado"
3. Na caixa de pesquisa, digite "roo.acceptInput"
4. Localize "Roo: Aceitar Entrada/Sugestão" nos resultados
5. Clique no ícone + à esquerda do comando
6. Pressione a combinação de teclas desejada (ex: `Ctrl+Enter` ou `Alt+Enter`)
7. Pressione Enter para confirmar

#### Método 2: Editando keybindings.json diretamente

1. Abra a Paleta de Comandos (`Ctrl+Shift+P` ou `Cmd+Shift+P` no Mac)
2. Digite "Preferências: Abrir Atalhos de Teclado (JSON)"
3. Adicione a seguinte entrada ao array JSON:

```json
{
  "key": "ctrl+enter",  // ou sua combinação de teclas preferida
  "command": "roo.acceptInput",
  "when": "rooViewFocused"  // Esta é uma condição de contexto que garante que o comando só funcione quando o Roo estiver em foco
}
```

Você também pode usar uma condição mais específica:
```json
{
  "key": "ctrl+enter",
  "command": "roo.acceptInput",
  "when": "webviewViewFocus && webviewViewId == 'roo-cline.SidebarProvider'"
}
```

#### Combinações de Teclas Recomendadas

Escolha uma combinação de teclas que não entre em conflito com os atalhos existentes do VS Code:

- `Alt+Enter` - Fácil de pressionar enquanto digita
- `Ctrl+Space` - Familiar para quem usa autocompletar
- `Ctrl+Enter` - Intuitivo para execução de comandos
- `Alt+A` - Mnemônico para "Aceitar"

### Casos de Uso Práticos

#### Fluxos de Trabalho Rápidos

- **Envio de Texto**: Envie mensagens para o Roo sem tirar as mãos do teclado
- **Confirmações de Ação**: Aceite operações como salvar arquivos, executar comandos ou aplicar diffs
- **Processos em Múltiplas Etapas**: Avance rapidamente por etapas que exigem confirmação ou entrada
- **Tarefas Consecutivas**: Encadeie várias tarefas com interrupção mínima

#### Desenvolvimento Centrado no Teclado

- **Fluxos de Trabalho Vim/Neovim**: Se você vem de um ambiente Vim/Neovim, mantenha seu fluxo de trabalho focado no teclado
- **Integração com IDE**: Use junto com outros atalhos de teclado do VS Code para uma experiência perfeita
- **Revisões de Código**: Aceite rapidamente sugestões ao revisar código com o Roo
- **Escrita de Documentação**: Envie texto e aceite sugestões de formatação ao gerar documentação

#### Casos de Uso de Acessibilidade

- **Limitações de Mobilidade nas Mãos**: Essencial para usuários com dificuldade em usar o mouse
- **Prevenção de Lesões por Esforço Repetitivo**: Reduza o uso do mouse para prevenir ou gerenciar lesões por esforço repetitivo
- **Integração com Leitores de Tela**: Funciona bem com leitores de tela para usuários com deficiência visual
- **Compatibilidade com Controle por Voz**: Pode ser acionado via comandos de voz ao usar software de controle por voz

### Benefícios de Acessibilidade

O comando `roo.acceptInput` foi projetado com acessibilidade em mente:

- **Redução da Dependência do Mouse**: Complete fluxos de trabalho inteiros sem precisar do mouse
- **Redução de Tensão Física**: Ajuda usuários que sentem desconforto ou dor ao usar o mouse
- **Método de Entrada Alternativo**: Suporta usuários com deficiências de mobilidade que dependem de navegação por teclado
- **Otimização do Fluxo de Trabalho**: Particularmente valioso para usuários vindos de ambientes centrados no teclado como Vim/Neovim

### Fluxos de Trabalho Centrados no Teclado

Aqui estão alguns exemplos completos de fluxos de trabalho mostrando como usar efetivamente atalhos de teclado com o Roo:

#### Exemplo de Fluxo de Desenvolvimento

1. Abra o VS Code e navegue até seu projeto
2. Abra o Roo através da barra lateral
3. Digite sua solicitação: "Crie um endpoint REST API para registro de usuário"
4. Quando o Roo perguntar sobre preferências de framework, use seu atalho `roo.acceptInput` para selecionar a primeira sugestão
5. Continue usando o atalho para aceitar sugestões de geração de código
6. Quando o Roo oferecer para salvar o arquivo, use o atalho novamente para confirmar
7. Use os atalhos internos do VS Code para navegar pelos arquivos criados

#### Fluxo de Revisão de Código

1. Selecione o código que deseja revisar e use o comando "Copiar" do VS Code
2. Peça ao Roo para revisá-lo: "Revise este código em busca de problemas de segurança"
3. Enquanto o Roo faz perguntas esclarecedoras sobre o contexto do código, use seu atalho para aceitar sugestões
4. Quando o Roo fornecer recomendações de melhoria, use o atalho novamente para aceitar sugestões de implementação

### Solução de Problemas

| Problema | Solução |
|-------|----------|
| Atalho não funciona | Certifique-se de que o Roo está em foco (clique no painel do Roo primeiro) |
| Sugestão errada selecionada | O comando sempre seleciona o primeiro botão (principal); use o mouse se precisar de uma opção diferente |
| Conflitos com atalhos existentes | Tente uma combinação de teclas diferente nas configurações de teclado do VS Code |
| Nenhum feedback visual quando usado | Isso é normal - o comando ativa silenciosamente a função sem confirmação visual |
| Atalho funciona inconsistentemente | Certifique-se de que a cláusula `when` está configurada corretamente em seu keybindings.json (ou `rooViewFocused` ou a condição específica do webview) |

### Implementação Técnica

O comando `roo.acceptInput` é implementado da seguinte forma:

- Comando registrado como `roo.acceptInput` com título de exibição "Roo: Aceitar Entrada/Sugestão" na paleta de comandos
- Quando acionado, envia uma mensagem "acceptInput" para o webview ativo do Roo
- O webview determina a ação apropriada com base no estado atual da UI:
  - Clica no botão de ação principal se os botões de ação estiverem visíveis e habilitados
  - Envia a mensagem se a área de texto estiver habilitada e contiver texto/imagens
- Nenhuma vinculação de tecla padrão - os usuários atribuem seu atalho preferido

### Limitações

- Funciona apenas quando a interface do Roo está ativa
- Não tem efeito se nenhuma entrada ou sugestão estiver disponível no momento
- Prioriza o botão principal (primeiro) quando várias opções são mostradas

---

## Navegação pelo Histórico de Prompts no Estilo Linha de Comando

Navegue pelo seu histórico de prompts com uma experiência semelhante a um terminal usando as teclas de seta. Este recurso facilita a reutilização e refinamento de prompts anteriores, seja da sua conversa atual ou de tarefas passadas.

### Principais Recursos
- **Setas Cima/Baixo**: Percorra os prompts anteriores.
- **Consciente do Contexto**: Alterna entre histórico de conversa e de tarefas.
- **Preserva Entrada**: Lembra o que você estava digitando.

### Por Que Isso é Importante

**Antes**: Reutilizar um prompt significava rolar para cima, copiar e colar.
- Tedioso e lento
- Fácil de perder seu lugar
- Interrompia seu fluxo de trabalho

**Com Navegação pelo Histórico de Prompts**: Acesse rapidamente prompts anteriores sem sair do teclado.

### Como Funciona

A navegação é projetada para ser intuitiva e se adaptar ao seu contexto atual.

#### Em uma Conversa Ativa
- **Seta Cima**: Mostra o último prompt que você enviou. Continue pressionando para voltar mais na conversa.
- **Seta Baixo**: Avança pelo histórico da conversa, eventualmente retornando ao texto que você estava digitando.

#### Iniciando um Novo Chat
- **Seta Cima**: Mostra o prompt mais recente do seu histórico de tarefas no workspace atual.
- **Seta Baixo**: Avança pelo seu histórico de tarefas.

#### Casos Especiais
- Se você começar a digitar enquanto navega, o histórico é descartado e seu novo texto é preservado.
- A navegação só funciona quando o cursor está na primeira ou última linha da caixa de entrada para evitar interferir com edição de múltiplas linhas.

### Configuração

Este recurso está habilitado por padrão. Não há configurações para ajustar.

### Benefícios

- **Fluxo de Trabalho Mais Rápido**: Reutilize prompts sem usar o mouse.
- **Melhor Contexto**: Acesse e construa facilmente sobre interações anteriores.
- **Menos Interrupção**: Mantenha o foco na tarefa atual.

### Perguntas Comuns

**"Por que nada acontece quando eu pressiono a seta para cima?"**
- Você pode estar no meio de um prompt de múltiplas linhas. O cursor deve estar na primeira linha.
- Pode não haver histórico disponível para o contexto atual.

**"Qual é a diferença entre histórico de conversa e histórico de tarefas?"**
- **Histórico de conversa** inclui prompts da sua sessão de chat ativa atual.
- **Histórico de tarefas** inclui os prompts iniciais de todas as tarefas anteriores no seu workspace atual.
