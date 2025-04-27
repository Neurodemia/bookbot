import sys
from stats import get_num_words
from stats import character_count
from stats import sort_report

def get_book_text(book_path):
	with open(book_path) as f:
		book_content = f.read()
	return book_content

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]
	book_content = get_book_text(book_path)
	word_count = get_num_words(book_content)
	chars = character_count(book_content)
	report = sort_report(chars)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {word_count} total words")
	print("--------- Character Count -------")
	for char_data in report:
        	if char_data["char"].isalpha():
        	    	print(f"{char_data['char']}: {char_data['num']}")
	print("============= END ===============")

main()
