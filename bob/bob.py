# Bob answers 'Sure.' if you ask him a question.
# He answers 'Whoa, chill out!' if you yell at him.
# He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
# He says 'Fine. Be that way!' if you address him without actually saying anything.
# He answers 'Whatever.' to anything else.

from enum import Enum, auto


class BobResponses(Enum):
    Sure = "Sure."
    WhoaChill = "Whoa, chill out!"
    CalmDown = "Calm down, I know what I'm doing!"
    Fine = "Fine. Be that way!"
    Whatever = "Whatever."


class PhraseType(Enum):
    Question = auto()
    Yelling = auto()
    YellingQuestion = auto()
    NotSayingAnything = auto()
    AnythingElse = auto()


class PhraseToResponseMap:
    def __init__(self):
        self.Map = {}
        self.populate_map()

    def populate_map(self):
        self.Map[PhraseType.Question] = BobResponses.Sure
        self.Map[PhraseType.Yelling] = BobResponses.WhoaChill
        self.Map[PhraseType.YellingQuestion] = BobResponses.CalmDown
        self.Map[PhraseType.NotSayingAnything] = BobResponses.Fine
        self.Map[PhraseType.AnythingElse] = BobResponses.Whatever


class Phrase:
    def __init__(self, phrase):
        assert type(phrase) is str
        self.PhraseString = phrase
        self.PhraseType = None
        self.phrase_type_finder()

    def phrase_type_finder(self):
        if self.PhraseString.endswith("?"):
            if self.PhraseString.isupper():
                self.PhraseType = PhraseType.YellingQuestion
            else:
                self.PhraseType = PhraseType.Question

        elif self.PhraseString.isupper():
            self.PhraseType = PhraseType.Yelling

        elif self.PhraseString.isspace() or not self.PhraseString:
            self.PhraseType = PhraseType.NotSayingAnything

        # curse you test_ending_with_whitespace!! (shakes fist)
        elif "?" in self.PhraseString and not self.PhraseString.endswith("?"):
            self.PhraseString = self.PhraseString.rstrip()
            if self.PhraseString.endswith("?"):
                self.PhraseType = PhraseType.Question
            else:
                self.PhraseType = PhraseType.AnythingElse

        else:
            self.PhraseType = PhraseType.AnythingElse


def hey(phrase):
    phrase_object = Phrase(phrase)
    phrase_map = PhraseToResponseMap()

    assert phrase_object.PhraseType is not None
    assert bool(phrase_map.Map) is True    # ensure map dictionary is not empty
    return phrase_map.Map[phrase_object.PhraseType].value
