import KangarooIcon from '@site/src/components/KangarooIcon';

# Temperatura do Modelo

A temperatura controla a aleatoriedade das saídas do modelo de IA. Ajustar essa configuração otimiza os resultados para diferentes tarefas - desde geração precisa de código até brainstorming criativo. A temperatura é um dos parâmetros mais poderosos para controlar o comportamento da IA. Uma configuração de temperatura bem ajustada pode melhorar drasticamente a qualidade e adequação das respostas para tarefas específicas.

<img src="/img/model-temperature/model-temperature.gif" alt="Animação mostrando ajuste do controle deslizante de temperatura" width="100%" />

---

## O que é Temperatura?

Temperatura é uma configuração (geralmente entre 0.0 e 2.0) que controla o quão aleatória ou previsível é a saída da IA. Encontrar o equilíbrio certo é fundamental: valores mais baixos tornam a saída mais focada e consistente, enquanto valores mais altos incentivam mais criatividade e variação. Para muitas tarefas de codificação, uma temperatura moderada (em torno de 0.3 a 0.7) geralmente funciona bem, mas a melhor configuração depende do que você está tentando alcançar.

:::info Temperatura e Código: Equívocos Comuns
A temperatura controla a aleatoriedade da saída, não a qualidade ou precisão do código diretamente. Pontos-chave:

*   **Temperatura Baixa (próximo de 0.0):** Produz código previsível e consistente. Bom para tarefas simples, mas pode ser repetitivo e carecer de criatividade. Não garante código *melhor*.
*   **Temperatura Alta:** Aumenta a aleatoriedade, potencialmente levando a soluções criativas, mas também a mais erros ou código sem sentido. Não garante código *de maior qualidade*.
*   **Precisão:** A precisão do código depende do treinamento do modelo e da clareza do prompt, não da temperatura.
*   **Temperatura 0.0:** Útil para consistência, mas limita a exploração necessária para problemas complexos.
:::

---

## Valores Padrão no Roo Code

O Roo Code usa uma temperatura padrão de 0.0 para a maioria dos modelos, otimizando para máxima determinismo e precisão na geração de código. Isso se aplica a modelos OpenAI, modelos Anthropic (variantes não pensantes), modelos LM Studio e a maioria dos outros provedores.

Alguns modelos usam temperaturas padrão mais altas - modelos DeepSeek R1 e certos modelos focados em raciocínio usam 0.6 como padrão, proporcionando um equilíbrio entre determinismo e exploração criativa.

Modelos com capacidades de pensamento (onde a IA mostra seu processo de raciocínio) requerem uma temperatura fixa de 1.0 que não pode ser alterada, pois essa configuração garante o desempenho ideal do mecanismo de pensamento. Isso se aplica a qualquer modelo com o flag ":thinking" ativado.

Alguns modelos especializados não suportam ajustes de temperatura, caso em que o Roo Code respeita essas limitações automaticamente.

---

## Quando Ajustar a Temperatura

Aqui estão alguns exemplos de configurações de temperatura que podem funcionar bem para diferentes tarefas:

*   **Modo Código (0.0-0.3):** Para escrever código preciso e correto com resultados consistentes e determinísticos
*   **Modo Arquiteto (0.4-0.7):** Para brainstorming de soluções de arquitetura ou design com equilíbrio entre criatividade e estrutura
*   **Modo Perguntar (0.7-1.0):** Para explicações ou perguntas abertas que exigem respostas diversas e perspicazes
*   **Modo Depuração (0.0-0.3):** Para solução de problemas de bugs com precisão consistente

Estes são pontos de partida - é importante [experimentar diferentes configurações](#experimentação) para descobrir o que funciona melhor para suas necessidades e preferências específicas.

---

## Como Ajustar a Temperatura

1.  **Abra o Painel do Roo Code:** Clique no ícone do Roo Code (<KangarooIcon />) na Barra de Atividades do VS Code
2.  **Abra as Configurações:** Clique no ícone <Codicon name="gear" /> no canto superior direito
3.  **Encontre o Controle de Temperatura:** Navegue até a seção Provedores
4.  **Ative a Temperatura Personalizada:** Marque a caixa "Usar temperatura personalizada"
5.  **Defina Seu Valor:** Ajuste o controle deslizante para o valor desejado

    <img src="/img/model-temperature/model-temperature.png" alt="Configuração de temperatura no painel de configurações do Roo Code" width="550" />
    *Controle deslizante de temperatura no painel de configurações do Roo Code*

---

## Usando Perfis de Configuração de API para Temperatura

Crie vários [perfis de configuração de API](/features/api-configuration-profiles) com diferentes configurações de temperatura:

**Como configurar perfis de temperatura específicos para tarefas:**

1. Crie perfis especializados como "Código - Temp Baixa" (0.1) e "Perguntar - Temp Alta" (0.8)
2. Configure cada perfil com as configurações de temperatura apropriadas
3. Alterne entre perfis usando o menu suspenso nas configurações ou interface de chat
4. Defina perfis diferentes como padrão para cada modo para alternância automática ao mudar de modos

Essa abordagem otimiza o comportamento do modelo para tarefas específicas sem ajustes manuais.

---

## Implementação Técnica

O Roo Code implementa o controle de temperatura com estas considerações:

*   Configurações definidas pelo usuário têm prioridade sobre os padrões
*   Comportamentos específicos do provedor são respeitados
*   Limitações específicas do modelo são aplicadas:
    *   Modelos com pensamento habilitado requerem temperatura fixa de 1.0
    *   Alguns modelos não suportam ajustes de temperatura

---

## Experimentação

Experimentar com diferentes configurações de temperatura é a maneira mais eficaz de descobrir o que funciona melhor para suas necessidades específicas:

### Teste Efetivo de Temperatura

1. **Comece com os padrões** - Use os valores predefinidos do Roo Code (0.0 para a maioria das tarefas) como linha de base
2. **Faça ajustes incrementais** - Altere os valores em pequenos passos (±0.1) para observar diferenças sutis
3. **Teste consistentemente** - Use o mesmo prompt em diferentes configurações de temperatura para comparações válidas
4. **Documente os resultados** - Anote quais valores produzem os melhores resultados para tipos específicos de tarefas
5. **Crie perfis** - Salve configurações eficazes como [perfis de configuração de API](/features/api-configuration-profiles) para acesso rápido

Lembre-se de que modelos diferentes podem responder de forma diferente aos mesmos valores de temperatura, e modelos com pensamento habilitado sempre usam uma temperatura fixa de 1.0, independentemente de suas configurações.

---

## Recursos Relacionados

- Funciona com todos [provedores de API](/providers/openai) suportados pelo Roo Code
- Complementa [instruções personalizadas](/features/custom-instructions) para ajustar respostas
- Funciona junto com [modos personalizados](/features/custom-modes) que você criar
