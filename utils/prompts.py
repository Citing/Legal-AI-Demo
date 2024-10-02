import streamlit as st
from css.layout import write_left, write_right


class Prompts:
    def __init__(self, systemPrompt="You are an AI assistant.", template=""):
        self.prompts = [{"role": "system", "content": systemPrompt}]
    
    def userPrompt(self, userPrompt):
        self.prompts.append({"role": "user", "content": userPrompt})

    def assistantPrompt(self, assistantPrompt):
        self.prompts.append({"role": "assistant", "content": assistantPrompt})

    def display(self):
        for _, prompt in enumerate(self.prompts[1:]):
            col1, col2 = st.columns([4, 6])
            if prompt['role'] == 'user':
                with col1:
                    write_left(prompt['content'])
            elif prompt['role'] == 'assistant':
                with col2:
                    write_right(prompt['content'])   

    def download(self):
        markdown_content = "# Conversation Log\n\n"
        for prompt in self.prompts[1:]:
            if prompt['role'] == 'user':
                markdown_content += f"**You**: {prompt['content']}\n\n"
            elif prompt['role'] == 'assistant':
                markdown_content += f"**Assistant**: {prompt['content']}\n\n"
        return markdown_content
        
