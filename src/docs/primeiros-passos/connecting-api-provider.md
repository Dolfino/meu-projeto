---
sidebar_label: Conectando ao Provedor de IA
---

import KangarooIcon from '@site/src/components/KangarooIcon';

# Conectando Seu Primeiro Provedor de IA

O Roo Code requer uma chave API de um provedor de modelos de IA para funcionar. Recomendamos estas opções para acessar o poderoso modelo **Claude 3.7 Sonnet**:

- **OpenRouter (Recomendado):** Fornece acesso a múltiplos modelos de IA com uma única chave API. Ideal para começar rapidamente com configuração mínima. [Ver preços](https://openrouter.ai/models?order=pricing-low-to-high).
- **Anthropic:** Acesso direto aos modelos Claude. Requer aprovação de acesso à API e pode ter [limites de taxa dependendo do seu nível](https://docs.anthropic.com/en/api/rate-limits#requirements-to-advance-tier). Veja a [página de preços da Anthropic](https://www.anthropic.com/pricing#anthropic-api) para detalhes.
---

## Obtendo Sua Chave API

### Opção 1: Roteadores LLM

Roteadores LLM permitem acessar múltiplos modelos de IA com uma chave API, simplificando o gerenciamento de custos e a troca entre modelos. Eles geralmente oferecem [preços competitivos](https://openrouter.ai/models?order=pricing-low-to-high) comparados a provedores diretos.

#### OpenRouter

1. Acesse [openrouter.ai](https://openrouter.ai/)
2. Faça login com sua conta Google ou GitHub
3. Navegue até a [página de chaves API](https://openrouter.ai/keys) e crie uma nova chave
4. Copie sua chave API - você precisará dela para configurar o Roo Code

<img src="/img/connecting-api-provider/connecting-api-provider-4.png" alt="Página de chaves API do OpenRouter" width="600" />

*Painel do OpenRouter com botão "Create key". Nomeie sua chave e copie após a criação.*

#### Requesty

1. Acesse [requesty.ai](https://requesty.ai/)
2. Faça login com sua conta Google ou email
3. Navegue até a [página de gerenciamento de API](https://app.requesty.ai/api-keys) e crie uma nova chave
4. **Importante:** Copie sua chave API imediatamente pois ela não será exibida novamente

<img src="/img/connecting-api-provider/connecting-api-provider-7.png" alt="Página de gerenciamento de API do Requesty" width="600" />

*Página de gerenciamento de API do Requesty com botão "Create API Key". Copie sua chave imediatamente - ela é mostrada apenas uma vez.*

### Opção 2: Provedores Diretos

Para acesso direto a modelos específicos de seus provedores originais, com acesso completo a seus recursos e capacidades:

#### Anthropic

1. Acesse [console.anthropic.com](https://console.anthropic.com/)
2. Crie uma conta ou faça login
3. Navegue até a [seção de chaves API](https://console.anthropic.com/settings/keys) e crie uma nova chave
4. **Importante:** Copie sua chave API imediatamente pois ela não será exibida novamente

<img src="/img/connecting-api-provider/connecting-api-provider-5.png" alt="Seção de chaves API do console Anthropic" width="600" />

*Seção de chaves API do console Anthropic com botão "Create key". Nomeie sua chave, defina expiração e copie imediatamente.*

#### OpenAI

1. Acesse [platform.openai.com](https://platform.openai.com/)
2. Crie uma conta ou faça login
3. Navegue até a [seção de chaves API](https://platform.openai.com/api-keys) e crie uma nova chave
4. **Importante:** Copie sua chave API imediatamente pois ela não será exibida novamente

<img src="/img/connecting-api-provider/connecting-api-provider-6.png" alt="Página de chaves API da OpenAI" width="600" />

*Plataforma OpenAI com botão "Create new secret key". Nomeie sua chave e copie imediatamente após a criação.*

---

## Configurando o Roo Code no VS Code

Após obter sua chave API:

1. Abra a barra lateral do Roo Code clicando no ícone do Roo Code (<KangarooIcon />) na Barra de Atividades do VS Code
2. Na tela de boas-vindas, selecione seu provedor de API no menu suspenso
3. Cole sua chave API no campo apropriado
4. Selecione seu modelo:
   - Para **OpenRouter**: selecione `anthropic/claude-3.7-sonnet` ([detalhes do modelo](https://openrouter.ai/anthropic/claude-3.7-sonnet))
   - Para **Anthropic**: selecione `claude-3-7-sonnet-20250219` ([detalhes do modelo](https://www.anthropic.com/pricing#anthropic-api))

:::info Conselho sobre Seleção de Modelo
Recomendamos fortemente o **Claude 3.7 Sonnet** para a melhor experiência - ele geralmente "funciona logo de cara". O Roo Code foi extensivamente otimizado para as capacidades deste modelo e seu comportamento de seguir instruções.

Selecionar modelos alternativos é um recurso avançado que introduz complexidade. Diferentes modelos variam significativamente em como seguem instruções de ferramentas, analisam formatos e mantêm contexto em operações de múltiplos passos. Se experimentar outros modelos, escolha aqueles especificamente projetados para raciocínio estruturado e uso de ferramentas.
:::

5. Clique em "Vamos lá!" para salvar suas configurações e começar a usar o Roo Code
