import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix,accuracy_score
import pickle

df = pd.read_csv('SMSSpamCollection',sep='\t',header=None,names=['label','text'])
df.head()


df.isnull().sum()

df['label'].value_counts()
x = df['text'] 
y = df['label']



bow = CountVectorizer(lowercase=True,token_pattern='(?u)\\b\\w\\w+\\w',stop_words='english')
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=99)

train = bow.fit_transform(x_train)
test = bow.transform(x_test)

bow.get_feature_names()[:10]

nb = MultinomialNB()
nb.fit(train,y_train)

y_pred = nb.predict(test)
train_pred = nb.predict(train)
train_acc = accuracy_score(y_train,train_pred)

accuracy = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)

#print(train_acc)
#print(accuracy)

'''
def prediction(text):
    data = [text]
    data = bow.transform(data)
    result = nb.predict(data)
    return result
print(prediction('How are you.'))

pickle.dump(nb,open('model.pkl','wb'))


#model = pickle.load(open('model.pkl','rb'))

#print(model.predict('How are you John'))
'''