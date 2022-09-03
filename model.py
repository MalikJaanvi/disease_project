import pandas as pd
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv(r"C:\Users\Swastik Computers\PycharmProjects\disease_project\diseaseDataset.csv")

target = df['Disease']
df = df.drop('Disease',axis=1)
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
targetdf = pd.DataFrame(target)
target_encoded = encoder.fit_transform(target)
targetdf["target_encoded"] = pd.DataFrame(target_encoded)

df['Sym1'] = encoder.fit_transform(df['Symptom1'])
df['Symp2'] = encoder.fit_transform(df['Symptom2'])
df['Symp3'] = encoder.fit_transform(df['Symptom3'])
df['Symp4'] = encoder.fit_transform(df['Symptom4'])
df['Symp5'] = encoder.fit_transform(df['Symptom5'])

data = df.drop(['Symptom1','Symptom2',"Symptom3","Symptom4","Symptom5"],axis=1)

def traning_model(symp1,sym2,sym3,sym4,sym5):

    s1 = df.loc[df['Symptom1'] == symp1,'Sym1'].iloc[0]
    s2 = df.loc[df['Symptom2'] == sym2,'Symp2'].iloc[0]
    s3 = df.loc[df['Symptom3'] == sym3,'Symp3'].iloc[0]
    s4 = df.loc[df['Symptom4'] == sym4,'Symp4'].iloc[0]
    s5 = df.loc[df['Symptom5'] == sym5,'Symp5'].iloc[0]

    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(data,target)

    decision_tree_model = DecisionTreeClassifier()
    svm_model = SVC()

    tree_trained_model=decision_tree_model.fit(X_train,y_train)
    svm_trained_model = svm_model.fit(X_train,y_train)


    tree_result = decision_tree_model.predict([[s1,s2,s3,s4,s5]])
    svm_result =  svm_model.predict([[s1,s2,s3,s4,s5]])

    tree_accuracy = tree_trained_model.score(X_train,y_train)
    svm_accuracy = svm_trained_model.score(X_train,y_train)

    print(tree_accuracy)
    print(svm_accuracy)
    result = tree_result
    if(svm_accuracy>tree_accuracy):
        result = svm_result
        # print(result)
    return result[0]
# traning_model()