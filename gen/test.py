from rules.search_replace import search_replace

print("Test tạo câu sai chính tả từ câu đúng:")

sent = input('Nhập câu đúng:')
sentences = search_replace.apply(sent, 1)
print('KẾT QUẢ')
print('--------------------------------------')
print('*' + sent, *sentences, sep='\n+')
print('--------------------------------------')
print('Tạo được %s câu lỗi' % len(sentences))
