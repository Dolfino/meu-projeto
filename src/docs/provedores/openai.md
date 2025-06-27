---
sidebar_label: OpenAI
---

# Usando a OpenAI com o Roo Code

O Roo Code suporta o acesso a modelos diretamente através da API oficial da OpenAI.

**Site:** [https://openai.com/](https://openai.com/)

---

## Obtendo uma Chave API

1.  **Cadastre-se/Login:** Acesse a [Plataforma OpenAI](https://platform.openai.com/). Crie uma conta ou faça login.
2.  **Navegue até Chaves API:** Vá para a página de [Chaves API](https://platform.openai.com/api-keys).
3.  **Crie uma Chave:** Clique em "Create new secret key". Dê um nome descritivo à sua chave (ex: "Roo Code").
4.  **Copie a Chave:** **Importante:** Copie a chave API *imediatamente*. Você não poderá vê-la novamente. Armazene-a com segurança.

---

## Modelos Suportados

O Roo Code suporta vários modelos da OpenAI, incluindo:

*	`o3-mini` (esforço de raciocínio médio)
*	`o3-mini-high` (alto esforço de raciocínio)
* `o3-mini-low` (baixo esforço de raciocínio)
* `o1`
* `o1-preview`
*	`o1-mini`
*   `gpt-4.5-preview`
* `gpt-4o`
* `gpt-4o-mini`

Consulte a [documentação de Modelos da OpenAI](https://platform.openai.com/docs/models) para a lista mais atualizada de modelos e capacidades.

---

## Configuração no Roo Code

1.  **Abra as Configurações do Roo Code:** Clique no ícone de engrenagem (<Codicon name="gear" />) no painel do Roo Code.
2.  **Selecione o Provedor:** Escolha "OpenAI" no menu suspenso "API Provider".
3.  **Insira a Chave API:** Cole sua chave API da OpenAI no campo "OpenAI API Key".
4.  **Selecione o Modelo:** Escolha seu modelo desejado no menu suspenso "Model".
5.  **(Opcional) URL Base:** Se precisar usar uma URL base personalizada, insira a URL. A maioria das pessoas não precisará ajustar isso.

---

## Dicas e Notas

*   **Preços:** Consulte a [página de Preços da OpenAI](https://openai.com/pricing) para detalhes sobre custos dos modelos.
*   **Serviço Azure OpenAI:** Se desejar usar o serviço Azure OpenAI, consulte nossa seção sobre provedores [compatíveis com OpenAI](/providers/openai-compatible).
