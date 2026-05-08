import json

from app.services.triage import analyze_triage


with open("app/evals/eval_cases.json", "r") as f:
    test_cases = json.load(f)


correct = 0
total = len(test_cases)


for case in test_cases:

    result = analyze_triage(case["input"])

    predicted = result["triage_level"]
    expected = case["expected_triage"]

    is_correct = predicted == expected

    if is_correct:
        correct += 1

    print("=" * 50)
    print(f"INPUT: {case['input']}")
    print(f"EXPECTED: {expected}")
    print(f"PREDICTED: {predicted}")
    print(f"RESULT: {'PASS' if is_correct else 'FAIL'}")


accuracy = correct / total * 100

print("=" * 50)
print(f"FINAL ACCURACY: {accuracy:.2f}%")
