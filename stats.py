def get_num_words(book_content):
	word_count = len(book_content.split())
	return word_count

def character_count(book_content):
	chars = {}
	conformed = book_content.lower()
	for char in conformed:
		if char in chars:
			chars[char] += 1
		else:
			chars[char] = 1
	return chars

def sort_report(chars):
	report_content = []
	for char, count in chars.items():
		report_content.append({"char": char, "num": count})

	def sort_on(report_order):
		return report_order["num"]

	report_content.sort(reverse=True, key=sort_on)

	return report_content
