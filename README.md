# AutoGen Agents with Function Calling using Groq API

Este projeto é um laboratório prático que explora a criação de agentes de IA utilizando a biblioteca **Microsoft Autogen**. O objetivo é demonstrar como capacitar um agente com "ferramentas" (tools), que são funções Python customizadas que ele pode chamar para executar tarefas específicas que vão além da simples geração de texto.

A aplicação utiliza a **Groq API** para inferência de alta velocidade com o modelo de linguagem Llama 3, permitindo interações fluidas e em tempo real com o agente.

## 🎯 O Desafio: De Conversor de Moedas a Assistente Residencial

O laboratório consiste em adaptar um agente inicialmente projetado para uma tarefa e transformá-lo para resolver um problema completamente diferente.

1.  **Estado Inicial**: Um agente (`currency_bot`) capaz de converter valores entre moedas.
2.  **Modificação**: O mesmo agente é reconfigurado para se tornar um assistente de automação residencial.
3.  **Resultado Final**: O agente, ao receber um comando em linguagem natural como "Está calor aqui na sala", utiliza sua nova ferramenta para ligar o ar condicionado.

![Resultado do Agente de Automação Residencial](https://i.imgur.com/5D6fBqY.png)

## 🧠 Conceitos Fundamentais

### 1. Microsoft Autogen
É um framework de código aberto para simplificar a orquestração, otimização e automação de fluxos de trabalho com múltiplos agentes de IA. Ele permite que agentes conversem entre si e com humanos para resolver tarefas complexas. Neste projeto, utilizamos dois tipos principais de agentes:
-   `AssistantAgent`: O agente "cérebro", que utiliza o LLM (Llama 3 via Groq) para entender, raciocinar e decidir qual ferramenta usar.
-   `UserProxyAgent`: Um proxy que atua em nome do usuário. Ele é responsável por executar o código ou as funções que o `AssistantAgent` sugere.

### 2. Function Calling (Uso de Ferramentas)
Esta é a capacidade de um LLM de, em vez de apenas responder com texto, indicar que precisa executar uma função predefinida para obter a informação necessária. O fluxo é o seguinte:
1.  O usuário envia uma mensagem (ex: "Ligue o ar da sala").
2.  O `AssistantAgent`, com base em sua configuração e nas descrições das ferramentas disponíveis, determina que a função `turn_on_airconditioner` deve ser chamada.
3.  Ele envia uma "sugestão de chamada de ferramenta" com os argumentos corretos (ex: `ambiente="Sala de estar"`, `estado=True`).
4.  O `UserProxyAgent` recebe essa sugestão, executa a função Python de fato e retorna o resultado.
5.  O `AssistantAgent` recebe o resultado da função e formula a resposta final para o usuário.

### 3. Groq API
Groq oferece uma plataforma de inferência de LLMs com latência extremamente baixa. Usá-la torna a resposta do agente quase instantânea, o que é ideal para aplicações interativas.

## 🛠️ Estrutura do Código

-   **Configuração do LLM**: O `config_list` é configurado para usar um modelo da Groq (ex: `llama3-8b-8192`) com a chave de API fornecida.
-   **Definição dos Agentes**: Criação das instâncias do `AssistantAgent` e do `UserProxyAgent`, definindo seus comportamentos e personas através do `system_message`.
-   **Criação da Ferramenta**: Uma função Python comum é definida (ex: `identify_language` ou `turn_on_airconditioner`).
-   **Registro da Ferramenta**: A função é "registrada" para os agentes usando decoradores:
    -   `@id_programming_bot.register_for_llm()`: Informa ao assistente que a ferramenta existe e para que serve (através da `description`).
    -   `@user_proxy.register_for_execution()`: Habilita o proxy a executar essa função quando solicitado.
-   **Iniciação da Conversa**: `user_proxy.initiate_chat()` dá início à interação, passando a mensagem inicial do usuário para o agente.

## 🚀 Como Executar o Projeto

Para rodar este laboratório, siga os passos abaixo. O ambiente ideal é o **Google Colab**.

### Passo 1: Obter uma API Key da Groq
1.  [cite_start]Crie uma conta gratuita na [GroqCloud](https://console.groq.com/login). [cite: 193, 194]
2.  [cite_start]No painel, vá para a seção de API Keys e crie uma nova chave. [cite: 205] Copie-a para usar no próximo passo.

### Passo 2: Configurar o Google Colab
1.  [cite_start]Abra o notebook `03_function_calling_agent.ipynb` no Google Colab. [cite: 238]
2.  [cite_start]No menu lateral esquerdo, clique no ícone de chave (🔑 **Secrets**). [cite: 243]
3.  [cite_start]Crie um novo "secret" com o nome `groq`. [cite: 260]
4.  [cite_start]No campo "Valor", cole a sua API Key da Groq. [cite: 243, 261] Habilite o acesso do notebook a este secret.

[cite_start]Esta prática (`userdata.get('groq')`) é muito mais segura do que colar a chave diretamente no código. [cite: 282, 284]

### Passo 3: Instalar as Dependências
Execute a primeira célula do notebook para instalar as bibliotecas necessárias:
```bash
!pip install autogen groq
```

### Passo 4: Executar o Notebook
Execute as células restantes em sequência para ver o agente em ação. [cite_start]Você pode modificar o `system_message`, as funções e a mensagem do usuário para experimentar diferentes cenários! [cite: 342, 348, 359]

## Licença

Este projeto está sob a licença MIT.
