import streamlit as st

def buturi(param1, param2):
    result = param1 - param2
    return result
def zyutu(param3, param4):
    result = param3 * (100 - param4) / 100
    return result
# ページのタイトルを設定
st.title("アークナイツダメージシミュレータ")

# 選択可能な項目のリストを作成
options = ["アンジェリーナ", "イフリータ", "エイヤフィヤトラ","エクシア","サリア","シルバーアッシュ","シージ","ホシグマ"]

# 選択された項目を受け取るセレクトボックスを表示
selected_option = st.selectbox("キャラクターを選択してください", options)

# 選択された項目に応じて対応する内容を表示
if selected_option == "アンジェリーナ":
    options = ["秘杖・急収束","秘杖・微粒子","秘杖・反重力"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "秘杖・急収束":
        st.write("攻撃力+110%")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
        param1 = st.number_input("攻撃力を入力してください", value=100)
        param1 = param1 * (1 + 1.1)
        if selected_option == "オリジムシ":
            param2 = 0
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "機動盾隊長":
            param2 = 300
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "軽装隊長":
            param2 = 500
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "重装隊長":
            param2 = 1000
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "遊撃隊盾兵隊長":
            param2 = 1500
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "「最後の蒸気騎士」":
            param2 = 2000
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
    elif selected_option == "秘杖・微粒子":
        st.write("通常攻撃の間隔を超大幅に短縮し、45%の攻撃力で術攻撃を行う")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
    elif selected_option == "秘杖・反重力":
        st.write("敵全員に反重力状態を付与し、攻撃範囲拡大、攻撃力+150%、敵最大5体を同時に攻撃")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
elif selected_option == "イフリータ":
    options = ["猛火","爆炎","灼獄"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "猛火":
        st.write("攻撃力+20%,攻撃速度+80")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
    elif selected_option == "爆炎": 
         st.write("次の通常攻撃時、敵に攻撃力の250%の術ダメージを与え、3秒間防御力-300、やけど状態にする")
         options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
         selectedselected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
    elif selected_option == "灼獄":
         st.write("攻撃範囲内、地面にいる敵全員に1秒ごとに攻撃力の140%の術ダメージを与え、術耐性-20")
         options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
         selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
elif selected_option == "エイヤフィヤトラ":
    options = ["二重詠唱","イグニッション","イラプション"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "二重詠唱":
        st.write("攻撃速度+60、2回目以降スキル使用時、更に攻撃力+60%")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
    elif selected_option == "イグニッション":
        st.write("次の通常攻撃時、敵に攻撃力の370%の術ダメージを与え、攻撃対象の周囲の敵に半分のダメージを与える。さらに6秒間術耐性-15%。")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
    elif selected_option == "イラプション":
        st.write("攻撃力+130%、攻撃範囲拡大、通常攻撃の間隔を大幅に短縮、ランダムで攻撃範囲内の敵最大6人を攻撃")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から術耐性の低い順です)", options)
elif selected_option == "エクシア":
    options = ["アサルトモード","バーストモード","オーバーロード"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "アサルトモード":
        st.write("次の通常攻撃時、3回連続で攻撃力の145%の物理ダメージを与える")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
        param1 = st.number_input("攻撃力を入力してください", value=100)
        param1 = param1 * (1 + 1.45)
        if selected_option == "オリジムシ":
            param2 = 0
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "機動盾隊長":
            param2 = 300
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "軽装隊長":
            param2 = 500
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "重装隊長":
            param2 = 1000
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "遊撃隊盾兵隊長":
            param2 = 1500
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "「最後の蒸気騎士」":
            param2 = 2000
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
    elif selected_option == "バーストモード":
        st.write("通常攻撃が攻撃力の125%での4回連続攻撃になる")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
        param1 = st.number_input("攻撃力を入力してください", value=100)
        param1 = param1 * (1 + 1.25)
        if selected_option == "オリジムシ":
            param2 = 0
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "機動盾隊長":
            param2 = 300
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "軽装隊長":
            param2 = 500
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "重装隊長":
            param2 = 1000
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "遊撃隊盾兵隊長":
            param2 = 1500
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "「最後の蒸気騎士」":
            param2 = 2000
            st.write(buturi(param1, param2) * 4)
    elif selected_option == "オーバーロード":
        st.write("通常攻撃が5回連続攻撃になり、攻撃間隔を短縮し、攻撃力が110%まで上昇")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
        param1 = st.number_input("攻撃力を入力してください", value=100)
        param1 = param1 * (1 + 1.1)
        if selected_option == "オリジムシ":
            param2 = 0
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "機動盾隊長":
            param2 = 300
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "軽装隊長":
            param2 = 500
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "重装隊長":
            param2 = 1000
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "遊撃隊盾兵隊長":
            param2 = 1500
            if buturi(param1,param2) <= param1 * 0.05:
                st.write(param1 * 0.05)
            else st.write(buturi(param1,param2))
        elif selected_option == "「最後の蒸気騎士」":
            param2 = 2000
            st.write(buturi(param1, param2) * 5)
elif selected_option == "シルバーアッシュ":
    options = ["強撃γ","雪境生存戦略","真銀斬"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "強撃γ":
        st.write("次の通常攻撃時、攻撃力が290%まで上昇")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
    elif selected_option == "雪境生存戦略":
        st.write("発動する度初期状態と次の状態とが切り替わる：攻撃範囲縮小、防御力+100%、1秒ごとにHPが最大値の6.0%回復")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
    elif selected_option == "真銀斬":
        st.write("防御力-70%、攻撃力+200%、攻撃範囲拡大、敵最大6体を同時に攻撃(近距離攻撃と見なす)")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
elif selected_option == "シージ":
    options = ["突撃指令γ","スカイスマッシュ","スカルクラッシュ"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "突撃指令γ":
        st.write("所持コスト+12")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
    elif selected_option == "スカイスマッシュ":
        st.write("次の通常攻撃時、所持コスト+3、周囲の敵全員に攻撃力の340%の物理ダメージを与える")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
    elif selected_option == "スカルクラッシュ":
        st.write("攻撃間隔が延長し、攻撃時攻撃力が380%まで上昇、更に40%の確率で攻撃した敵を1.5秒間スタンさせる")
elif selected_option == "ホシグマ":
    options = ["戦意高揚","荊棘","般若"]
    selected_option = st.selectbox("スキルを選択してください", options)
    if selected_option == "戦意高揚":
        st.write("防御力+80%、攻撃力+40%")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
    elif selected_option == "荊棘":
        st.write("防御力+30%、攻撃される度自身の攻撃力の100%の物理ダメージで敵に反撃する")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
    elif selected_option == "般若":
        st.write("攻撃力+140%、防御力+90%、盾を回転し、前方1マスにいる敵全員を同時に攻撃")
        options = ["オリジムシ","機動盾隊長","軽装隊長","重装隊長","遊撃隊盾兵隊長","「最後の蒸気騎士」"]
        selected_option = st.selectbox("敵を選択してください(上から防御力の低い順です)", options)
