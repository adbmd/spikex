import cProfile
import pstats
from pathlib import Path

import plac
import spacy
from spacy.matcher import Matcher
from srsly import read_jsonl
from tqdm import tqdm
from wasabi import msg

from ..matcher import REMatcher


@plac.annotations()
def profile(patterns_path, matcher_type: str = None):
    sample_doc = doc()
    matcher = (
        REMatcher() if matcher_type == "respacy" else Matcher(sample_doc.vocab)
    )
    matcher.add("Profile", patterns(patterns_path))
    # matcher.add("Profile", [[{"ORTH": {"NOT_IN": ["streptococco"]}, "OP": "*"}, {"ORTH": "diagrammatically"}]])
    cProfile.runctx(
        "matches(matcher, sample_doc)", globals(), locals(), "Profile.prof"
    )
    s = pstats.Stats("Profile.prof")
    msg.divider("Profile stats")
    s.strip_dirs().sort_stats("time").print_stats()


def matches(matcher, doc):
    print(sum([1 for _ in tqdm(matcher(doc))]))


def patterns(patterns_path):
    return list(read_jsonl(patterns_path))


def doc():
    return spacy.load("en_core_web_sm")(
        open(Path("resources").joinpath("sample.txt"), "r").read()
    )
