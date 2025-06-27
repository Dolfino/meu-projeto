# access_mcp_resource

A ferramenta `access_mcp_resource` recupera dados de recursos expostos por servidores conectados ao Model Context Protocol (MCP). Permite que o Roo acesse arquivos, respostas de API, documentação ou informações do sistema que fornecem contexto adicional para tarefas.

---

## Parâmetros

A ferramenta aceita estes parâmetros:

- `server_name` (obrigatório): Nome do servidor MCP que fornece o recurso
- `uri` (obrigatório): URI que identifica o recurso específico a ser acessado

---

## Funcionamento

Esta ferramenta conecta-se a servidores MCP e obtém dados de seus recursos expostos. Diferente do `use_mcp_tool` que executa ações, esta ferramenta especificamente recupera informações que servem como contexto para tarefas.

---

## Quando é usada?

- Quando o Roo precisa de contexto adicional de sistemas externos
- Quando o Roo precisa acessar dados específicos de domínio de servidores MCP especializados
- Quando o Roo precisa recuperar documentação de referência hospedada por servidores MCP
- Quando o Roo precisa integrar dados em tempo real de APIs externas via MCP

---

## Principais recursos

- Recupera dados textuais e imagens de recursos MCP
- Requer aprovação do usuário antes de acessar recursos
- Usa endereçamento baseado em URI para identificar recursos precisamente
- Integra-se com o SDK do Model Context Protocol
- Exibe conteúdo de recursos apropriadamente baseado no tipo de conteúdo
- Suporta timeouts para operações de rede confiáveis
- Gerencia estados de conexão do servidor (conectado, conectando, desconectado)
- Descobre recursos disponíveis de servidores conectados
- Processa dados estruturados de resposta com metadados
- Trata conteúdo de imagem com renderização especial

---

## Limitações

- Depende de servidores MCP externos estarem disponíveis e conectados
- Limitado aos recursos fornecidos por servidores conectados
- Não pode acessar recursos de servidores desativados
- Problemas de rede podem afetar confiabilidade e performance
- Acesso a recursos sujeito a timeouts configurados
- Formatos de URI são determinados pela implementação específica do servidor MCP
- Sem capacidade de acesso offline ou com cache a recursos

---

## Como funciona

Quando a ferramenta `access_mcp_resource` é invocada, segue este processo:

1. **Validação de conexão**:
   - Verifica se um hub MCP está disponível e inicializado
   - Confirma que o servidor especificado existe na lista de conexões
   - Checa se o servidor está desativado (retorna erro se estiver)

2. **Aprovação do usuário**:
   - Apresenta a requisição de acesso ao recurso para aprovação do usuário
   - Fornece nome do servidor e URI do recurso para verificação
   - Prossegue somente se o usuário aprovar o acesso

3. **Requisição do recurso**:
   - Usa o SDK do Model Context Protocol para comunicação com servidores
   - Faz uma requisição `resources/read` ao servidor através do hub MCP
   - Aplica timeouts configurados para evitar travamentos em servidores sem resposta

4. **Processamento da resposta**:
   - Recebe uma resposta estruturada com metadados e arrays de conteúdo
   - Processa conteúdo textual para exibição ao usuário
   - Trata dados de imagem especialmente para exibição apropriada
   - Retorna os dados processados do recurso para o Roo usar na tarefa atual

---

## Tipos de recursos

Servidores MCP podem fornecer dois tipos principais de recursos:

1. **Recursos padrão**:
   - Recursos fixos com URIs específicos
   - Nome, descrição e tipo MIME definidos
   - Acesso direto sem parâmetros
   - Tipicamente representam dados estáticos ou informações em tempo real

2. **Modelos de recursos**:
   - Recursos parametrizados com valores placeholder em URIs
   - Permitem geração dinâmica de recursos baseada em parâmetros fornecidos
   - Podem representar consultas ou visões filtradas de dados
   - Mais flexíveis mas requerem formatação adicional de URI

---

## Exemplos de uso

- Ao ajudar com desenvolvimento de API, o Roo recupera especificações de endpoints de recursos MCP para garantir implementação correta.
- Ao auxiliar com visualização de dados, o Roo acessa amostras de dados atuais de servidores MCP conectados.
- Ao trabalhar em domínios especializados, o Roo recupera documentação técnica para fornecer orientação precisa.
- Ao gerar código específico de indústria, o Roo referencia requisitos de conformidade de recursos de documentação.

---

## Exemplos de utilização

Acessando dados meteorológicos atuais:
```
<access_mcp_resource>
<server_name>weather-server</server_name>
<uri>weather://san-francisco/current</uri>
</access_mcp_resource>
```

Recuperando documentação de API:
```
<access_mcp_resource>
<server_name>api-docs</server_name>
<uri>docs://payment-service/endpoints</uri>
</access_mcp_resource>
```

Acessando conhecimento específico de domínio:
```
<access_mcp_resource>
<server_name>knowledge-base</server_name>
<uri>kb://medical/terminology/common</uri>
</access_mcp_resource>
```

Obtendo configuração de sistema:
```
<access_mcp_resource>
<server_name>infra-monitor</server_name>
<uri>config://production/database</uri>
</access_mcp_resource>
