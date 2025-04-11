import streamlit as st
from wordle_helper import wordle_helper, ensure_nltk_words_downloaded

def main():
    st.set_page_config(
        page_title="Wordle Helper",
        page_icon="🎯",
        layout="centered"
    )

    # 确保 NLTK 词库已下载
    ensure_nltk_words_downloaded()

    st.title("🎯 Wordle Helper")
    st.markdown("### 帮助你解决 Wordle 游戏的小助手")

    # 用户输入区域
    pattern = st.text_input(
        "输入模式",
        help="使用下划线(_)表示未知字母，例如: _a_im_"
    ).strip().lower()

    col1, col2 = st.columns(2)
    with col1:
        include_input = st.text_input(
            "必须包含的字母",
            help="用逗号分隔，例如: e,o"
        ).strip().lower()
    
    with col2:
        exclude_input = st.text_input(
            "必须排除的字母",
            help="用逗号分隔，例如: t,s,r"
        ).strip().lower()

    if pattern:
        include_letters = set(include_input.split(",")) if include_input else set()
        exclude_letters = set(exclude_input.split(",")) if exclude_input else set()

        # 移除空字符串
        include_letters.discard("")
        exclude_letters.discard("")

        results = wordle_helper(pattern, include_letters, exclude_letters)

        if results:
            st.success(f"找到 {len(results)} 个匹配的单词")
            st.write("可能的单词：")
            # 使用列表显示结果
            st.write(", ".join(results))
        else:
            st.error("没有找到匹配的单词")

    # 添加使用说明
    with st.expander("使用说明"):
        st.markdown("""
        1. **模式输入**：使用下划线(_)表示未知字母，已知字母直接输入
        2. **必须包含的字母**：输入你知道单词中包含的字母，用逗号分隔
        3. **必须排除的字母**：输入你确定不在单词中的字母，用逗号分隔
        
        例如：
        - 如果你知道第二个字母是'a'，其他未知，输入：`_a___`
        - 如果你知道单词包含'e'和'o'，在"必须包含的字母"中输入：`e,o`
        - 如果你确定单词不含't'、's'和'r'，在"必须排除的字母"中输入：`t,s,r`
        """)

if __name__ == "__main__":
    main()