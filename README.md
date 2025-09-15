<div align="center">
  <h1>
    Agentes de IA com Autogen e Function Calling
  </h1>
</div>

<p align="center">
  <img alt="Linguagem Principal" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Licença" src="https://img.shields.io/github/license/vrsmarcos26/Automatic-Tesk-IA?style=for-the-badge&color=blue">
</p>

<p align="center">
  Um laboratório prático que explora a criação de agentes de IA com o framework Microsoft Autogen, utilizando Function Calling para estender suas capacidades com ferramentas Python customizadas.
</p>

<p align="center">
  <a href="#-objetivos-de-aprendizagem">Objetivos</a> •
  <a href="#-tecnologias-utilizadas">Tecnologias</a> •
  <a href="#-como-rodar-o-projeto">Como Rodar</a> •
  <a href="#-demonstração">Demonstração</a> •
  <a href="#-licença">Licença</a>
</p>

---

### 🎯 Objetivos de Aprendizagem

-   Entender o paradigma de **sistemas multi-agente** com Microsoft Autogen.
-   Implementar **"Function Calling" (Uso de Ferramentas)** para dar aos agentes capacidades além da linguagem.
-   Integrar um LLM de alta velocidade via **Groq API** (com o modelo Llama 3).
-   Diferenciar os papéis do `AssistantAgent` (o pensador) e do `UserProxyAgent` (o executor).

---

### 🛠️ Tecnologias Utilizadas

Este projeto combina um framework de agentes de IA com uma API de inferência de LLM de alta performance.

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"></a>
  <a href="#"><img src="https://img.shields.io/badge/AutoGen-A724B5?style=for-the-badge&logo=microsoft&logoColor=white" alt="AutoGen"></a>
  <a href="#"><img src="https://img.shields.io/badge/Groq-00C592?style=for-the-badge&logo=groq&logoColor=white" alt="Groq"></a>
</p>

---

### ⚙️ Como Rodar o Projeto

O laboratório foi projetado para ser executado no **Google Colab**.

#### 1. Pré-requisitos
-   Uma **API Key da Groq**. Você pode obter uma gratuitamente no (https://console.groq.com/login).

#### 2. Configure a API Key
-   Abra o notebook `03_function_calling_agent.ipynb` no Google Colab.
-   No menu esquerdo, vá em **Secrets (🔑)** e crie um novo secret chamado `groq`.
-   Cole sua API Key da Groq no campo de valor. [cite: 243, 261] [cite_start]A utilização do `userdata.get('groq')` é uma forma mais segura de gerenciar chaves.

#### 3. Instale as Dependências
Execute a primeira célula do notebook para instalar as bibliotecas:
```bash
pip install autogen groq
```

#### 4. Execute o Laboratório
Execute as células em sequência para ver os agentes em ação. Sinta-se à vontade para modificar o `system_message`, as funções e as mensagens do usuário para testar outros cenários.

---

### 🎬 Demonstração

O laboratório consiste em adaptar um agente. Inicialmente, ele é um `currency_bot` para conversão de moedas. Depois, seu `system_message` e suas ferramentas são alterados para que ele se torne um assistente de automação residencial.

**Comando do Usuário:** `E ai, truta! Está calor, hein? [cite_start]Estou na sala`

**Resultado:** O agente entende a intenção, chama a ferramenta correta (`turn_on_airconditioner`) com os parâmetros certos (`ambiente="Sala de estar"`, `estado=True`) e confirma a execução da tarefa.

<summary><strong>💡 Análise Técnica do Fluxo (Write-up)</strong></summary>
<br>

O conceito de **Function Calling** no Autogen segue um fluxo de trabalho claro:

1.  **Definição da Ferramenta**: Uma função Python comum é criada (ex: `turn_on_airconditioner`).

2.  **Registro da Ferramenta**: A função é registrada usando dois decoradores:
    -   `@agent.register_for_llm()`: Informa ao `AssistantAgent` que a ferramenta existe, o que ela faz (através da `description`) e quais parâmetros ela aceita.
    -   `@user_proxy.register_for_execution()`: Autoriza o `UserProxyAgent` a executar essa função quando o assistente solicitar.

3.  **Fluxo de Execução**:
    -   O usuário envia uma mensagem através de `user_proxy.initiate_chat()`. 
    -   O `AssistantAgent` (com o LLM) analisa a mensagem e a descrição das ferramentas. Ele conclui que deve chamar uma função.
    -   Ele não executa a função, mas envia uma "sugestão de chamada de ferramenta" ao proxy, com os argumentos preenchidos (ex: `{"ambiente": "Sala de estar", "estado":true}`).
    -   O `UserProxyAgent` recebe a sugestão, executa a função Python localmente (`EXECUTING FUNCTION...`) e retorna o resultado (ex: "Ar condicionado do Sala de estar foi ligado").
    -   O `AssistantAgent` recebe este resultado e formula uma resposta final em linguagem natural para o usuário (ex: "Ahhh, que um ar fresco começou a circular!").


---

### 📝 Licença

Este projeto está sob a licença MIT.

<hr>

<p align="center">
  Desenvolvido por <b>Marcos Vinícius Rocha Silva</b>
</p>
