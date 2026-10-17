# BOOTCAMP II — FASE 3: ENTREGA FINAL
## RELATÓRIO TÉCNICO DE CONTEINERIZAÇÃO, ORQUESTRAÇÃO E DEPLOY

---

### DADOS DE IDENTIFICAÇÃO DO ESTUDANTE E DO PROJETO

* **Instituição de Ensino:** Centro Universitário de Brasília (UniCEUB)
* **Curso:** Bacharelado em Ciência da Computação (8º Semestre)
* **Estudante:** Klaus Müller Marques
* **Matrícula / RA:** 22301876
* **E-mail Institucional:** klaus.muller.@sempreceub.com
* **Componente Curricular:** Bootcamp II (Carga Horária: 75h)
* **Tema da Fase 3:** Engenharia DevOps — Conteinerização, Orquestração e Deploy do TaskTracker

---

### VETOR DE ENTREGA FINAL (LINKS ATIVOS)

* **Repositório Oficial no GitHub:**  
  [https://github.com/klausmullerDev/tasktracker-projeto](https://github.com/klausmullerDev/tasktracker-projeto)

* **Vídeo de Demonstração Técnica no YouTube (5 minutos - Formato 16:9):**  
  [https://www.youtube.com/watch?v=SEU_LINK_AQUI](https://www.youtube.com/watch?v=SEU_LINK_AQUI)  
  *(Configuração de Privacidade: Não Listado ou Público | Áudio e Rosto do Estudante Visíveis)*

---

### 1. INTRODUÇÃO E CONTEXTO EVOLUTIVO

O projeto **TaskTracker** foi concebido e implementado de ponta a ponta ao longo de três fases estruturadas de engenharia de software e infraestrutura moderna:

1. **Fase 1 (Arquiteto de Software - 10 pts):** Concepção lógica, modelagem de dados, algoritmos em português estruturado e planejamento da árvore de diretórios (`docs/planejamento_logico.pdf`).
2. **Fase 2 (Desenvolvedor de Software - 15 pts):** Implementação da aplicação CLI modular em camadas em Python 3 (`src/`), cobertura das regras de negócio com validação estrita e versionamento semântico no Git/GitHub.
3. **Fase 3 (Engenheiro DevOps - 25 pts):** Empacotamento hermético, conteinerização através de imagem leve e segura, e orquestração do canal interativo de entrada/saída (CLI) via Docker Compose.

---

### 2. ARTEFATOS OBRIGATÓRIOS E ESTRUTURA DO REPOSITÓRIO

A árvore do repositório garante total rastreabilidade entre as fases:

```plaintext
tasktracker-projeto/
├── Dockerfile                  # [Fase 3] Receita de empacotamento da imagem Docker leve
├── docker-compose.yml          # [Fase 3] Orquestrador do container interativo (CLI)
├── README.md                   # [Fase 3] Documentação completa e instruções de execução
├── .dockerignore               # [Fase 3] Otimização de contexto do Docker
├── .gitignore                  # [Fase 1/2] Exclusão de caches e ambientes virtuais
├── docs/                       
│   ├── planejamento_logico.pdf # [Fase 1] Planejamento lógico da arquitetura
│   └── relatorio_final_fase3.md# [Fase 3] Documento base para submissão PDF
└── src/                        # [Fase 2] Código-fonte da aplicação em camadas
    ├── main.py                 # Ponto de entrada (Bootstrapping)
    ├── controllers/            # Camada de Interface CLI
    ├── services/               # Camada de Regras de Negócio e Validações
    ├── repositories/           # Camada de Persistência em Memória
    └── models/                 # Modelo de Dados da Entidade Task
```

---

### 3. DEEP DIVE TÉCNICO: CONTEINERIZAÇÃO E ORQUESTRAÇÃO

#### 3.1 Dockerfile (Empacotamento Estático)
* **`FROM python:3.11-slim`:** Utilização de imagem base enxuta com Debian Slim (~130 MB), reduzindo vulnerabilidades de segurança e tempo de trânsito de rede.
* **`WORKDIR /app`:** Isolamento e padronização do diretório raiz da aplicação.
* **`ENV PYTHONUNBUFFERED=1`:** Impede o buffer interno de stdout/stderr, garantindo a exibição síncrona imediata das instruções e menus da CLI.
* **`COPY src/ /app/src/`:** Injeção seletiva do código-fonte no container.
* **`CMD ["python", "src/main.py"]`:** Gatilho de execução padrão no formato *exec form*.

#### 3.2 docker-compose.yml (Orquestração e Interatividade)
Por padrão, containers executam de forma desconectada de terminais de entrada interativa, quebrando funções como `input()` da CLI. A orquestração via Docker Compose resolveu isso com:
* **`stdin_open: true`:** Mantém o canal de entrada padrão (`STDIN`) aberto permanentemente.
* **`tty: true`:** Aloca um pseudoterminal virtual (`TTY`), permitindo a captura dos comandos do usuário no console.

#### 3.3 Matriz Comparativa: Dockerfile vs. docker-compose.yml

| Critério | Dockerfile | docker-compose.yml |
| :--- | :--- | :--- |
| **Finalidade** | Empacotamento de dependências e código | Orquestração da execução e I/O interativo |
| **Resultado** | Imagem Docker (`tasktracker:latest`) | Container ativo gerenciado |
| **Comando de Execução** | `docker build` | `docker compose run` |
| **Localização** | Raiz do Repositório | Raiz do Repositório |

---

### 4. GUIA DE COMANDOS DE EXECUÇÃO

Os comandos a seguir foram validados e garantem execução idêntica em qualquer ambiente com Docker instalado:

#### 1. Construção da Imagem (`docker build`):
```bash
docker build -t tasktracker .
```

#### 2. Execução Isolada no Terminal (`docker run -it`):
```bash
docker run -it --rm tasktracker
```

#### 3. Execução Orquestrada via Docker Compose (`docker compose run` — Recomendado):
```bash
docker compose run --rm tasktracker
```

---

### 5. ROTEIRO E STORYBOARD DO VÍDEO NO YOUTUBE (5 MINUTOS)

* **0:00 - 0:30 (Introdução):** Identificação completa do estudante (Klaus Müller Marques, RA 22301876, UniCEUB) e escopo da Fase 3.
* **0:30 - 1:30 (GitHub):** Demonstração da árvore de arquivos, histórico de commits semânticos e novos artefatos DevOps.
* **1:30 - 2:30 (Dockerfile & Compose):** Explicação das decisões técnicas (`python:3.11-slim`, `PYTHONUNBUFFERED`, `stdin_open`, `tty`).
* **2:30 - 4:30 (Demonstração Prática):** Execução do `docker build`, `docker run -it`, demonstração do menu da aplicação (cadastro, erro defensivo, listagem) e execução via `docker compose run`.
* **4:30 - 5:00 (Conclusão):** Síntese da evolução arquitetural e prontidão para ambientes de produção.
