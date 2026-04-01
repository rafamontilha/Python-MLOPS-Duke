import utils
import program.items

print(dir(utils))
#print(utils.str_to_bool('yes'))
#print(utils.str_to_int('3.14'))

from utils import str_to_bool, str_to_int
print(str_to_bool('yes'))
print(str_to_int('3.14'))


print(program.items.some_function())

