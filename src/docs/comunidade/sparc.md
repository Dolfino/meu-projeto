# SPARC por ruvnet

[Ver Projeto no GitHub](https://github.com/ruvnet/rUv-dev)

O SPARC orquestra fluxos de trabalho de desenvolvimento agentes "definir e esquecer" através de um framework estruturado usando Tarefas Boomerang do Roo Code. Ele automatiza o desenvolvimento de código complexo mantendo o controle total do desenvolvedor.
O framework é open-source com documentação abrangente e exemplos, suportando desde aplicações simples até sistemas complexos.

---

## Principais Recursos

- **Scaffolding**: Gera estruturas completas de projetos executando `npx create-sparc init` na pasta raiz, incluindo subdiretórios, configurações e código boilerplate
- **Prompting**: Templates otimizados para geração de código consistente e de alta qualidade
- **Modo Boomerang**: Defina requisitos → gere código → revise → refine em um loop contínuo de feedback
- **Tarefas Boomerang**: Define tarefas específicas de desenvolvimento que podem ser "lançadas" para o Roo e retornadas com implementações, permitindo resolução focada de problemas
- **Orquestração de Fluxo**: Coordena sequências complexas de desenvolvimento com cadeias de tarefas pré-definidas e gerenciamento de dependências
- **Serviços MCP**: Estende as capacidades do Roo com ferramentas e recursos especializados através da integração com Model Context Protocol
- **Gerenciamento de Modos**: Configurações sensíveis ao contexto que otimizam o comportamento para fases específicas de desenvolvimento

### Início Rápido
Você não precisa instalar este [pacote diretamente](https://www.npmjs.com/package/create-sparc). Basta executar npx do seu diretório raiz para instalá-lo:

```bash
 npx create-sparc init
 npx create-sparc --help
