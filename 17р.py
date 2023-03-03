import colorama
import inspect
type(colorama.Back)
type(colorama.Cursor)
type(colorama.Fore)
type(colorama.Style)

for method in dir(colorama.Back):
    print(method)
for method in dir(colorama.Cursor):
    print(method)
for method in dir(colorama.Fore):
    print(method)
for method in dir(colorama.Style):
    print(method)

print(inspect.ismodule(colorama.Back))
print(inspect.isclass(colorama.Back))
print(inspect.isfunction(colorama.Back))

print(inspect.ismodule(colorama.Cursor))
print(inspect.isclass(colorama.Cursor))
print(inspect.isfunction(colorama.Cursor))

print(inspect.ismodule(colorama.Fore))
print(inspect.isclass(colorama.Fore))
print(inspect.isfunction(colorama.Fore))

print(inspect.ismodule(colorama.Style))
print(inspect.isclass(colorama.Style))
print(inspect.isfunction(colorama.Style))