"""
Benchmark Dataset for Smart Virtual Assistant Evaluation.

Format Specification:
---------------------
Each benchmark case is an instance of `BenchmarkQuestion`:
- `id` (int): Unique identifier (1 to 15).
- `category` (str): Type of user input (e.g., greeting, office_location, fallback, unusual).
- `input_text` (str): The raw prompt/query sent to the assistant.
- `expected_keywords` (list[str]): Critical keywords or phrases that MUST appear in a valid response.
- `evaluation_type` (str): Matching strategy ("contains_any", "contains_all", "exact_match", "fallback_trigger").
- `description` (str): Explanation of the test case scenario.
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class BenchmarkQuestion:
    id: int
    category: str
    input_text: str
    expected_keywords: List[str]
    evaluation_type: str
    description: str


BENCHMARK_QUESTIONS: List[BenchmarkQuestion] = [
    # --- Category 1: Greeting Questions (2 questions) ---
    BenchmarkQuestion(
        id=1,
        category="greeting",
        input_text="Xin chào! Bạn có thể giúp gì cho tôi?",
        expected_keywords=["chào", "giúp", "trợ lý"],
        evaluation_type="contains_any",
        description="Standard friendly Vietnamese greeting."
    ),
    BenchmarkQuestion(
        id=2,
        category="greeting",
        input_text="Hello, who are you?",
        expected_keywords=["hello", "assistant", "help"],
        evaluation_type="contains_any",
        description="English greeting and identity query."
    ),

    # --- Category 2: Campus Office Location Questions (4 questions) ---
    BenchmarkQuestion(
        id=3,
        category="office_location",
        input_text="Phòng Đào tạo ở đâu?",
        expected_keywords=["Phòng Đào tạo", "tòa nhà", "tầng"],
        evaluation_type="contains_any",
        description="Location request for Academic Affairs Office (Phòng Đào tạo)."
    ),
    BenchmarkQuestion(
        id=4,
        category="office_location",
        input_text="Cho mình hỏi văn phòng Khoa Công nghệ Thông tin nằm ở đâu?",
        expected_keywords=["Công nghệ Thông tin", "Khoa CNTT"],
        evaluation_type="contains_any",
        description="Location request for Faculty of Information Technology office."
    ),
    BenchmarkQuestion(
        id=5,
        category="office_location",
        input_text="Phòng Công tác Sinh viên ở tòa nhà nào?",
        expected_keywords=["Công tác Sinh viên", "phòng"],
        evaluation_type="contains_any",
        description="Specific query about Student Affairs Office building."
    ),
    BenchmarkQuestion(
        id=6,
        category="office_location",
        input_text="Where is the campus library located?",
        expected_keywords=["library", "building", "thư viện"],
        evaluation_type="contains_any",
        description="English query for campus library location."
    ),

    # --- Category 3: Unknown or Unsupported Questions (5 questions) ---
    BenchmarkQuestion(
        id=7,
        category="unsupported",
        input_text="Thời tiết hôm nay ở Hà Nội như thế nào?",
        expected_keywords=["không thể", "xin lỗi", "không hỗ trợ", "chưa có thông tin"],
        evaluation_type="fallback_trigger",
        description="Off-topic general knowledge query (weather)."
    ),
    BenchmarkQuestion(
        id=8,
        category="unsupported",
        input_text="Giá vàng hôm nay bao nhiêu một lượng?",
        expected_keywords=["không thể", "xin lỗi", "không hỗ trợ"],
        evaluation_type="fallback_trigger",
        description="Off-topic financial query."
    ),
    BenchmarkQuestion(
        id=9,
        category="unsupported",
        input_text="Giải giúp tôi phương trình bậc 2: x^2 + 5x + 6 = 0",
        expected_keywords=["chuyên môn", "chưa hỗ trợ", "xin lỗi"],
        evaluation_type="fallback_trigger",
        description="Out-of-scope complex math query."
    ),
    BenchmarkQuestion(
        id=10,
        category="unsupported",
        input_text="Bạn thích ăn món gì nhất?",
        expected_keywords=["trợ lý", "không ăn", "ảo"],
        evaluation_type="contains_any",
        description="Chitchat / personal preference query for AI."
    ),
    BenchmarkQuestion(
        id=11,
        category="unsupported",
        input_text="How do I bake a chocolate cake?",
        expected_keywords=["sorry", "cannot", "unsupported", "không thể"],
        evaluation_type="fallback_trigger",
        description="English out-of-domain recipe query."
    ),

    # --- Category 4: Empty or Unusual Input Cases (4 questions) ---
    BenchmarkQuestion(
        id=12,
        category="unusual",
        input_text="",
        expected_keywords=["nhập", "câu hỏi", "nội dung"],
        evaluation_type="contains_any",
        description="Empty string input edge case."
    ),
    BenchmarkQuestion(
        id=13,
        category="unusual",
        input_text="   \n\t  ",
        expected_keywords=["nhập", "câu hỏi", "nội dung"],
        evaluation_type="contains_any",
        description="Whitespace-only input edge case."
    ),
    BenchmarkQuestion(
        id=14,
        category="unusual",
        input_text="???!!!!!...",
        expected_keywords=["hiểu", "nhập", "lại"],
        evaluation_type="contains_any",
        description="Punctuation-only string."
    ),
    BenchmarkQuestion(
        id=15,
        category="unusual",
        input_text="asdfghjklqwertyuiop123456789",
        expected_keywords=["không hiểu", "thông tin", "thử lại"],
        evaluation_type="contains_any",
        description="Gibberish random string input."
    ),
]