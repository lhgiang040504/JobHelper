import uuid

class CVsInfoExtraction:
    def __init__(self, llm, prompt, parser):
        # Kiểm tra các đối tượng đầu vào
        if not callable(llm):
            raise ValueError("llm must be a callable object")
        if not hasattr(prompt, "__or__"):
            raise ValueError("prompt must support the '|' operator")
        if not hasattr(parser, "__or__"):
            raise ValueError("parser must support the '|' operator")

        self.llm = llm
        self.prompt = prompt
        self.parser = parser

        # Tạo chain pipeline
        try:
            self.chain = self.prompt | self.llm | self.parser
        except Exception as e:
            raise ValueError(f"Failed to initialize chain: {e}")

    def extract_info(self, text: str):
        # Kiểm tra nếu chain có method invoke
        if not hasattr(self.chain, "invoke"):
            raise ValueError("chain object must have an 'invoke' method")
        try:
            info = self.chain.invoke(input={"query": text})

            # Kiểm tra và tạo 'id' nếu thiếu hoặc rỗng
            if "_id" not in info or not info["_id"]:
                info["_id"] = str(uuid.uuid4())  # Tạo 'id' ngẫu nhiên

            return info
        except Exception as e:
            raise ValueError(f"Error during information extraction: {e}")
