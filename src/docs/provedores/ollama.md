---
sidebar_label: Ollama
---

import KangarooIcon from '@site/src/components/KangarooIcon';

# Usando o Ollama com o Roo Code

O Roo Code suporta a execução local de modelos usando o Ollama. Isso proporciona privacidade, acesso offline e potencialmente custos menores, mas requer mais configuração e um computador potente.

**Site:** [https://ollama.com/](https://ollama.com/)
---

## Configurando o Ollama

1.  **Baixe e instale o Ollama:** Baixe o instalador do Ollama para seu sistema operacional no [site do Ollama](https://ollama.com/). Siga as instruções de instalação. Certifique-se que o Ollama está rodando

    ```bash
    ollama serve
    ```

2.  **Baixe um modelo:** O Ollama suporta muitos modelos diferentes. Você pode encontrar uma lista de modelos disponíveis no [site do Ollama](https://ollama.com/library). Alguns modelos recomendados para tarefas de programação incluem:

    *   `codellama:7b-code` (bom ponto de partida, menor)
    *   `codellama:13b-code` (melhor qualidade, maior)
    *   `codellama:34b-code` (qualidade ainda melhor, muito grande)
    *   `qwen2.5-coder:32b`
    *   `mistralai/Mistral-7B-Instruct-v0.1` (bom modelo de propósito geral)
    *   `deepseek-coder:6.7b-base` (bom para tarefas de programação)
    *   `llama3:8b-instruct-q5_1` (bom para tarefas gerais)

    Para baixar um modelo, abra seu terminal e execute:

    ```bash
    ollama pull <nome_do_modelo>
    ```

    Por exemplo:

    ```bash
    ollama pull qwen2.5-coder:32b
    ```

3. **Configure o Modelo:** por padrão, o Ollama usa um tamanho de janela de contexto de 2048 tokens, que é muito pequeno para requisições do Roo Code. Você precisa ter pelo menos 12k para obter resultados decentes, idealmente 32k. Para configurar um modelo, você precisa definir seus parâmetros e salvar uma cópia dele.

   Carregue o modelo (usaremos `qwen2.5-coder:32b` como exemplo):

    ```bash
    ollama run qwen2.5-coder:32b
    ```

   Altere o parâmetro de tamanho de contexto:

    ```bash
    /set parameter num_ctx 32768
    ```

    Salve o modelo com um novo nome:

    ```bash
    /save seu_nome_de_modelo
    ```

4.  **Configure o Roo Code:**
    *   Abra a barra lateral do Roo Code (ícone <KangarooIcon />).
    *   Clique no ícone de engrenagem (<Codicon name="gear" />).
    *   Selecione "ollama" como Provedor de API.
    *   Insira o nome do modelo da etapa anterior (ex: `seu_nome_de_modelo`).
    *   (Opcional) Você pode configurar a URL base se estiver executando o Ollama em uma máquina diferente. O padrão é `http://localhost:11434`.
    *   (Opcional) Configure o tamanho do contexto do Modelo nas configurações avançadas, para que o Roo Code saiba como gerenciar sua janela deslizante.

---

## Dicas e Notas

*   **Requisitos de Recursos:** Executar modelos de linguagem grandes localmente pode consumir muitos recursos. Certifique-se que seu computador atende aos requisitos mínimos para o modelo escolhido.
*   **Seleção de Modelos:** Experimente diferentes modelos para encontrar o que melhor atende suas necessidades.
*   **Uso Offline:** Após baixar um modelo, você pode usar o Roo Code offline com esse modelo.
*   **Monitoramento de Tokens:** O Roo Code rastreia o uso de tokens para modelos executados via Ollama, ajudando você a monitorar o consumo.
*   **Documentação do Ollama:** Consulte a [documentação do Ollama](https://ollama.com/docs) para mais informações sobre instalação, configuração e uso.
