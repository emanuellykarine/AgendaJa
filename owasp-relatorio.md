# Atividade I.IV: OWASP Top 10 2025

[A OWASP Top 10](https://owasp.org/Top10/2025/) mostra os principais riscos de segurança em aplicações web. Ao analisar o projeto AgendeJá, foi possível identificar vários problemas relevantes, especialmente em acesso, autenticação, configuração e proteção de dados.

Com exceção do risco de software desatualizado, então o item A03 foi excluído.

## 1. A01: Broken Access Control
Esse risco acontece quando um usuário consegue acessar dados ou ações que não deveriam ser permitidas. No projeto, o endpoint de agendamentos recebe `user_id` e `profissional_id` pela URL e acessa registros sem validar se o usuário logado tem permissão.

Exemplo do código:

```python
user_id = request.GET.get('user_id')
profissional_id = request.GET.get('profissional_id')

usuario = Usuario.objects.get(id=user_id)
profissional = usuario.profissional
```

Isso pode permitir visualização indevida de agendamentos de terceiros. A solução é verificar a identidade do usuário e limitar o acesso por perfil.

## 2. A02: Cryptographic Failures
Esse risco acontece quando dados sensíveis são armazenados ou transmitidos sem proteção adequada. No projeto, as mensagens do chat são salvas em arquivo JSON em texto simples.

Exemplo do código:

```python
with open(CHAT_MESSAGES_FILE, 'r') as f:
    return json.load(f)

with open(CHAT_MESSAGES_FILE, 'w') as f:
    json.dump(messages, f, indent=2)
```

Isso expõe conversas sensíveis se alguém conseguir acesso ao arquivo. A solução é armazenar esses dados em banco de dados protegido e usar criptografia e HTTPS.

## 3. A04: Insecure Design
Esse risco aparece quando a lógica da aplicação foi planejada de forma insegura desde o início. O chat e os agendamentos foram implementados sem controle forte de autorização e sem validação clara de quem pode acessar cada informação.

Exemplo do problema:

```python
room = request.GET.get('room')
messages = _load_chat_messages()
room_messages = messages.get(room, [])
```

O sistema aceita qualquer sala informada pelo usuário, sem verificar se o usuário autenticado realmente tem direito a acessar aquela conversa. A solução é definir regras de acesso bem estruturadas desde a modelagem do sistema.

## 4. A05: Security Misconfiguration
Esse risco acontece por má configuração do sistema. No projeto, o Django está com `DEBUG = True`, `ALLOWED_HOSTS = ['*']` e a `SECRET_KEY` está fixa no código.

Exemplo do código:

```python
DEBUG = True
ALLOWED_HOSTS = ['*']
SECRET_KEY = 'django-insecure-...'
```

Isso é perigoso em produção porque expõe erros internos e facilita exploração. A solução é desativar o debug em produção, restringir hosts e armazenar chaves em variáveis de ambiente.

## 5. A06: Vulnerable and Outdated Components
Esse risco aparece quando o projeto usa bibliotecas antigas ou vulneráveis. O sistema usa Django e dependências do ecossistema Python, então é importante manter tudo atualizado.

Exemplo de dependência e configuração:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'corsheaders',
]
```

A solução é revisar dependências regularmente e aplicar correções de segurança.

## 6. A07: Identification and Authentication Failures
Esse risco acontece quando a autenticação não garante que o usuário correto está acessando a aplicação. O login usa autenticação do Django, mas o chat e outros endpoints sensíveis não têm validação forte de identidade.

Exemplo do código:

```python
user = authenticate(username=username, password=password)
```

Isso pode permitir acesso indevido. A solução é exigir autenticação em todos os endpoints importantes e controlar sessão e permissão corretamente.

## 7. A08: Software and Data Integrity Failures
Esse risco acontece quando dados e processos podem ser alterados sem autorização. Como o projeto usa consultas diretas e arquivos para armazenar informações, há risco de manipulação se a integridade não for controlada.

Exemplo:

```python
with connection.cursor() as cursor:
    cursor.execute("SELECT ... FROM agendamento ...", [cliente.id])
```

Se a checagem de autorização não for feita corretamente, um usuário pode manipular consultas e acessar dados que não deveriam. A solução é validar entradas e proteger dados e ações críticas com autorização.

## 8. A09: Security Logging and Monitoring Failures
Esse risco acontece quando o sistema expõe detalhes internos de erro para o usuário ou não registra eventos importantes. No código, há `except Exception as e` retornando a mensagem de erro diretamente para o cliente.

Exemplo do código:

```python
except Exception as e:
    return Response({'erro': str(e)}, status=status.HTTP_400_BAD_REQUEST)
```

Isso pode revelar estrutura do sistema e facilitar ataques. A solução é registrar erros em logs internos e mostrar mensagens genéricas ao usuário.

## 9. A10: Server-Side Request Forgery (SSRF)
Esse risco aparece quando o servidor consegue acessar URLs externas ou internas sem autorização. No projeto, esse problema não foi identificado diretamente.

## Conclusão
O projeto AgendeJá apresenta riscos reais de segurança, principalmente em acesso indevido, autenticação, configuração insegura e proteção de dados. Esses problemas afetam diretamente a confiabilidade da aplicação e podem ser reduzidos com medidas como controle de autorização, armazenamento seguro, autenticação reforçada e configuração correta para produção.

A análise foi feita com base na OWASP Top 10 2025 e os principais pontos identificados foram A01, A02, A04, A05, A06, A07, A08 e A09.