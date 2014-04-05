happy_words = '''
Absolutely	Abundant	Accept
Acclaimed	Accomplishment	Achievement
Action	Active	Activist
Acumen	Adjust	Admire
Adopt	Adorable	Adored
Adventure	Affirmation	Affirmative
Affluent	Agree	Airy
Alive	Alliance	Ally
Alter	Amaze	Amity
Animated	Answer	Appreciation
Approve	Aptitude	Artistic
Assertive	Astonish	Astounding
Astute	Attractive	Authentic
Basic	Beaming	Beautiful
Believe	Benefactor	Benefit
Bighearted	Blessed	Bliss
Bloom	Bountiful	Bounty
Brave	Bright	Brilliant
Bubbly	Bunch	Burgeon
Calm	Care	Celebrate
Certain	Change	Character
Charitable	Charming	Cheer
Cherish	Clarity	Classy
Clean	Clever	Closeness
Commend	Companionship	Complete
Comradeship	Confident	Connect
Connected	Constant	Content
Conviction	Copious	Core
Coupled	Courageous	Creative
Cuddle	Cultivate	Cure
Curious	Cute	Dazzling
Delight	Direct	Discover
Distinguished	Divine	Donate
Each Day	Eager	Earnest
Easy	Ecstasy	Effervescent
Efficient	Effortless	Electrifying
Elegance	Embrace	Encompassing
Encourage	Endorse	Energized
Energy	Enjoy	Enormous
Enthuse	Enthusiastic	Entirely
Essence	Established	Esteem
Everyday	Everyone	Excited
Exciting	Exhilarating	Expand
Explore	Express	Exquisite
Exultant	Faith	Familiar
Family	Famous	Feat
Fit	Flourish	Fortunate
Fortune	Freedom	Fresh
Friendship	Full	Funny
Gather	Generous	Genius
Genuine	Give	Glad
Glow	Good	Gorgeous
Grace	Graceful	Gratitude
Green	Grin	Group
Grow	Handsome	Happy
Harmony	Healed	Healing
Healthful	Healthy	Heart
Hearty	Heavenly	Helpful
Here	Highest Good	Hold
Holy	Honest	Honor
Hug	I affirm	I allow
I am willing	I am.	I Can
I choose	I create	I follow
I know	I know, without a doubt	I make
I realize	I take action	I trust
Idea	Ideal	Imaginative
Increase	Incredible	Independent
Ingenious	Innate	Innovate
Inspire	Instantaneous	Instinct
Intellectual	Intelligence	Intuitive
Inventive	Joined	Jovial
Joy	Jubilation	Keen
Key	Kind	Kiss
Knowledge	Laugh	Leader
Learn	Legendary	Let Go
Light	Lively	Love
Loveliness	Lucidity	Lucrative
Luminous	Maintain	Marvelous
Master	Meaningful	Meditate
Mend	Metamorphosis	Mind-Blowing
Miracle	Mission	Modify
Motivate	Moving	Natural
Nature	Nourish	Nourished
Novel	Now	Nurture
Nutritious	One	Open
Openhanded	Optimistic	Paradise
Party	Peace	Perfect
Phenomenon	Pleasure	Plenteous
Plentiful	Plenty	Plethora
Poise	Polish	Popular
Positive	Powerful	Prepared
Pretty	Principle	Productive
Project	Prominent	Prosperous
Protect	Proud	Purpose
Quest	Quick	Quiet
Ready	Recognize	Refinement
Refresh	Rejoice	Rejuvenate
Relax	Reliance	Rely
Remarkable	Renew	Renowned
Replenish	Resolution	Resound
Resources	Respect	Restore
Revere	Revolutionize	Rewarding
Rich	Robust	Rousing
Safe	Secure	See
Sensation	Serenity	Shift
Shine	Show	Silence
Simple	Sincerity	Smart
Smile	Smooth	Solution
Soul	Sparkling	Spirit
Spirited	Spiritual	Splendid
Spontaneous	Still	Stir
Strong	Style	Success
Sunny	Support	Sure
Surprise	Sustain	Synchronized
Team	Thankful	Therapeutic
Thorough	Thrilled	Thrive
Today	Together	Tranquil
Transform	Triumph	Trust
Truth	Unity	Unusual
Unwavering	Upbeat	Value
Vary	Venerate	Venture
Very	Vibrant	Victory
Vigorous	Vision	Visualize
Vital	Vivacious	Voyage
Wealthy	Welcome	Well
Whole	Wholesome	Willing
Wonder	Wonderful	Wondrous
Xanadu	Yes	Yippee
Young	Youth	Youthful
Zeal	Zest	Zing
Zip
'''

positive = happy_words.split()
for i in range(len(positive)):
	positive[i] = positive[i].lower()

sad_words = '''
A
abysmal
adverse
alarming
angry
annoy
anxious
apathy
appalling
atrocious
awful
B
bad
banal
barbed
belligerent
bemoan
beneath
boring
broken
C
callous
can't
clumsy
coarse
cold
cold-hearted
collapse
confused
contradictory
contrary
corrosive
corrupt
crazy
creepy
criminal
cruel
cry
cutting
D
dead
decaying
damage
damaging
dastardly
deplorable
depressed
deprived
deformed
D Cont.
deny
despicable
detrimental
dirty
disease
disgusting
disheveled
dishonest
dishonorable
dismal
distress
don't
dreadful
dreary
E
enraged
eroding
evil
F
fail
faulty
fear
feeble
fight
filthy
foul
frighten
frightful
G
gawky
ghastly
grave
greed
grim
grimace
gross
grotesque
gruesome
guilty
H
haggard
hard
hard-hearted
harmful
hate
hideous
homely
horrendous
horrible
hostile
hurt
hurtful
I
icky
ignore
ignorant
ill
immature
imperfect
impossible
inane
inelegant
infernal
injure
injurious
insane
insidious
insipid
J
jealous
junky
L
lose
lousy
lumpy
M
malicious
mean
menacing
messy
misshapen
missing
misunderstood
moan
moldy
monstrous
N
naive
nasty
naughty
negate
negative
never
no
nobody
nondescript
nonsense
not
noxious
O
objectionable
odious
offensive
old
oppressive
P
pain
perturb
pessimistic
petty
plain
poisonous
poor
prejudice
Q
questionable
quirky
quit
R
reject
renege
repellant
reptilian
repulsive
repugnant
revenge
revolting
rocky
rotten
rude
ruthless
S
sad
savage
scare
scary
scream
severe
shoddy
shocking
sick
sickening
sinister
slimy
smelly
sobbing
sorry
spiteful
sticky
stinky
stormy
stressful
stuck
stupid
substandard
suspect
suspicious
T
tense
terrible
terrifying
threatening
U
ugly
undermine
unfair
unfavorable
unhappy
unhealthy
unjust
unlucky
unpleasant
upset
unsatisfactory
unsightly
untoward
unwanted
unwelcome
unwholesome
unwieldy
unwise
upset
vice
vicious
vile
villainous
vindictive
wary
weary
wicked
woeful
worthless
wound
yell
yucky
zero
'''

negative = sad_words.split()
for i in range(len(negative)):
	negative[i] = negative[i].lower()


