n, m = map(int, input().split())
colors_ani = set()
colors_borya = set()
for _ in range(n):
    colors_ani.add(int(input()))
for _ in range(m):
    colors_borya.add(int(input()))
common_colors = sorted(colors_ani.intersection(colors_borya))
unique_colors_ani = sorted(colors_ani.difference(colors_borya))
unique_colors_borya = sorted(colors_borya.difference(colors_ani))
print(len(common_colors))
print(*common_colors)
print(len(unique_colors_ani))
print(*unique_colors_ani)
print(len(unique_colors_borya))
print(*unique_colors_borya)