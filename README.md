# TaskTracker — Sistema de Gestão Modular de Tarefas (CLI)

> **Bootcamp II — Fase 3: Entrega Final (Conteinerização, Orquestração e Deploy)**  
> **Instituição:** Centro Universitário de Brasília (UniCEUB)  
> **Estudante:** Klaus Müller Marques  
> **Matrícula / RA:** 22301876  
> **Curso:** Bacharelado em Ciência da Computação (8º Semestre)  
> **E-mail Institucional:** klaus.muller.@sempreceub.com  
> **Repositório GitHub Oficial:** [https://github.com/klausmullerDev/tasktracker-projeto](https://github.com/klausmullerDev/tasktracker-projeto)  
> **Vídeo de Demonstração (YouTube - 5 min):** [https://www.youtube.com/watch?v=SEU_LINK_AQUI](https://www.youtube.com/watch?v=SEU_LINK_AQUI) *(Configurado como Público ou Não Listado — Formato 16:9)*

---

## 📌 1. Visão Geral do Projeto

O **TaskTracker** é uma aplicação em linha de comando (CLI — *Command Line Interface*) desenvolvida em **Python 3**, projetada sob os princípios da **Arquitetura em Camadas (Layered Architecture)**, boas práticas da Engenharia de Software e padrões modernos de **DevOps (Conteinerização e Orquestração)**. O sistema resolve a perda de prazos e a sobrecarga cognitiva através da centralização, priorização objetiva e acompanhamento do ciclo de vida de tarefas.

O projeto consolidou a jornada completa do **Bootcamp II (75 horas)** dividida em três fases cumulativas:
1. **Fase 1 — Arquiteto(a) de Software (Concluída - 10 pts):** Planejamento Lógico, Arquitetura de Dados, Decomposição do Problema, Algoritmo em Português Estruturado e Mapeamento para Git/GitHub (`docs/planejamento_logico.pdf`).
2. **Fase 2 — Desenvolvedor(a) de Software (Concluída - 15 pts):** Estruturação do repositório, versionamento semântico profissional, implementação da arquitetura modular em Python 3 (`src/`) e validação estrita das regras de negócio.
3. **Fase 3 — Engenheiro(a) DevOps (Etapa Final - 25 pts):** Empacotamento hermético com Docker (`Dockerfile`), orquestração da interatividade CLI com Docker Compose (`docker-compose.yml`), padronização de ambiente idêntico e reprodutível, e documentação técnica completa.

---

## 🗂️ 2. A Árvore de Diretórios (Rastreabilidade Total)

A estrutura do projeto mantém a rastreabilidade histórica e documental entre todas as fases do Bootcamp:

```plaintext
tasktracker-projeto/
├── Dockerfile                  # [Fase 3] Receita de empacotamento da imagem Docker leve
├── docker-compose.yml          # [Fase 3] Orquestrador do container interativo (CLI)
├── README.md                   # [Fase 3] Documentação técnica completa e guia de execução
├── .dockerignore               # [Fase 3] Otimização de contexto descartando arquivos desnecessários
├── .gitignore                  # [Fase 1/2] Exclusão de caches, temporários e ambientes virtuais
├── docs/                       
│   ├── planejamento_logico.pdf # [Fase 1] Planejamento Lógico oficial mantido para rastreabilidade
│   └── relatorio_final_fase3.md# [Fase 3] Guia para submissão e conversão em PDF no AVA
└── src/                        # [Fase 2] Código-fonte da aplicação em camadas
    ├── main.py                 # Ponto de entrada (Bootstrapping) e injeção de dependências
    ├── controllers/            
    │   ├── __init__.py
    │   └── task_controller.py  # Camada de Interface do Usuário (CLI) e controle de menus
    ├── services/               
    │   ├── __init__.py
    │   └── task_service.py     # Camada de Regras de Negócio e Validações estritas
    ├── repositories/           
    │   ├── __init__.py
    │   └── task_repository.py  # Camada de Persistência e Acesso a Dados em memória
    └── models/                 
        ├── __init__.py
        └── task_model.py       # Modelo da Entidade Task (dados e propriedades)
```

---

## 🐳 3. Deep Dive Técnico: Conteinerização e Orquestração (Fase 3)

### 3.1 O Dockerfile (A Receita de Empacotamento)

O `Dockerfile` é responsável por criar uma imagem enxuta, segura e autossuficiente para a aplicação:

```dockerfile
# 1. Imagem base oficial leve do Python 3.11 baseada em Debian Slim
FROM python:3.11-slim

# 2. Define o diretório de trabalho padrão dentro do container
WORKDIR /app

# 3. Garante que os fluxos de saída (stdout e stderr) sejam enviados imediatamente 
#    ao terminal sem armazenamento em buffer (essencial para interatividade da CLI)
ENV PYTHONUNBUFFERED=1

# 4. Copia o código-fonte da aplicação local para o diretório de trabalho do container
COPY src/ /app/src/

# 5. Comando executado ao iniciar o container disparando a aplicação CLI
CMD ["python", "src/main.py"]
```

#### Decisões Arquiteturais:
* **`FROM python:3.11-slim`:** Reduz drasticamente a superfície de ataque e o tamanho final da imagem (~130 MB contra mais de 1 GB da versão completa), contendo apenas os binários essenciais para rodar o Python.
* **`WORKDIR /app`:** Estabelece um ponto de ancoragem isolado para a aplicação dentro da hierarquia do Linux.
* **`ENV PYTHONUNBUFFERED=1`:** Impede que o Python retenha logs ou prints na memória antes de exibi-los. Isso garante que cada menu ou mensagem de prompt seja impresso imediatamente no console do usuário.
* **`COPY src/ /app/src/`:** Copia estritamente os módulos de código da aplicação, preservando os princípios de mínimo privilégio e menor contexto (reforçado pelo `.dockerignore`).
* **`CMD ["python", "src/main.py"]`:** Define o gatilho padrão de inicialização na sintaxe *exec form* (`["executavel", "parametro"]`).

---

### 3.2 O Desafio da CLI: Orquestração e Interatividade com `docker-compose.yml`

Aplicações CLI interativas dependem da chamada `input()` do Python. Em ambientes de container tradicionais, o container é executado em segundo plano ou desconectado da entrada padrão (`STDIN`), resultando no encerramento imediato ou em erro de `EOFError` (*End Of File*).

O `docker-compose.yml` resolve essa limitação atuando como a **ponte de interatividade**:

```yaml
services:
  tasktracker:
    build: .
    image: tasktracker:latest
    container_name: tasktracker-cli
    stdin_open: true  # Mantém o STDIN aberto para capturar dados digitados
    tty: true         # Aloca um pseudoterminal (TTY) emulando o console interativo

  # Serviço auxiliar 'app' mapeado para compatibilidade imediata com 'docker compose run app'
  app:
    build: .
    image: tasktracker:latest
    stdin_open: true
    tty: true
```

* **`stdin_open: true`:** Mantém o canal de entrada de dados aberto mesmo quando não há processos explicitamente anexados.
* **`tty: true`:** Aloca um terminal virtual completo (TTY), habilitando recursos de cores, quebra de linha correta e captura de teclado em tempo real.

---

### 3.3 Matriz de Comparação: Empacotar vs. Executar

| Característica | Dockerfile (A Receita) | docker-compose.yml (O Maestro) |
| :--- | :--- | :--- |
| **Papel Principal** | Empacota a aplicação, runtime e dependências estáticas. | Orquestra a execução interativa da CLI e aloca canais de I/O. |
| **Artefato de Saída** | Gera a **Imagem Docker** (`tasktracker:latest`). | Executa e gerencia o ciclo de vida do **Container**. |
| **Comando Chave** | `docker build` | `docker compose run` |
| **Obrigatório na Raiz?** | **Sim** (raiz do repositório) | **Sim** (raiz do repositório) |

---

## 🚀 4. Guia de Execução Docker (Comandos Avaliados)

> **Dica para Avaliadores:** Todos os comandos abaixo devem ser executados a partir da raiz do repositório.

### Passo 1: Construir a Imagem Docker (`docker build`)
Compila a imagem local utilizando o `Dockerfile`:

```bash
docker build -t tasktracker .
```

---

### Passo 2: Executar o Container em Modo Isolado Interativo (`docker run -it`)
Roda o container diretamente com terminal interativo alocado (`-i` para manter o STDIN aberto, `-t` para alocar o pseudo-TTY, e `--rm` para remover o container temporário após o encerramento):

```bash
docker run -it --rm tasktracker
```

---

### Passo 3: Executar via Orquestração com Docker Compose (`docker compose run` — Recomendado)
Executa o serviço CLI orquestrado pelo `docker-compose.yml`:

```bash
docker compose run --rm tasktracker
```

*(Nota de compatibilidade: caso prefira chamar pelo nome de serviço alternativo, `docker compose run --rm app` também está disponível).*

---

### (Opcional) Execução Local Sem Docker (Legado Fase 2)
Caso deseje rodar a aplicação diretamente no interpretador do host:

```bash
python3 src/main.py
```

---

## ⚙️ 5. Regras de Negócio e Validações Implementadas

O sistema aplica rigorosamente todas as validações desenhadas no algoritmo da Fase 1 e refinadas na Fase 2:

| Regra / Campo | Tipo | Obrigatoriedade | Descrição e Validação Estrita |
| :--- | :--- | :--- | :--- |
| **`id`** | Inteiro | Automático | Identificador único sequencial gerado automaticamente pelo repositório (1, 2, 3...). |
| **`title`** | String | Obrigatório | Não pode ser nulo, vazio ou composto unicamente por espaços em branco. O sistema repete o prompt defensivamente até um valor válido ser fornecido. |
| **`description`** | String | Opcional | Texto descritivo opcional com o detalhamento das ações. Teclar Enter preserva em branco. |
| **`priority`** | String | Obrigatório | **Validação Estrita:** aceita exclusivamente as opções `"Alta"`, `"Média"` (ou `"Media"`) e `"Baixa"` (sem distinção de maiúsculas/minúsculas). Entradas fora do padrão geram mensagem de erro e repetição do prompt. |
| **`due_date`** | String | Opcional | Data no formato `DD/MM/AAAA` ou `AAAA-MM-DD`. O serviço valida e rejeita datas retroativas em relação ao dia atual. |
| **`status`** | String | Automático | Definido automaticamente como `"Pendente"` no momento do cadastro. Transições aceitas: `"Pendente"`, `"Em Andamento"` e `"Concluída"`. |
| **Integridade** | Sistema | Obrigatório | Ações de busca, edição, exclusão e alteração de status exigem ID válido existente no repositório. |

---

## 📱 6. Módulos e Funcionalidades (Menu CLI)

Ao iniciar a aplicação dentro do container, o menu interativo é renderizado:

```plaintext
==========================================================
               TASKTRACKER - MENU PRINCIPAL
==========================================================
  --- Requisitos Centrais da Fase 2 ---
  [1] Cadastrar nova tarefa
  [2] Visualizar tarefas cadastradas
  [3] Sair da aplicação
  --- Módulos Estendidos do Planejamento Lógico (Fase 1) ---
  [4] Buscar tarefa por ID
  [5] Atualizar status da tarefa
  [6] Editar tarefa
  [7] Remover tarefa
  [8] Filtrar tarefas por prioridade
----------------------------------------------------------
```

1. **[1] Cadastrar nova tarefa:** Validação de título obrigatório, prioridade (`Alta`, `Média`, `Baixa`) e prazo.
2. **[2] Visualizar tarefas cadastradas:** Exibe feedback informativo quando vazia ou lista formatada em cartões de tarefas.
3. **[3] Sair da aplicação:** Encerramento elegante com mensagem de despedida.
4. **[4] Buscar tarefa por ID:** Localização instantânea de tarefas por identificador único.
5. **[5] Atualizar status da tarefa:** Transição de status (`Pendente` -> `Em Andamento` -> `Concluída`).
6. **[6] Editar tarefa:** Modificação seletiva mantendo os campos originais com Enter.
7. **[7] Remover tarefa:** Exclusão com confirmação defensiva (`S/N`).
8. **[8] Filtrar tarefas por prioridade:** Agrupamento por criticidade.

---

## 🌿 7. Estratégia de Versionamento Git

O versionamento do repositório reflete uma esteira evolutiva clara com Commits Semânticos:

1. **`docs: registro do README.md, .gitignore e documento da Fase 1 (docs/planejamento_logico.pdf)`** (Commit inicial da Fase 1)
2. **`feat: implementação da estrutura principal em src/main.py (menu e loop principal)`** (Fase 2)
3. **`feat: adição das funções de validação de dados (título não vazio e prioridades)`** (Fase 2)
4. **`feat(architecture): implementação da arquitetura em camadas (Model, Repository, Service, Controller) e módulos estendidos da Fase 1`** (Fase 2)
5. **`feat(devops): conteinerização com Dockerfile, orquestração com docker-compose e atualização do README para a Fase 3`** (Fase 3 - Entrega Final)

---

## 📹 8. Storyboard do Vídeo de Demonstração (YouTube - 5 Minutos)

Conforme os critérios inegociáveis de avaliação (10 pontos no barema), o vídeo deve cumprir:
* **Formato:** Horizontal (16:9) — estritamente proibido Shorts ou vídeo vertical.
* **Identificação:** Rosto do estudante na webcam e áudio próprios obrigatórios durante todo o vídeo.
* **Visibilidade:** Público ou Não Listado (nunca Privado).

### Cronograma de Gravação (5:00 min):

| Minuto | Etapa | O que mostrar na tela | O que falar (Roteiro sugerido) |
| :--- | :--- | :--- | :--- |
| **0:00 - 0:30** | **Introdução** | Câmera aberta + slide ou VS Code com o repositório | "Olá, meu nome é Klaus Müller Marques, RA 22301876, estudante de Ciência da Computação (8º semestre) no UniCEUB. Esta é a apresentação da Fase 3 (Entrega Final) do Bootcamp II: Conteinerização e Deploy do TaskTracker." |
| **0:30 - 1:30** | **GitHub e Rastreabilidade** | Navegador aberto no repositório GitHub | "Aqui no GitHub observamos a árvore completa do projeto: os artefatos mantidos da Fase 1 (`planejamento_logico.pdf`), o código em camadas da Fase 2 (`src/`), e os novos artefatos DevOps da Fase 3: o `Dockerfile`, o `docker-compose.yml` e o `README.md` detalhado. Mostro também o histórico de commits semânticos comprovando a evolução contínua." |
| **1:30 - 2:30** | **Deep Dive Técnico: Dockerfile e Compose** | Editor de código destacando o `Dockerfile` e `docker-compose.yml` | "No `Dockerfile`, escolhi a imagem base `python:3.11-slim` para obter leveza e segurança. Configuramos o `WORKDIR /app`, `PYTHONUNBUFFERED=1` para garantir que o stdout não fique preso em buffers na CLI, e a cópia do código com `CMD ['python', 'src/main.py']`. No `docker-compose.yml`, solucionamos o desafio da CLI com `stdin_open: true` e `tty: true`, permitindo a entrada interativa via teclado." |
| **2:30 - 4:30** | **Demonstração Prática no Terminal** | Terminal em tela cheia | 1. Executar `docker build -t tasktracker .`<br>2. Executar `docker run -it --rm tasktracker`<br>3. Menu: Opção 2 (lista vazia).<br>4. Opção 1 (cadastrar): forçar erro de título vazio, forçar erro de prioridade (`Urgente`), cadastrar com sucesso (`Estudar Docker`, prioridade `Alta`).<br>5. Opção 2 (mostrar tarefa cadastrada).<br>6. Opção 3 (sair).<br>7. Executar `docker compose run --rm tasktracker` e demonstrar o funcionamento orquestrado. |
| **4:30 - 5:00** | **Conclusão e Reflexão** | Câmera + Terminal limpo | "Concluímos com sucesso a jornada do Bootcamp II, saindo do planejamento lógico na Fase 1, passando pela arquitetura em camadas na Fase 2, e finalizando com um deploy conteinerizado, hermético e pronto para produção com Docker na Fase 3. Muito obrigado!" |

---

## 📋 9. Vetor de Entrega Final (Para Submissão no AVA)

* **Estudante:** Klaus Müller Marques
* **Matrícula / RA:** 22301876
* **Instituição:** UniCEUB — Centro Universitário de Brasília
* **Repositório GitHub Ativo:** [https://github.com/klausmullerDev/tasktracker-projeto](https://github.com/klausmullerDev/tasktracker-projeto)
* **Vídeo no YouTube Ativo:** [https://www.youtube.com/watch?v=SEU_LINK_AQUI](https://www.youtube.com/watch?v=SEU_LINK_AQUI)
