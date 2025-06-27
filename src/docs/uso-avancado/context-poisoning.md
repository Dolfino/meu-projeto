# Envenenamento de Contexto (Context Poisoning)

:::info
O envenenamento de contexto é um problema persistente dentro de uma sessão. Quando o contexto de uma sessão de chat é comprometido, trate essa sessão como descartável. Começar do zero com um contexto limpo é crucial para manter a precisão e eficácia do seu agente Roo Code.
:::

O envenenamento de contexto ocorre quando dados imprecisos ou irrelevantes contaminam o contexto ativo do modelo de linguagem. Isso leva o modelo a tirar conclusões incorretas, fornecer informações erradas para ferramentas e desviar progressivamente da tarefa pretendida a cada interação.

---

## Sintomas de Envenenamento de Contexto

Identifique o envenenamento de contexto observando estes comportamentos:

*   **Qualidade Degradada da Saída:** Sugestões tornam-se sem sentido, repetitivas ou irrelevantes.
*   **Desalinhamento de Ferramentas:** Chamadas de ferramentas não correspondem mais às solicitações do usuário.
*   **Falhas na Orquestração:** Cadeias de orquestração podem travar, entrar em loop indefinidamente ou falhar ao completar.
*   **Correções Temporárias:** Reaplicar um prompt limpo ou instruções oferece apenas um alívio breve antes que os problemas reapareçam.
*   **Confusão no Uso de Ferramentas:** O modelo tem dificuldade em usar corretamente ou lembrar como usar ferramentas definidas no prompt do sistema.

---

## Causas Comuns

O envenenamento de contexto pode ser desencadeado por vários fatores:

*   **Alucinação do Modelo:** O modelo gera uma informação incorreta e subsequentemente a trata como parte factual do contexto.
*   **Comentários no Código:** Comentários desatualizados, incorretos ou ambíguos no código podem ser mal interpretados pelo modelo.
*   **Entrada do Usuário Contaminada:** Copiar e colar logs ou textos contendo caracteres de controle ocultos ou maliciosos.
*   **Estouro da Janela de Contexto:** À medida que uma sessão cresce, informações úteis mais antigas podem ser empurradas para fora da janela de contexto limitada do modelo.

Dados ruins no contexto tendem a persistir. O modelo reavalia essas informações contaminadas em ciclos de raciocínio subsequentes.

---

## Um "Prompt de Reativação" Resolve o Envenenamento de Contexto?

**Resposta Curta:** Não.

Um prompt corretivo pode suprimir temporariamente os sintomas, mas os dados problemáticos permanecem no buffer da conversa. O modelo provavelmente reverterá ao estado envenenado assim que a interação desviar do escopo restrito do prompt corretivo.

**Explicação Detalhada:**

*   Reaplicar as definições de ferramentas pode mascarar o dano por algumas interações.
*   O contexto envenenado subjacente permanece. Qualquer tarefa fora do "remendo" imediato provavelmente reativará o problema.
*   Essa abordagem é pouco confiável, como colocar um aviso em um cano vazando em vez de consertá-lo.

---

## Estratégias Eficazes de Recuperação

Para se recuperar do envenenamento de contexto:

*   **Reinício Completo da Sessão:** A solução mais confiável é iniciar uma nova sessão de chat.
*   **Minimize Despejos de Dados Manuais:** Ao colar logs, inclua apenas informações essenciais.
*   **Gerencie o Tamanho da Janela de Contexto:** Para tarefas grandes, divida em sessões menores e focadas.
*   **Valide a Saída das Ferramentas:** Se uma ferramenta retornar dados incorretos, exclua essa mensagem do histórico antes que o modelo a processe.

---

## Respondendo a uma Pergunta Comum: O Prompt "Bala Mágica"

Uma pergunta frequente da comunidade:
> "Existe algum prompt que reative o modelo? Talvez um prompt com as instruções das ferramentas que possamos reinserir manualmente?"

Como explicado, nenhum prompt único oferece uma solução duradoura. Qualquer melhoria imediata é superficial porque as linhas de texto corrompidas persistem no histórico da sessão. A única solução robusta é descartar a sessão comprometida e iniciar uma nova com um prompt limpo.
