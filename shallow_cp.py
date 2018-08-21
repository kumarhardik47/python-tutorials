# ================================================================
# === ShallowCopy.py =============================================
# ================================================================
#
class Foo:
    def __init__(self, data):
        self._data = data

aa = Foo ('aaa')
bb = Foo ('bbb')

# The initial list has two elements containing 'aaa' and 'bbb'
OldList = [aa,bb]
print OldList[0]._data

# The shallow copy makes a new list pointing to the old elements
NewList = OldList[:]
print NewList[0]._data

# Updating one of the elements through the new list sees the
# change reflected when you access that element through the
# old list.
NewList[0]._data = 'xxx'
print OldList[0]._data

# Updating the new list to point to something new is not reflected
# in the old list.
NewList[0] = Foo ('ccc')
print NewList[0]._data
print OldList[0]._data
