import openai

class Comikify:
    def __init__(self, topic, openai_key):
        self.topic = topic
        self.openai_key = openai_key
        self.prompt = f'write a script dialogue with two characters on topic: "{self.topic}"'

    def start(self):
        openai.api_key = self.openai_key
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=self.prompt,
            max_tokens=200,
            temperature=0.7,
            n=1,
            stop=None,
        )

        dialogue = response.choices[0].text.strip().split('\n')

        if len(dialogue) < 2:
            return ["Character 1: [Dialogue missing]", "Character 2: [Dialogue missing]"]

        return dialogue

if __name__ == "__main__":
    # Usage example
    topic = "Artificial Intelligence"
    openai_key = "your_openai_api_key"

    generator = Comikify(topic, openai_key)
    dialogue = generator.start()

    for line in dialogue:
        print(line)
