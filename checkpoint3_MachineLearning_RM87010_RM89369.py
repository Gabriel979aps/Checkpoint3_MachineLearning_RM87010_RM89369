'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini
Atividade: Check Point 3 
Alunos 
Gabriel Anselmo Pires Dos Santos - RM87010
Vinicius Fernandes - RM89369 
'''
from sklearn import tree #importa o módulo "tree" do Sklearn Árvore de Decisão
features = [99, 139, 199], [89, 120, 160], [70, 110, 110], [65, 90, 90], [50, 80, 100], [40, 119, 170], [90, 100, 100], [60, 129, 159], [67, 124, 125],[97, 132, 109], [110, 150, 199], [100, 140, 180], [120, 145, 170], [121, 160, 198], [124, 180, 90], [126, 190, 100], [100, 169, 190], [111, 157, 113], [121, 190, 170], [105, 168, 192], [126, 200, 200], [190, 290, 248], [312, 241, 410], [431, 234, 210], [129, 265, 205], [137, 280, 341], [290, 345, 211], [138, 231, 230], [127, 201, 230], [154, 214, 294]
#labels = [Jejum, Pós_Sobrecarga, Casual]
#Glicose normal:  0  Tolerância à glicose diminuída:  1   Diagnóstico de Diabetes Mellitus: 2
labels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
classif = tree.DecisionTreeClassifier() #Classificador
classif.fit(features, labels)
Jejum = float(input("\n \033[1;32mDigite o valor da glicemia do paciente em jejum: "))
Pós_Sobrecarga = float(input("\033[1;33m Digite o valor da glicemia do paciente Pós-Sobrecarga: "))
Casual = float(input("\033[1;4;31m Digite o valor da glicema casual do paciente: "))
x = classif.predict([[Jejum, Pós_Sobrecarga, Casual]])
if x== 0:
    print ("\033[1;34m=-=" *14)
    print("\033[1;32mSua glicemia está normal!")
    print ("\033[1;34m=-=" *14)
    print('\033[1;4;31;43mAtenção! O diagnóstico apresentado não é definitivo, não deixe de consultar o seu médico!\033[m')
elif x== 1:
    print ("\033[1;34m=-=" *14)
    print("\033[1;33mVocê possui tolerância à glicose diminuída.")
    print("\033[1;34m=-=" *14)
    print('\033[1;4;31;43mAtenção! O diagnóstico apresentado não é definitivo, não deixe de consultar o seu médico!\033[m')

elif x== 2:
    print ("\033[1;34m=-=-=" *10)
    print("\033[1;4;31mVocê apresenta um diagnóstico de Diabetes Mellitus.")
    print ("\033[1;34m=-=-=" *10)
    print('\033[1;4;31;43mAtenção! O diagnóstico apresentado não é definitivo, não deixe de consultar o seu médico!\033[m')
