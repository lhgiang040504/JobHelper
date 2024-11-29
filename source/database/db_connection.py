from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.database = None
    
    def init(self):
        """Khởi tạo kết nối MongoDB nếu chưa kết nối"""
        if not self.client:
            self.client = MongoClient(self.uri)
        if not self.database:
            self.database = self.client[self.db_name]  # Tạo hoặc truy cập cơ sở dữ liệu
    
    def close(self):
        """Đóng kết nối MongoDB"""
        if self.client:
            self.client.close()
