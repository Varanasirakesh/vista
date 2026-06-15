import ollama

class RAGGenerator:
    def __init__(
        self,
        model_name: str = "llama3.1:8b",
    ):
        self.model_name = model_name

    def generate(
        self,
        query: str,
        context: str,
    ) -> str:

        prompt = f"""
        You are a support assistant.
        Answer the user's question ONLY using the provided context.
        If the answer cannot be found in the context, say:
        "I could not find this information in the provided documents."
        Context:
        {context}
        Question:
        {query}
        Answer:
        """
        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        return response["message"]["content"]