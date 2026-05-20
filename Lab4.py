file = open('text_test.txt', 'r', encoding='utf-8')
text = file.read()
file.close()

# print(text)

words = text.split() 

stop_words = [
    'и', 'в', 'на', 'с', 'к', 'у', 'за', 'по', 'из', 'от', 'до', 'для', 'без', 'через',
    'о', 'об', 'под', 'над', 'перед', 'между', 'при', 'про', 'ради', 'сквозь',
    'а', 'но', 'да', 'или', 'либо', 'то', 'же', 'ведь', 'вот', 'вон', 'лишь',
    'бы', 'б', 'не', 'ни', 'даже', 'уже', 'ещё', 'только', 'почти',
    'что', 'чтобы', 'потому', 'так', 'также', 'тоже', 'зато', 'однако',
    'который', 'которая', 'которое', 'которые', 'которых', 'котором', 'которому',
    'этот', 'эта', 'это', 'эти', 'этого', 'этому', 'этим', 'этими', 'этих',
    'весь', 'вся', 'всё', 'все', 'всех', 'всем', 'всеми',
    'мой', 'твоя', 'твое', 'твои', 'твоего', 'твоему', 'твоим', 'твоей',
    'его', 'её', 'ее', 'их', 'наш', 'наша', 'наше', 'наши', 'ваш', 'ваша', 'ваше', 'ваши',
    'кто', 'какой', 'какая', 'какое', 'какие', 'какого', 'какому', 'чей',
    'так', 'там', 'тут', 'здесь', 'туда', 'сюда', 'оттуда', 'куда', 'откуда',
    'очень', 'слишком', 'немного', 'немало', 'много', 'мало',
    'можно', 'нельзя', 'нужно', 'надо', 'нужное',
    
    'the', 'a', 'an', 'and', 'or', 'but', 'so', 'for', 'nor', 'yet',
    'of', 'to', 'in', 'for', 'on', 'with', 'without', 'by', 'at', 'into',
    'through', 'during', 'including', 'without', 'against', 'among',
    'is', 'am', 'are', 'was', 'were', 'be', 'been', 'being',
    'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing',
    'will', 'would', 'shall', 'should', 'may', 'might', 'must', 'could',
    'i', 'you', 'he', 'she', 'it', 'we', 'they', 'them', 'us',
    'my', 'your', 'his', 'her', 'its', 'our', 'their',
    'this', 'that', 'these', 'those', 'there', 'their',
    'some', 'any', 'no', 'every', 'each', 'all', 'both', 'neither', 'either',
    'what', 'which', 'who', 'whom', 'whose',
    'not', 'very', 'just', 'from', 'up', 'down', 'off', 'over', 'under',
    'again', 'further', 'then', 'once', 'here', 'when', 'where', 'why', 'how',
    'each', 'few', 'more', 'most', 'other', 'some', 'such', 'than', 'too',
    'only', 'own', 'same', 'so', 'than', 'too', 'very',
    's', 't', 'm', 'll', 've', 're', 'd', 'o', '—'
]

freq = {}

for word in words:
    word_clean = word.lower()
    if word_clean in stop_words:
        continue
    if word_clean in freq:
        freq[word_clean] += 1
    else:
        freq[word_clean] = 1

# print(freq)

for i in freq:
    print(i, "->", freq[i], "\n")