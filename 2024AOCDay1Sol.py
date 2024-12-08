
left_list = [
    35446, 46314, 33933, 83974, 98207, 38488, 95930, 52767, 16477, 14481, 29083, 36158, 61387,
  #(addrest)
]

right_list = [
    18696, 66062, 83974, 34443, 12657, 57125, 81859, 12657, 53659, 84757, 51122, 15438, 10295, 
    # (add rest)
]


left_sorted = sorted(left_list)
right_sorted = sorted(right_list)


total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

print(f"Total Distance: {total_distance}")
