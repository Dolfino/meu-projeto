---
sidebar_label: Anthropic
---

# Usando a Anthropic com o Roo Code

A Anthropic é uma empresa de pesquisa e segurança em IA que constrói sistemas de IA confiáveis, interpretáveis e controláveis. Seus modelos Claude são conhecidos por suas fortes habilidades de raciocínio, utilidade e honestidade.

**Site:** [https://www.anthropic.com/](https://www.anthropic.com/)

---

## Obtendo uma Chave API

1.  **Cadastre-se/Login:** Acesse o [Console da Anthropic](https://console.anthropic.com/). Crie uma conta ou faça login.
2.  **Navegue até Chaves API:** Vá para a seção [Chaves API](https://console.anthropic.com/settings/keys).
3.  **Crie uma Chave:** Clique em "Create Key". Dê um nome descritivo à sua chave (ex: "Roo Code").
4.  **Copie a Chave:** **Importante:** Copie a chave API *imediatamente*. Você não poderá vê-la novamente. Armazene-a com segurança.

---

## Modelos Suportados

O Roo Code suporta os seguintes modelos Claude da Anthropic:

*   `claude-opus-4-20250514`
*   `claude-opus-4-20250514:thinking` (Variante Extended Thinking)
*   `claude-sonnet-4-20250514` (Recomendado)
*   `claude-sonnet-4-20250514:thinking` (Variante Extended Thinking)
*   `claude-3-7-sonnet-20250219`
*   `claude-3-7-sonnet-20250219:thinking` (Variante Extended Thinking)
*   `claude-3-5-sonnet-20241022`
*   `claude-3-5-haiku-20241022`
*   `claude-3-opus-20240229`
*   `claude-3-haiku-20240307`

Consulte a [Documentação de Modelos da Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) para mais detalhes sobre as capacidades de cada modelo.

---

## Configuração no Roo Code

1.  **Abra as Configurações do Roo Code:** Clique no ícone de engrenagem (<Codicon name="gear" />) no painel do Roo Code.
2.  **Selecione o Provedor:** Escolha "Anthropic" no menu suspenso "API Provider".
3.  **Insira a Chave API:** Cole sua chave API da Anthropic no campo "Anthropic API Key".
4.  **Selecione o Modelo:** Escolha seu modelo Claude desejado no menu suspenso "Model".
5.  **(Opcional) URL Base Personalizada:** Se precisar usar uma URL base personalizada para a API da Anthropic, marque "Use custom base URL" e insira a URL. A maioria das pessoas não precisará ajustar isso.

---

## Dicas e Notas

*   **Cache de Prompts:** Os modelos Claude 3 suportam [cache de prompts](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching), que pode reduzir significativamente custos e latência para prompts repetidos.
*   **Janela de Contexto:** Os modelos Claude têm grandes janelas de contexto (200.000 tokens), permitindo incluir uma quantidade significativa de código e contexto em seus prompts.
*   **Preços:** Consulte a [página de Preços da Anthropic](https://www.anthropic.com/pricing) para informações atualizadas sobre preços.
*   **Limites de Taxa:** A Anthropic tem limites de taxa rigorosos baseados em [níveis de uso](https://docs.anthropic.com/en/api/rate-limits#requirements-to-advance-tier). Se estiver atingindo repetidamente os limites, considere entrar em contato com o time de vendas da Anthropic ou acessar o Claude através de outro provedor como [OpenRouter](/providers/openrouter) ou [Requesty](/providers/requesty).
