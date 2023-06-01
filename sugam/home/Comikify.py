import openai

class Comikify:
    def __init__(self, topic, openai_key):
        self.topic = topic
        self.openai_key = openai_key
        self.prompt = f'write a script dialogue on topic: "{self.topic}", script should be generated in such a way so that we can understand the whole topic'

    def start(self):
        openai.api_key = self.openai_key
        response = openai.Completion.create(
            engine="davinci",
            prompt=self.prompt,
            max_tokens=500,
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
    openai_key = "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"

    generator = Comikify(topic, openai_key)
    dialogue = generator.start()
    print(dialogue)

    for line in dialogue:
        print(line)
