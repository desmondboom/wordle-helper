import streamlit as st
from wordle_helper import wordle_helper, ensure_nltk_words_downloaded, LANG


def main():
    st.set_page_config(page_title="Wordle Helper", page_icon="🎯", layout="centered")

    ensure_nltk_words_downloaded()

    if "language" not in st.session_state:
        st.session_state.language = "en"

    title_col, lang_col = st.columns([4, 1])
    with title_col:
        st.title("🎯 Wordle Helper")
    with lang_col:
        selected_lang = st.selectbox(
            "Language / 语言",
            options=["zh", "en"],
            index=0 if st.session_state.language == "zh" else 1,
            key="lang_select",
        )
        if selected_lang != st.session_state.language:
            st.session_state.language = selected_lang

    msg = LANG[st.session_state.language]
    st.markdown(msg["welcome"])

    pattern = st.text_input(msg["pattern"], help=msg["pattern"]).strip().lower()

    col1, col2 = st.columns(2)
    with col1:
        include_input = (
            st.text_input(msg["include"], help=msg["include"]).strip().lower()
        )

    with col2:
        exclude_input = (
            st.text_input(msg["exclude"], help=msg["exclude"]).strip().lower()
        )

    search_button = st.button("🔍 Search / 搜索")

    # st.divider()
    results_container = st.container()

    if pattern and search_button:
        include_letters = set(include_input.split(",")) if include_input else set()
        exclude_letters = set(exclude_input.split(",")) if exclude_input else set()

        include_letters.discard("")
        exclude_letters.discard("")

        results = wordle_helper(pattern, include_letters, exclude_letters)

        with results_container:
            if results:
                st.markdown("### 🎯 " + msg["results"].format(n=len(results)))

                # 使用 Streamlit 的 columns API 创建 3 列网格
                # 将结果按 3 列分组
                cols_per_row = 3
                rows = [
                    results[i : i + cols_per_row]
                    for i in range(0, len(results), cols_per_row)
                ]

                for row in rows:
                    cols = st.columns(cols_per_row)
                    for i, word in enumerate(row):
                        with cols[i]:
                            # 使用 st.container 创建卡片效果
                            with st.container():
                                st.markdown(
                                    f"""
                                    <div style="
                                        background-color: #f0f2f6;
                                        border: 1px solid #e0e0e0;
                                        border-radius: 8px;
                                        padding: 16px;
                                        text-align: center;
                                        font-size: 18px;
                                        font-weight: bold;
                                        color: #262730;
                                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                                        margin: 4px 0;
                                    ">
                                        {word.upper()}
                                    </div>
                                    """,
                                    unsafe_allow_html=True,
                                )

            else:
                st.error(msg["no_results"])

    st.divider()

    with st.expander(msg.get("help_title", "Help / 使用说明")):
        if st.session_state.language == "zh":
            st.markdown(
                """
            1. **模式输入**：使用下划线(_)表示未知字母，已知字母直接输入
            2. **必须包含的字母**：输入你知道单词中包含的字母，用逗号分隔
            3. **必须排除的字母**：输入你确定不在单词中的字母，用逗号分隔
            
            例如：
            - 如果你知道第二个字母是'a'，其他未知，输入：`_a___`
            - 如果你知道单词包含'e'和'o'，在"必须包含的字母"中输入：`e,o`
            - 如果你确定单词不含't'、's'和'r'，在"必须排除的字母"中输入：`t,s,r`
            """
            )
        else:
            st.markdown(
                """
            1. **Pattern Input**: Use underscore (_) for unknown letters, directly input known letters
            2. **Required Letters**: Enter letters you know are in the word, comma-separated
            3. **Excluded Letters**: Enter letters you know are not in the word, comma-separated
            
            Examples:
            - If you know the second letter is 'a' and others are unknown, enter: `_a___`
            - If you know the word contains 'e' and 'o', enter: `e,o` in Required Letters
            - If you know the word doesn't contain 't', 's', and 'r', enter: `t,s,r` in Excluded Letters
            """
            )


if __name__ == "__main__":
    main()
