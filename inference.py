import os
import json
from transformers import pipeline

def main():
    statement = os.getenv('STATEMENT', 'DEFAULT_STATEMENT')

    # initialize the model
    pipe = pipeline("text2text-generation",
                      model="./local-flan-t5-small")
    
    candidate_labels = ['positive', 'negative']
    
    # Construct a query we can supply to the model from the input the user gives us
    input = f'Statement: ${statement}. Is the statement positive or negative?'
    
    # Generate the text response from the output
    output = pipe(input, max_new_tokens=20)
    
    # Grab the generated text
    classification = output[0]['generated_text']
    
    output_path = f'/outputs/response.json'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Output whether the classification was bullish (i.e positive) or bearish (i.e. negative)
    if classification == candidate_labels[0]:
        data = {"data" : "bullish"}
    else:
        data = {"data" : "bearish"}
        
    with open(output_path, 'w') as file:
            json.dump(data, file, indent=4)

    print(data)

    return data
if __name__ == '__main__':
    main()