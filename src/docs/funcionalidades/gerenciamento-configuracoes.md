---
title: Importar, Exportar e Redefinir Configurações
sidebar_label: Importar/Exportar/Redefinir Configurações
description: Gerencie as configurações do Roo Code exportando, importando ou redefinindo para os padrões.
---

# Importar, Exportar e Redefinir Configurações

O Roo Code permite gerenciar suas configurações de forma eficaz através de opções de exportação, importação e redefinição. Esses recursos são úteis para fazer backup da sua configuração, compartilhar configurações com outros ou restaurar as configurações padrão, se necessário.

Você pode encontrar essas opções na parte inferior da página de configurações do Roo Code, acessível através do ícone de engrenagem (<i class="codicon codicon-gear"></i>) na visualização de chat do Roo Code.

<img src="/img/settings-management/settings-management.png" alt="Botões Exportar, Importar e Redefinir nas configurações do Roo Code" width="400" />
*Imagem: Botões Exportar, Importar e Redefinir.*

---

## Exportar Configurações

Clicar no botão **Exportar** salva suas configurações atuais do Roo Code em um arquivo JSON.

*   **O que é exportado:** O arquivo inclui seus Perfis de Provedor de API configurados e Configurações Globais (preferências de UI, configurações de modo, configurações de contexto, etc.).
*   **Aviso de segurança:** O arquivo JSON exportado contém **todas** as suas configurações de Perfis de Provedor de API e Configurações Globais. Crucialmente, isso inclui **chaves de API em texto claro**. Trate este arquivo como altamente sensível. Não o compartilhe publicamente ou com pessoas não confiáveis, pois ele concede acesso às suas contas de API.
*   **Processo:**
    1.  Clique em **Exportar**.
    2.  Um diálogo de salvamento de arquivo aparece, sugerindo `roo-code-settings.json` como nome do arquivo (geralmente na pasta `~/Documents`).
    3.  Escolha um local e salve o arquivo.

Isso cria um backup da sua configuração ou um arquivo que você pode compartilhar.

---

## Importar Configurações

Clicar no botão **Importar** permite carregar configurações de um arquivo JSON exportado anteriormente.

*   **Processo:**
    1.  Clique em **Importar**.
    2.  Um diálogo de abertura de arquivo aparece. Selecione o arquivo `roo-code-settings.json` (ou arquivo com nome similar) que deseja importar.
    3.  O Roo Code lê o arquivo, valida seu conteúdo em relação ao esquema esperado e aplica as configurações.
*   **Mesclagem:** Importar configurações **mescla** as configurações. Ele adiciona novos perfis de API e atualiza os existentes e configurações globais com base no conteúdo do arquivo. Ele **não** exclui configurações presentes na sua configuração atual, mas ausentes no arquivo importado.
*   **Validação:** Apenas configurações válidas que correspondam ao esquema interno podem ser importadas, prevenindo erros de configuração. Uma notificação de sucesso aparece após a conclusão.

---

## Redefinir Configurações

Clicar no botão **Redefinir** limpa completamente todos os dados de configuração do Roo Code e retorna a extensão ao seu estado padrão. Esta é uma ação destrutiva destinada a solução de problemas ou para começar do zero.

*   **Aviso:** Esta ação é **irreversível**. Ela exclui permanentemente todas as configurações de API (incluindo chaves armazenadas no armazenamento secreto), modos personalizados, configurações globais e histórico de tarefas.

*   **Processo:**
    1.  Clique no botão vermelho **Redefinir**.
    2.  Um diálogo de confirmação aparece, avisando que a ação não pode ser desfeita.
    3.  Clique em "Sim" para confirmar.

*   **O que é redefinido:**
    *   **Perfis de Provedor de API:** Todas as configurações são excluídas das configurações e do armazenamento secreto.
    *   **Configurações Globais:** Todas as preferências (UI, modos, aprovações, navegador, etc.) são redefinidas para os padrões.
    *   **Modos Personalizados:** Todos os modos definidos pelo usuário são excluídos.
    *   **Armazenamento Secreto:** Todas as chaves de API e outros segredos gerenciados pelo Roo Code são limpos.
    *   **Histórico de Tarefas:** A pilha de tarefas atual é limpa.

*   **Resultado:** O Roo Code retorna ao seu estado inicial, como se fosse instalado recentemente, com configurações padrão e sem configurações do usuário.

Use esta opção apenas se tiver certeza de que deseja remover todos os dados do Roo Code ou se for instruído durante a solução de problemas. Considere exportar suas configurações primeiro se quiser restaurá-las posteriormente.
