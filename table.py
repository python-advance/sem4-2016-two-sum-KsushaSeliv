def deco(func):
  import functools
  import time
  import math

  @functools.wraps(func)
  def inner(*args, **kwargs):
      start_timer = time.time()
      result = func(*args, **kwargs)
      end_timer = time.time()
      delta_timer = end_timer - start_timer
      print(f"Время выполнения порграммы {func.__name__} заняло: {delta_timer}")
      return result
  return inner

@deco
def two_sum_brute(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[j] == target - nums[i]:
               return [i, j]

@deco
def two_sum(nums, target):
    dict = {}
    for index, value in enumerate(nums):
        diff = target - value
        if diff in dict:
            return [dict[diff], index]
        dict[value] = index


if __name__ == "__main__":
  print(two_sum_brute([2, 7, 11, 15, 6, 3], 9))
  assert two_sum_brute([2, 7, 11, 15, 6, 3], 9) == [0, 1], 'способ 1'
  print(two_sum([2, 7, 11, 15, 6, 3], 9))
  assert two_sum([2, 7, 11, 15, 6, 3], 9) == [0, 1], 'способ 2'
