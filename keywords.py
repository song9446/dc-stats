import pickle
from krwordrank.word import summarize_with_keywords
from wordcloud import WordCloud
from soykeyword.lasso import LassoKeywordExtractor
from soynlp.noun import LRNounExtractor_v2
from soynlp.tokenizer import LTokenizer, MaxScoreTokenizer
from soyspacing.countbase import RuleDict, CountSpace


import matplotlib.pyplot as plt

space = CountSpace()
space.load_model('soyspacing.model', json_format=False)

with open('grouped.pickle', 'rb') as f:
    grouped = pickle.load(f)
with open('nouns.pickle', 'rb') as f:
    nouns = pickle.load(f)
with open('words.pickle', 'rb') as f:
    words = pickle.load(f)

scores = {w:s.score for w,s in nouns.items()}
#scores.update(
#    {w:s.cohesion_forward+scores.get(w, 0) for w,s in words.items()})
#print(scores["가"])
tokenizer = MaxScoreTokenizer(scores)
#tokenizer = LTokenizer(scores)
def keywords(doc):
    space.correct(doc)
    tokens = tokenizer.tokenize(doc, flatten=False)
    tokens = [subtoken[0] for token in tokens for subtoken in token if subtoken[3]>0.0]
    return tokens

#print(keywords("안녕하세요 반갑습니다. C++을전공하는 김덕배라고해요 ㅎㅎ자바 java좋아합니다. 좋다하세요. 위키"))

FONT_PATH = "fonts/IropkeBatangM.ttf" 
krwordrank_cloud = WordCloud(
    font_path = FONT_PATH,
    width = 400,
    height = 300,
    background_color="white"
)


def wordcloud_gen(wordrank, path):
    cloud = krwordrank_cloud.generate_from_frequencies(wordrank)
    plt.axis('off')
    plt.imshow(cloud)
    plt.savefig(path, bbox_inches='tight', dpi=1024)


grouped_keywords = [(i[0], keywords(" ".join(j["text"] for j in i[1]).replace("\n", " "))) for i in grouped[:100] if not i[0].startswith("ㅇㅇ")]

user_keywords = [i for _, i in grouped_keywords]
print(user_keywords[0])
exit(1)
users = [i for i, _ in grouped_keywords]

vectorizer = BaseVectorizer(
    verbose=True
)

#with open("keywords.pickle", "wb") as f:
#    pickle.dump(keywords, f)

#for author, wordrank in keywords:
#    wordcloud_gen(wordrank, "wordcloud/" + author + ".png")



