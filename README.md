# Qdrant + LangChain + OpenAI: Semantic Search Powerhouse

## 📘 Visão Geral

Este repositório demonstra uma poderosa integração entre:
- 📦 **Banco de Vetores**: Qdrant
- 🔗 **Biblioteca de Integração**: LangChain
- 🤖 **Embeddings**: OpenAI text-embedding-ada-002

Uma aplicação moderna de recuperação de informações (RetrievalQA) que utiliza embeddings semânticos de alta performance.

## ✨ Funcionalidades Principais

- 🗃️ **Banco de Vetores Escalável**: Qdrant para armazenamento de vetores de alta dimensão
- 🧠 **Embeddings Inteligentes**: Geração via modelo text-embedding-ada-002
- �حث **Recuperação Semântica**: Buscas inteligentes com LangChain
- 📄 **Processamento Inteligente**: Divisão otimizada de textos
- 🔒 **Segurança**: Proteção de credenciais com .env

## 🛠️ Requisitos

- **Python**: 3.9+
- **Docker** (opcional)
- **Conta OpenAI**

## 🚀 Instalação Rápida

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure suas credenciais:
   Crie um arquivo `.env` na raiz com:
   ```
   QDRANT_URL=http://localhost:6333
   OPENAI_API_KEY=sua-chave-api
   ```

## 🔬 Como Usar

1. Iniciar Qdrant (Docker):
   ```bash
   docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
   ```

2. Executar aplicação:
   ```bash
   python main.py
   ```

3. Adicione seu texto base em `base_dados.txt`

## 🧮 Sobre a Dimensão 1536

Por que usamos 1536 dimensões?

- 🚀 **Alta Performance**: Captura semântica de qualidade
- 💨 **Eficiência**: Modelo ada-002 econômico e rápido
- 🔍 **Ideal para**: Busca semântica, clustering, análise de similaridade

## 📂 Estrutura do Projeto

```
.
├── .env                # Credenciais (git-ignored)
├── base_dados.txt      # Texto base para embeddings
├── main.py             # Script principal
├── requirements.txt    # Dependências
├── README.md           # Documentação
└── .gitignore          # Arquivos ignorados
```

## 🤝 Contribuições

Contribuições são super bem-vindas! 

- Abra issues
- Envie pull requests
- Compartilhe feedbacks

## 📄 Licença

[MIT License](LICENSE)

---
