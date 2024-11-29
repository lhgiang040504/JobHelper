class JobInfoExtraction:
    def __init__(self, llm, chain, parser):
        self.llm = llm
        self.chain = chain
        self.parser = parser
        chain = self.chain | self.llm | self.parser 
        
    def extract_info(self, jobs ,text: str):
        info = self.chain.invoke(input={'job_description':text})
        return info

        