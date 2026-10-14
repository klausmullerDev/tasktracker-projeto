# TaskTracker — Sistema de Gestão Modular de Tarefas (CLI)

> **Bootcamp II — Fase 2: Entrega Intermediária (Desafio de Desenvolvimento e Versionamento)**  
> **Instituição:** Centro Universitário de Brasília (UniCEUB)  
> **Estudante:** Klaus Müller Marques  
> **Matrícula / RA:** 22301876  
> **Curso:** Bacharelado em Ciência da Computação (8º Semestre)  

---

## 📌 1. Visão Geral do Projeto

O **TaskTracker** é uma aplicação em linha de comando (CLI — *Command Line Interface*) desenvolvida em **Python 3**, com foco no gerenciamento eficiente, estruturado e intuitivo de tarefas e atividades cotidianas. 

O projeto compõe a trilha prática e cumulativa do **Bootcamp II**, estruturado em três fases interdependentes:
1. **Fase 1 — Entrega Inicial (Concluída):** Planejamento Lógico, Arquitetura de Dados, Decomposição do Problema, Algoritmo em Português Estruturado e Estratégia de Versionamento Git/GitHub.
2. **Fase 2 — Entrega Intermediária (Etapa Atual):** Estruturação física do repositório, versionamento profissional com Git/GitHub, implementação da lógica de negócio e validações estritas em Python 3.
3. **Fase 3 — Entrega Final (Próxima Etapa):** Empacotamento da aplicação, conteinerização com Docker, testes automatizados e deploy.

---

## 🗂️ 2. Arquitetura e Estrutura do Repositório

O projeto segue rigorosamente a árvore de diretórios planejada e documentada na Fase 1:

```plaintext
tasktracker-projeto/
├── README.md                 # Documentação principal da aplicação e guia de execução
├── .gitignore                # Regras de exclusão para arquivos temporários, Python e ambiente virtual
├── docs/
│   └── planejamento_logico.pdf # Documento original de planejamento arquitetural da Fase 1
└── src/
    └── main.py               # Código-fonte principal da aplicação TaskTracker em Python 3
```

### Detalhamento dos Componentes:
- **`README.md`**: Guia completo de documentação, regras de negócio, tecnologias, passos de execução e rastreabilidade da aplicação.
- **`.gitignore`**: Configurado para ignorar diretórios de cache (`__pycache__/`, `*.pyc`), ambientes virtuais (`.venv`, `env`) e arquivos de sistema (`.DS_Store`).
- **`docs/planejamento_logico.pdf`**: Artefato documental da Fase 1, mantido no repositório para assegurar a rastreabilidade e integridade do ciclo de vida do software.
- **`src/main.py`**: Ponto central da aplicação, contendo o loop contínuo de menu, rotinas de cadastro, validação defensiva de dados e exibição formatada de tarefas.

---

## ⚙️ 3. Regras de Negócio e Validações Implementadas

Cada tarefa é modelada como uma estrutura de dados com os seguintes campos e validações estritas:

| Campo | Tipo | Obrigatoriedade | Regra de Validação / Comportamento |
| :--- | :--- | :--- | :--- |
| **`id`** | Inteiro | Automático | Identificador único incremental gerado sequencialmente pelo sistema (1, 2, 3...). |
| **`title`** | String | Obrigatório | Rejeita strings vazias ou formadas apenas por espaços em branco. O sistema repete o prompt até uma entrada válida ser fornecida. |
| **`description`** | String | Opcional | Detalhamento livre da tarefa. Pode ser deixado em branco (tecla Enter). |
| **`priority`** | String | Obrigatório | **Validação Estrita:** aceita exclusivamente as opções `"Alta"`, `"Média"` (ou `"Media"`) e `"Baixa"` (sem distinção de maiúsculas/minúsculas). Entradas fora do padrão geram aviso de erro e nova solicitação imediata. |
| **`due_date`** | String | Opcional / Informado | Data limite planejada para a conclusão (formato livre ou `DD/MM/AAAA`). |
| **`status`** | String | Automático | Definido automaticamente como `"Pendente"` no instante do cadastro da tarefa. |

### Comportamento da Listagem:
- **Lista Vazia:** Se nenhuma tarefa tiver sido cadastrada, o sistema apresenta uma mensagem informativa clara: `[INFO] Nenhuma tarefa cadastrada no momento.`
- **Lista Preenchida:** Apresenta todas as propriedades dos registros de forma visualmente organizada, com separadores e campos legíveis no terminal.

---

## 🚀 4. Guia de Instalação e Execução

### Pré-requisitos
- **Python 3.8+** instalado no sistema operacional.
- **Git** configurado para controle de versão.

### Passo 1: Clonar o Repositório
```bash
git clone git@github.com:klausmullerDev/tasktracker-projeto.git
cd tasktracker-projeto
```
*(Caso esteja executando localmente na pasta do projeto, basta abrir o terminal no diretório raiz).*

### Passo 2: Executar a Aplicação
Execute o arquivo principal via Python 3:
```bash
python3 src/main.py
```

### Menu Interativo:
Ao executar o programa, você verá a interface interativa CLI:
```plaintext
==================================================
           TASKTRACKER - MENU PRINCIPAL
==================================================
  [1] Cadastrar nova tarefa
  [2] Visualizar tarefas cadastradas
  [3] Sair da aplicação
--------------------------------------------------
Escolha uma opção (1-3): 
```

---

## 🌿 5. Estratégia de Versionamento Git

O desenvolvimento da Fase 2 foi estruturado em commits coerentes e rastreáveis, refletindo o ciclo evolutivo de desenvolvimento de software:

1. **`git init`**: Inicialização do repositório local e preparação da árvore de pastas.
2. **Commit Inicial (`docs/init`)**: Inclusão do `README.md`, `.gitignore` e `docs/planejamento_logico.pdf`.
3. **Commit de Desenvolvimento (`feat/menu`)**: Implementação do esqueleto principal em `src/main.py` com o loop de menu CLI e controle de navegação.
4. **Commit de Regras e Validações (`feat/validations`)**: Implementação completa das funções de validação (título obrigatório não vazio, prioridade estrita "Alta"/"Média"/"Baixa"), estrutura de dados em memória e rotina de listagem legível.
5. **Publicação Remota (`git push`)**: Vinculação com o repositório remoto no GitHub (`origin main`).

---

## 📹 6. Roteiro da Demonstração em Vídeo (YouTube)

O vídeo da Fase 2 possui duração máxima de 5 minutos, formato 16:9 com webcam e voz própria, cobrindo:

1. **Introdução (30s):** Identificação completa (Klaus Müller Marques, RA 22301876, Ciência da Computação UniCEUB) e escopo da Fase 2 do Bootcamp II.
2. **Apresentação do Repositório GitHub (1m30s):** Demonstração da estrutura de pastas, arquivo `README.md`, presença do artefato `docs/planejamento_logico.pdf` da Fase 1 e histórico de commits semânticos.
3. **Demonstração Prática no Terminal (2m):**
   - Execução de `python3 src/main.py`.
   - Consulta à listagem com repositório vazio (validação de estado inicial).
   - Teste de cadastro forçando erro de validação (título vazio com espaços).
   - Teste de cadastro forçando erro de validação (prioridade inválida).
   - Cadastro realizado com sucesso após correção dos dados.
   - Exibição da listagem atualizada com a tarefa cadastrada.
4. **Encerramento (30s):** Conclusão das metas da Fase 2 e contextualização para a Fase 3 (Empacotamento, Containerização Docker e Deploy).

---

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3 (padrão PEP 8, tipagem estática opcional, sem dependências externas)
- **Controle de Versão:** Git & GitHub
- **Metodologia:** Engenharia de Software, Arquitetura Limpa e Commits Semânticos
