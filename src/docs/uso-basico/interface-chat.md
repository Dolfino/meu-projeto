import KangarooIcon from '@site/src/components/KangarooIcon';

# Interface do Chat

A interface de chat do Roo Code é a principal forma de interação. Está localizada no painel do Roo Code, que pode ser aberto clicando no ícone do Roo Code (<KangarooIcon />) na Barra de Atividades do VS Code.

---

## Componentes da Interface

A interface de chat consiste nos seguintes elementos principais:

1. **Histórico de Conversa:** Exibe o histórico entre você e o Roo Code. Mostra suas solicitações, respostas e ações realizadas (como edições de arquivo ou execução de comandos).

2. **Campo de Entrada:** Onde você digita tarefas e perguntas para o Roo Code. Pode usar linguagem natural.

3. **Botões de Ação:** Aparecem acima do campo de entrada. Permitem aprovar ou rejeitar ações propostas pelo Roo Code. Os botões variam conforme o contexto.

4. **Botão Enviar:** Ícone de avião no canto direito do campo. Envia mensagens para o Roo após digitação.

5. **Botão Plus (+):** Localizado no cabeçalho. Reinicia a sessão atual.

6. **Botão Configurações:** Ícone de engrenagem. Abre as configurações para personalização.

7. **Seletor de Modo:** Dropdown à esquerda do campo de entrada. Seleciona o modo de operação do Roo.

<img src="/img/the-chat-interface/the-chat-interface-1.png" alt="Componentes da interface de chat com numeração" width="900" />

*Elementos numerados mostrando os principais componentes da interface do Roo Code.*

---

## Interação com Mensagens

* **Links Clicáveis:** Caminhos de arquivo e URLs no histórico são clicáveis. Arquivos abrem no editor, URLs no navegador padrão.
* **Copiar Texto:** Selecione texto e use Ctrl/Cmd + C. Blocos de código têm botão "Copiar" dedicado.
* **Expandir/Recolher:** Clique em uma mensagem para alternar.

---

## Indicadores de Status

* **Carregamento:** Spinner aparece durante processamento.
* **Erros:** Mensagens em vermelho indicam problemas.
* **Sucesso:** Mensagens em verde confirmam ações concluídas.
