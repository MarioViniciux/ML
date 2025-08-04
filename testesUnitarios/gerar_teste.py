import os
import re
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def limpar_bloco_de_codigo(texto_completo: str) -> str:
    """
    Extrai o código Python de um bloco de Markdown.

    Exemplo de entrada:
    ```python
    import unittest
    # ...
    ```

    Args:
        texto_completo: A string completa retornada pelo LLM.

    Returns:
        Apenas o código Python, sem o encapsulamento do Markdown.
    """
    padrao = re.compile(r"^(?:```|''')(?:python)?\n(.*?)\n(?:```|''')$", re.DOTALL)
    
    match = padrao.search(texto_completo.strip())
    
    if match:
        return match.group(1).strip()
    else:
        return texto_completo.strip()

def gerar_teste_unitario(caminho_arquivo: str):
    """
    Lê uma função de um arquivo e gera o código de teste unitário para ela.

    Args:
        caminho_arquivo: O caminho para o arquivo .py que contém a função.
    """
    print(f"Lendo o código da função do arquivo: {caminho_arquivo}...")

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            codigo_da_funcao = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em '{caminho_arquivo}'")
        return

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system",
             """
             Você é um assistente de programação de elite, especializado em Python e na criação de testes de software robustos.
             Sua tarefa é gerar código de teste unitário para uma função Python fornecida.

             Diretrizes:
             - Use a biblioteca `unittest` nativa do Python.
             - Importe a função a ser testada do módulo correto.
             - Crie uma classe de teste que herde de `unittest.TestCase`.
             - Crie métodos de teste distintos para:
               1.  Um caso de uso típico (o "caminho feliz").
               2.  Casos extremos (edge cases), como valores zero, limites, etc.
               3.  Casos de erro, verificando se as exceções esperadas (`Exceptions`) são levantadas corretamente. Use o método `self.assertRaises`.
             - Os testes devem ser claros, concisos e cobrir os cenários descritos na docstring da função.
             - Não adicione comentários desnecessários, apenas o código do teste.
             - Inclua a estrutura `if __name__ == '__main__': unittest.main()` para que o arquivo possa ser executado diretamente.
             """
             ),
            ("human",
             """
             Por favor, gere o código de teste unitário para a seguinte função Python:

             {codigo_funcao}
             """
            )
        ]
    )

    chain = prompt_template | llm | StrOutputParser()

    resposta_do_llm = chain.invoke({"codigo_funcao": codigo_da_funcao})

    print("Limpando a formatação do código recebido...")
    codigo_limpo = limpar_bloco_de_codigo(resposta_do_llm)

    nome_base = os.path.splitext(os.path.basename(caminho_arquivo))[0]
    caminho_teste = f"teste_{nome_base}.py"

    with open(caminho_teste, 'w', encoding='utf-8') as f:
        f.write(codigo_limpo)

    print("-" * 50)
    print(f"Sucesso! O teste unitário foi salvo em: {caminho_teste}")
    print("-" * 50)
    print("Conteúdo do arquivo gerado:\n")
    print(codigo_limpo) 

if __name__ == '__main__':
    arquivo = "desconto.py"
    gerar_teste_unitario(arquivo)