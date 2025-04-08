import re
import nltk
from nltk.corpus import words


def ensure_nltk_words_downloaded():
    try:
        words.words()
    except LookupError:
        print("🔍 Downloading NLTK word list...")
        nltk.download("words")
        print("✅ Download complete!")


# 中英文提示定义
LANG = {
    "en": {
        "welcome": "🎯 Welcome to the Wordle Helper (Interactive Mode)",
        "pattern": "Enter your pattern (use _ for unknown letters, e.g. _a_im_): ",
        "include": "Enter required letters (comma-separated, e.g. e,o): ",
        "exclude": "Enter excluded letters (comma-separated, e.g. t,s,r): ",
        "results": "✅ Found {n} matching words:",
        "no_results": "❌ No matching words found.",
        "again": "Would you like to try another round? (y/n): ",
        "bye": "👋 Thanks for using Wordle Helper. Goodbye!",
        "lang_prompt": "Select language / 选择语言: (en/zh): ",
    },
    "zh": {
        "welcome": "🎯 欢迎使用 Wordle 单词助手（交互模式）",
        "pattern": "请输入模式字符串（使用 _ 表示未知字母，例如 _a_im_）：",
        "include": "请输入必须包含的字母（用逗号分隔，例如 e,o）：",
        "exclude": "请输入必须排除的字母（用逗号分隔，例如 t,s,r）：",
        "results": "✅ 匹配到 {n} 个单词：",
        "no_results": "❌ 没有找到匹配的单词。",
        "again": "是否继续下一轮？(y/n)：",
        "bye": "👋 感谢使用，再见！",
        "lang_prompt": "选择语言 / Select language: (zh/en)：",
    },
}


def wordle_helper(
    pattern: str, include_letters: set[str], exclude_letters: set[str]
) -> list[str]:
    pattern = pattern.lower()
    regex = "^" + pattern.replace("_", ".") + "$"
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


def run_game(lang="en"):
    msg = LANG[lang]
    print(msg["welcome"])

    while True:
        pattern = input(f"\n{msg['pattern']}").strip().lower()
        include_input = input(msg["include"]).strip().lower()
        exclude_input = input(msg["exclude"]).strip().lower()

        include_letters = set(include_input.split(",")) if include_input else set()
        exclude_letters = set(exclude_input.split(",")) if exclude_input else set()

        results = wordle_helper(pattern, include_letters, exclude_letters)

        if results:
            print(f"\n{msg['results'].format(n=len(results))}")
            for word in results:
                print(word)
        else:
            print(msg["no_results"])

        again = input(f"\n{msg['again']}").strip().lower()
        if again != "y":
            print(msg["bye"])
            break


def main():
    ensure_nltk_words_downloaded()

    lang = input(LANG["en"]["lang_prompt"]).strip().lower()
    if lang not in LANG:
        lang = "en"  # fallback
    run_game(lang)


if __name__ == "__main__":
    main()
