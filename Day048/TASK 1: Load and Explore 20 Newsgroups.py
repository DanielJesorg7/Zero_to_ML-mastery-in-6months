from sklearn.datasets import fetch_20newsgroups

categories = ['sci.space', 'rec.sport.hockey', 'talk.politics.guns']
data = fetch_20newsgroups(subset='train', categories=categories, remove=('headers', 'footers', 'quotes'), random_state=42)

print(len(data.data))
print(data.data[0][:200])
print(data.target[0])
print(data.target_names[data.target[0]])
