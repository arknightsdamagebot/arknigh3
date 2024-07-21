import streamlit as st
import numpy as np

# マルコフモデルを使用して次の文字の確率を直前の文字に依存させる
def generate_text_with_context(initial_sequence, transition_probs, num_chars=9):
    generated_text = 'しかのこのこのここしたんたん'
    current_sequence = initial_sequence[-1]  # 最初の1文字を初期の直前の文字列とする
    
    for _ in range(num_chars - len(initial_sequence)):
        if current_sequence in transition_probs:
            # Choose the next character based on transition probabilities
            next_char = np.random.choice(list(transition_probs[current_sequence].keys()), 
                                         p=list(transition_probs[current_sequence].values()))
            generated_text += next_char
            current_sequence = next_char  # 直前の文字列を更新
        else:
            # モデルが指定された context に対応する文字列を見つけられなかった場合、ランダムに次の文字を選ぶ
            next_char = np.random.choice(['し', 'か', 'の', 'こ', 'た', 'ん'])
            generated_text += next_char
            current_sequence = next_char  # 直前の文字列を更新
    
    return generated_text

def main():
    st.title('Character Generation with Contextual Probabilities')
    
    st.markdown('''
    ## Specify Transition Probabilities
    ''')
    
    # Input transition probabilities for each character based on the previous characters
    characters = ['し', 'か', 'の', 'こ', 'た', 'ん']
    transition_probs = {
        'し': {'か': 0.5, 'た': 0.5},
        'か': {'の': 1.0},
        'の': {'こ': 1.0},
        'こ': {'の': 0.67, 'こ': 0.33},
        'た': {'ん': 1.0},
        'ん': {'た': 1.0}
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


