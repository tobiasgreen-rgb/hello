def math_question_answerer(question):
    try:
        answer = eval(question)
        return f'The answer is: {answer}'
    except Exception as e:
        return f'Error in calculating the answer: {e}'

# Example usage
if __name__ == '__main__':
    question = input('Enter a math question (e.g., 2 + 2): ')
    print(math_question_answerer(question))