import time
from typing import Callable, Dict, Any
from data.benchmark_data import BENCHMARK_QUESTIONS, BenchmarkQuestion

# TODO: Replace this dummy function with your actual assistant call endpoint
def call_assistant_api(prompt: str) -> str:
    """
    Placeholder endpoint for the Smart Virtual Assistant pipeline.
    Replace this with your actual model invocation or HTTP client call.
    """
    if not prompt.strip():
        return "Vui lòng nhập nội dung câu hỏi."
    if "Phòng Đào tạo" in prompt:
        return "Phòng Đào tạo nằm ở Tầng 1, Tòa nhà A."
    if "xin chào" in prompt.lower():
        return "Xin chào! Tôi là trợ lý ảo, tôi có thể giúp gì cho bạn?"
    
    return "Xin lỗi, tôi chưa hỗ trợ hoặc chưa có thông tin về câu hỏi này."


def evaluate_response(question: BenchmarkQuestion, response: str) -> bool:
    """Evaluates assistant output against expected keywords and evaluation rules."""
    response_lower = response.lower()
    
    if question.evaluation_type in ("contains_any", "fallback_trigger"):
        return any(kw.lower() in response_lower for kw in question.expected_keywords)
    elif question.evaluation_type == "contains_all":
        return all(kw.lower() in response_lower for kw in question.expected_keywords)
    elif question.evaluation_type == "exact_match":
        return response.strip().lower() == question.expected_keywords[0].lower()
    
    return False


def run_benchmark(assistant_fn: Callable[[str], str]) -> Dict[str, Any]:
    """Runs the benchmark suite and displays results."""
    print("=" * 70)
    print("STARTING SMART VIRTUAL ASSISTANT BENCHMARK")
    print("=" * 70)
    
    passed_count = 0
    total_count = len(BENCHMARK_QUESTIONS)
    results = []

    start_suite_time = time.time()

    for q in BENCHMARK_QUESTIONS:
        t_start = time.time()
        try:
            response = assistant_fn(q.input_text)
        except Exception as e:
            response = f"[ERROR: Exception occurred: {str(e)}]"
            
        elapsed_ms = (time.time() - t_start) * 1000
        is_passed = evaluate_response(q, response)
        
        if is_passed:
            passed_count += 1
            status = "PASSED"
        else:
            status = "FAILED"

        results.append({
            "id": q.id,
            "category": q.category,
            "status": status,
            "time_ms": elapsed_ms,
            "input": q.input_text,
            "output": response
        })

        print(f"[{status}] Test #{q.id:02d} [{q.category}] ({elapsed_ms:.1f}ms)")
        print(f"  Input : {repr(q.input_text)}")
        print(f"  Output: {repr(response)}")
        print("-" * 70)

    total_time = time.time() - start_suite_time
    pass_rate = (passed_count / total_count) * 100

    print("\n" + "=" * 70)
    print("BENCHMARK SUMMARY REPORT")
    print("=" * 70)
    print(f"Total Tests Run : {total_count}")
    print(f"Passed          : {passed_count}")
    print(f"Failed          : {total_count - passed_count}")
    print(f"Pass Rate       : {pass_rate:.2f}%")
    print(f"Total Duration  : {total_time:.2f}s")
    print("=" * 70)

    return {
        "pass_rate": pass_rate,
        "total_tests": total_count,
        "passed": passed_count,
        "failed": total_count - passed_count,
        "details": results
    }


if __name__ == "__main__":
    run_benchmark(call_assistant_api)