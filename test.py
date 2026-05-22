memory = []

def ai_response(user_input):
    # 과거 기억 참고
    context = " ".join(memory[-5:])

    response = f"""
    이전 기억:
    {context}

    사용자 입력:
    {user_input}

    더 나은 답변 생성
    """

    return response

while True:
    user = input("You: ")

    answer = ai_response(user)

    print("AI:", answer)

    feedback = input("좋았나? (y/n): ")

    if feedback == "y":
        memory.append(user)
        memory.append(answer)