import os
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
dirname = os.getcwd()
SAMPLE_FILEPATH = './/Models//Samples//'

def load_model():
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    return model

def extract_vector(sentence):
    return  model.encode([sentence])

def calculate_distance(sentence1, sentence2):
    v1 =  extract_vector(sentence1)
    v2 =  extract_vector(sentence2)
    return float(cosine_similarity(v1, v2))

def read_txt_file(filename):
    with open(filename, encoding="utf8") as f:
        lines = f.readlines()
    return lines

def initialize_vectors():
    # Read model strings and calculate the vectors
    loan_agreement_sample_file = os.path.join(SAMPLE_FILEPATH, 'loanAgreement.txt')
    la_contents = read_txt_file(loan_agreement_sample_file)
    v1 = extract_vector(la_contents)

    loan_interest_sample_file = os.path.join(SAMPLE_FILEPATH, 'loanInterestDetails.txt')
    lrd_contents = read_txt_file(loan_interest_sample_file)
    v2 = extract_vector(lrd_contents )

    loan_security_sample_file = os.path.join(SAMPLE_FILEPATH, 'loanSecurity.txt')
    ls_contents = read_txt_file(loan_security_sample_file)
    v3 = extract_vector(ls_contents)

    return [v1,v2, v3]

def find_match(input_vector):
    # find the top matching vector
    match = [cosine_similarity(i, input_vector) for i in sample_vectors]
    if max(match) < 0.70:
        print('Highest Match : ', max(match)[0][0])
        return 3

    index = match.index(max(match))
    print('Highest Match : ', max(match)[0][0])
    return index

def init():
    global model, sample_vectors, mapping
    model = load_model()
    sample_vectors = initialize_vectors()
    mapping = { 0: "Loan Agreement", 1: "Loan Interest Details", 2: "Loan Security", 3: "Need Manual Check"}

def run(input_sentence):
    input_vector = extract_vector(input_sentence)
    match_index = find_match(input_vector)
    return mapping[match_index]

if __name__ == "__main__":
    init()
    # local test code
    # No need to pushed to application
    test_folder = ".\\Test"
    for test_file in os.listdir(test_folder):
        print('Testing : ',test_file)
        test_file = os.path.join(test_folder, test_file)
        test_input = read_txt_file(test_file)
        print("Match : ", run(test_input))

