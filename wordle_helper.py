import re
import nltk
from nltk.corpus import words

def ensure_nltk_words_downloaded():
    try:
        words.words()
    except LookupError:
        print("🔍 检测到缺少词库，正在下载 NLTK 的英文单词词典...")
        nltk.download('words')
        print("✅ 下载完成！")

def wordle_helper(pattern: str, include_letters: set[str], exclude_letters: set[str]) -> list[str]:
    pattern = pattern.lower()
    regex = '^' + pattern.replace('_', '.') + '$'
    regex_pattern = re.compile(regex)

    word_list = [w.lower() for w in words.words() if len(w) == len(pattern)]

    results = []
    for word in word_list:
        if not regex_pattern.match(word):
            continue
        if any(letter in word for letter in exclude_letters):
            continue
        if not all(letter in word for letter in include_letters):
            continue
        results.append(word)
    
    return results

def run_game():
    print("🎯 欢迎使用 Wordle 辅助工具（问答版）")

    while True:
        pattern = input("\n请输入模式字符串（使用 _ 表示未知字母，例如 _a_im_）： ").strip().lower()
        include_input = input("请输入必须包含的字母（用逗号分隔，例如 e,o）： ").strip().lower()
        exclude_input = input("请输入必须排除的字母（用逗号分隔，例如 t,s,r）： ").strip().lower()

        include_letters = set(include_input.split(',')) if include_input else set()
        exclude_letters = set(exclude_input.split(',')) if exclude_input else set()

        results = wordle_helper(pattern, include_letters, exclude_letters)

        if results:
            print(f"\n✅ 匹配到 {len(results)} 个单词：")
            for word in results:
                print(word)
        else:
            print("❌ 没有找到匹配的单词。")

        again = input("\n是否继续下一轮？(y/n)： ").strip().lower()
        if again != 'y':
            print("👋 感谢使用，再见！")
            break

def main():
    ensure_nltk_words_downloaded()
    run_game()

if __name__ == '__main__':
    main()
