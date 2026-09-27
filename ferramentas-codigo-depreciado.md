# Atividade I.VI: Código Depreciado

## Objetivo

Analisar o projeto inteiro e detectar código depreciado antes de realizar as correções.

O projeto possui código em Python, Java e JavaScript. Por isso, devem ser usadas ferramentas específicas para cada tecnologia.

## Python

### Análise de todos os arquivos

Ferramenta: **Ruff**.

Comando:

```powershell
ruff check --select UP005,UP019,UP023,UP026,UP035,UP051 agendeja_rest gateway chat_tcp_udp
```

Esse comando analisa os arquivos Python dos diretórios `agendeja_rest`, `gateway` e `chat_tcp_udp` sem executar servidores ou abrir sockets.

### Depreciações em tempo de execução

Comando geral:

```powershell
python -W error::DeprecationWarning -m pytest
```

O parâmetro `-W error::DeprecationWarning` transforma qualquer aviso de depreciação emitido durante os testes em erro.

## Java

Ferramenta: **jdeprscan**, incluída no JDK.

Primeiro, o projeto deve ser compilado:

```powershell
cd soap
javac -cp "lib/*" -d build src/com/agendeja/soap/*.java
```

Depois, a análise pode ser executada:

```powershell
jdeprscan --class-path "lib/*;build" build
```

No GitHub Actions, o separador do classpath deve ser `:`:

```bash
jdeprscan --class-path "lib/*:build" build
```

O `jdeprscan` identifica o uso de APIs depreciadas do Java SE nos arquivos compilados.

## JavaScript

O frontend possui arquivos `.js`, mas não possui `package.json`, TypeScript ou configuração ESLint.

Para configurar uma análise futura, pode ser utilizado o ESLint:

```powershell
npx eslint "frontend/**/*.js"
```

A detecção específica de APIs depreciadas em JavaScript exige configuração adicional e informações de tipos. O ESLint sozinho não identifica todas as APIs depreciadas.

## Fontes

- [Python: warnings](https://docs.python.org/3/library/warnings.html)
- [Pytest: captura de warnings](https://docs.pytest.org/en/stable/how-to/capture-warnings.html)
- [Ruff: regras](https://docs.astral.sh/ruff/rules/)
- [Oracle: jdeprscan](https://docs.oracle.com/en/java/javase/21/docs/specs/man/jdeprscan.html)
- [ESLint: linha de comando](https://eslint.org/docs/latest/use/command-line-interface)
