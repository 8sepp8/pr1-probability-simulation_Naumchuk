print(10*'=',"БЛОК 4. Варіант 4. Класифікатор ",10*'=')

total_objects = 5000
correct_count = 4600
error_count = 400

p_correct = correct_count / total_objects 
p_error = error_count / total_objects

print(f"Загальна кількість об'єктів: {total_objects}")
print(f"P(Correct) = {correct_count} / {total_objects} = {p_correct}")
print(f"P(Error)   = {error_count} / {total_objects} = {p_error}\n")

total = p_correct + p_error
print(f"Перевірка повної групи: P(Correct) + P(Error) = {total}")