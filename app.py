
import streamlit as st
import time

# ---------------------------------------------------------
# 1) CONFIGURAÇÃO INICIAL E LISTA DE PERGUNTAS
# ---------------------------------------------------------
st.set_page_config(page_title="Chatbot Questionário", layout="centered")

# 
INTERVIEWER_NAME = "Entrevistador"  # Nome de quem está entrevistando

QUESTIONS = [
    {
        "pergunta": "Como você quer ser reconhecido(a) pelos seus clientes?",
        "opcoes": [
            "Qualidade dos produtos & serviços",
            "Atendimento personalizado",
            "Produtos & Serviços exclusivos",
            "Até esse momento, não tinha pensado nisso",
            "Preço Baixo",
            "Atendimento humanizado e personalizado"
        ]
    },
    {
        "pergunta": "Você costuma analisar seus concorrentes para ver o que eles estão fazendo de bom?",
        "opcoes": [
            "Sim, analiso, mas com cautela",
            "Dou uma olhada",
            "Nunca olho",
            "Peço para uma pessoa de confiança ir aos concorrentes e falar sobre essa experiência",
            "Até esse momento, não tinha pensado nisso"
        ]
    },
    {
        "pergunta": "Você usa as redes sociais para divulgar os produtos e serviços da empresa?",
        "opcoes": [
            "Sim, mas ainda acho que podemos usar mais",
            "Sim, usamos Whatsapp, Facebook, Instagram, etc",
            "Não, meus clientes \"não são muito digitais\"",
            "Eu não sei como usar essas redes para a minha empresa"
        ]
    },
    {
        "pergunta": "Na sua opinião, a localização da sua empresa ajuda nas vendas?",
        "opcoes": [
            "Não pensei na hora de começar, abri onde foi possível, mas dei sorte e o ponto é bom",
            "As vendas pela internet cresceram e a localização da empresa não é mais tão importante",
            "Não ajuda, estou pensando em mudar",
            "Sim, escolhi o ponto estrategicamente, pensando no impacto positivo para o negócio",
            "Não sei se afeta de maneira boa ou ruim, apenas abri onde apareceu",
            "A localização da empresa não é relevante já que as vendas podem ser feitas pela Internet ou diretamente nos clientes"
        ]
    },
    {
        "pergunta": "É possível vender os produtos da sua empresa pela internet?",
        "opcoes": [
            "Ainda não é possível adquirir nossos produtos e serviços pela internet",
            "Sim, a venda pela internet faz parte da estratégia da empresa",
            "Sim, mas temos poucos clientes na internet",
            "Sim, durante a pandemia a venda pela internet foi uma questão de sobrevivência",
            "Não se aplica",
            "Sim, as vendas pela internet fazem parte da estratégia da empresa",
            "Ainda não é possível vender nossos produtos e serviços pela internet",
            "Sim, as vendas pela internet tornou-se uma questão de sobrevivência"
        ]
    },
    {
        "pergunta": "Em relação à concorrência, seus preços são:",
        "opcoes": [
            "Na média",
            "Mais altos",
            "Não sei dizer",
            "Mais baixos",
            "Depende do produto",
            "nan"  # Você pode remover "nan" se não quiser exibir
        ]
    },
    {
        "pergunta": "Você ainda tem que \"meter a mão na massa\" na maior parte do tempo?",
        "opcoes": [
            "Sim, todos os dias",
            "Ainda tenho uma função operacional, mas é menor que 75% do meu tempo",
            "Não, atualmente me dedico apenas à gestão da empresa",
            "Não sei dizer o percentual do tempo que me dedico à operação",
            "Só quando temos uma falta na equipe",
            "Sim, todos os dias. Sou a principal responsável operacional na empresa",
            "Ainda tenho uma função operacional. Mas, hoje divido o meu tempo entre o atendimento e a parte administrativa (gestão)"
        ]
    },
    {
        "pergunta": "Você acha que a sua empresa está realmente preparada para crescer? (pense na equipe, capital de giro, instalações, processos, ...)",
        "opcoes": [
            "Sim, a empresa está preparada para crescer",
            "Não, mas com baixo investimento conseguiríamos crescer rapidamente",
            "Não, precisamos fortalecer várias áreas antes de pensar em crescimento",
            "Não tenho interesse de crescer muito a empresa",
            "Nunca pensei nisso antes"
        ]
    },
    {
        "pergunta": "A sua empresa possui algum sistema de apoio? (sistema de controle de vendas, controle de estoque, controle financeiro etc.)",
        "opcoes": [
            "Minha empresa é muito pequena para usar essas soluções sistêmicas",
            "Temos alguns sistemas, mas ainda precisamos de mais soluções tecnológicas",
            "Eu não entendo muito de tecnologia",
            "Sim, a empresa está informatizada",
            "Não temos recursos financeiros para investir em tecnologia",
            "nan",
            "Minha empresa é muito pequena para usar essas soluções sofisticadas"
        ]
    },
    {
        "pergunta": "Como você definiria a sua liderança?",
        "opcoes": [
            "Compartilho todas as decisões com o time",
            "Eu tomo quase todas as decisões na empresa e sou respeitada pela equipe",
            "Sou muito carismática e a equipe gosta do meu jeito",
            "Tenho mais experiência e consigo executar o trabalho melhor que a equipe. Sou respeitada por isso",
            "Não se aplica",
            "Não se aplica. Não tenho colaboradores"
        ]
    },
    {
        "pergunta": "Quando você não está na empresa, você conta com uma pessoa preparada para substituí-la?",
        "opcoes": [
            "Sim, mas ainda não consigo me ausentar por muito tempo",
            "Não, minha equipe é muito inexperiente. Tenho a sensação que a empresa para se eu não estiver junto",
            "Sim, tenho uma pessoa da equipe bem preparada",
            "Não, estou tentando, mas ainda não consegui formar um substituto",
            "Trabalho sozinha e fecho empresa quando tenho que sair"
        ]
    },
    {
        "pergunta": "Qual a atividade da sua empresa?",
        "opcoes": [
            "Vestuário (lojas, confecção, ...)",
            "Outros",
            "Serviços de beleza (cabelereiro, estética, depilação, manicure, massagem, ...)",
            "Alimentação (restaurantes, bares, entrega de comida, ...)",
            "Comércio Varejista em Geral"
        ]
    },
    {
        "pergunta": "A sua empresa é formal, tem CNPJ?",
        "opcoes": [
            "Sim, tenho uma pequena empresa formalizada",
            "Sim, tenho uma MEI formalizada",
            "Não, tenho uma empresa informal",
            "Estou em processo de formalização da empresa"
        ]
    },
    {
        "pergunta": "Em qual etapa do ciclo de crescimento está a sua empresa?",
        "opcoes": [
            "Empresa recém criada",
            "Empresa nova, começando a crescer",
            "Empresa Estabilizada",
            "Empresa em fase de crescimento",
            "Empresa em momento de recuperação"
        ]
    },
    {
        "pergunta": "Um plano estratégico descreve o caminho que a sua empresa percorrerá para atingir seus objetivos. Você tem um documento como esse?",
        "opcoes": [
            "Sim, está tudo na minha cabeça mas nunca coloquei no papel",
            "Sim, tenho isso documentado, mas não compartilho com o meu time",
            "Nunca pensei nisso",
            "Sim, tenho isso documentado e compartilho com o meu time",
            "Não conheço esses conceitos"
        ]
    },
    {
        "pergunta": "Os resultados que a sua empresa vem obtendo estão alinhados com o que você planejou?",
        "opcoes": [
            "Nunca me planejei",
            "Sim, os resultados estão próximos ao que planejei",
            "Os resultados estão abaixo do que planejei",
            "Os resultados superaram muito às minhas expectativas"
        ]
    },
    {
        "pergunta": "Você sabe o que é necessário fazer para corrigir esses pontos fracos da sua empresa?",
        "opcoes": [
            "Sim, mas não tenho capacidade para corrigir os pontos fracos sem ajuda",
            "Sei o que tenho que fazer, mas faltam recursos financeiros para eliminá-los",
            "Sei o que tenho que fazer, mas faltam não tenho recursos financeiros para eliminá-los",
            "Sei o que tenho que fazer e tenho um plano de ação para eliminá-los",
            "Conheço os pontos fracos mas eles não atrapalham muito o crescimento da empresa",
            "Conheço os pontos fracos, mas eles não atrapalham muito o crescimento da empresa",
            "Minha empresa não tem pontos fracos"
        ]
    },
    {
        "pergunta": "Caso precisasse recomeçar do zero, sabe o que faria diferente?",
        "opcoes": [
            "Não mudaria nada",
            "Mudaria algumas coisas",
            "Mudaria muita coisa",
            "Não sei ",
            "Faria tudo diferente"
        ]
    },
    {
        "pergunta": "Você tem metas para sua empresa? Acompanha as metas que definiu?",
        "opcoes": [
            "Ainda não defini as metas da empresa",
            "Sim, acompanho as metas em um caderno",
            "Sim, tenho uma planilha de acompanhamento das metas empresa",
            "nan",
            "Não tenho tempo para acompanhar as metas",
            "Minha empresa é pequena e não vejo necessidade",
            "Sim, tenho uma planilha/sistema de acompanhamento das metas empresa (em um caderno, no computador, na planilha etc.)",
            "Sim, acompanho as metas na minha cabeça"
        ]
    },
    {
        "pergunta": "Você tem contas bancárias separadas para a empresa e para seu uso pessoal?",
        "opcoes": [
            "Sim, as contas são totalmente separadas",
            "Sim, mas às vezes uso a conta da empresa para pagar gastos pessoais (ou vice-versa)",
            "Não faço distinção entre os gastos da empresa e os pessoais",
            "Sim, as contas são totalmente separadas. Conta PF para despesas pessoais e conta PJ para fluxo financeiro da empresa",
            "Não separo os gastos da empresa e os pessoais"
        ]
    },
    {
        "pergunta": "Para calcular o custo da sua empresa, você considera itens como o seu tempo de dedicação ao negócio, o tempo de seus familiares, o aluguel ou a depreciação do seu imóvel próprio, o uso do seu carro, a gasolina?",
        "opcoes": [
            "Sim, considero todos esses custos",
            "Mais ou menos. Considero só alguns custos",
            "Não"
        ]
    },
    {
        "pergunta": "O seu negócio já atingiu o ponto de equilíbrio? (quanto você precisa faturar para cobrir os custos mensais do seu negócio)",
        "opcoes": [
            "Sim",
            "Não",
            "Não sei o que é ponto de equilíbrio"
        ]
    },
    {
        "pergunta": "Você controla as contas que tem para pagar?",
        "opcoes": [
            "Faço um controle mensal",
            "Controlo diariamente",
            "Faço um controle semanal",
            "Faço o controle de cabeça",
            "Não controlo, pago as contas quando elas aparecem",
            "Controlo diariamente com fechamento de caixa e controle de boletos de contas variáveis e fixas"
        ]
    },
    {
        "pergunta": "Você controla as contas que tem para receber?",
        "opcoes": [
            "Faço um controle mensal",
            "Controlo diariamente",
            "Faço um controle semanal",
            "Só vendo à vista",
            "Não controlo",
            "Controlo diariamente, por meio de controles de cada um dos meus clientes"
        ]
    },
    {
        "pergunta": "Você controla o fluxo de caixa da empresa?",
        "opcoes": [
            "Sim, controlo o fluxo de caixa com a ajuda de uma ferramenta (caderno, planilha ou aplicativo)",
            "Acompanho os extratos dos bancos e olho o caixa físico da empresa",
            "Não controlo muito",
            "Não sei direito o que é fluxo de caixa",
            "Sim, controlo o fluxo de caixa com a ajuda de uma ferramenta (caderno, planilha, sistema próprio ou aplicativo)"
        ]
    },
    {
        "pergunta": "A empresa tem capital de giro suficiente para crescer?",
        "opcoes": [
            "Não, mas temos condições de conseguir com bancos ",
            "Não, mas temos condições de conseguir com familiares / amigos",
            "Sim",
            "Não, nesse momento não temos condições de crescer",
            "Mantemos um fundo de emergência, mas não para crescer"
        ]
    },
    {
        "pergunta": "Você tem feito uma reserva para uma emergência?",
        "opcoes": [
            "Gostaria de ter uma reserva, mas não consegui ainda",
            "Sim, tenho uma reserva de emergência",
            "Não, prefiro pensar somente no presente"
        ]
    }
]
# ----------------------------------------------------------------
# 3) FUNÇÕES DE INICIALIZAÇÃO E AJUDA
# ----------------------------------------------------------------
def init_session():
    """Inicializa variáveis de sessão."""
    if "messages" not in st.session_state:
        st.session_state["messages"] = []  # histórico completo do chat
    if "question_index" not in st.session_state:
        st.session_state["question_index"] = 0
    if "finished" not in st.session_state:
        st.session_state["finished"] = False
    if "user_name" not in st.session_state:
        st.session_state["user_name"] = None

    # Para indicar se já digitamos algo (ex.: "ask_name" ou pergunta i).
    # Ex.: {"ask_name": True, 0: True, 1: False, ...}
    if "typed_flags" not in st.session_state:
        st.session_state["typed_flags"] = {}

def typing_effect(text: str, speed=0.03):
    """
    Efeito de digitação: mostra 'text' caractere a caractere.
    Retorna a string final (caso precise reutilizar).
    """
    typed_text = ""
    placeholder = st.empty()
    for char in text:
        typed_text += char
        placeholder.markdown(typed_text)
        time.sleep(speed)
    placeholder.empty()
    return typed_text

def show_history():
    """Exibe todas as mensagens (assistant + user) como um chat."""
    for msg in st.session_state["messages"]:
        if msg["role"] == "assistant":
            with st.chat_message("assistant"):
                st.markdown(f"**{INTERVIEWER_NAME}:**\n{msg['content']}")
        else:
            with st.chat_message("user"):
                username = st.session_state["user_name"] or "Você"
                st.markdown(f"**{username}:**\n{msg['content']}")

# ----------------------------------------------------------------
# 4) EXEMPLO DE CONFIGURAÇÃO DE LANGCHAIN (AJUSTE SE QUISER)
# ----------------------------------------------------------------
#
# Este bloco é um exemplo de como você pode integrar sua análise com a LangChain
# Lembre-se de instalar as bibliotecas necessárias (langchain_openai, etc.)
# e substituir seus dados de API, se necessário.
#

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# # Configura seu modelo:
model = ChatOpenAI(model='gpt-4o', temperature=0.7)

# # Define o prompt:
prompt = ChatPromptTemplate.from_template(
    """     Você é um profissional que está auxiliando uma mulher microempreendedora a melhorar a empresa dela.
     Ela respondeu um questionário diagnóstico dizendo como está a empresa dela.
     A partir das respostas dela, faça uma análise profunda, mas com linguagem simples e direta.
     Não use siglas, não invente informações e não use termos técnicos.
     Faça sugestões de melhorias e aponte pontos fortes e fracos, mas tudo baseado apenas no que ela respondeu.
     {questionario}
     """
 )

# # Define o parser de saída:
output_parser = StrOutputParser()

# # Cria a "chain" de execução:
chain = prompt | model | output_parser

# ----------------------------------------------------------------
# 5) APLICAÇÃO PRINCIPAL
# ----------------------------------------------------------------
def main():
    st.title("Autodiagnóstico Sicredi")
    init_session()

    # 0) Se já finalizamos, mostramos o histórico e chamamos a análise
    if st.session_state["finished"]:
        show_history()

        # Monta uma string com todas as perguntas e respostas
        questionario = ""
        for q in QUESTIONS:
            pergunta = q["pergunta"]
            resposta_user = None
            # A resposta do user está sempre logo após a pergunta no histórico
            for i, msg in enumerate(st.session_state["messages"]):
                if msg["role"] == "assistant" and msg["content"] == pergunta:
                    if i + 1 < len(st.session_state["messages"]):
                        nxt = st.session_state["messages"][i+1]
                        if nxt["role"] == "user":
                            resposta_user = nxt["content"]
            if resposta_user:
                questionario += f"Pergunta: {pergunta}\nResposta: {resposta_user}\n\n"

        # Mensagem de análise em andamento
        with st.chat_message("assistant"):
            st.markdown(f"**{INTERVIEWER_NAME}:**\nEstamos analisando o seu perfil...")

        # Exemplo de chamada da chain (descomente e ajuste se estiver usando LangChain):
        analysis_result = chain.invoke({'questionario': questionario})

        # Exibe no chat o resultado da análise
        with st.chat_message("assistant"):
            st.markdown(f"**{INTERVIEWER_NAME}:**\n{analysis_result}")

        return

    # 1) Exibe o histórico (mensagens anteriores)
    show_history()

    # 2) Se não temos o nome do usuário, perguntamos agora
    if st.session_state["user_name"] is None:
        # 2A) Se ainda não fizemos a pergunta "qual seu nome?", fazemos agora
        if not st.session_state["typed_flags"].get("ask_name", False):
            with st.chat_message("assistant"):
                typed_text = typing_effect("Olá! Antes de começarmos, qual o seu nome?")
            # Salva no histórico
            st.session_state["messages"].append({
                "role": "assistant",
                "content": typed_text
            })
            st.session_state["typed_flags"]["ask_name"] = True
            time.sleep(0.1)
            st.rerun()

        # 2B) Agora exibimos o campo para digitar o nome
        name_input = st.chat_input("Digite seu nome e tecle Enter...")
        if name_input:
            st.session_state["user_name"] = name_input.strip()
            st.session_state["messages"].append({
                "role": "user",
                "content": name_input.strip()
            })
            st.rerun()
        return

    # 3) Caso já tenhamos o nome, vamos para as perguntas do questionário
    i = st.session_state["question_index"]
    if i < len(QUESTIONS):
        pergunta = QUESTIONS[i]["pergunta"]
        opcoes = QUESTIONS[i]["opcoes"]

        # 3A) Se ainda não digitamos a pergunta, digitamos agora
        if not st.session_state["typed_flags"].get(i, False):
            with st.chat_message("assistant"):
                typed_text = typing_effect(pergunta)
            st.session_state["messages"].append({
                "role": "assistant",
                "content": typed_text
            })
            st.session_state["typed_flags"][i] = True
            time.sleep(0.1)
            st.rerun()

        # 3B) Mostramos as opções de resposta
        chosen = st.radio(
            label="Selecione a opção:",
            options=opcoes,
            key=f"radio_{i}"
        )
        if st.button("Responder", key=f"btn_{i}"):
            # Salva a resposta do usuário no histórico
            st.session_state["messages"].append({
                "role": "user",
                "content": chosen
            })
            # Passa para a próxima pergunta
            st.session_state["question_index"] += 1
            # Se já chegamos ao fim das perguntas, sinalizamos finished
            if st.session_state["question_index"] >= len(QUESTIONS):
                st.session_state["finished"] = True
            st.rerun()
    else:
        # Caso não haja mais perguntas, finalizamos
        st.session_state["finished"] = True
        st.rerun()

# ----------------------------------------------------------------
# 6) EXECUÇÃO DA APLICAÇÃO
# ----------------------------------------------------------------
if __name__ == "__main__":
    main()