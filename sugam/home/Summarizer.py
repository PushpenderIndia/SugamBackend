
class Summarizer:
    def __init__(self, original_txt, lang):
        self.original_txt = original_txt
        self.lang = lang

    def start(self):
        summarized_txt = ""
        return summarized_txt
    
if __name__ == "__main__":
    summarize =  Summarizer("original txt", "hindi")
    summarized_txt = summarize.start()