# write_to_file

A ferramenta `write_to_file` cria novos arquivos ou substitui completamente arquivos existentes no sistema. É especialmente útil para gerar código, configurações ou documentação de forma programática.

:::warning Substituição Completa
Esta ferramenta substitui TODO o conteúdo do arquivo especificado. Para modificações parciais, considere usar [`apply_diff`](/advanced-usage/available-tools/apply-diff) ou [`insert_content`](/advanced-usage/available-tools/insert-content).
:::

---

## Parâmetros

- `path` (obrigatório): Caminho do arquivo a ser criado/atualizado (relativo ao diretório de trabalho)
- `content` (obrigatório): Conteúdo completo a ser escrito no arquivo
- `line_count` (obrigatório): Número total de linhas do conteúdo

:::important Conteúdo Completo
Você DEVE fornecer o conteúdo COMPLETO do arquivo, mesmo para atualizações. Omitir partes do arquivo resultará em perda de dados.
:::

---

## Quando é Usada?

- Criar novos arquivos de código, configuração ou documentação
- Substituir completamente arquivos existentes quando necessário
- Gerar arquivos automaticamente baseados em templates
- Inicializar projetos ou componentes

---

## Principais Recursos

- Cria automaticamente diretórios necessários no caminho
- Garante quebras de linha consistentes de acordo com o sistema operacional
- Valida o conteúdo antes de escrever para evitar arquivos corrompidos
- Fornece confirmação explícita antes de substituir arquivos existentes

---

## Limitações

- Não suporta modificações parciais (use `apply_diff` ou `insert_content`)
- Requer que todo o conteúdo do arquivo seja fornecido de uma vez
- Arquivos muito grandes podem exceder limites de memória/tokens

---

## Exemplos de Uso

### Criando um novo arquivo de configuração

```xml
<write_to_file>
<path>config.json</path>
<content>
{
  "apiEndpoint": "https://api.example.com",
  "timeout": 5000,
  "features": {
    "darkMode": true,
    "notifications": false
  }
}

### Atualizando um arquivo existente

```xml
<write_to_file>
<path>src/utils.js</path>
<content>
export function debounce(func, delay) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), delay);
  };
}

export function throttle(func, limit) {
  let lastFunc;
  let lastRan;
  return function(...args) {
    if (!lastRan) {
      func.apply(this, args);
      lastRan = Date.now();
    } else {
      clearTimeout(lastFunc);
      lastFunc = setTimeout(() => {
        if ((Date.now() - lastRan) >= limit) {
          func.apply(this, args);
          lastRan = Date.now();
        }
      }, limit - (Date.now() - lastRan));
    }
  };
}
</content>
<line_count>20</line_count>
</write_to_file>
```

---

## Boas Práticas

1. **Verifique o conteúdo**: Sempre revise o conteúdo antes de escrever no arquivo
2. **Use versionamento**: Certifique-se de ter commitado as alterações atuais antes de substituir arquivos
3. **Mantenha backups**: Considere criar uma cópia do arquivo original antes de substituí-lo
4. **Teste em ambiente seguro**: Execute operações de escrita primeiro em ambientes de desenvolvimento

---

## Considerações de Segurança

- Evite escrever arquivos em diretórios sensíveis do sistema
- Não inclua credenciais ou informações sensíveis no conteúdo
- Valide todos os caminhos para evitar ataques de path traversal
- Considere usar `security-review` para arquivos que lidam com autenticação ou dados sensíveis

---

## Compatibilidade

Funciona em todos os sistemas operacionais suportados pelo Roo Code. As quebras de linha são automaticamente convertidas para o formato do sistema operacional alvo.
