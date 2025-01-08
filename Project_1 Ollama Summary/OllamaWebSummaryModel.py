from openai import OpenAI
from IPython.display import display, Markdown
from Website import Website

class OllamaWebSummaryModel:
    def __init__(self):
        self.system_prompt = "You are an assistant that analyzes the contents of the website or article and summarizes it, providing summaries in markdown."
        self.ollama_api = "http://localhost:11434/api/chat"
        self.headers = {"Content-Type": "application/json"}
        self.model = "llama3.2"

    def _user_prompt_for(self, website):
        user_prompt = f"You are looking at a website titled {website.title}"
        user_prompt += "\nThe contents of this website is as follows; Please provide a summary of the website. \n\n"
        user_prompt += website.text
        return user_prompt

    def _messages_for(self, website):
        return [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self._user_prompt_for(website)}
        ]

    def _summarize(self, url):
        ollama_via_openai = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
        website = Website(url)
        response = ollama_via_openai.chat.completions.create(
            model=self.model,
            messages=self._messages_for(website)
        )
        website.close()
        return response.choices[0].message.content  # Fixed this line

    def summarize_website(self, url):
        summary = self._summarize(url)
        return summary

