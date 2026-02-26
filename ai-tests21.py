8 Simple Steps
#Step 1: Set Runs
N = 10  # Quick:5, Confident:20

#Step 2: Run N Times
for i in range(N):
    responses[i] = call_ai(prompt, temp=0.7)

#Step 3: Check Each
for resp in responses:
    rule_pass[i] = check_rules(resp)  # JSON/SQL/keywords

#Step 4: Score Each
scores[i] = llm_judge(resp)  # 0-1 score
sim[i] = bert_similarity(resp, expected)

#Step 5: Calculate Stats
pass_rate = sum(rule_pass)/N
avg_score = mean(scores)
std_dev = stdev(scores)
avg_sim = mean(sim)

#Step 6: Check Thresholds
PASS if: pass_rate≥80% AND avg_score≥0.7 AND std_dev≤0.2 AND avg_sim≥0.85

# Step 7: Final Decision
OVERALL_PASS = all_thresholds_ok AND no_safety_fails

#Step 8: Report
print(f"Pass: {pass_rate*100}% | Score: {avg_score} | Std: {std_dev}")

Run: pytest test_probabilistic.py
Pass: All 4 metrics green + no safety issues.
Done. N runs → stats → PASS/FAIL.