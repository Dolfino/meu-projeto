# Edições Rápidas/Diffs

:::info Configuração Padrão
As Edições Rápidas (usando a configuração "Habilitar edições via diffs") estão ativadas por padrão no Roo Code. Normalmente você não precisa alterar essas configurações, a menos que encontre problemas específicos ou queira experimentar diferentes estratégias de diff.
:::

O Roo Code oferece uma configuração avançada para mudar como ele edita arquivos, usando diffs (diferenças) em vez de reescrever arquivos inteiros. Habilitar esse recurso traz benefícios significativos.

:::note Configuração por Provedor
A configuração de edição por diffs é definida por [Perfil de Configuração de API](/features/api-configuration-profiles), permitindo que você personalize o comportamento de edição para diferentes provedores e modelos.
:::

---

## Habilitar Edições Via Diffs

Abra as configurações do painel do Roo Code clicando no ícone de engrenagem <Codicon name="gear" />. A seção `Providers` estará visível. Selecione o [Perfil de Configuração de API](/features/api-configuration-profiles) específico que deseja configurar.

Quando **Habilitar edições via diffs** estiver marcado:

    <img src="/img/fast-edits/fast-edits-2.png" alt="Configurações do Roo Code mostrando Habilitar edições via diffs" width="500" />
1.  **Edição de Arquivos Mais Rápida**: O Roo modifica arquivos mais rapidamente aplicando apenas as alterações necessárias.
2.  **Previne Gravações Truncadas**: O sistema detecta automaticamente e rejeita tentativas da IA de gravar conteúdo de arquivo incompleto, o que pode acontecer com arquivos grandes ou instruções complexas. Isso ajuda a prevenir arquivos corrompidos.

:::note Desativando Edições Rápidas
Se você desmarcar **Habilitar edições via diffs**, o Roo voltará a escrever o conteúdo completo do arquivo para cada edição usando a ferramenta [`write_to_file`](/advanced-usage/available-tools/write-to-file), em vez de aplicar alterações direcionadas com [`apply_diff`](/advanced-usage/available-tools/apply-diff). Essa abordagem de gravação completa é geralmente mais lenta para modificar arquivos existentes e leva a um maior uso de tokens.
:::

---

## Precisão de Correspondência

Este controle deslizante define o quão próximo as seções de código identificadas pela IA devem corresponder ao código real em seu arquivo antes que uma alteração seja aplicada.

    <img src="/img/fast-edits/fast-edits-4.png" alt="Configurações do Roo Code mostrando a caixa Habilitar edições via diffs e o controle deslizante Precisão de correspondência" width="500" />

*   **100% (Padrão)**: Exige uma correspondência exata. Esta é a opção mais segura, minimizando o risco de alterações incorretas.
*   **Valores Mais Baixos (80%-99%)**: Permite correspondência "fuzzy". O Roo pode aplicar alterações mesmo que a seção de código tenha pequenas diferenças do que a IA esperava. Isso pode ser útil se o arquivo foi ligeiramente modificado, mas **aumenta o risco** de aplicar alterações no lugar errado.

**Use valores abaixo de 100% com extremo cuidado.** Precisão mais baixa pode ser necessária ocasionalmente, mas sempre revise as alterações propostas cuidadosamente.

Internamente, essa configuração ajusta um `fuzzyMatchThreshold` usado com algoritmos como distância de Levenshtein para comparar similaridade de código.
