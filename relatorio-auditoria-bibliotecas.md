# Atividade I.VII: Bibliotecas Seguras

## Ferramenta utilizada

Foi utilizado o **pip-audit** para verificar vulnerabilidades conhecidas nas dependências Python do projeto.

## Comando de auditoria

```powershell
pip-audit -r requirements.txt
```

## Resultado inicial

A auditoria encontrou:

```text
Found 69 known vulnerabilities in 6 packages
```

Pacotes identificados:

| Pacote | Versão anterior |
|---|---:|
| Django | 5.0.3 |
| djangorestframework | 3.15.1 |
| requests | 2.31.0 |
| python-dotenv | 1.0.1 |
| lxml | 4.9.3 |
| starlette | 0.37.2 |

## Comando de correção

```powershell
pip-audit -r requirements.txt --fix
```

## Atualizações aplicadas

| Pacote | Versão anterior | Versão atualizada |
|---|---:|---:|
| Django | 5.0.3 | 5.2.17 |
| djangorestframework | 3.15.1 | 3.17.2 |
| requests | 2.31.0 | 2.33.0 |
| python-dotenv | 1.0.1 | 1.2.2 |
| lxml | 4.9.3 | 6.1.0 |
| starlette | 0.37.2 | 1.3.1 |

O `pip-audit` também tentou adicionar o pacote `starlette` explicitamente ao arquivo `requirements.txt`, pois ele é uma dependência utilizada por outra biblioteca. Porém, essa alteração gerou conflito com `fastapi==0.111.0`, que exige uma versão diferente do Starlette. Por isso, o pacote transitivo não deve ser fixado manualmente sem atualizar o FastAPI de forma compatível.

## Falha na auditoria após a correção automática

Ao executar novamente:

```powershell
pip-audit -r requirements.txt
```

foi apresentada a falha:

```text
ERROR: Cannot install -r requirements.txt (line 7) and starlette==1.3.1 because these package versions have conflicting dependencies.
ERROR: ResolutionImpossible
```

A linha `starlette==1.3.1` foi removida do `requirements.txt`. A dependência Starlette deve ser resolvida pelo FastAPI, ou ambos devem ser atualizados juntos em uma etapa posterior.

## Evidência da correção

A saída do comando informou:

```text
Found 69 known vulnerabilities in 6 packages and fixed 69 vulnerabilities in 6 packages
```

## Conclusão

O `pip-audit` identificou vulnerabilidades nas bibliotecas Python e atualizou os pacotes para versões corrigidas. A auditoria deve ser executada novamente para confirmar que não restaram vulnerabilidades conhecidas:

```powershell
pip-audit -r requirements.txt
```
