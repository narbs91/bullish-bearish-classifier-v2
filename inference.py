import os
from transformers import pipeline

def main():
    statement = os.getenv('STATEMENT', 'DEFAULT_STATEMENT')

    # initialize the zero-shot classification pipeline
    pipe = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")
    
    candidate_labels = ['bullish', 'bearish']
    
    # Generate the classificatin score of the input
    generated_score = pipe(statement, candidate_labels)
    
    # Output whether the classification score was bullish or bearish
    if generated_score['labels'][0] > generated_score['labels'][1]:
        print({"data" : candidate_labels[0]})
    else:
        print({"data" : candidate_labels[1]})

if __name__ == '__main__':
    main()