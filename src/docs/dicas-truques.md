# Dicas & Truques

Uma coleção de dicas rápidas para ajudar você a aproveitar ao máximo o Roo Code.

- Arraste o Roo Code para a [Barra Lateral Secundária](https://code.visualstudio.com/api/ux-guidelines/sidebars#secondary-sidebar) para continuar vendo o Explorer, Search, Source Control etc.
<img src="/img/right-column-roo.gif" alt="Coloque o Roo na Coluna Direita" width="900" />
- Com o Roo Code em uma barra lateral separada do explorador de arquivos, você pode arrastar arquivos do explorador para a janela de chat (e até vários de uma vez). Apenas certifique-se de segurar a tecla Shift depois de começar a arrastar os arquivos.
- Se não estiver usando [MCP](/features/mcp/overview), desative-o na aba <Codicon name="server" /> MCP Servers para reduzir significativamente o tamanho do prompt do sistema.
- Para manter seus [modos personalizados](/features/custom-modes) no caminho certo, limite os tipos de arquivos que eles podem editar.
- Se encontrar o temido erro `input length and max tokens exceed context limit`, você pode recuperar-se deletando uma mensagem, voltando a um checkpoint anterior ou alternando para um modelo com janela de contexto maior como o Gemini.
- Seja criterioso com a configuração de `Tokens Máximos` para modelos de pensamento. Cada token alocado reduz o espaço disponível para histórico da conversa. Considere usar altos valores de `Tokens Máximos` apenas em modos como Architect e Debug, mantendo o Code mode com 16k tokens ou menos.
- Se houver uma vaga de emprego real para algo que você quer que um modo personalizado faça, peça ao Code mode para `Criar um modo personalizado baseado na vaga em @[url]`
- Para acelerar ainda mais, clone múltiplas cópias do seu repositório e execute o Roo Code em todas em paralelo (usando git para resolver conflitos, como com devs humanos).
- Ao usar o Debug mode, peça ao Roo para "iniciar uma nova tarefa no Debug mode com todo o contexto necessário para resolver X" para que o processo de debug use sua própria janela de contexto.
- Adicione suas próprias dicas clicando em "Editar esta página" abaixo!
- Para gerenciar arquivos grandes e reduzir uso de recursos, ajuste a configuração `Limite de truncamento automático de leitura de arquivo`. Este controle define quantas linhas são lidas de um arquivo por vez. Valores menores melhoram performance com arquivos muito grandes.
- Configure um atalho de teclado para o comando [`roo.acceptInput`](/features/keyboard-shortcuts) para aceitar sugestões sem usar o mouse. Ideal para fluxos de trabalho focados em teclado.
- Use **Modelos Fixos** para atribuir modelos especializados a diferentes modos (modelo de raciocínio para planejamento, modelo não-racional para codificação). O Roo alterna automaticamente entre os modelos.
