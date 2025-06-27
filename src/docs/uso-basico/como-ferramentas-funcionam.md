# Como as Ferramentas Funcionam

O Roo Code utiliza ferramentas para interagir com seu código e ambiente. Esses auxiliares especializados realizam ações como ler arquivos, fazer edições, executar comandos ou pesquisar na base de código. As ferramentas automatizam tarefas comuns de desenvolvimento.

---

## Fluxo de Trabalho

Descreva o que deseja realizar em linguagem natural, e o Roo Code irá:

1. Selecionar a ferramenta apropriada
2. Apresentar a ferramenta e seus parâmetros para revisão
3. Executar a ferramenta aprovada e mostrar os resultados
4. Repetir o processo até a conclusão da tarefa

---

## Categorias de Ferramentas

| Categoria | Finalidade | Nomes das Ferramentas |
| :-------- | :--------- | :-------------------- |
| Leitura | Acessar conteúdo de arquivos e estrutura de código | `read_file`, `search_files`, `list_files`, `list_code_definition_names` |
| Edição | Criar ou modificar arquivos | `write_to_file`, `apply_diff` |
| Execução | Rodar comandos e operações no sistema | `execute_command` |
| Navegador | Interagir com conteúdo web | `browser_action` |
| Fluxo | Gerenciar tarefas e contexto | `ask_followup_question`, `attempt_completion`, `switch_mode`, `new_task` |

---

## Exemplo: Usando Ferramentas

Veja como uma interação típica funciona:

<img src="/img/how-tools-work/how-tools-work.png" alt="Interface de aprovação mostrando botões Salvar e Rejeitar com opção de Auto-aprovação" width="600" />

*Interface de aprovação mostra botões Salvar/Rejeitar e opção de Auto-aprovação.*

**Usuário:** Crie um arquivo `greeting.js` que mostre uma mensagem

**Roo Code:** (Propõe a ferramenta `write_to_file` como na imagem)
```xml
<write_to_file>
<path>greeting.js</path>
<content>
function greet(name) {
  console.log(`Hello, ${name}!`);
}

greet('World');
</content>
<line_count>5</line_count>
</write_to_file>
```

**Usuário:** (Clica em "Salvar")

**Roo Code:** (Confirma criação do arquivo)

---

## Segurança e Aprovação

Toda ferramenta requer aprovação explícita. Quando o Roo propõe uma ferramenta, você verá:

* Botão "Salvar" para aprovar e executar
* Botão "Rejeitar" para recusar
* Opção "Auto-aprovar" para operações confiáveis

Esse mecanismo garante controle sobre modificações em arquivos e execução de comandos. Sempre revise as propostas cuidadosamente.

---

## Referência de Ferramentas

| Ferramenta | Descrição | Categoria |
| :--------- | :-------- | :-------- |
| `read_file` | Lê conteúdo de arquivo com numeração de linhas | Leitura |
| `search_files` | Busca por texto ou padrões regex | Leitura |
| `list_files` | Lista arquivos e diretórios | Leitura |
| `list_code_definition_names` | Lista definições como classes e funções | Leitura |
| `write_to_file` | Cria ou sobrescreve arquivos | Edição |
| `apply_diff` | Faz alterações precisas em partes específicas | Edição |
| `execute_command` | Executa comandos no terminal do VS Code | Execução |
| `browser_action` | Ações em navegador headless | Navegador |
| `ask_followup_question` | Faz perguntas para esclarecimento | Fluxo |
| `attempt_completion` | Indica conclusão da tarefa | Fluxo |
| `switch_mode` | Muda para outro modo operacional | Fluxo |
| `new_task` | Cria uma nova subtarefa | Fluxo |

---

## Saiba Mais

Para detalhes sobre cada ferramenta, incluindo parâmetros e padrões avançados, consulte a documentação [Visão Geral das Ferramentas](/advanced-usage/available-tools/tool-use-overview).
