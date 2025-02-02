def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or handle it in another way (raise exception, return a special value, etc.)

result = function(10, 0) 
print(result) #Output: 0