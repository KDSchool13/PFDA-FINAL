

def main():
    with open("story.txt", 'r', encoding="utf-8") as adventure_story:
        story_snippet = adventure_story.readlines()[0:1].pop()
    print(f"{story_snippet}".strip('[]').rstrip())



if __name__ == "__main__":
    main()