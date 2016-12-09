# Starting with the code snippet below, write a regex that will match:
#
# All words that contain a v
# All words that contain a double-s
# All words that end with an e
# All words that contain an b, any character, then another b
# All words that contain an b, any number of characters (including zero), then another b
# All words that include all five vowels in order
# All words that only use the letters in regular expression (each letter can appear any number of times)
# All words that contain a double letter

import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    return [word for word in words if re.search(regex, word)]


regex = r"v"
print get_matching_words(regex)

# regex = r"ss"
# print get_matching_words(regex)

# regex = r"e$"
# print get_matching_words(regex)

# regex = r"b.b"
# print get_matching_words(regex)

# regex = r"b.*b"
# print get_matching_words(regex)

# regex = r"a.*e.*i.*o.*u"
# print get_matching_words(regex)

# regex = r"^[aegilnoprsux]"
# print get_matching_words(regex)

# regex = r"(.)\1"
# print get_matching_words(regex)
