n = int(input())
knownlangs = set()
anyknownlangs = set()

for _ in range(n):
    n = int(input())
    knowns = set()
    for _ in range(n):
        language = input()
        knowns.add(language)
    if not knownlangs:
        knownlangs = knowns.copy()
    else:
        knownlangs &= knowns
    anyknownlangs |= knowns
print(len(knownlangs))

for language in sorted(knownlangs):
    print(language)
print(len(anyknownlangs))
for language in sorted(anyknownlangs):
    print(language)