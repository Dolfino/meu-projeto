# browser_action

A ferramenta `browser_action` permite automação e interação web via um navegador controlado pelo Puppeteer. Permite que o Roo inicie navegadores, acesse sites, clique em elementos, digite texto e role páginas com feedback visual através de screenshots.

---

## Parâmetros

A ferramenta aceita estes parâmetros:

- `action` (obrigatório): A ação a ser executada:
  * `launch`: Inicia uma nova sessão do navegador em uma URL
  * `click`: Clica em coordenadas x,y específicas
  * `type`: Digita texto via teclado
  * `scroll_down`: Rola para baixo uma altura de página
  * `scroll_up`: Rola para cima uma altura de página
  * `close`: Encerra a sessão do navegador
- `url` (opcional): A URL para navegar quando usar a ação `launch`
- `coordinate` (opcional): As coordenadas x,y para a ação `click` (ex: "450,300")
- `text` (opcional): O texto a digitar quando usar a ação `type`

---

## Funcionalidade

Esta ferramenta cria uma sessão automatizada de navegador que o Roo pode controlar para navegar em sites, interagir com elementos e executar tarefas que requerem automação de navegador. Cada ação fornece um screenshot do estado atual, permitindo verificação visual do processo.

---

## Quando é usada?

- Quando o Roo precisa interagir com aplicações web ou sites
- Ao testar interfaces de usuário ou funcionalidades web
- Ao capturar screenshots de páginas web
- Ao demonstrar fluxos de trabalho web visualmente

---

## Principais recursos

- Fornece feedback visual com screenshots após cada ação e captura logs do console
- Suporta fluxos completos desde abertura até interação com páginas e fechamento
- Permite interações precisas via coordenadas, entrada de teclado e rolagem
- Mantém sessões consistentes de navegador com detecção inteligente de carregamento
- Opera em dois modos: local (instância isolada do Puppeteer) ou remoto (conecta a Chrome existente)
- Trata erros de forma elegante com limpeza automática de sessão e mensagens detalhadas
- Otimiza saída visual com suporte a vários formatos e configurações de qualidade
- Rastreia estado de interação com indicadores de posição e histórico de ações

---

## Modos de navegador

A ferramenta opera em dois modos distintos:

### Modo Local (Padrão)
- Baixa e gerencia uma instância local do Chromium através do Puppeteer
- Cria um ambiente limpo de navegador a cada inicialização
- Sem acesso a perfis de usuário, cookies ou extensões existentes
- Comportamento consistente e previsível em ambiente sandbox
- Fecha completamente o navegador quando a sessão termina

### Modo Remoto
- Conecta a uma instância existente do Chrome/Chromium com depuração remota ativada
- Pode acessar estado existente do navegador, cookies e potencialmente extensões
- Inicialização mais rápida pois reutiliza um processo de navegador existente
- Suporta conexão com navegadores em containers Docker ou máquinas remotas
- Apenas desconecta (não fecha) do navegador quando a sessão termina
- Requer Chrome rodando com porta de depuração remota aberta (normalmente porta 9222)

---

## Limitações

- Enquanto o navegador está ativo, apenas a ferramenta `browser_action` pode ser usada
- Coordenadas são relativas à viewport, não à página
- Ações de clique devem ter como alvo elementos visíveis na viewport
- Sessões devem ser explicitamente fechadas antes de usar outras ferramentas
- Janela do navegador tem dimensões configuráveis (padrão 900x600)
- Não pode interagir diretamente com DevTools do navegador
- Sessões são temporárias e não persistem entre reinícios do Roo
- Funciona apenas com navegadores Chrome/Chromium, não Firefox ou Safari
- Modo local não tem acesso a cookies existentes; modo remoto requer Chrome com depuração ativada

---

## Como funciona

Quando a ferramenta `browser_action` é invocada, segue este processo:

1. **Validação de ação e gerenciamento do navegador**:
   - Valida os parâmetros necessários para a ação solicitada
   - Para `launch`: Inicializa uma sessão do navegador (instância local do Puppeteer ou Chrome remoto)
   - Para ações de interação: Usa a sessão existente do navegador
   - Para `close`: Encerra ou desconecta do navegador apropriadamente

2. **Interação com página e estabilidade**:
   - Garante que páginas estejam totalmente carregadas usando detecção de estabilidade DOM via algoritmo `waitTillHTMLStable`
   - Executa ações solicitadas (navegação, clique, digitação, rolagem) com temporização adequada
   - Monitora atividade de rede após cliques e aguarda navegação quando necessário

3. **Feedback visual**:
   - Captura screenshots otimizados usando formato WebP (com fallback para PNG)
   - Registra logs do console para depuração
   - Rastreia posição do mouse e mantém histórico paginado de ações

4. **Gerenciamento de sessão**:
   - Mantém estado do navegador entre múltiplas ações
   - Trata erros e limpa recursos automaticamente
   - Impõe sequência adequada de fluxo de trabalho (abertura → interações → fechamento)

---

## Sequência de fluxo de trabalho

Interações com navegador devem seguir esta sequência específica:

1. **Inicialização da sessão**: Todos os fluxos devem começar com ação `launch`
2. **Fase de interação**: Múltiplas ações `click`, `type` e scroll podem ser executadas
3. **Término da sessão**: Todos os fluxos devem terminar com ação `close`
4. **Troca de ferramentas**: Após fechar o navegador, outras ferramentas podem ser usadas

---

## Exemplos de uso

- Ao criar um processo de envio de formulário web, o Roo inicia um navegador, navega para o formulário, preenche campos com ação `type` e clica em enviar.
- Ao testar um site responsivo, o Roo navega para o site e usa ações de scroll para examinar diferentes seções.
- Ao capturar screenshots de uma aplicação web, o Roo navega por diferentes páginas e tira screenshots em cada passo.
- Ao demonstrar um fluxo de checkout e-commerce, o Roo simula todo o processo desde seleção de produto até confirmação de pagamento.

---

## Exemplos de uso

Iniciando um navegador e navegando para um site:
```
<browser_action>
<action>launch</action>
<url>https://example.com</url>
</browser_action>
```

Clicando em coordenadas específicas (ex: um botão):
```
<browser_action>
<action>click</action>
<coordinate>450,300</coordinate>
</browser_action>
```

Digitando texto em um campo de entrada com foco:
```
<browser_action>
<action>type</action>
<text>Hello, World!</text>
</browser_action>
```

Rolando para baixo para ver mais conteúdo:
```
<browser_action>
<action>scroll_down</action>
</browser_action>
```

Fechando a sessão do navegador:
```
<browser_action>
<action>close</action>
</browser_action>
