""" Agentes com Autogen - Function Calling - Hands-On

Agradecimento ao professor Julio Cesar dos Reis pelo material.

## Descrição

Exploramos a implementação de agentes simples utilizando a biblioteca 
Autogen. O objetivo é demonstrar como configurar e interagir com agentes 
capazes de executar tarefas automatizadas de forma eficiente. Aprenderemos
a estruturar prompts, configurar agentes com diferentes especializações e
testar interações dinâmicas entre eles.
"""

!pip install autogen
!pip install --upgrade pydantic
!pip install ipywidgets
!pip install groq

from typing import Literal
import autogen
from typing_extensions import Annotated
import getpass

# Solicitar a API key de forma segura
from google.colab import userdata
api_key =  userdata.get('groq')

config_list = [
    {
      "model": "llama3-8b-8192",
      "api_key": api_key,
      "api_type": "groq"
    }
]

llm_config = {
    "config_list": config_list,
    "timeout": 120
}

#agente que efetua traducao
"""currency_bot = autogen.AssistantAgent(
    name="currency_bot",
    system_message="Você é um tradutor de idiomas, use apenas as funções que você recebeu. Responda TERMINATE "
                   "quando a tarefa estiver concluída.",
    llm_config=llm_config
)"""

#agente que efetua traducao
id_programming_bot = autogen.AssistantAgent(
    name="id_programming_bot",
    system_message="Você é um identificador de linguagens de programação, use apenas as funções que você recebeu. Responda TERMINATE "
                   "quando a tarefa estiver concluída.",
    llm_config=llm_config
)


#agente user proxy
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    human_input_mode="NEVER",
    max_consecutive_auto_reply=1,
    code_execution_config=False
)

"""CurrencySymbol = Literal["USD", "EUR"]

#função de taxa_de_câmbio
def exchange_rate(base_currency: CurrencySymbol, quote_currency: CurrencySymbol) -> float:
    if base_currency == quote_currency:
        return 1.0
    elif base_currency == "USD" and quote_currency == "EUR":
        return 1 / 1.09
    elif base_currency == "EUR" and quote_currency == "USD":
        return 1 / 1.1
    else:
        raise ValueError(f"Moedas desconhecidas: {base_currency}, {quote_currency}")  # Tradução: "Moedas desconhecidas:..."

#registrando a ferramenta
@user_proxy.register_for_execution()
# Register the tool signature with the assistant agent.
@currency_bot.register_for_llm(description="Calculadora de câmbio de moeda")  # Tradução: "Calculadora de câmbio de moeda"
def currency_calculator(
        base_amount: Annotated[float, "Quantia da moeda em base_currency"],  # Tradução: "Quantia da moeda em base_currency"
        base_currency: Annotated[CurrencySymbol, "Moeda base"] = "USD",  # Tradução: "Moeda base"
        quote_currency: Annotated[CurrencySymbol, "Moeda de cotação"] = "EUR"  # Tradução: "Moeda de cotação"
) -> str:
    quote_amount = exchange_rate(base_currency, quote_currency) * base_amount
    return f"{quote_amount} - {quote_currency}"


#######################################
#inicialização da conversa
user_proxy.initiate_chat(
    currency_bot,
    message="E ai, pai? Tenho 200 dolares e estou indo pra europa, quanto eu tenho na moeda local?"  # Tradução: "Converter 100 USD para EUR"
)"""

LanguageSymbol = Literal["Python", "Java","C","PHP","SQL","Javascript","Go"]

# Função que identifica a linguagem de programação com base no código-fonte
@user_proxy.register_for_execution()
@id_programming_bot.register_for_llm(description="Identifica a linguagem de programação de um trecho de código")
def identify_language(
    code_snippet: Annotated[str, "Trecho de código a ser analisado"]
) -> LanguageSymbol:
    if "def " in code_snippet and ":" in code_snippet:
        return "Python"
    elif "public static void main" in code_snippet:
        return "Java"
    elif "#include" in code_snippet or "int main() {" in code_snippet:
        return "C"
    elif "<?php" in code_snippet:
        return "PHP"
    elif "SELECT" in code_snippet.upper():
        return "SQL"
    elif "function" in code_snippet or "console.log" in code_snippet:
        return "Javascript"
    elif "func main()" in code_snippet:
        return "Go"
    else:
        raise ValueError("Não foi possível identificar a linguagem")

# Iniciar a conversa com o agente

codigo_python = """
#include <stdio.h>

int main() {
    printf("Olá, mundo!\n");
    return 0;
}


"""
user_proxy.initiate_chat(
    id_programming_bot,
    message=f"Qual linguagem é essa?\n\n{codigo_python}"
)
