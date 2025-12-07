ll = []
ll.append("Rajan")
ll.append(22)

print(ll)
print(len(ll))
ll.append("Hello")
ll.insert(1, "World")
print(ll)
ll.remove(22)  # Remove the integer before sorting
ll.sort()
print(ll)
ll.sort(reverse=True)
print(ll)
ll.reverse()
print(ll)
del ll[1]
print(ll)
ll.pop()
print(ll)