# Digitando Suas Solicitações

O Roo Code foi projetado para entender linguagem natural. Você não precisa usar comandos ou sintaxe especiais. Basta digitar sua solicitação em português claro, como se estivesse falando com um desenvolvedor humano.

<img src="/img/typing-your-requests/naturally.gif" alt="Exemplo de digitação de solicitação no Roo Code" width="600" />

---

## Estratégias Eficazes

Seja claro sobre o que deseja que o Roo Code faça. Evite linguagem vaga ou ambígua.

| Estratégia | Implementação |
|------------|---------------|
| **Seja específico** | "Corrija o bug em `calculateTotal` que retorna resultados incorretos" em vez de "Corrija o código" |
| **Forneça contexto** | Use @ [Menções de Contexto](/basic-usage/context-mentions) para referenciar arquivos |
| **Divida tarefas** | Envie tarefas complexas em etapas menores |
| **Inclua exemplos** | Forneça código de exemplo quando precisar de formatação específica |

---

## Exemplos de Solicitações

```
crie um arquivo `utils.py` com uma função `add` que recebe dois números e retorna a soma
```
```
no arquivo @src/components/Button.tsx, mude a cor do botão para azul
```
```
encontre todas as ocorrências de `oldValue` em @/src/App.js e substitua por `newValue`
```
```
execute o comando `npm install` no terminal
```
```
explique a função `calculateTotal` em @/src/utils.ts
```
```
@problems corrija todos os problemas detectados
```

---

## Armadilhas Comuns a Evitar

| NÃO FAÇA | FAÇA |
|----------|------|
| Solicitações vagas | Especifique exatamente o que precisa ser feito |
| Assumir contexto | Referencie explicitamente arquivos e funções |
| Jargão técnico excessivo | Use linguagem clara e direta |
| Múltiplas tarefas não relacionadas | Envie uma solicitação focada por vez |
| Prosseguir sem confirmação | Verifique se o código está completo |
