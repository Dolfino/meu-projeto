# Dicas de Engenharia de Prompt (Prompt Engineering)

Engenharia de prompt é a arte de criar instruções eficazes para modelos de IA como o Roo Code. Prompts bem escritos levam a melhores resultados, menos erros e um fluxo de trabalho mais eficiente.

---

## Princípios Gerais

*   **Seja Claro e Específico:** Diga claramente o que você quer que o Roo Code faça. Evite ambiguidades.
    *   **Ruim:** Conserte o código.
    *   **Bom:** Corrija o bug na função `calculateTotal` que faz ela retornar resultados incorretos.

*   **Forneça Contexto:** Use [Menções de Contexto](/basic-usage/context-mentions) para referenciar arquivos, pastas ou problemas específicos.
    *   **Bom:** `@/src/utils.ts` Refatore a função `calculateTotal` para usar async/await.

*   **Divida Tarefas:** Separe tarefas complexas em etapas menores e bem definidas.

*   **Dê Exemplos:** Se você tem um estilo de código ou padrão específico em mente, forneça exemplos.

*   **Especifique o Formato de Saída:** Se precisar da saída em um formato específico (ex: JSON, Markdown), especifique no prompt.

*   **Itere:** Não tenha medo de refinar seu prompt se os resultados iniciais não forem os esperados.

---

## Pensar vs. Fazer

É útil guiar o Roo Code através de um processo "pensar-depois-fazer":

1.  **Analisar:** Peça ao Roo Code para analisar o código atual e identificar problemas.
2.  **Planejar:** Faça o Roo Code descrever os passos para completar a tarefa.
3.  **Executar:** Instrua o Roo Code a implementar o plano, um passo por vez.
4.  **Revisar:** Revise cuidadosamente os resultados de cada etapa antes de prosseguir.

---

## Usando Instruções Personalizadas

Você pode fornecer instruções personalizadas para adaptar o comportamento do Roo Code. Há dois tipos:

*   **Instruções Globais:** Aplicam-se a todos os modos.
*   **Instruções Específicas por Modo:** Aplicam-se apenas a um modo específico (ex: Code, Architect, Ask, Debug).

Instruções personalizadas são adicionadas ao prompt do sistema, fornecendo orientação persistente. Você pode usá-las para:

*   Definir diretrizes de estilo de código.
*   Especificar bibliotecas ou frameworks preferidos.
*   Definir convenções específicas do projeto.
*   Ajustar o tom ou personalidade do Roo Code.

Veja a seção [Instruções Personalizadas](/features/custom-instructions) para mais detalhes.

---

## Lidando com Ambiguidades

Se sua solicitação for ambígua ou faltar detalhes, o Roo Code pode:

*   **Fazer Suposições:** Pode prosseguir baseado no seu melhor palpite.
*   **Perguntar para Esclarecer:** Pode usar a ferramenta `ask_followup_question` para clarificar sua solicitação.

É melhor fornecer instruções claras desde o início para evitar idas e vindas desnecessárias.

---

## Fornecendo Feedback

Se o Roo Code não produzir os resultados esperados, você pode fornecer feedback:

*   **Rejeitando Ações:** Clique em "Rejeitar" quando uma ação proposta não for desejada.
*   **Explicando:** Ao rejeitar, explique o motivo para ajudar o Roo Code a aprender.
*   **Reformulando:** Tente reformular sua tarefa inicial com instruções mais específicas.
*   **Corrigindo Manualmente:** Para pequenos problemas, você pode editar o código diretamente.

---

## Exemplos

**Bom Prompt:**

> `@/src/components/Button.tsx` Refatore o componente `Button` para usar o hook `useState` ao invés de `useReducer`.

**Prompt Ruim:**

> Conserte o botão.

**Bom Prompt:**

> Crie um arquivo chamado `utils.py` com uma função `calculate_average` que recebe uma lista de números e retorna a média.

**Prompt Ruim:**

> Escreva algum código Python.

**Bom Prompt:**

> `@problems` Corrija todos os erros e warnings no arquivo atual.

**Prompt Ruim:**

> Conserte tudo.

Seguindo essas dicas, você pode criar prompts eficazes que aproveitam ao máximo as capacidades do Roo Code.
