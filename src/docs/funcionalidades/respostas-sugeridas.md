---
sidebar_label: Respostas Sugeridas
---

import Codicon from '@site/src/components/Codicon';

# Respostas Sugeridas

Quando o Roo precisa de mais informações para completar uma tarefa, ele usa a ferramenta [`ask_followup_question`](/advanced-usage/available-tools/ask-followup-question). Para tornar a resposta mais fácil e rápida, o Roo frequentemente fornece respostas sugeridas junto com a pergunta.

---

## Visão Geral

As Respostas Sugeridas aparecem como botões clicáveis diretamente abaixo da pergunta do Roo na interface de chat. Elas oferecem respostas pré-formatadas relevantes à pergunta, ajudando você a fornecer informações rapidamente.

<img src="/img/suggested-responses/suggested-responses.png" alt="Exemplo do Roo fazendo uma pergunta com botões de resposta sugerida abaixo" width="500" />

---

## Como Funciona

1.  **A Pergunta Aparece**: O Roo faz uma pergunta usando a ferramenta `ask_followup_question`.
2.  **Sugestões Exibidas**: Se o Roo fornecer sugestões, elas aparecem como botões abaixo da pergunta.
3.  **Interação**: Você pode interagir com essas sugestões de duas maneiras.

---

## Interagindo com as Sugestões

Você tem três opções para usar respostas sugeridas:

1.  **Seleção Direta**:
    *   **Ação**: Simplesmente clique no botão contendo a resposta que deseja fornecer.
    *   **Resultado**: A resposta selecionada é imediatamente enviada de volta ao Roo como sua resposta. Esta é a forma mais rápida de responder se uma das sugestões corresponder perfeitamente à sua intenção.

2.  **Atalho de Teclado**:
    *   **Ação**: Use o comando `roo.acceptInput` com o atalho de teclado configurado.
    *   **Resultado**: A sugestão principal (primeira) é automaticamente selecionada.
    *   **Nota**: Para detalhes de configuração, veja [Atalhos de Teclado](/features/keyboard-shortcuts).

3.  **Editar Antes de Enviar**:
    *   **Ação**:
        *   Mantenha pressionado `Shift` e clique no botão de sugestão.
        *   *Alternativamente*, passe o mouse sobre o botão de sugestão e clique no ícone de lápis (<Codicon name="edit" />) que aparece.
    *   **Resultado**: O texto da sugestão é copiado para a caixa de entrada do chat. Você pode então modificar o texto conforme necessário antes de pressionar Enter para enviar sua resposta personalizada. Isso é útil quando uma sugestão está próxima, mas precisa de pequenos ajustes.

<img src="/img/suggested-responses/suggested-responses-1.png" alt="Caixa de entrada do chat mostrando texto copiado de uma resposta sugerida, pronto para edição" width="600" />

---

## Benefícios

*   **Velocidade**: Responda rapidamente sem digitar respostas completas.
*   **Clareza**: As sugestões frequentemente esclarecem o tipo de informação que o Roo precisa.
*   **Flexibilidade**: Edite sugestões para fornecer respostas precisas e personalizadas quando necessário.

Este recurso agiliza a interação quando o Roo requer esclarecimentos, permitindo que você guie a tarefa de forma eficaz com o mínimo de esforço.
