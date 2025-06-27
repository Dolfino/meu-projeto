---
sidebar_label: Sua Primeira Tarefa
---

import KangarooIcon from '@site/src/components/KangarooIcon';

# Iniciando Sua Primeira Tarefa com o Roo Code

Agora que você [configurou seu provedor de IA e modelo](/getting-started/connecting-api-provider), está pronto para começar a usar o Roo Code! Este guia orienta você em sua primeira interação.
---

## Passo 1: Abra o Painel do Roo Code

Clique no ícone do Roo Code (<KangarooIcon />) na Barra de Atividades do VS Code (barra vertical na lateral da janela) para abrir a interface de chat. Se não vir o ícone, verifique se a extensão está instalada e habilitada.

<img src="/img/your-first-task/your-first-task.png" alt="Ícone do Roo Code na Barra de Atividades do VS Code" width="800" />

*O ícone do Roo Code na Barra de Atividades abre a interface de chat.*

---

## Passo 2: Digite Sua Tarefa

Digite uma descrição clara e concisa do que deseja que o Roo Code faça na caixa de chat na parte inferior do painel. Exemplos de tarefas eficazes:

* "Crie um arquivo chamado `hello.txt` contendo 'Olá, mundo!'."
* "Escreva uma função Python que some dois números."
* "Crie um arquivo HTML para um site simples com o título 'Teste Roo'"

Nenhum comando ou sintaxe especial é necessária - use apenas linguagem natural.

<img src="/img/your-first-task/your-first-task-6.png" alt="Digitando uma tarefa na interface de chat do Roo Code" width="500" />
*Digite sua tarefa em linguagem natural - sem sintaxe especial necessária.*

---

## Passo 3: Envie Sua Tarefa

Pressione Enter ou clique no ícone Enviar (<Codicon name="send" />) à direita da caixa de entrada.

---

## Passo 4: Revise e Aprove Ações

O Roo Code analisa sua solicitação e propõe ações específicas. Estas podem incluir:

* **Ler arquivos:** Mostra conteúdos de arquivos que precisa acessar
* **Escrever em arquivos:** Exibe um diff com as alterações propostas (linhas adicionadas em verde, removidas em vermelho)
* **Executar comandos:** Mostra o comando exato a ser executado no terminal
* **Usar o Navegador:** Descreve ações no navegador (clicar, digitar, etc.)
* **Fazer perguntas:** Solicita esclarecimentos quando necessário para prosseguir

<img src="/img/your-first-task/your-first-task-7.png" alt="Revisando uma ação proposta de criação de arquivo" width="800" />
*O Roo Code mostra exatamente qual ação deseja realizar e aguarda sua aprovação.*

**Cada ação requer sua aprovação explícita** (a menos que a aprovação automática esteja habilitada):

* **Aprovar:** Clique no botão "Aprovar" para executar a ação proposta
* **Rejeitar:** Clique no botão "Rejeitar" e forneça feedback se necessário

---

## Passo 5: Iteração

O Roo Code trabalha de forma iterativa. Após cada ação, ele aguarda seu feedback antes de propor o próximo passo. Continue este ciclo de revisão-aprovação até que sua tarefa seja concluída.

<img src="/img/your-first-task/your-first-task-8.png" alt="Resultado final de uma tarefa concluída mostrando o processo de iteração" width="500" />
*Após concluir a tarefa, o Roo Code mostra o resultado final e aguarda sua próxima instrução.*

---

## Conclusão

Você concluiu sua primeira tarefa com o Roo Code! Através deste processo, você aprendeu:

* Como interagir com o Roo Code usando linguagem natural
* O fluxo de trabalho baseado em aprovação que mantém você no controle
* A abordagem iterativa que o Roo Code usa para resolver problemas passo a passo

Este fluxo de trabalho iterativo e baseado em aprovação é central para o funcionamento do Roo Code - permitindo que a IA lide com partes tediosas da programação enquanto você mantém supervisão total. Agora que você entende o básico, está pronto para tarefas mais complexas, explorar diferentes [modos](/basic-usage/using-modes) para fluxos especializados ou experimentar o [recurso de aprovação automática](/features/auto-approving-actions) para agilizar tarefas repetitivas.
