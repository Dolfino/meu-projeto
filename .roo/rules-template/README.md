# Template de Regras para Modos SPARC

```yaml
---
title: Nome do Modo
description: Descrição breve do propósito do modo
slug: slug-do-modo
version: 1.0.0
---
```

## Estrutura Básica
1. **Definições Principais**:
   - Objetivo do modo
   - Quando usar
   - Restrições

2. **Handoffs**:
   - Quais modos podem acionar este modo
   - Para quais modos pode delegar

3. **Artefatos**:
   - Tipos de arquivos/saídas esperadas
   - Templates recomendados

## Exemplo de Uso
```markdown
# Modo Exemplo

```yaml
handoff_to:
  - code: quando_precisa_implementar
  - test: quando_precisa_testar
```

## Related Links
- [Guia de Boas Práticas](./guidelines.md)
- [Exemplos](./examples/)
