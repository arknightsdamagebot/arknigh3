import streamlit as st
import numpy as np

# マルコフモデルを使用して次の文字の確率を直前の文字に依存させる
def generate_text_with_context(initial_sequence, transition_probs, num_chars=9):
    generated_text = initial_sequence
    current_sequence = initial_sequence[-3:]  # 最初の3文字を初期の直前の文字列とする
    
    for _ in range(num_chars - len(initial_sequence)):
        # Choose the next character based on transition probabilities
        next_char = np.random.choice(list(transition_probs[current_sequence].keys()), 
                                     p=list(transition_probs[current_sequence].values()))
        generated_text += next_char
        current_sequence = current_sequence[1:] + next_char
    
    return generated_text

def main():
    st.title('Character Generation with Contextual Probabilities')
    
    st.markdown('''
    ## Specify Transition Probabilities
    ''')
    
    # Input transition probabilities for each character based on the previous characters
    characters = ['し', 'か', 'の', 'こ', 'た', 'ん']
    transition_probs = {
        'しかの': {'こ': 0.5, 'た': 0.5},
        'かのこ': {'の': 0.67, 'た': 0.33},
        'のこの': {'こ': 0.5, 'た': 0.5},
        'このこ': {'の': 0.67, 'た': 0.33},
        'このこの': {'こ': 1.0},
        'このこ': {'の': 0.67, 'た': 0.33},
        'のこた': {'ん': 1.0},
        'こたん': {'た': 0.5, 'ん': 0.5},
        'たんた': {'ん': 1.0},
        'んたん': {'し': 1.0}
    }
    
    st.markdown('''
    ## Generated Text
    ''')
    
    # ボタンを押すと生成される
    if st.button('Generate'):
        initial_sequence = 'しかのこのこのここしたんたん'
        generated_text = generate_text_with_context(initial_sequence, transition_probs)
        st.write(generated_text)

if __name__ == '__main__':
    main()
