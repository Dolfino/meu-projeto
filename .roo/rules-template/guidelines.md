# Diretrizes para Documentação de Modos SPARC

## Boas Práticas

1. **Estrutura**:
   - Manter arquivos ≤ 500 linhas
   - Usar front matter YAML para metadados
   - Organizar por seções lógicas

2. **Conteúdo**:
   - Documentar todos os handoffs
   - Listar artefatos esperados
   - Incluir exemplos práticos

3. **Estilo**:
   - Usar voz ativa
   - Frases curtas (≤ 25 palavras)
   - Código em blocos com syntax highlighting

## Convenções

### Nomenclatura
- `slug-do-modo`: sempre em inglês, kebab-case
- Arquivos: `rules-[slug].md`
- Diretórios: `[slug]-examples/`

### Exemplo de Front Matter
```yaml
---
title: Nome do Modo
description: Descrição clara do propósito
slug: slug-do-modo
version: 1.0.0
requires:
  - outro-modo
  - ferramenta-específica
---
```

## Related Links
- [Template Base](./README.md)
- [Exemplos Completos](./examples/)
