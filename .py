name1 = "listen"
name2 = ["silent", "happy", "enlist", "sad", "tinsel"]

def find_anagrams():
    anagrams = []
    for word in name2:
        if sorted(name1) == sorted(word):
            anagrams.append(word)
    return anagrams

print(find_anagrams())
