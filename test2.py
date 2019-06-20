def table_things(**kwargs):
     for name, value in kwargs.items():
         print '{0} = {1}'.format(name, value)
         print kwargs,type(kwargs)

table_things(apple = 'fruit', cabbage = 'vegetable')
