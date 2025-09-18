initial_weight = float(input())
for year in range(1, 11):
    earth_weight = initial_weight + 0.5 * year
    moon_weight = earth_weight * 0.165
    print(f"{year} {earth_weight:.1f} {moon_weight:.3f}")# 在这个文件里编写代码
