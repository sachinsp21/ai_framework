import pytest, openai, numpy as np
client = openai.OpenAI()

@pytest.fixture
def prompt(): return "Write SQL: count users by date"

def test_evals(prompt):
    scores = []
    for i in range(5):  # N=5
        resp = client.chat.completions.create(model="gpt-4o-mini", 
            messages=[{"role":"user","content":prompt}], temp=0.7
        ).choices[0].message.content
        
        score = 100 if "SELECT" in resp and "GROUP BY" in resp else 0
        scores.append(score)
    
    avg, std = np.mean(scores), np.std(scores)
    assert avg >= 70, f"Avg: {avg}"
    assert sum(s>=70 for s in scores)/5 >= 0.8, f"Pass: {sum(s>=70 for s in scores)/5}"
    print(f"✅ PASS: {avg:.1f}% ± {std:.1f}%")
