import hog
from dice import four_sided, six_sided, make_test_dice

# dice = make_test_dice(1,2,3)
# print(dice())
# print(dice())
# print(dice())
# print(dice())
# print(dice())

print("hog roll_dice begin")
print(hog.roll_dice(1, make_test_dice(4, 2, 1, 3)))
print(hog.roll_dice(2, make_test_dice(4, 2, 1, 3)))
print(hog.roll_dice(3, make_test_dice(4, 2, 1, 3)))
print(hog.roll_dice(4, make_test_dice(4, 2, 1, 3)))
print("hog roll_dice end")
print("hog take_turn begin")
print(hog.take_turn(2, 0, make_test_dice(4, 6, 1)))
print(hog.take_turn(3, 0, make_test_dice(4, 6, 1)))
print(hog.take_turn(0, 35))
print(hog.take_turn(0, 71))
print(hog.take_turn(0, 7))
print(hog.take_turn(0, 0))
print(hog.take_turn(0, 9))
print(hog.take_turn(2, 0, make_test_dice(6)))
print(hog.take_turn(0, 50))
print("hog take_turn end")
print("hog select_dice begin")
print(hog.select_dice(4, 24) == four_sided)
print(hog.select_dice(16, 64) == four_sided)
print(hog.select_dice(0, 0) == four_sided)
print(hog.select_dice(50, 80) == four_sided)
print("hog select_dice end")
print("hog is_swap begin")
print(hog.is_swap(19, 91))
print(hog.is_swap(20, 40))
print(hog.is_swap(41, 14))
print(hog.is_swap(23, 42))
print(hog.is_swap(55, 55))
print(hog.is_swap(114, 41))  # We check the last two digits
print("hog is_swap end")
print("hog play begin")

hog.four_sided = make_test_dice(1)
hog.six_sided = make_test_dice(3)
always = hog.always_roll
print("should be: 106, 10. got: {0}".format(hog.play(always(5), always(3), score0=91, score1=10)))
print("should be: 1, 15. got: {0}".format(hog.play(always(5), always(5), goal=10)))
print("should be: 15, 51. got: {0}".format(hog.play(always(5), always(3), score0=36, score1=15, goal=50)))
# Swine swap applies to 3 digit scores
print("should be: 31, 113. got: {0}".format(hog.play(always(5), always(3), score0=98, score1=31)))
# Goal edge case
print("should be: 100, 20. got: {0}".format(hog.play(always(4), always(3), score0=88, score1=20)))
print("hog play end")
