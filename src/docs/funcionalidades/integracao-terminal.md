# Integração com Terminal Shell

A Integração com Terminal Shell é um recurso fundamental que permite ao Roo Code executar comandos no seu terminal e processar inteligentemente sua saída. Essa comunicação bidirecional entre a IA e seu ambiente de desenvolvimento desbloqueia poderosas capacidades de automação.

---

## O que é Integração Shell?

A integração shell é ativada automaticamente no Roo Code e se conecta diretamente ao ciclo de execução de comandos do seu terminal sem exigir configuração adicional. Esse recurso integrado permite que o Roo:

- Execute comandos em seu nome através da ferramenta [`execute_command`](/advanced-usage/available-tools/execute-command)
- Leia a saída de comandos em tempo real sem copiar/colar manual
- Detecte e corrija automaticamente erros em aplicações em execução
- Observe códigos de saída para determinar sucesso ou falha
- Acompanhe mudanças de diretório de trabalho conforme você navega no projeto
- Reaja inteligentemente à saída do terminal sem intervenção do usuário
- Pare comandos em execução diretamente da interface de chat usando o botão de parada que aparece ao lado da mensagem de execução do comando.

<img src="/img/v3.15/v3.15.png" alt="Botão Parar Comando na UI do Chat" width="600" />

Quando você pede ao Roo para executar tarefas como instalar dependências, iniciar um servidor de desenvolvimento ou analisar erros de build, a integração shell trabalha nos bastidores para tornar essas interações suaves e eficazes.

---

## Solução de Problemas da Integração Shell

A integração shell está integrada ao Roo Code e funciona automaticamente na maioria dos casos. Se você vir mensagens "Integração Shell Indisponível" ou tiver problemas com execução de comandos, tente estas soluções:

1. **Atualize o VSCode/Cursor** para a versão mais recente (VSCode 1.93+ necessário)
2. **Certifique-se de que um shell compatível está selecionado**: Paleta de Comandos (`Ctrl+Shift+P` ou `Cmd+Shift+P`) → "Terminal: Selecionar Perfil Padrão" → Escolha bash, zsh, PowerShell ou fish
3. **Usuários do Windows PowerShell**: Execute `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` e reinicie o VSCode
4. **Usuários WSL**: Adicione `. "$(code --locate-shell-integration-path bash)"` ao seu `~/.bashrc`

---

## Fallback de Execução de Comandos

O Roo Code tem um mecanismo de fallback para execução de comandos. Isso é mais relevante se você optou por usar a integração de terminal do VS Code (desmarcando a configuração [`Desativar integração shell do terminal`](#desativar-integracao-shell-do-terminal)) e essa integração falhar.

- **Como funciona**: Se o Roo Code estiver configurado para usar a integração de terminal do VS Code mas não conseguir conectar ou encontrar problemas, ele pode tentar executar o comando diretamente usando um processo em segundo plano. Isso é um fallback para garantir que o comando ainda tente ser executado.
- **Notificação**: Você pode ver uma notificação no chat se esse fallback for usado, indicando que o comando está sendo executado sem os recursos completos do terminal inline do Roo ou da integração shell do VS Code (por exemplo, streaming de saída em tempo real ou detecção precisa de código de saída podem ser limitados).
<img src="/img/v3.15.0/v3.15.0.png" alt="Exemplo de notificação de fallback de execução de comando" width="600" />

- **Resolução**: Se você encontrar esse fallback, normalmente indica um problema com sua configuração de integração shell do VS Code. Revise as etapas de solução de problemas neste documento ou considere usar o terminal inline recomendado pelo Roo Code, garantindo que a configuração [`Desativar integração shell do terminal`](#desativar-integracao-shell-do-terminal) esteja MARCADA.

<img src="/img/shell-integration/shell-integration-12.png" alt="Terminal inline recomendado do Roo Code em ação" width="600" />
*Exemplo do terminal inline recomendado do Roo Code.*

---

## Configurações de Integração Terminal

O Roo Code fornece configurações para ajustar como ele interage com terminais. Para acessar essas configurações:
1. Clique no ícone <Codicon name="gear" /> no canto superior direito da barra lateral do Roo Code.
2. No painel de configurações que abrir, selecione o grupo "Terminal" no menu à esquerda.

### Configurações Básicas

#### Limite de Saída do Terminal
<img src="/img/shell-integration/shell-integration.png" alt="Controle deslizante de limite de saída do terminal definido para 500" width="600" />
Esta configuração controla quanta saída o Roo Code captura de seus comandos. Considere diminuir se estiver preocupado com uso de tokens ou se o Roo parecer lento processando saídas muito longas (você ainda obterá o início e o fim). Considere aumentar se frequentemente precisar de mais conteúdo do meio de comandos longos diretamente no contexto do Roo, mas esteja atento aos possíveis custos de tokens. Padrão: 500 linhas.

#### Comprimir saída de barra de progresso
<img src="/img/shell-integration/shell-integration-10.png" alt="Caixa de seleção Comprimir saída de barra de progresso" width="600" />
Mantenha isso ativado (padrão) para saída mais limpa e economia de tokens. Faz o Roo Code processar saída dinâmica como barras de progresso ou spinners mais como um terminal real, mostrando apenas o estado final. Desative apenas em casos raros onde você especificamente precisa depurar a saída bruta intermediária de uma barra de progresso ou exibição dinâmica similar.

### Configurações Avançadas

:::info Importante
**Reinicialização do terminal necessária para estas configurações**

Alterações nas configurações avançadas do terminal só têm efeito após reiniciar seus terminais. Para reiniciar um terminal:

1. Clique no ícone de lixeira no painel do terminal para fechar o terminal atual
2. Abra um novo terminal com Terminal → Novo Terminal ou <kbd>Ctrl</kbd>+<kbd>`</kbd> (acento grave)

Sempre reinicie todos os terminais abertos após alterar qualquer uma dessas configurações.
:::

#### Herdar variáveis de ambiente
<img src="/img/shell-integration/shell-integration-11.png" alt="Caixa de seleção Herdar variáveis de ambiente" width="600" />
Esta configuração controla se as sessões de terminal do Roo Code usam as mesmas variáveis de ambiente (como `PATH`, chaves de API, etc.) que seu ambiente principal do VSCode/Cursor. Espelha diretamente a configuração global do VSCode [`terminal.integrated.inheritEnv`](https://code.visualstudio.com/docs/editor/integrated-terminal#_inherit-environment-variables). Mantenha isso ativado (padrão para VSCode) se quiser que os comandos do Roo operem com o mesmo contexto e ferramentas disponíveis no seu terminal regular do VSCode. Considere desativar apenas se precisar de um ambiente completamente limpo e isolado para tarefas de terminal do Roo ou estiver solucionando conflitos complexos de variáveis de ambiente.

### Ambiente de Tempo de Execução
No macOS (e possivelmente outros sistemas operacionais) o ambiente fornecido ao VSCode e consequentemente ao Roo Code pode variar dependendo de como o VSCode é iniciado.
Se iniciado a partir da linha de comando `vscode`, o VSCode e o Roo Code herdarão o ambiente do shell que o iniciou, e tudo (geralmente) funcionará bem.
Se iniciado a partir do Finder, Dock ou Spotlight, o ambiente exportado de `.zshrc` ou `.zprofile` provavelmente estará ausente. Se você tiver variáveis de ambiente definidas em um desses arquivos e descobrir que estão ausentes ao executar o VSCode, mova-as para .zshenv e faça logout e login novamente, para que o gerenciador de janelas pegue as novas configurações de ambiente.

#### Desativar integração shell do terminal
<img src="/img/shell-integration/shell-integration-9.png" alt="Caixa de seleção Desativar integração shell do terminal" width="600" />
Esta configuração determina como o Roo Code executa comandos de terminal.
-   **Mantenha esta caixa de seleção MARCADA (recomendado):** O Roo Code executará comandos usando seu terminal inline integrado, exibindo a saída diretamente na interface de chat. Este método é geralmente robusto, fornece saída clara e é a forma preferida para a maioria dos usuários interagir com comandos de terminal através do Roo Code. Ele garante que os comandos sejam executados em um ambiente consistente gerenciado pelo Roo Code.

    <img src="/img/shell-integration/shell-integration-12.png" alt="Terminal inline do Roo Code com 'Desativar integração shell do terminal' MARCADA" width="600" />
    *Terminal inline do Roo Code, ativo quando "Desativar integração shell do terminal" está MARCADA.*

-   **DESMARQUE esta caixa de seleção (para usar a integração de terminal do VS Code):** O Roo Code tentará executar comandos diretamente dentro do painel de terminal ativo do VS Code. Este método alternativo pode ser útil para casos específicos onde você explicitamente precisa que comandos sejam executados dentro do seu ambiente shell totalmente personalizado do VS Code ou requer interação com recursos específicos do terminal do VS Code para um comando. No entanto, isso pode às vezes ser menos confiável dependendo da sua configuração shell e versão do VS Code.

As seguintes configurações são opções avançadas que se aplicam **apenas se você DESMARCOU 'Desativar integração shell do terminal'** (escolhendo usar a integração de terminal do VS Code em vez do terminal inline recomendado do Roo Code):

##### Tempo limite de integração shell do terminal
<img src="/img/shell-integration/shell-integration-1.png" alt="Controle deslizante de tempo limite de integração shell do terminal definido para 15s" width="600" />
Se a integração shell estiver ativada mas você ainda vir 'Integração Shell Indisponível', especialmente com configurações shell complexas (ex: Zsh com muitos plugins, ou um ambiente corporativo de carregamento lento), seu shell pode estar demorando muito para inicializar. Aumente este valor para dar ao seu shell mais tempo para sinalizar sua prontidão para o Roo Code. Tente incrementos de 5-10 segundos. Padrão: 15s (como mostrado na UI).

##### Atraso de comando do terminal
<img src="/img/shell-integration/shell-integration-2.png" alt="Controle deslizante de atraso de comando do terminal definido para 0ms" width="600" />
Se a saída do comando aparecer incompleta ou o Roo parecer perder o final da saída de um comando (mesmo com integração shell ativada), um pequeno atraso pode ajudar. Introduza um pequeno atraso (ex: 50ms ou 100ms). Isso dá ao terminal mais tempo para liberar toda a saída antes que o Roo Code considere o comando completo. Esta é uma solução alternativa para possíveis problemas de tempo no terminal do VS Code ou certos shells (veja bug do VSCode [#237208](https://github.com/microsoft/vscode/issues/237208)). Padrão: 0ms.

##### Ativar solução alternativa para contador do PowerShell
<img src="/img/shell-integration/shell-integration-3.png" alt="Caixa de seleção Ativar solução alternativa para contador do PowerShell" width="600" />
Específico para usuários do PowerShell. Ative isso se você descobrir que o Roo Code tem dificuldade em executar *exatamente o mesmo comando PowerShell várias vezes seguidas*, ou se a captura de saída de comandos PowerShell for pouco confiável. Isso adiciona um contador único aos comandos para ajudar o PowerShell a diferenciá-los.

##### Limpar marca EOL do ZSH
<img src="/img/shell-integration/shell-integration-4.png" alt="Caixa de seleção Limpar marca EOL do ZSH" width="600" />
Específico para usuários do Zsh. O Zsh às vezes adiciona um caractere especial (frequentemente `%`) no final de uma linha se ela não terminar com uma nova linha. Ative isso se o Roo Code parecer interpretar mal ou ficar confuso com a saída de comandos Zsh, particularmente se a última linha da saída parecer incluir um caractere inesperado. Isso tenta remover esse marcador (`PROMPT_EOL_MARK=''`).

##### Ativar integração Oh My Zsh
<img src="/img/shell-integration/shell-integration-5.png" alt="Caixa de seleção Ativar integração Oh My Zsh" width="600" />
Para usuários da popular estrutura Oh My Zsh para Zsh. Ative isso se você usar Oh My Zsh e tiver problemas gerais com execução de comandos de terminal ou renderização de saída que não sejam resolvidos por outras configurações. Isso ajuda o Roo Code a se alinhar com os mecanismos específicos de integração shell do Oh My Zsh definindo `ITERM_SHELL_INTEGRATION_INSTALLED=Yes`. Reiniciar o IDE pode ser necessário.

##### Ativar integração Powerlevel10k
<img src="/img/shell-integration/shell-integration-6.png" alt="Caixa de seleção Ativar integração Powerlevel10k" width="600" />
Para usuários do tema Powerlevel10k para Zsh. Ative isso se seu prompt Powerlevel10k (que pode ser bastante complexo) parecer interferir na capacidade do Roo Code de detectar corretamente limites de comandos, analisar saída ou rastrear o diretório de trabalho atual. Isso define `POWERLEVEL9K_TERM_SHELL_INTEGRATION=true`.

##### Ativar manipulação ZDOTDIR
<img src="/img/shell-integration/shell-integration-7.png" alt="Caixa de seleção Ativar manipulação ZDOTDIR" width="600" />
Uma opção avançada para usuários Zsh com locais personalizados de arquivos de inicialização Zsh. Ative isso se você usar `ZDOTDIR` para especificar um diretório personalizado para seus arquivos de configuração Zsh (como `.zshrc`). Esta configuração ajuda o Roo Code a funcionar corretamente com tais configurações criando um `ZDOTDIR` isolado e temporário para seus próprios scripts de integração, prevenindo conflitos com seu ambiente Zsh pessoal.

---

## Como a Integração Shell Funciona

A integração shell conecta o Roo ao processo de execução de comandos do seu terminal em tempo real:

1. **Conexão**: Quando você abre um terminal, o VS Code estabelece uma conexão especial com seu shell.

2. **Rastreamento de Comandos**: O VS Code monitora suas atividades de terminal detectando:
   - Quando um novo prompt aparece
   - Quando você insere um comando
   - Quando o comando começa a ser executado
   - Quando o comando termina (e se teve sucesso ou falhou)
   - Em qual diretório você está atualmente

3. **Shells Diferentes, Mesmo Resultado**: Cada tipo de shell (Bash, Zsh, PowerShell, Fish) implementa isso de forma ligeiramente diferente nos bastidores, mas todos fornecem a mesma funcionalidade para o Roo.

4. **Coleta de Informações**: O Roo pode ver quais comandos estão sendo executados, onde estão sendo executados, quanto tempo levam, se têm sucesso e sua saída completa - tudo sem que você precise copiar e colar nada.

---

## Solução de Problemas de Integração Shell

### Política de Execução do PowerShell (Windows)

O PowerShell restringe a execução de scripts por padrão. Para configurar:

1. Abra o PowerShell como Administrador
2. Verifique a política atual: `Get-ExecutionPolicy`
3. Defina a política apropriada: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`

Políticas comuns:
- `Restricted`: Nenhum script permitido (padrão)
- `RemoteSigned`: Scripts locais podem ser executados; scripts baixados precisam ser assinados
- `Unrestricted`: Todos os scripts são executados com avisos
- `AllSigned`: Todos os scripts devem ser assinados

### Instalação Manual de Integração Shell

Se a integração automática falhar, adicione a linha apropriada à sua configuração shell:

**Bash** (`~/.bashrc`):
```bash
[[ "$TERM_PROGRAM" == "vscode" ]] && . "$(code --locate-shell-integration-path bash)"
```

**Zsh** (`~/.zshrc`):
```bash
[[ "$TERM_PROGRAM" == "vscode" ]] && . "$(code --locate-shell-integration-path zsh)"
```

**PowerShell** (`$Profile`):
```powershell
if ($env:TERM_PROGRAM -eq "vscode") { . "$(code --locate-shell-integration-path pwsh)" }
```

**Fish** (`~/.config/fish/config.fish`):
```fish
string match -q "$TERM_PROGRAM" "vscode"; and . (code --locate-shell-integration-path fish)
```

### Problemas de Personalização de Terminal

Se você usar ferramentas de personalização de terminal:

**Powerlevel10k**:
```bash
# Adicione antes de carregar powerlevel10k em ~/.zshrc
typeset -g POWERLEVEL9K_TERM_SHELL_INTEGRATION=true
```

**Alternativa**: Ative a configuração de Integração Powerlevel10k no Roo Code.

### Verificando Status da Integração Shell

Confirme que a integração shell está ativa com estes comandos:

**Bash**:
```bash
set | grep -i '[16]33;'
echo "$PROMPT_COMMAND" | grep vsc
trap -p DEBUG | grep vsc
```

**Zsh**:
```zsh
functions | grep -i vsc
typeset -p precmd_functions preexec_functions
```

**PowerShell**:
```powershell
Get-Command -Name "*VSC*" -CommandType Function
Get-Content Function:\Prompt | Select-String "VSCode"
```

**Fish**:
```fish
functions | grep -i vsc
functions fish_prompt | grep -i vsc
```

Indicadores visuais de integração shell ativa:
1. Indicador de integração shell na barra de título do terminal
2. Destaque de detecção de comandos
3. Atualizações de diretório de trabalho no título do terminal
4. Relatório de duração e código de saída de comandos

---

## Métodos de Integração Terminal WSL

Ao usar o Windows Subsystem for Linux (WSL), existem duas formas distintas de usar o VSCode com WSL, cada uma com implicações diferentes para integração shell:

### Método 1: VSCode Windows com Terminal WSL

Nesta configuração:
- VSCode é executado nativamente no Windows
- Você usa o recurso de integração de terminal WSL no VSCode
- Comandos shell são executados através da ponte WSL
- Pode experimentar latência adicional devido à comunicação Windows-WSL
- Marcadores de integração shell podem ser afetados pelo limite WSL-Windows: você deve garantir que `source "$(code --locate-shell-integration-path <shell>)"` seja carregado para seu shell dentro do ambiente WSL porque pode não ser carregado automaticamente; veja acima.

### Método 2: VSCode Executando Dentro do WSL

Nesta configuração:
- Você inicia o VSCode diretamente de dentro do WSL usando `code .`
- Servidor VSCode é executado nativamente no ambiente Linux
- Acesso direto ao sistema de arquivos Linux e ferramentas
- Melhor desempenho e confiabilidade para integração shell
- Integração shell é carregada automaticamente já que o VSCode é executado nativamente no ambiente Linux
- Abordagem recomendada para desenvolvimento WSL

Para integração shell ideal com WSL, recomendamos:
1. Abra sua distribuição WSL
2. Navegue até seu diretório de projeto
3. Inicie o VSCode usando `code .`
4. Use o terminal integrado dentro do VSCode

---

## Problemas Conhecidos e Soluções Alternativas

### Cygwin (bash, zsh)

O Cygwin fornece um ambiente Unix-like em sistemas Windows. Para configurar o Cygwin como seu terminal no VS Code:

1. Instale o Cygwin de [https://www.cygwin.com/](https://www.cygwin.com/)

2. Abra as configurações do VS Code:
   - Selecione Arquivo > Preferências > Configurações
   - Clique no ícone "Abrir Configurações (JSON)" no canto superior direito

3. Adicione a seguinte configuração ao seu `settings.json` (dentro das chaves principais `{}`):
   ```json
   {
     "terminal.integrated.profiles.windows": {
       "Cygwin": {
         "path": "C:\\cygwin64\\bin\\bash.exe",
         "args": ["--login"],
         "env": {"CHERE_INVOKING": "1"}
       }
     },
     "terminal.integrated.defaultProfile.windows": "Cygwin"
   }
   ```

   > Nota: Se você tiver o Cygwin de 32 bits instalado, use `"C:\\cygwin\\bin\\bash.exe"` para o caminho.

4. Entendendo a configuração:
   - `path`: Aponta para o executável Bash na sua instalação Cygwin
   - `args`: A flag `--login` garante que o shell leia os arquivos de perfil
   - `env`: A variável de ambiente `CHERE_INVOKING` diz ao Cygwin para usar o diretório atual como diretório de trabalho
   - `terminal.integrated.defaultProfile.windows`: Define o Cygwin como o perfil de terminal padrão

5. Para abrir um novo terminal Cygwin:
   - Pressione Ctrl+Shift+(acento grave) para abrir um novo terminal, ou
   - Pressione `F1`, digite "Terminal: Criar Novo Terminal (com Perfil)", e selecione "Cygwin"

Embora nossos testes mostrem que isso funciona imediatamente, se você encontrar problemas de integração shell com Cygwin, certifique-se de ter adicionado os ganchos apropriados de integração shell ao seu perfil bash do Cygwin conforme descrito na seção "Instalação Manual de Integração Shell".

### Integração Shell do VS Code para Fish + Cygwin no Windows

Para usuários Windows executando terminal Fish em um ambiente Cygwin, veja como funciona a integração shell do VS Code:

1.  **(Opcional) Localize o Script de Integração Shell:**
    Abra seu terminal Fish *dentro do VS Code* e execute o seguinte comando:
    ```bash
    code --locate-shell-integration-path fish
    ```
    Isso irá gerar o caminho para o script `shellIntegration.fish`. Anote este caminho.

2.  **Atualize Sua Configuração Fish:**
    Edite seu arquivo `config.fish` (geralmente localizado em `~/.config/fish/config.fish` dentro do seu diretório home Cygwin). Adicione a seguinte linha, preferencialmente dentro de um bloco `if status is-interactive` ou no final do arquivo:

    ```fish
    # Exemplo de estrutura config.fish
    if status is-interactive
        # Suas outras configurações de shell interativo...
        # localização automática do script de integração:
        string match -q "$TERM_PROGRAM" "vscode"; and . (code --locate-shell-integration-path fish)

        # Ou se o acima falhar para você:
        # Carregue o script de integração shell do VS Code
        # IMPORTANTE: Substitua o caminho de exemplo abaixo pelo caminho real que você encontrou no Passo 1.
        # Certifique-se de que o caminho está em um formato que o Cygwin pode entender (ex: usando /cygdrive/c/...).
        # source "/cygdrive/c/Users/SeuUsuario/.vscode/extensions/..../shellIntegration.fish"
    end
    ```
    *Lembre-se de substituir o caminho de exemplo pelo caminho real do Passo 1, formatado corretamente para Cygwin.*

3.  **Configure o Perfil de Terminal do VS Code:**
    Abra seu arquivo `settings.json` do VS Code (Ctrl+Shift+P -> "Preferências: Abrir Configurações do Usuário (JSON)"). Atualize ou adicione o perfil Fish em `terminal.integrated.profiles.windows` assim:

    ```json
    {
      // ... outras configurações ...

      "terminal.integrated.profiles.windows": {
        // ... outros perfis ...

        // Recomendado: Use bash.exe para iniciar fish como um shell de login
        "fish": {
          "path": "C:\\cygwin64\\bin\\bash.exe", // Ou seu caminho bash Cygwin
          "args": [
            "--login", // Garante que scripts de login sejam executados (importante para ambiente Cygwin)
            "-i",      // Garante que bash seja executado interativamente
            "-c",
            "exec fish" // Substitui o processo bash por fish
          ],
          "icon": "terminal-bash" // Opcional: Use um ícone reconhecível
        }
        // Alternativa (se o acima falhar): Inicie fish diretamente
        "fish-direct": {
          "path": "C:\\cygwin64\\bin\\fish.exe", // Certifique-se de que isso está no seu PATH Windows ou forneça o caminho completo
          // Use 'options' aqui em vez de 'args'; caso contrário, você pode encontrar o erro "terminal process terminated exit code 1".
          "options": ["-l", "-c"], // Exemplo: flags de login e interativo.
          "icon": "terminal-fish" // Opcional: Use um ícone fish
        }
      },

      // Opcional: Defina fish como seu padrão se desejar
    ---
    ```

4.  **Reinicie o VS Code:**
    Feche e reabra completamente o Visual Studio Code para aplicar as alterações.

5.  **Verifique:**
    Abra um novo terminal Fish no VS Code. Os recursos de integração shell (como decorações de comando, melhor navegação no histórico de comandos, etc.) agora devem estar ativos. Você pode testar a funcionalidade básica executando comandos simples como `echo "Olá do Fish integrado!"`. <img src="/img/shell-integration/shell-integration-8.png" alt="Exemplo de Integração Fish Cygwin" width="600" />

Esta configuração funciona de forma confiável em sistemas Windows usando Cygwin, Fish e o prompt Starship, e deve ajudar usuários com configurações similares.

### Falhas de Integração Shell Após VSCode 1.98

**Problema**: Após atualizações do VSCode além da versão 1.98, a integração shell pode falhar com o erro "Sequência de escape de início de saída VSCE (]633;C ou ]133;C) não recebida".

**Soluções**:
1. **Definir Atraso de Comando Terminal**:
   - Defina o Atraso de Comando Terminal para 50ms nas configurações do Roo Code
   - Reinicie todos os terminais após alterar esta configuração
   - Isso corresponde ao comportamento padrão mais antigo e pode resolver o problema, no entanto alguns usuários relataram que um valor de 0ms funciona melhor. Esta é uma solução alternativa para problemas upstream do VSCode.

2. **Reverter Versão do VSCode**:
   - Baixe o VSCode v1.98 de [Atualizações do VSCode](https://code.visualstudio.com/updates/v1_98)
   - Substitua sua instalação atual do VSCode
   - Nenhum backup das configurações do Roo é necessário

3. **Solução Alternativa Específica para WSL**:
   - Se usar WSL, certifique-se de iniciar o VSCode de dentro do WSL usando `code .`

4. **Usuários ZSH**:
   - Tente ativar algumas ou todas as soluções alternativas relacionadas ao ZSH nas configurações do Roo
   - Essas configurações podem ajudar independentemente do seu sistema operacional

### Comportamento Ctrl+C

**Problema**: Se já houver texto digitado no terminal quando o Roo tentar executar um comando, o Roo pressionará Ctrl+C primeiro para limpar a linha, o que pode interromper processos em execução.

**Solução alternativa**: Certifique-se de que seu prompt de terminal esteja vazio (sem comandos parciais digitados) antes de pedir ao Roo para executar comandos de terminal.

### Problemas de Comandos Multi-linha

**Problema**: Comandos que abrangem várias linhas podem confundir o Roo e podem mostrar saída de comandos anteriores misturada com a saída atual.

**Solução alternativa**: Em vez de comandos multi-linha, use encadeamento de comandos com `&&` para manter tudo em uma linha (ex: `echo a && echo b` em vez de digitar cada comando em uma linha separada).

### Problemas Específicos do PowerShell

1. **Conclusão Prematura**: O PowerShell às vezes informa ao Roo que um comando terminou antes que toda a saída tenha sido mostrada.
2. **Comandos Repetidos**: O PowerShell pode se recusar a executar o mesmo comando duas vezes seguidas.

**Solução alternativa**: Ative a configuração "Solução alternativa para contador do PowerShell" e defina um atraso de comando terminal de 150ms nas configurações para dar mais tempo aos comandos para completarem.

### Saída de Terminal Incompleta

**Problema**: Às vezes o VS Code não mostra ou captura toda a saída de um comando.

**Solução alternativa**: Se você notar saída faltando, tente fechar e reabrir a aba do terminal, então execute o comando novamente. Isso atualiza a conexão do terminal.
---
## Recursos de Solução de Problemas

### Verificando Logs de Depuração
Quando ocorrerem problemas de integração shell, verifique os logs de depuração:
1. Abra Ajuda → Alternar Ferramentas de Desenvolvedor → Console
2. Defina "Mostrar Todos os Níveis" para ver todas as mensagens de log
3. Procure por mensagens contendo `[Terminal Process]`
4. Verifique o conteúdo `preOutput` em mensagens de erro:
   - preOutput vazio (`''`) significa que o VSCode não enviou dados
   - Isso indica um potencial problema de integração shell do VSCode, ou um bug upstream que está fora do nosso controle
   - A ausência de marcadores de integração shell pode exigir ajustes de configurações para contornar possíveis bugs upstream ou problemas de configuração de estação de trabalho local relacionados à inicialização do shell e carregamento de ganchos especiais de integração shell do VSCode

### Usando a Extensão de Teste de Integração Terminal do VSCode
A [Extensão de Teste de Integração Terminal do VSCode](https://github.com/KJ7LNW/vsce-test-terminal-integration) ajuda a diagnosticar problemas de integração shell testando diferentes combinações de configurações:

1. **Quando Comandos Paralisam**:
   - Se você vir avisos "comando já em execução", clique em "Reset Stats" para redefinir o estado do terminal
   - Esses avisos indicam que a integração shell não está funcionando
   - Tente diferentes combinações de configurações até encontrar uma que funcione
   - Se realmente travar, reinicie a extensão fechando a janela e pressionando F5

2. **Testando Configurações**:
   - Tente sistematicamente diferentes combinações de:
     * Atraso de Comando Terminal
     * Configurações de Integração Shell
   - Documente quais combinações têm sucesso ou falham
   - Isso ajuda a identificar padrões em problemas de integração shell

3. **Relatando Problemas**:
   - Uma vez que encontrar uma configuração problemática
   - Documente a combinação exata de configurações
   - Anote seu ambiente (SO, versão VSCode, shell e qualquer personalização de prompt shell)
   - Abra um problema com esses detalhes para ajudar a melhorar a integração shell

### Recursos Adicionais

- [Problema de Saída de Terminal do VSCode #237208](https://github.com/microsoft/vscode/issues/237208)
- [Repositório de Teste de Integração Terminal do VSCode](https://github.com/KJ7LNW/vsce-test-terminal-integration)
- [PR de Arquitetura de Integração Shell do Roo Code](https://github.com/RooCodeInc/Roo-Code/pull/1365)

---
## Suporte

Se você ainda estiver com problemas:

1. Verifique [Problemas do Roo Code no GitHub](https://github.com/RooCodeInc/Roo-Code/issues)
2. Crie um novo problema com:
   - SO e versão do VSCode
   - Tipo de shell
   - Passos para reproduzir
   - Mensagens de erro

Para ajuda adicional, junte-se ao nosso [Discord](https://discord.gg/roocode).
