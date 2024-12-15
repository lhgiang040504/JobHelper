# Job Resume Matching Project

## Mô Tả

Dự án này sử dụng Python, JavaScript, React, FastAPI, MongoDB, LangChain, và mô hình Llama 3.3 để trích xuất và phân tích thông tin từ các hồ sơ xin việc (resume) và các tin tuyển dụng. Mục tiêu là xây dựng một hệ thống có thể tự động so sánh hồ sơ và tin tuyển dụng dựa trên các đặc điểm quan trọng, từ đó giúp việc tuyển dụng trở nên nhanh chóng và chính xác hơn. Hệ thống sử dụng các công nghệ hiện đại để trích xuất thông tin từ các tệp PDF, lưu trữ vào MongoDB và sử dụng mô hình AI để phân tích và đối chiếu dữ liệu.

## Công Nghệ

- **Python**: Dùng để trích xuất thông tin từ các tệp PDF, với các thư viện như `PyPDF2`, `pdfminer`, hoặc `pdfplumber`.
- **React**: Dùng để xây dựng giao diện người dùng phía frontend.
- **FastAPI**: Dùng để xây dựng API cho việc xử lý dữ liệu và giao tiếp giữa frontend và backend.
- **MongoDB**: Cơ sở dữ liệu NoSQL dùng để lưu trữ thông tin đã trích xuất từ PDF.
- **LangChain**: Dùng để xử lý và kết nối với các mô hình AI, giúp xây dựng các workflows tự động trong việc phân tích dữ liệu.
- **Llama 3.3**: Mô hình ngôn ngữ AI sử dụng để phân tích, so sánh và đưa ra các kết quả khớp giữa hồ sơ và yêu cầu tuyển dụng.