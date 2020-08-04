#GPA計算プログラム
name = input('あなたの名前を教えてください')
grade = input('あなたの学年を教えてください')
try :
   take_class = input('受講した科目数を打ち込んでください')
   class_count = int(take_class)
   input_S = input('Sをとった科目数を打ち込んでください')
   count_S = int(input_S)
   input_A = input('Aをとった科目数を打ち込んでください')
   count_A = int(input_A)
   input_B = input('Bをとった科目数を打ち込んでください')
   count_B = int(input_B)
   input_C = input('Cをとった科目数を打ち込んでください')
   count_C = int(input_C)
   input_D = input('Dをとった科目数を打ち込んでください')
   count_D = int(input_D)

   if class_count == count_S + count_A + count_B + count_C + count_D :
      total_point = count_S * 4 + count_A * 3 + count_B * 2 + count_C * 1 + count_D * 0
      GPA = total_point / class_count
      print(f"金沢工業大学{grade}年生の{name}さん、あなたのGPAは{GPA}です。")

      import matplotlib.pyplot as plt
      data = [count_S,count_A,count_B,count_C,count_D]
      grade = ["S","A","B","C","D"]
      data_gpa=[GPA]
      grade_gpa=["GPA"]

      plt.subplot(1,2,1)
      plt.bar(grade,data)
      plt.title("GPA")
      plt.xlabel("grade")
      plt.ylabel("class")

      plt.subplot(1,2,2)
      plt.bar(grade_gpa,data_gpa)
      plt.title("GPA")
      plt.xlabel("grade")
      plt.ylim(0,4)

      plt.show()

   else : 
      print('講義数と成績の数が一致していません')

except ValueError:
   print('数字での入力のみを受け付けています')
except:
   print("数字で入力してください")