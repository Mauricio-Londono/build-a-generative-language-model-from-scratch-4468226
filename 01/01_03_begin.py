
import random
from string import punctuation
from collections import defaultdict


class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    def train(self, text):
        tokens = self._tokenize(text)
        for i, token in enumerate(tokens):
            if (len(tokens)-1) == i:
                break
            self.graph[token].append(tokens[i+1])            

    def generate(self, prompt, length=20):
        # get the lask token from the prompt
        current = self._tokenize(prompt)[-1]
        # initialize the output
        output = prompt
        for i in range(length):
            # look up the options in the graph dictionary
            options = self.graph.get(current, [])
            if not options:
                continue
            # use random.choice method to pick a current option
            current = random.choice(options)
            # add the random choice to the output string
            print(f" {current}")
        return output
    
text = """
There's a fire starting in my heart
Reaching a fever pitch and it's bringing me out the dark
Finally, I can see you crystal clear
Go ahead and sell me out and I'll lay your shit bare
See how I'll leave with every piece of you
Don't underestimate the things that I will do
There's a fire starting in my heart
Reaching a fever pitch, and it's bringing me out the dark

The scars of your love remind me of us
They keep me thinkin' that we almost had it all
The scars of your love, they leave me breathless
I can't help feeling

We could've had it all (You're gonna wish you never had met me)
Rolling in the deep (Tears are gonna fall, rolling in the deep)
You had my heart inside of your hand (You're gonna wish you never had met me)
And you played it to the beat (Tears are gonna fall, rolling in the deep)

Baby, I have no story to be told
But I've heard one on you, now I'm gonna make your head burn
Think of me in the depths of your despair
Make a home down there, as mine sure won't be shared
See Adele Live
Get tickets as low as $126

You might also like
When I Was Your Man
Bruno Mars
FUK SUMN
¥$, Kanye West & Ty Dolla $ign
Set Fire to the Rain
Adele

(You're gonna wish you never had met me) The scars of your love remind me of us
(Tears are gonna fall, rolling in the deep) They keep me thinkin' that we almost had it all
(You're gonna wish you never had met me) The scars of your love, they leave me breathless
(Tears are gonna fall, rolling in the deep) I can't help feeling

We could've had it all (You're gonna wish you never had met me)
Rolling in the deep (Tears are gonna fall, rolling in the deep)
You had my heart inside of your hand (You're gonna wish you never had met me)
And you played it to the beat (Tears are gonna fall, rolling in the deep)
Could've had it all
Rolling in the deep
You had my heart inside of your hand
But you played it with a beating

Throw your soul through every open door (Ooh woah, oh)
Count your blessings to find what you look for (Woah)
Turn my sorrow into treasured gold (Ooh woah, oh)
You'll pay me back in kind and reap just what you sow

(You're gonna wish you never had met me)
We could've had it all (Tears are gonna fall, rolling in the deep)
We could've had it all, yeah (You're gonna wish you never had met me)
It all, it all, it all (Tears are gonna fall, rolling in the deep)

We could've had it all (You're gonna wish you never had met me)
Rolling in the deep (Tears are gonna fall, rolling in the deep)
You had my heart inside of your hand (You're gonna wish you never had met me)
And you played it to the beat (Tears are gonna fall, rolling in the deep)
Could've had it all (You're gonna wish you never had met me)
Rolling in the deep (Tears are gonna fall, rolling in the deep)
You had my heart inside of your hand (You're gonna wish you never had met me)
But you played it, you played it, you played it
You played it to the beat
"""

chain = MarkovChain()
chain.train(text)
sample_prompt = "I have"
print(chain.generate(sample_prompt))
result = chain.generate(sample_prompt)