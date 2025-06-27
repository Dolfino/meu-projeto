# Usando Modelos Locais

O Roo Code suporta a execução de modelos de linguagem localmente na sua máquina usando [Ollama](https://ollama.com/) e [LM Studio](https://lmstudio.ai/). Isso oferece várias vantagens:

*   **Privacidade:** Seu código e dados nunca saem do seu computador.
*   **Acesso Offline:** Você pode usar o Roo Code mesmo sem conexão com a internet.
*   **Economia de Custos:** Evita taxas de uso de API associadas a modelos baseados em nuvem.
*   **Personalização:** Experimente diferentes modelos e configurações.

**Porém, usar modelos locais também tem algumas desvantagens:**

*   **Requisitos de Recursos:** Modelos locais podem exigir muito do sistema, precisando de um computador potente com boa CPU e, idealmente, uma GPU dedicada.
*   **Complexidade de Configuração:** Configurar modelos locais pode ser mais complexo que usar APIs em nuvem.
*   **Desempenho do Modelo:** O desempenho varia significativamente. Alguns são excelentes, mas podem não igualar os modelos mais avançados em nuvem.
*   **Recursos Limitados:** Modelos locais (e muitos online) frequentemente não suportam recursos avançados como cache de prompt, uso de computador e outros.

---

## Provedores de Modelos Locais Suportados

Atualmente o Roo Code suporta dois principais provedores:

1.  **Ollama:** Ferramenta open-source popular para executar LLMs localmente. Suporta ampla variedade de modelos.
2.  **LM Studio:** Aplicativo desktop com interface amigável que simplifica o download, configuração e execução de modelos locais. Também fornece um servidor local que emula a API da OpenAI.

---

## Configurando Modelos Locais

Para instruções detalhadas de configuração, consulte:
* [Configurando Ollama](/providers/ollama)
* [Configurando LM Studio](/providers/lmstudio)

Ambos oferecem capacidades similares mas com interfaces diferentes. Ollama fornece mais controle via linha de comando, enquanto LM Studio tem uma interface gráfica mais amigável.

---

## Solução de Problemas

*   **"Nenhuma conexão pôde ser feita porque a máquina de destino a recusou ativamente":** Normalmente significa que o servidor Ollama ou LM Studio não está rodando, ou está em porta/endereço diferente do configurado no Roo Code. Verifique a URL base.

*   **Tempos de Resposta Lentos:** Modelos locais podem ser mais lentos que os em nuvem, especialmente em hardware menos potente. Se performance for problema, tente usar um modelo menor.

*   **Modelo Não Encontrado:** Verifique se digitou corretamente o nome do modelo. No Ollama, use o mesmo nome fornecido no comando `ollama run`.
