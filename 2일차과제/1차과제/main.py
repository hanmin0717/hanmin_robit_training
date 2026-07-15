import csv
import json

try:
    students_path = "D:/과제1/students.csv"
    clean_path = "D:/과제1/clean_students.csv"
    summary_path = "D:/과제1/summary.json"

    #정제된 파일 만들기
    with open(students_path, "r", newline="", encoding="utf-8") as infile, \
         open(clean_path, "w", newline="", encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        header = next(reader)
        writer = csv.writer(outfile)
        writer.writerow(["name", "score"])

        for row in reader:
            try:
                name = row[0]
                score = int(row[1])
                if score < 0 or score > 100:
                    print(f"{name} 범위에 맞지 않는 입력입니다.")
                else:
                    print(name, score)
                    writer.writerow([f"{name}", f"{score}"])
            except ValueError:
                print(f"{name} 입력 방식에 맞지 않습니다.")

    #통계치 요약 json 파일 만들기
    with open(clean_path, "r", newline="", encoding="utf-8") as infile, \
         open(summary_path, "w", encoding="utf-8") as outfile:
        reader = csv.reader(infile)
        header = next(reader)
        count = 0
        total = 0
        max_val = -1

        for row in reader:
            name = row[0]
            score = int(row[1])
            count += 1
            total += score
            if score > max_val:
                max_val = score

        avg = round(total / count, 2) if count > 0 else 0
        data = {"인원수": count, "평균": avg, "최고점": max_val}
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    print("\n실행 성공")

except FileNotFoundError:
    print("D:/과제1 폴더에 students.csv 파일이 있는지 확인해 주세요.")
