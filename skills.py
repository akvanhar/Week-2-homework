# To work on the advanced problems, set to True
ADVANCED = False


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    #split the words into a string at whitespace
    list_of_words = input_string.split()
    dict_of_words = {}
    #add the words to the dictionary, increase count by 1 each time
    for word in list_of_words:
        if word in dict_of_words:
            dict_of_words[word] += 1
        else:
            dict_of_words[word] = 1

    return dict_of_words


def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """
    #holds one string still while comparing the other strings items to it.
    multiple_items = []
    for first_item in list1:
        for item in list2:
            if item == first_item:
                multiple_items.append(item)

    return multiple_items


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    #finds the intersection of two sets.

    set1 = set(list1)
    set2 = set(list2)

    common_items = set1 & set2

    return common_items


def get_sum_zero_pairs(input_list):
    """Given a list of numbers,
    return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    #create a set of lists to eliminate duplicates
    set_of_list = set(input_list)
    list_of_little_lists = []
    
    #for each number in a set of lists, create a mini-list to hold the pairs.
    for num in set_of_list:
        little_list = []
       
        #if a number is negative or zero, find it's positive pair, and append them both to the mini list
        if num <= 0 and abs(num) in set_of_list:
            little_list.append(num)
            little_list.append(abs(num))
        
        #as long as the little list isn't empty, append it to the long list.
        if little_list != []:
            list_of_little_lists.append(little_list)

    #sort the final list so that it's in order.
    final_list = sorted(list_of_little_lists)

    return final_list


def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed
    without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    #creates a dictionary to eliminate duplicates, returns a list of the keys.

    dict_of_list_words = {}
    for word in words:
        dict_of_list_words[word] = None

    no_duplicates_list = dict_of_list_words.keys()

    return no_duplicates_list

def encode(phrase):
    """Given a phrase, replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u". Return the encoded string.

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """

    #uses the replace method on the string to in turn replace the letters
    new_phrase = phrase.replace('e', 'p')
    new_phrase = new_phrase.replace('a', 'd')
    new_phrase = new_phrase.replace('t', 'o')
    new_phrase = new_phrase.replace('i', 'u')

    return new_phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    dictionary_of_word_lengths = {}
    for word in words:
        if len(word) not in dictionary_of_word_lengths.keys():
            dictionary_of_word_lengths[len(word)] = [word]
        else:
            dictionary_of_word_lengths[len(word)].append(word)

    list_of_lengths = []
    for key, value in dictionary_of_word_lengths.iteritems():
        list_of_lengths.append((key, value))

    return list_of_lengths

def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """
    pirate_dictionary = {
                        'sir': 'matey',
                        'hotel': 'fleabag inn',
                        'student': 'swabbie',
                        'boy': 'matey',
                        'madam': 'proud beauty',
                        'professor': 'foul blaggart',
                        'restaurant': 'galley',
                        'your': 'yer',
                        'excuse': 'arr',
                        'students': 'swabbies',
                        'are': 'be',
                        'lawyer': 'foul blaggart',
                        'the': 'th\'',
                        'restroom': 'head',
                        'my': 'me',
                        'hello': 'avast',
                        'is': 'be',
                        'man': 'matey'
                        }

    word_list = phrase.split()
    pirate_translation = []
    
    for word in word_list:
        if word in pirate_dictionary.keys():
            pirate_translation.append(pirate_dictionary[word])
        else:
            pirate_translation.append(word)

    pirate_translation = " ".join(pirate_translation)

    return pirate_translation


# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """
    #initiallize empty dictionary
    dictionary_of_letters = {}

    #for each letter in the dictionary, count how many times it occurse
    for letter in input_string:
        if letter not in dictionary_of_letters and letter.isalpha():
            dictionary_of_letters[letter] = 1
        elif letter.isalpha():
            dictionary_of_letters[letter] += 1
        else:
            continue

    #turn the dictionary list into tuples
    list_of_tuples = []

    for key, value in dictionary_of_letters.items():
        new_tuple = (value, key)
        list_of_tuples.append(new_tuple)

    #this is where I got stumped. I can find the max item, but I can't figure out how to do it if it's a tie.
    max_item = max(list_of_tuples)
    top_letter_list = []
    top_letter_list.append(max_item)
    for i in range(len(top_letter_list)):
        top_letter_list = [top_letter_list[i][1]]

    return top_letter_list


def adv_alpha_sort_by_word_length(words):
    """    
    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """
    #I ran out of time.

    return []


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
