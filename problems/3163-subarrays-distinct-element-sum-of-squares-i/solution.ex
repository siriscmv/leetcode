defmodule Solution do
  def sum_counts(nums) do
    Enum.reduce(1..length(nums), 0, fn i, acc ->
      acc + Enum.reduce(0..(length(nums)-i), 0, fn j, sub_acc ->
        sub_acc + Enum.count(Enum.uniq(Enum.slice(nums, j, i))) ** 2
      end)
    end)
  end
end
