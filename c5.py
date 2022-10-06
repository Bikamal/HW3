# Write a class called Wordplay. It should have a ﬁeld that holds a list of words.
#  The user of the class should pass the list of words they want to use to the class. 
# There should be the following methods:
# words_with_length(length) — returns a list of all the words of length length

# starts_with(s) — returns a list of all the words that start with s

# ends_with(s) — returns a list of all the words that end with s

# palindromes() — returns a list of all the palindromes in the list

# only(L) — returns a list of the words that contain only those letters in L

# avoids(L) — returns a list of the words that contain none of the letters in L

class Wordplay():
    def __init__(self,words):
        self.words=words

    def words_with_length(self):
        return('{}:{}'.format(w,len(w)) for w in b )
    def starts_with(self):
        return(w for w in b if w[0]=='s')
    def ends_with(self):
        return(w for w in b if w[-1]=='s')
    def palindromes():
        return(w for w in b if w[:]==w[: : -1])
    def only(L):
        return(w for w in b if 'l' in w)
    def avoids(L):
        return(w for w in b if 'l' not in w)

b=["some", "sale", "sunset", "lakes", "love", "lost", "tops"]
c= Wordplay(b)
print(c.words_with_length())
print(c.starts_with())
print(c.ends_with())
print(c.palindromes())
print(c.avoids())