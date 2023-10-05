from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 加载Iris数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# 使用线性核函数的SVM模型
svm_model = SVC(kernel='linear')

# 训练训练集和测试集
svm_model.fit(X_train, y_train)
train_predictions = svm_model.predict(X_train)
test_predictions = svm_model.predict(X_test)

# 输出训练集、测试集的准确度
train_accuracy = accuracy_score(y_train, train_predictions)
print(f"训练集准确度: {train_accuracy}")
test_accuracy = accuracy_score(y_test, test_predictions)
print(f"测试集准确度: {test_accuracy}")

# 输出分类结果
print("训练集分类结果:")
for i in range(len(X_train)):
    print(f"样本 {i+1}: 预测类别 {train_predictions[i]}, 实际类别 {y_train[i]}")
print("测试集分类结果:")
for i in range(len(X_test)):
    print(f"样本 {i+1}: 预测类别 {test_predictions[i]}, 实际类别 {y_test[i]}")
