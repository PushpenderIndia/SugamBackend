
class GenerateFollowup:
    def __init__(self, original_text, summarized_text):
        self.original_text = original_text
        self.summarized_text = summarized_text

    def start(self, question):
        follow_up = ""
        return follow_up
    
if __name__ == "__main__":
    test = GenerateFollowup("hello orignal txt", "summarized hello")
    follow_up = test.start("this doc is about which topic?")