import streamlit as st
import numpy as np

def generate_text_with_context(initial_sequence, transition_probs, num_chars=9):
    generated_text = initial_sequence
    current_sequence = initial_sequence[-1]  # 最後の文字を初期の直前の文字とする
    
    for _ in range(num_chars):  # 常に指定された数の新しい文字を生成
        if current_sequence in transition_probs:
            next_char = np.random.choice(list(transition_probs[current_sequence].keys()), 
                                         p=list(transition_probs[current_sequence].values()))
        else:
            next_char = np.random.choice(['し', 'か', 'の', 'こ', 'た', 'ん'])
        
        generated_text += next_char
        current_sequence = next_char  # 直前の文字を更新
    
    return generated_text

def main():
    st.title('Character Generation with Contextual Probabilities')
    
    st.markdown('## Transition Probabilities')
    
    transition_probs = {
        'し': {'か': 0.5, 'た': 0.5},
        'か': {'の': 1.0},
        'の': {'こ': 1.0},
        'こ': {'の': 0.67, 'こ': 0.33},
        'た': {'ん': 1.0},
        'ん': {'た': 1.0}
    }
    
    st.json(transition_probs)  # 遷移確率を表示
    
    st.markdown('## Generated Text')
    
    initial_sequence = st.text_input('Initial sequence', value='しかのこのこのここしたんたん')
    num_chars = st.number_input('Number of new characters to generate', min_value=1, value=20)
    
    if st.button('Generate'):
        generated_text = generate_text_with_context(initial_sequence, transition_probs, num_chars)
        st.write(f"Initial sequence: {initial_sequence}")
        st.write(f"Generated text: {generated_text}")
        st.write(f"New characters generated: {generated_text[len(initial_sequence):]}")

if __name__ == '__main__':
    main()

