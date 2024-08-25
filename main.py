def main():
    file_contents = file_get_contents('books/frankenstein.txt')
    word_count = get_word_count(file_contents)
    character_counts = get_character_counts(file_contents)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{word_count} words found in the document')
    print('')
    for record in character_counts:
        print(f'character "{record['character']}" was found {record['count']} times')
    print('--- End report ---')

def get_word_count(content):
    return len(content.split())

def get_character_counts(content):
    counts = {}
    for character in content.lower():
        counts[character] = 1 if counts.get(character) == None else counts[character]+1
        
    result = []
    for character in counts:
        result.append({'character': character, 'count': counts[character]})
    
    result.sort(reverse=True, key=lambda dict: dict['count'])
    return filter(lambda record: record['character'].isalpha(), result)

def file_get_contents(file_name):
    with open(file_name) as file_handle:
        return file_handle.read()

main()