🧠 Lyra – Chatbot de Registros Anônimos para Saúde Mental Corporativa

O Lyra é um chatbot desenvolvido em Python com o propósito de oferecer aos colaboradores uma forma prática, segura e totalmente anônima de registrar reclamações e sugestões. A ferramenta promove um ambiente de trabalho mais saudável ao incentivar a comunicação interna e dar voz aos funcionários sem riscos de identificação.

📌 Funcionalidades: 

O sistema possui as seguintes funcionalidades principais:

- Permite registrar reclamações anonimamente.

- Permite registrar sugestões anonimamente.

- Salva automaticamente todos os registros em um arquivo chamado registros.csv.

- Exibe os registros diretamente no console.

- Ordena os registros utilizando o algoritmo Quick Sort.

- Gera um gráfico comparando a quantidade de reclamações e sugestões.

- Oferece uma interface simples via terminal para fácil utilização.
  

🎯 Objetivo do Projeto

O principal objetivo do Lyra é proporcionar um canal seguro para que colaboradores expressem suas opiniões, preocupações e ideias. Isso ajuda a empresa a monitorar o ambiente organizacional e agir proativamente para melhorar o bem-estar emocional e estrutural do local de trabalho.
A ferramenta facilita:

- A coleta de feedbacks.

- O armazenamento organizado das informações.

- A visualização dos dados.

- A análise dos tipos de registros recebidos.
- 

🚀 Como Funciona:

Ao iniciar o chatbot, o usuário é recebido pelo Lyra com uma apresentação amigável. Em seguida, é exibido um menu com cinco opções:

- Registrar reclamação.

- Registrar sugestão.

- Visualizar todos os registros armazenados.

- Gerar um gráfico com a contagem de cada tipo de registro.

- Encerrar o programa.

Após escolher registrar algo, o usuário digita a mensagem que deseja enviar. O sistema salva automaticamente o registro no arquivo e confirma a ação. Caso o usuário queira visualizar os dados, o próprio chatbot mostra no console todos os registros ordenados.


📂 Estrutura do Sistema

O sistema é organizado em funções para facilitar a manutenção e a leitura do código. A estrutura segue a seguinte lógica:

- A função responsável pelo menu organiza e controla todas as opções disponíveis.

- A função de registro recebe o tipo de entrada (reclamação ou sugestão), coleta o texto do usuário e aciona a função interna que salva o registro no arquivo.

- O algoritmo Quick Sort é utilizado para ordenar os registros antes da visualização.

- A função de visualização lê o arquivo, organiza os registros e os apresenta no console.

- A função de geração de gráfico utiliza a biblioteca Matplotlib para ilustrar a quantidade de cada tipo de registro.
  


🗂 Armazenamento dos Dados

Todos os registros são salvos em um arquivo chamado registros.csv. Cada linha contém duas informações: o tipo do registro e a mensagem escrita pelo usuário. Esse arquivo permite análises posteriores e facilita a integração com ferramentas externas.


📊 Visualização Gráfica

O Lyra conta com uma função que calcula quantas reclamações e quantas sugestões foram registradas até o momento. Com esses dados, é gerado um gráfico de barras simples utilizando Matplotlib, permitindo uma visualização clara da predominância de cada tipo de registro.


🛠 Tecnologias Utilizadas

O projeto utiliza os seguintes recursos:

- Linguagem Python

- Biblioteca CSV

- Biblioteca Matplotlib para visualização gráfica


Integrantes:
Matheus Machado Caposse RM560340
Caio Berardo RM560357
