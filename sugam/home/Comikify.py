import openai

class Comikify:
    def __init__(self, topic):
        self.topic = topic
        openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your OpenAI API key

    def generate_dialogue(self):
        prompt = f'write a script dialogue with two characters on topic: "{self.topic}"'

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,  # Adjust the number of tokens as per your needs
            temperature=0.6,  # Adjust the temperature as per your preference
            n=1,
            stop=None
        )

        dialogue = response.choices[0].text.strip()
        return dialogue

if __name__ == "__main__":
    topic = "Artificial Intelligence"  # Replace with your desired topic
    script = Comikify(topic)
    dialogue = script.generate_dialogue()
    print(dialogue)
