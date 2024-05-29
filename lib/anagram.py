class Anagram:
    def __init__(self, word):
        """
        Initialize the Anagram object with a word.
        
        Parameters:
        word (str): The word to find anagrams for.
        """
        # Store the word in lowercase to make the comparison case-insensitive.
        self.word = word.lower()
        # Store the sorted version of the word, which will be used for comparison.
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, words_list):
        """
        Find all anagrams of the initialized word in the provided list of words.
        
        Parameters:
        words_list (list): List of words to check for anagrams.
        
        Returns:
        list: List of words that are anagrams of the initialized word.
        """
        # Iterate through each word in the list, sort it, and compare it with the sorted initialized word.
        # Return a list of words that are anagrams.
        return [word for word in words_list if ''.join(sorted(word.lower())) == self.sorted_word]
