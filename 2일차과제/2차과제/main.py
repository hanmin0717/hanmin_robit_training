import matplotlib.pyplot as plt

#시각화할 독립적인 데이터 준비
languages = ['Python', 'Java', 'C++', 'JavaScript', 'HTML/CSS']
preference = [35, 25, 15, 15, 10]

#그래프 크기 설정
plt.figure(figsize=(6, 4))

#막대그래프 그리기
colors = ['#4f46e5', '#3b82f6', '#10b981', '#f59e0b', '#ef4444']
bars = plt.bar(languages, preference, color=colors, width=0.5)

#그래프 제목 및 축 이름 설정
plt.title('Most Popular Programming Languages', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Languages', fontsize=10, labelpad=10)
plt.ylabel('Preference (%)', fontsize=10, labelpad=10)
plt.ylim(0, 50) # y축의 범위를 0%부터 50%까지로 설정

#막대그래프 꼭대기에 실제 수치 표시해 주기
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2.0, 
        height + 1, 
        f'{height}%', 
        ha='center', 
        va='bottom', 
        fontweight='bold'
    )

#레이아웃을 예쁘게 다듬고 그래프 이미지 파일로 저장하기
plt.tight_layout()
plt.savefig('programming_languages_chart.png', dpi=150)
print("🎉 [과제 2] 그래프 이미지(programming_languages_chart.png)가 성공적으로 저장되었습니다!")
