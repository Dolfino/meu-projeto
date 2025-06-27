# Ações de Código

As Ações de Código são um recurso poderoso do VS Code que fornecem correções rápidas, refatorações e outras sugestões relacionadas a código diretamente no editor. O Roo Code integra-se a esse sistema para oferecer assistência com IA para tarefas comuns de codificação.

---

## O que são Ações de Código?

As Ações de Código aparecem como um ícone de lâmpada (💡) na área lateral do editor (à esquerda dos números de linha). Elas também podem ser acessadas via menu de contexto (botão direito) ou atalho de teclado. São acionadas quando:

*   Você seleciona um trecho de código.
*   Seu cursor está em uma linha com um problema (erro, aviso ou dica).
*   Você as invoca via comando.

Clicar na lâmpada, clicar com o botão direito e selecionar "Roo Code", ou usar o atalho de teclado (`Ctrl+.` ou `Cmd+.` no macOS, por padrão), exibe um menu de ações disponíveis.

---

## Ações de Código do Roo Code

O Roo Code fornece 5 ações de código, embora sua disponibilidade varie conforme o contexto:

### Ações do Menu de Contexto (Botão Direito)
*   **Adicionar ao Contexto:** Adiciona rapidamente o código selecionado ao seu chat com o Roo, incluindo o nome do arquivo e números de linha para que o Roo saiba exatamente de onde vem o código. Aparece primeiro no menu para fácil acesso.
*   **Explicar Código:** Pede ao Roo Code para explicar o código selecionado.
*   **Melhorar Código:** Pede ao Roo Code para sugerir melhorias no código selecionado.

### Ações Adicionais
*   **Corrigir Código:** Disponível através do menu da lâmpada e da paleta de comandos (mas não no menu de contexto). Pede ao Roo Code para corrigir problemas no código selecionado.
*   **Nova Tarefa:** Cria uma nova tarefa com o código selecionado. Disponível através da paleta de comandos.

### Lógica de Exibição Condicional
O menu da lâmpada mostra ações diferentes com base no contexto:
- **Quando há diagnósticos (erros/avisos):** Apenas "Adicionar ao Contexto" e "Corrigir Código" aparecem
- **Quando não há diagnósticos:** "Adicionar ao Contexto", "Explicar Código" e "Melhorar Código" são mostrados

### Detalhes sobre "Adicionar ao Contexto"

A ação **Adicionar ao Contexto** aparece primeiro no menu de Ações de Código para que você possa rapidamente adicionar trechos de código à sua conversa. Quando você a usa, o Roo Code inclui o nome do arquivo e números de linha junto com o código.

Isso ajuda o Roo a entender o contexto exato do seu código dentro do projeto, permitindo que ele forneça assistência mais relevante e precisa.

**Exemplo de Entrada no Chat:**

```
Você pode explicar esta função?
@meuArquivo.js:15:25
```

*(Onde `@meuArquivo.js:15:25` representa o código adicionado via "Adicionar ao Contexto")*

---

## Usando Ações de Código

Há três formas principais de usar as Ações de Código do Roo Code:

### 1. Pela Lâmpada (💡)

1.  **Selecione o Código:** Selecione o código com o qual deseja trabalhar. Você pode selecionar uma única linha, múltiplas linhas ou um bloco inteiro de código.
2.  **Procure pela Lâmpada:** Um ícone de lâmpada aparecerá na área lateral ao lado do código selecionado (ou da linha com erro/aviso).
3.  **Clique na Lâmpada:** Clique no ícone de lâmpada para abrir o menu de Ações de Código.
4.  **Escolha uma Ação:** Selecione a ação desejada do Roo Code no menu.
5.  **Revise e Aprove:** O Roo Code proporá uma solução no painel de chat. Revise as alterações propostas e aprove ou rejeite.

### 2. Pelo Menu de Contexto (Botão Direito)

1.  **Selecione o Código:** Selecione o código com o qual deseja trabalhar.
2.  **Clique com o Botão Direito:** Clique com o botão direito no código selecionado para abrir o menu de contexto.
3.  **Escolha "Roo Code":** Selecione a opção "Roo Code" no menu de contexto. Um submenu aparecerá com as ações disponíveis do Roo Code.
4.  **Escolha uma Ação:** Selecione a ação desejada no submenu.
5.  **Revise e Aprove:** O Roo Code proporá uma solução no painel de chat. Revise as alterações propostas e aprove ou rejeite.

### 3. Pela Paleta de Comandos

1.  **Selecione o Código:** Selecione o código com o qual deseja trabalhar.
2.  **Abra a Paleta de Comandos:** Pressione `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (macOS).
3.  **Digite um Comando:** Digite "Roo Code" para filtrar os comandos, então escolha a ação de código relevante (ex: "Roo Code: Explicar Código"). A ação será aplicada no contexto mais lógico (geralmente a tarefa de chat ativa atual, se existir).
4.  **Revise e Aprove:** O Roo Code proporá uma solução no painel de chat. Revise as alterações propostas e aprove ou rejeite.

---

## Ações de Terminal

O Roo Code também fornece ações similares para saída de terminal:

*   **Terminal: Adicionar ao Contexto:** Adiciona a saída de terminal selecionada ao seu chat
*   **Terminal: Corrigir Comando:** Pede ao Roo Code para corrigir um comando de terminal que falhou
*   **Terminal: Explicar Comando:** Pede ao Roo Code para explicar saída ou comandos de terminal

Essas ações estão disponíveis quando você seleciona texto no terminal e clica com o botão direito.

---

## Personalizando Prompts de Ações de Código

Você pode personalizar os prompts usados para cada Ação de Código modificando os "Prompts de Suporte" na aba **Prompts**. Isso permite ajustar as instruções dadas ao modelo de IA e adaptar as respostas às suas necessidades específicas.

1.  **Abra a Aba Prompts:** Clique no ícone <Codicon name="notebook" /> na barra de menu superior do Roo Code.
2. **Encontre "Prompts de Suporte":** Você verá os prompts de suporte, incluindo "Aprimorar Prompt", "Explicar Código", "Melhorar Código" e "Corrigir Código".
3. **Edite os Prompts:** Modifique o texto na área de texto para o prompt que deseja personalizar. Os prompts usam espaços reservados no formato `${placeholder}`:
    - `${filePath}` - O caminho do arquivo atual
    - `${selectedText}` - O texto atualmente selecionado
    - `${diagnostics}` - Quaisquer mensagens de erro ou aviso (para Corrigir Código)
4. **Clique em "Concluído":** Salve suas alterações.

### Exemplo de Modelo de Prompt
```
Por favor, explique o seguinte código de ${filePath}:

${selectedText}
```

Ao usar as Ações de Código do Roo Code, você pode obter rapidamente assistência com IA diretamente em seu fluxo de trabalho de codificação. Isso pode economizar seu tempo e ajudá-lo a escrever um código melhor.
