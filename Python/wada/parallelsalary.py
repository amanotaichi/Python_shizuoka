import func_salary
import sys
args = sys.argv

#複数の給与を入力
salarys = [int(arg) for arg in args[1:]]

#計算して表示
for salary in salarys:
    price,tax = func_salary.calcsalary(salary)
    print("給与:"+str(salary)+"、支給額:"+str(price)+"、税額:"+str(tax))
