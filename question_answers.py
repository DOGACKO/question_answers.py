#%%
from transformers import AutoModelForQuestionAnswering,AutoTokenizer,pipeline

#%%
nlp = pipeline('question-answering',model='deepset/roberta-base-squad2',
               tokenizer=('deepset/roberta-base-squad2'))
#%%
wikipedia_text = """
Deep learning is a method in artificial intelligence (AI) that teaches computers to process data in a way that is inspired by the human brain. Deep learning models can recognize complex patterns in pictures, text, sounds, and other data to produce accurate insights and predictions.
"""
#%%
question_set = {
                'question':'What is deep learning',
                'context':wikipedia_text
               }
#%%
results = nlp(question_set)
#%%
results['answer']
#%%
import tkinter as tk
def get_answer():
    # Get the user's input from the entry widgets
    question = question_entry.get()
    context = context_entry.get()

    # Use the pipeline to get the answer
    result = nlp({'question': question, 'context': context})

    # Display the question and answer in the label widget
    answer_label.config(text=f"Question: {question}\nAnswer: {result['answer']}")

# Create the main window
window = tk.Tk()
window.title("Question Answering App")

# Create and place widgets

context_label = tk.Label(window, text="Enter the context:", font=('Helvetica', 14))  # Font size set to 14
context_label.pack(pady=5)

context_entry = tk.Entry(window, width=40)
context_entry.pack(pady=10)

question_label = tk.Label(window, text="Enter your question:")
question_label.pack(pady=10)

question_entry = tk.Entry(window, width=40)
question_entry.pack(pady=10)



submit_button = tk.Button(window, text="Get Answer", command=get_answer)
submit_button.pack(pady=10)

answer_label = tk.Label(window, text="")
answer_label.pack(pady=10)

# Start the GUI main loop
window.mainloop()
