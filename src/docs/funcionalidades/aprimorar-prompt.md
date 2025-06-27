# Aprimorar Prompt

O recurso "Aprimorar Prompt" no Roo Code ajuda você a melhorar a qualidade e eficácia de seus prompts antes de enviá-los ao modelo de IA. Ao clicar no ícone <Codicon name="sparkle" /> na entrada do chat, você pode refinar automaticamente sua solicitação inicial, tornando-a mais clara, específica e com maior probabilidade de produzir os resultados desejados.

---

## Por Que Usar o Aprimorar Prompt?

*   **Melhor Clareza:** O Roo Code pode reformular seu prompt para torná-lo mais compreensível para o modelo de IA.
*   **Contexto Adicionado:** O processo de aprimoramento pode adicionar contexto relevante ao seu prompt, como o caminho do arquivo atual ou código selecionado.
*   **Instruções Melhores:** O Roo Code pode adicionar instruções para guiar a IA para uma resposta mais útil (ex: solicitando formatação específica ou um nível particular de detalhe).
*   **Redução de Ambiguidade:** Aprimorar Prompt ajuda a eliminar ambiguidades e garantir que o Roo Code entenda sua intenção.
*   **Consistência:** O Roo formatará os prompts de forma consistente para a IA.

---

## Como Usar o Aprimorar Prompt

1.  **Digite seu prompt inicial:** Insira sua solicitação na caixa de entrada de chat do Roo Code como faria normalmente. Pode ser uma pergunta simples, uma descrição de tarefa complexa ou qualquer coisa entre esses extremos.
2.  **Clique no ícone <Codicon name="sparkle" />:** Em vez de pressionar Enter, clique no ícone <Codicon name="sparkle" /> localizado no canto inferior direito da caixa de entrada de chat.
3.  **Revise o Prompt Aprimorado:** O Roo Code substituirá seu prompt original por uma versão aprimorada. Revise o prompt aprimorado para garantir que reflita com precisão sua intenção. Você pode refinar ainda mais o prompt aprimorado antes de enviar.
4.  **Envie o Prompt Aprimorado:** Pressione Enter ou clique no ícone Enviar (<Codicon name="send" />) para enviar o prompt aprimorado ao Roo Code.

---

## Personalizando o Processo de Aprimoramento

O recurso "Aprimorar Prompt" usa um modelo de prompt personalizável. Você pode modificar este modelo para adaptar o processo de aprimoramento às suas necessidades específicas.

1.  **Abra a Aba Prompts:** Clique no ícone <Codicon name="notebook" /> na barra de menu superior do Roo Code.
2.  **Selecione a Aba "APRIMORAR":** Você verá os prompts de suporte listados, incluindo "APRIMORAR". Clique nesta aba.
3.  **Edite o Modelo de Prompt:** Modifique o texto no campo "Prompt".

O modelo de prompt padrão inclui o marcador `${userInput}`, que será substituído pelo seu prompt original. Você pode modificar isso para se adequar ao formato de prompt do modelo e instruí-lo sobre como aprimorar sua solicitação.

---

## Configuração da API

A configuração da API usada para Aprimorar Prompt é, por padrão, a mesma selecionada para tarefas do Roo Code, mas pode ser alterada:

1.  **Abra a Aba Prompts:** Clique no ícone <Codicon name="notebook" /> na barra de menu superior do Roo Code.
2.  **Selecione a Aba "APRIMORAR":** Você verá um menu suspenso "Configuração da API"
3.  **Selecione uma Configuração de API:** Escolha uma configuração existente e futuras solicitações de Aprimorar Prompt serão enviadas para aquele provedor/modelo configurado.

---

## Limitações e Melhores Práticas

*   **Recurso Experimental:** O aprimoramento de prompt é um recurso experimental. A qualidade do prompt aprimorado pode variar dependendo da complexidade de sua solicitação e das capacidades do modelo subjacente.
*   **Revise Cuidadosamente:** Sempre revise o prompt aprimorado antes de enviá-lo. O Roo Code pode fazer alterações que não estejam alinhadas com suas intenções.
*   **Processo Iterativo:** Você pode usar o recurso "Aprimorar Prompt" várias vezes para refinar iterativamente seu prompt.
*   **Não Substitui Instruções Claras:** Embora "Aprimorar Prompt" possa ajudar, ainda é importante escrever prompts claros e específicos desde o início.

Ao usar o recurso "Aprimorar Prompt", você pode melhorar a qualidade de suas interações com o Roo Code e obter respostas mais precisas e úteis.
