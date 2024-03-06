import gradio as gr
from langchain.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")
# initialize the models

def chatbot(user_input):
    # defining a template
    template = """Question: {question}
    please provide step by step Answer:
    """
    prompt = PromptTemplate(template=template, input_variables=["question"])
    formated_prompt =prompt.format(question=str(user_input))
    return llm.invoke(formated_prompt).content
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(share=True)