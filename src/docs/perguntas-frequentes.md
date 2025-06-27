import KangarooIcon from '@site/src/components/KangarooIcon';

# Perguntas Frequentes

Esta página responde perguntas comuns sobre o Roo Code.

---

## Geral

### O que é o Roo Code?

Roo Code é um agente autônomo de codificação com IA que vive no seu editor.

### Como o Roo Code funciona?

O Roo Code usa modelos de linguagem (LLMs) para entender suas solicitações e traduzi-las em ações. Ele pode:

* Ler e escrever arquivos no seu projeto
* Executar comandos no terminal do VS Code
* Navegar na web (se habilitado)
* Usar ferramentas externas via Model Context Protocol (MCP)

Você interage com o Roo Code através de um chat, onde fornece instruções e revisa/aprova as ações propostas.

### O que o Roo Code pode fazer?

O Roo Code ajuda com diversas tarefas de programação, incluindo:

* Gerar código a partir de descrições em linguagem natural
* Refatorar código existente
* Corrigir bugs
* Escrever documentação
* Explicar código
* Responder perguntas sobre sua base de código
* Automatizar tarefas repetitivas
* Criar novos arquivos e projetos

### O Roo Code é gratuito?

A extensão Roo Code é gratuita e open-source. Porém, ele depende de provedores de API externos (como [Anthropic](providers/anthropic), [OpenAI](providers/openai), etc.) que cobram pelo uso baseado em tokens processados.

### Quais são os riscos de usar o Roo Code?

* **Pode cometer erros** - Sempre revise as mudanças propostas
* **Pode executar comandos** - Tenha cuidado ao permitir comandos, especialmente com aprovação automática
* **Pode acessar a internet** - Esteja ciente de possíveis acessos a informações sensíveis

---

## Configuração & Instalação

### Como instalar o Roo Code?

Veja o [Guia de Instalação](/getting-started/installing).

### Quais provedores de API são suportados?

* [Anthropic (Claude)](/providers/anthropic)
* [OpenAI](/providers/openai)
* [Google Gemini](/providers/gemini)
* [AWS Bedrock](/providers/bedrock)
* [Ollama](/providers/ollama) (para modelos locais)
* E outros...

### Como obter uma chave de API?

Cada provedor tem seu próprio processo. Veja [Configurando seu Primeiro Provedor de IA](/getting-started/connecting-api-provider).

### Posso usar modelos locais?

Sim, usando [Ollama](/providers/ollama) ou [LM Studio](/providers/lmstudio).

---

## Uso

### Como iniciar uma nova tarefa?

Abra o painel do Roo Code (<KangarooIcon />) e digite sua tarefa no chat. Seja claro e específico.

### O que são modos no Roo Code?

São personas especializadas com focos diferentes:

* **Código:** Para programação geral
* **Arquitetura:** Para planejamento técnico
* **Perguntar:** Para responder dúvidas
* **Depuração:** Para diagnóstico de problemas
* **Modos Personalizados:** Crie os seus próprios

### Como alternar entre modos?

Use o menu dropdown no chat ou o comando `/`.

### O que são ferramentas?

São como o Roo Code interage com seu sistema. Ele seleciona automaticamente as ferramentas necessárias.

### O Roo Code pode acessar a internet?

Sim, se usar um provedor com suporte a navegação web.

### Posso personalizar o Roo Code?

Sim, com:
* Instruções personalizadas
* Modos customizados
* Arquivos `.roorules`
* Configurações diversas

---

## Recursos Avançados

### O que é MCP?

[Model Context Protocol](/features/mcp/overview) permite que o Roo Code se comunique com servidores externos para estender suas capacidades.

### O que é Indexação de Código?

Recurso experimental que cria um índice de busca semântica do seu projeto usando embeddings de IA.

---

## Solução de Problemas

### O Roo Code não está respondendo

* Verifique sua chave de API e conexão
* Consulte o status do provedor
* Reinicie o VS Code

### Como desfazer mudanças indesejadas?

Use o comando "Desfazer" padrão (Ctrl/Cmd + Z) ou os checkpoints experimentais.

### Problemas com arquivos Markdown

Podem ser causados por:
* Extensões com "formatar ao salvar"
* Configurações que abrem markdown em modo preview

Soluções:
* Desative extensões de formatação automática
* Ajuste as configurações do VS Code
* Reinicie o VS Code

### Como reportar bugs?

Use a [página de Issues](https://github.com/RooCodeInc/Roo-Code/issues) no GitHub.
