# Exemplo: Modo Logger Simples

```yaml
---
title: Simple Logger
description: Modo para registro centralizado de logs
slug: simple-logger
version: 1.0.0
requires:
  - memory-bank-system
---
```

## Quando Usar
- Registrar eventos importantes
- Rastrear fluxos complexos
- Auditoria de operações

## Handoffs
```yaml
handoff_from:
  - code: quando_ocorre_erro
  - debug: quando_precisa_rastrear

handoff_to:
  - memory-bank-system: para_armazenar_logs
```

## Artefatos Esperados
1. Arquivos de log formatados
2. Estatísticas de eventos
3. Alertas configurados

## Exemplo de Implementação
```python
def log_event(event_type, message):
    """Registra evento formatado"""
    entry = f"[{datetime.now()}] {event_type}: {message}"
    write_to_memory_bank(entry)
```

## Related Links
- [Guidelines](../guidelines.md)
- [Template](../README.md)
