# ==============================================================================
# TaskTracker — Dockerfile (Fase 3: Conteinerização e Deploy)
# Bootcamp II — Ciência da Computação (UniCEUB)
# Estudante: Klaus Müller Marques | RA: 22301876
# ==============================================================================

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
