# execute_command

A ferramenta `execute_command` executa comandos CLI no sistema do usuário. Permite que o Roo realize operações de sistema, instale dependências, construa projetos, inicie servidores e execute outras tarefas baseadas em terminal necessárias para atingir os objetivos do usuário.

---

## Parâmetros

A ferramenta aceita estes parâmetros:

- `command` (obrigatório): O comando CLI a ser executado. Deve ser válido para o sistema operacional do usuário.
- `cwd` (opcional): O diretório de trabalho onde o comando será executado. Se não fornecido, o diretório de trabalho atual será usado.

---

## O que ela faz

Esta ferramenta executa comandos de terminal diretamente no sistema do usuário, permitindo uma ampla gama de operações desde manipulação de arquivos até execução de servidores de desenvolvimento. Os comandos são executados em instâncias de terminal gerenciadas com captura de saída em tempo real, integradas ao sistema de terminal do VS Code para desempenho e segurança otimizados.

---

## Quando é usada?

- Ao instalar dependências de projeto (npm install, pip install, etc.)
- Ao construir ou compilar código (make, npm run build, etc.)
- Ao iniciar servidores de desenvolvimento ou executar aplicações
- Ao inicializar novos projetos (git init, npm init, etc.)
- Ao realizar operações de arquivo além do que outras ferramentas fornecem
- Ao executar testes ou operações de linting
- Quando necessário executar comandos especializados para tecnologias específicas

---

## Principais recursos

- Integra-se com a API de shell do VS Code para execução confiável de terminal
- Reutiliza instâncias de terminal quando possível através de um sistema de registro
- Captura a saída do comando linha por linha com feedback em tempo real
- Suporta comandos de longa duração que continuam em segundo plano
- Permite especificação de diretórios de trabalho personalizados
- Mantém histórico e estado do terminal entre execuções de comandos
- Lida com cadeias de comandos complexas apropriadas para o shell do usuário
- Fornece status detalhado de conclusão e interpretação de códigos de saída
- Suporta aplicações interativas de terminal com loop de feedback do usuário
- Mostra terminais durante a execução para transparência
- Valida comandos para segurança usando análise shell-quote
- Bloqueia padrões potencialmente perigosos de execução de subshell
- Integra-se com o sistema RooIgnore para controle de acesso a arquivos
- Processa sequências de escape de terminal para saída limpa

---

## Limitações

- O acesso a comandos pode ser restrito por regras RooIgnore e validações de segurança
- Comandos com requisitos de permissão elevada podem precisar de configuração do usuário
- O comportamento pode variar entre sistemas operacionais para certos comandos
- Comandos de execução muito longa podem requerer tratamento específico
- Caminhos de arquivo devem ser escapados corretamente de acordo com as regras do shell do SO
- Nem todos os recursos de terminal podem funcionar com cenários de desenvolvimento remoto

---

## Como funciona

Quando a ferramenta `execute_command` é invocada, ela segue este processo:

1. **Validação de Comando e Verificações de Segurança**:
   - Analisa o comando usando shell-quote para identificar componentes
   - Valida contra restrições de segurança (uso de subshell, arquivos restritos)
   - Verifica contra regras RooIgnore para permissões de acesso a arquivos
   - Garante que o comando atenda aos requisitos de segurança do sistema

2. **Gerenciamento de Terminal**:
   - Obtém ou cria um terminal através do TerminalRegistry
   - Configura o contexto do diretório de trabalho
   - Prepara listeners de eventos para captura de saída
   - Mostra o terminal para visibilidade do usuário

3. **Execução e Monitoramento de Comando**:
   - Executa via API shellIntegration do VS Code
   - Captura saída com processamento de sequências de escape
   - Limita o tratamento de saída em intervalos de 100ms
   - Monitora conclusão ou erros do comando
   - Detecta processos "quentes" como compiladores para tratamento especial

4. **Processamento de Resultados**:
   - Remove sequências de escape ANSI/VS Code para saída limpa
   - Interpreta códigos de saída com informações detalhadas de sinal
   - Atualiza rastreamento do diretório de trabalho se alterado pelo comando
   - Fornece status do comando com contexto apropriado

---

## Detalhes de Implementação do Terminal

A ferramenta usa um sistema sofisticado de gerenciamento de terminal:

1. **Primeira Prioridade: Reutilização de Terminal**
   - O TerminalRegistry tenta reutilizar terminais existentes quando possível
   - Isso reduz a proliferação de instâncias de terminal e melhora o desempenho
   - O estado do terminal (diretório de trabalho, histórico) é preservado entre comandos

2. **Segunda Prioridade: Validação de Segurança**
   - Comandos são analisados usando shell-quote para análise de componentes
   - Padrões perigosos como `$(...)` e crases são bloqueados
   - Comandos são verificados contra regras RooIgnore para controle de acesso a arquivos
   - Um sistema de lista de permissões baseado em prefixo valida padrões de comandos

3. **Otimizações de Desempenho**
   - A saída é processada em intervalos limitados de 100ms para evitar sobrecarga da UI
   - Gerenciamento de buffer zero-copy usa rastreamento baseado em índice para eficiência
   - Tratamento especial para compilação e processos "quentes"
   - Otimizações específicas para Windows PowerShell

4. **Tratamento de Erros e Sinais**
   - Códigos de saída são mapeados para informações detalhadas de sinal (SIGTERM, SIGKILL, etc.)
   - Detecção de core dump para falhas críticas
   - Mudanças no diretório de trabalho são rastreadas e tratadas automaticamente
   - Recuperação limpa de cenários de desconexão de terminal

---

## Exemplos de Uso

- Ao configurar um novo projeto, o Roo executa comandos de inicialização como `npm init -y` seguido da instalação de dependências.
- Ao construir uma aplicação web, o Roo executa comandos de build como `npm run build` para compilar assets.
- Ao implantar código, o Roo executa comandos git para commitar e enviar alterações para um repositório.
- Ao solucionar problemas, o Roo executa comandos de diagnóstico para coletar informações do sistema.
- Ao iniciar um servidor de desenvolvimento, o Roo executa o comando apropriado (ex: `npm start`).
- Ao executar testes, o Roo executa o comando do test runner para o framework de testes do projeto.

---

## Exemplos de Utilização

Executando um comando simples no diretório atual:
```
<execute_command>
<command>npm run dev</command>
</execute_command>
```

Instalando dependências para um projeto:
```
<execute_command>
<command>npm install express mongodb mongoose dotenv</command>
</execute_command>
```

Executando múltiplos comandos em sequência:
```
<execute_command>
<command>mkdir -p src/components && touch src/components/App.js</command>
</execute_command>
```

Executando um comando em um diretório específico:
```
<execute_command>
<command>git status</command>
<cwd>./my-project</cwd>
</execute_command>
```

Construindo e depois iniciando um projeto:
```
<execute_command>
<command>npm run build && npm start</command>
</execute_command>
