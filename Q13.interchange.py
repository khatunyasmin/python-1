lst = eval(input("enter a value:")) #[23, 100, 54, 56, 98]

#interchanging the first and last element
lst[0], lst[-1] = lst[-1], lst[0]
print(lst)
