# Versionamento semântico e LTS

**Projeto:** AgendaJá  
**Data da pesquisa:** 27/09/2026

## Componentes analisados

| Componente | Evidência no projeto | Versionamento semântico | LTS |
|---|---|---|---|
| Django 5.0.3 | [requirements.txt](requirements.txt#L1) | **Sim, parcialmente.** O Django usa uma forma flexível de Semantic Versioning, com versões no formato `A.B.C`. | **Sim.** O projeto Django possui versões LTS. Porém, a versão usada (`5.0.3`) não é LTS e está fora de suporte. |
| RabbitMQ 3 | [docker-compose.yml](docker-compose.yml#L2) | **Sim.** As versões oficiais usam o formato `major.minor.patch`, como `4.3.6`, `4.2.10` e `3.13.7`. | **Sim.** O RabbitMQ possui suporte de longo prazo, principalmente na modalidade comercial. A imagem usada (`rabbitmq:3-management`) não fixa a versão menor nem o patch. |
| FastAPI 0.111.0 | [requirements.txt](requirements.txt#L6) | **Sim, na prática.** As releases oficiais usam versões com três componentes, como `0.141.1` e `0.140.13`. | **Não identificado.** Não há evidência oficial de um ciclo LTS para o FastAPI. |

## Evidências oficiais

### Django

A documentação oficial informa:

> "Starting with Django 2.0, version numbers will use a loose form of semantic versioning."

Também informa:

> "Certain feature releases will be designated as long-term support (LTS) releases."

- [Django: processo de releases](https://docs.djangoproject.com/en/5.0/internals/release-process/)
- [Django: versões suportadas e LTS](https://www.djangoproject.com/download/)

### RabbitMQ

A página oficial apresenta releases como `4.3.6`, `4.2.10`, `4.1.8` e `3.13.7`. A mesma página possui a seção **LONG TERM SUPPORT** e informa as datas de suporte comunitário e comercial.

- [RabbitMQ: informações de releases](https://www.rabbitmq.com/release-information)

### FastAPI

O repositório oficial apresenta releases como `0.141.1`, `0.141.0` e `0.140.13`, evidenciando o uso de versões no formato `major.minor.patch`. Entretanto, não há indicação oficial de versões LTS.

- [FastAPI: releases oficiais](https://github.com/fastapi/fastapi/releases)

## Conclusão

- **Django:** possui versionamento semântico e versões LTS.
- **RabbitMQ:** possui versionamento semântico e suporte de longo prazo/comercial.
- **FastAPI:** possui versionamento semântico, mas não foi identificada política oficial de LTS.

