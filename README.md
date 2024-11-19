Qdrant com LangChain e OpenAI
Este repositório demonstra como integrar o banco de vetores Qdrant com a biblioteca LangChain e os embeddings da OpenAI, criando uma aplicação de perguntas e respostas baseada em recuperação de informações (RetrievalQA).

A aplicação utiliza uma coleção de vetores com dimensão 1536, que corresponde à saída do modelo de embeddings da OpenAI text-embedding-ada-002, um dos mais avançados e otimizados para tarefas de similaridade semântica.

Funcionalidades
Banco de vetores escalável: Qdrant é utilizado para armazenar e gerenciar vetores de alta dimensão.
Embeddings poderosos: Geração de embeddings por meio do modelo text-embedding-ada-002 da OpenAI.
Recuperação de informações: Integração com LangChain para realizar buscas semânticas e criar fluxos de perguntas e respostas.
Divisão de textos: Fragmentação de texto em partes menores para otimização no armazenamento e consulta.
Boas práticas de segurança: Proteção de credenciais e URLs com .env.
Requisitos
Certifique-se de ter os seguintes itens instalados:

Python 3.9 ou superior
Docker (opcional, para rodar o Qdrant localmente)
Uma conta na OpenAI para obter a chave da API.
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
Instale as dependências do projeto:

bash
Copiar código
pip install -r requirements.txt
Configure o arquivo .env:

Crie um arquivo .env na raiz do projeto com as credenciais e URL do Qdrant:

plaintext
Copiar código
QDRANT_URL=http://localhost:6333
OPENAI_API_KEY=sua-chave-api
Como Usar
Inicie o Qdrant:

Se estiver usando Docker:
bash
Copiar código
docker run -d --name qdrant -p 6333:6333 qdrant/qdrant
Execute o script principal:

bash
Copiar código
python main.py
Adicione seu texto-base no arquivo base_dados.txt e personalize conforme necessário.

Faça perguntas e veja as respostas no console!

Por que usar dimensão 1536?
A dimensão 1536 foi escolhida porque o modelo de embeddings da OpenAI, text-embedding-ada-002, gera vetores com exatamente essa dimensão. Isso é importante porque:

Alta performance: Essa configuração captura informações semânticas de alta qualidade, permitindo melhores resultados em buscas.
Eficiência: O modelo ada-002 é econômico e rápido, ideal para tarefas de busca semântica, clustering e análise de similaridade.
Caso utilize outro modelo ou serviço de embeddings, a dimensão pode variar. Nesse caso, ajuste a configuração do Qdrant para refletir as mudanças.

Estrutura do Projeto
bash
Copiar código
.
├── .env                # Credenciais e configurações (não enviado ao GitHub)
├── base_dados.txt      # Arquivo com o texto base para criação de embeddings
├── main.py             # Script principal
├── requirements.txt    # Dependências do projeto
├── README.md           # Documentação do repositório
└── .gitignore          # Arquivos ignorados pelo Git
Boas Práticas
Proteção de Credenciais: O arquivo .env é usado para armazenar informações sensíveis e está listado no .gitignore para evitar exposição pública.
Configuração flexível: O Qdrant pode ser configurado localmente via Docker ou em um servidor remoto.
Simplicidade: Tudo foi projetado para ser fácil de entender e replicar.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto está licenciado sob a MIT License.

