# ब्राह्मिक - A Transliteration Tool

This project is for accurate cross-script tranliteration. It contains a bunch of
software, as well as dictionaries and other mappings that help in it.

Primary focus is on English(Language=English, Script=Latin) to
Devnagri(Language=English, Script=Devnagri).

Many Indian languages share a common alphabet, ka, kha, ga, but written
differently eg Hindi (क, ख, ग) vs Telgu (క, ఖ, గ). I think its the same sounds,
but written differently, and has different unicode characters assigned. I think
we may have been able to make do with same unicode characters codes and
different fonts too as well. That would have made this part of this project
redundent, but since its not so, this project can help you transliterate
Hindi(Language=Hindi, Script=Devnagri) to Telgu(Language=Hindi, Script=Devnagri)
or Telgu(Language=Telgu, Script=Telgu) to Hindi(Language=Telgu,
Script=Devnagri).


## Motivation

I am trying to create a transliteration thing.

Basically imagine a tool for my mom. She knows how to read and write Hindi well,
but does not know English. Now I want her to learn English, but learning English
means she has to learn two things simultaneously, the english language and
grammer/words etc, and reading/writing things.

Or consider one of my friend, whose domestic language is Telgu, but his wife
knows Hindi. Now she is learning Telgu, but making her learn a foreign looking
క, ఖ, గ, when its really क, ख, ग, is a wastage. She can already read and write
her name in Hindi, but Telgu speakers can read it. This tool will help her auto
transliterate to Telgu so Telgu speakers can read it, as well it will
transliterate Telgu texts like website content etc to Devnagri, so she can read
it (understanding it would be a different matter, she will have to learn the
words etc).

If you look at kids, they first learn grammar/words and then once they are
fluent they learn reading/writing.

If I can make reading writing easy for her, learning would be divided in two
separate phases, she can focus on words/grammar and not worry about
reading/writing in beginning.

Eventual goal is to write a browser extension, which transliterates everything,
but before that we need a basic transliteration library. And ब्राह्मिक is an
effort towards that.


## Another Motivation - Replace IPA with Devnagri

Wikipedia uses
[IPA](http://en.wikipedia.org/wiki/International_Phonetic_Alphabet), but IPA is
not capable of accurately representing sounds in all languages, devnagri has
bigger set of sounds. Also nearly no one can fluently read IPA (try reading
/ˈnjuːtən/, best of luck!), where as there are upwards of a 100 million who can
read devnagri. So this project also aims to replace IPA and other similar
schemes, eg the one used by [CMU](http://en.wikipedia.org/wiki/Arpabet)(try
reading B AA1 R B ER0 Z), or the one [Google uses](https://ww w.dropbox.com/s/yu
73fuf022psrq3/Screenshot%202015-04-20%2016.11.51.png?dl=0)(looks like Khuṇ
k̄hxbkhuṇ).

You see all these approaches are wrong. IPA, Arpabet, That Thing That Google
Uses, they are all reinventing crap after crap. They can't agree with each
other. Google chose to ignore both IPA and Arpabet, which are both standards
with significant volume of work done in. Because it was crap. But they only
created another crap, that nobody other than Google will use, and may be when
Apple realizes that Oh there are non english speakers in the world, they will
invent their own crap ignoring Googla/IPA/Arbabet. This must end.

One can argue that no English speaker will find "रीपॉसैटारी"" more readable than
"repository", but they will not find the IPA/Arpabet readable either. Google's
scheme would work for them though. But that is an English centric world view,
and the problem of "I can not pronounce English properly" is not a English
speaking world problem, but a problem of people with non English as a native
language. For them Google/IPA/Arpabet would be as hard as Devnagri, but at least
for close to billion people, they already know Devnagri (or some other [Brahmic
Script](http://en.wikipedia.org/wiki/Brahmic_scripts)).

May be world will never support, may be this will only make the job of Indians
better, so what, that alone is a worthy goal.


## Approach

Currently I am using [cmudict](https://github.com/cmusphinx/cmudict), which
lists English pronounciation code for some 40-50K words. I am [mapping those
codes to Devnagri](https://github.com/amitu/brahmic/blob/master/cmu.py#L25-L68).



## Result So Far

The second half of this page is auto transliterated with zero manual correction
using this tool.

Look at [the gist](https://gist.github.com/amitu/47e8438321d0b9e4b3cd) which
shows the conversion of 1000 most frequently used words in English language. It
is only 70-80% accurate so far. Even the accuracy rate is not known, as I am not
that great in English pronunciation myself.

## Help Me Please!

Fork the [gist](https://gist.github.com/amitu/47e8438321d0b9e4b3cd), and correct
it, and send me a mail. Or may be just mark the lines you think are wrong.

Any help with fixing cmu.py is highly appreciated too.

----

# ब्राह्मिक - ऐ Transliteration टूल

दिस प्रॉजेक्ट इस फॉर ऐक्य्रैट क्रॉस-स्क्रिप्ट tranliteration. इट कैन्टेऽन्स ऐ बान्च आव
सॉफ्ट्वेर, ऐस वेल ऐस डिक्शैनेरीस ऐन्ड आदर mappings दैट हेल्प इन इट.

प्राय्मेरी फोकैस इस ऑन इंग्ग्लिश(लैंग्ग्वैज=इंग्ग्लिश, स्क्रिप्ट=लैटैन) टू
Devnagri(लैंग्ग्वैज=इंग्ग्लिश, स्क्रिप्ट=Devnagri).

मेनी इन्डीऐन लैंग्ग्वैजैस शेर ऐ कॉमैन ऐल्फैबेट, कॉ, kha, गॉ, बाट रिटैन
डिफ्रैन्ट्ली eg हिन्डी (क, ख, ग) वीएस Telgu (క, ఖ, గ). आय थिंग्क इट्स दै सेऽम साव्न्ड्स,
बाट रिटैन डिफ्रैन्ट्ली, ऐन्ड हैस डिफ्रैन्ट unicode कैरैक्ट्र्स ऐसाय्न्ड. आय थिंग्क
वी मेऽ हैव बिन एऽबैल टू मेऽक डू विद सेऽम unicode कैरैक्ट्र्स कोड्स ऐन्ड
डिफ्रैन्ट फॉन्ट्स टू ऐस वेल. दैट वूड हैव मेऽड दिस पॉर्ट आव दिस प्रॉजेक्ट
redundent, बाट सिन्स इट्स नॉट सो, दिस प्रॉजेक्ट कैन हेल्प यू transliterate
हिन्डी(लैंग्ग्वैज=हिन्डी, स्क्रिप्ट=Devnagri) टू Telgu(लैंग्ग्वैज=हिन्डी, स्क्रिप्ट=Devnagri)
ऑर Telgu(लैंग्ग्वैज=Telgu, स्क्रिप्ट=Telgu) टू हिन्डी(लैंग्ग्वैज=Telgu,
स्क्रिप्ट=Devnagri).


## मोटैवेऽशैन

आय ऐम ट्रायिंग टू क्रीएऽट ऐ transliteration थिंग.

बेऽसिक्ली इमैजैन ऐ टूल फॉर माय मॉम. शी नोस हाव टू रेड ऐन्ड राय्ट हिन्डी वेल,
बाट डास नॉट नो इंग्ग्लिश. नाव आय वॉन्ट हर टू ल्र्न इंग्ग्लिश, बाट ल्र्निंग इंग्ग्लिश
मीन्स शी हैस टू ल्र्न टू थिंग्स साय्मैल्टेऽनीऐस्ली, दै इंग्ग्लिश लैंग्ग्वैज ऐन्ड
ग्रैम्र/वर्ड्स एट्सेट्रै, ऐन्ड रीडिंग/राय्टिंग थिंग्स.

ऑर कैन्सिड्र वान आव माय फ्रेन्ड, हूस डैमेस्टिक लैंग्ग्वैज इस Telgu, बाट हिस वाय्फ
नोस हिन्डी. नाव शी इस ल्र्निंग Telgu, बाट मेऽकिंग हर ल्र्न ऐ फॉरैन लूकिंग
క, ఖ, గ, वेन इट्स रिली क, ख, ग, इस ऐ wastage. शी कैन आल्रेडी रेड ऐन्ड राय्ट
हर नेऽम इन हिन्डी, बाट Telgu स्पीक्र्स कैन रेड इट. दिस टूल विल हेल्प हर ऑटो
transliterate टू Telgu सो Telgu स्पीक्र्स कैन रेड इट, ऐस वेल इट विल
transliterate Telgu टेक्स्ट्स लाय्क वेब्साय्ट कॉन्टेन्ट एट्सेट्रै टू Devnagri, सो शी कैन रेड
इट (ऽन्ड्र्स्टैन्डिंग इट वूड बी ऐ डिफ्रैन्ट मैट्र, शी विल हैव टू ल्र्न दै
वर्ड्स एट्सेट्रै).

इफ यू लूक ऐट किड्स, देऽ फ्र्स्ट ल्र्न ग्रैम्र/वर्ड्स ऐन्ड देन वान्स देऽ ऑर
फ्लूऐन्ट देऽ ल्र्न रीडिंग/राय्टिंग.

इफ आय कैन मेऽक रीडिंग राय्टिंग ईसी फॉर हर, ल्र्निंग वूड बी डिवाय्डैड इन टू
सेप्रेऽट फेऽसैस, शी कैन फोकैस ऑन वर्ड्स/ग्रैम्र ऐन्ड नॉट वरी ऐबाव्ट
रीडिंग/राय्टिंग इन बिगिनिंग.

ऐवेन्चुऐल गोल इस टू राय्ट ऐ ब्राव्स्र इक्स्टेन्शैन, विच transliterates एव्रीथिंग,
बाट बिफॉर दैट वी नीड ऐ बेऽसिक transliteration लाय्ब्रेरी. ऐन्ड ब्राह्मिक इस ऐन
एफ्र्ट टैवॉर्ड्स दैट.


## ऐनादर मोटैवेऽशैन - रीप्लेऽस IPA विद Devnagri

विकीपीडीऐ यूसैस
[IPA](http://एन.विकीपीडीऐ.ऑर्ग/विकी/International_Phonetic_Alphabet), बाट IPA इस
नॉट केऽपैबैल आव ऐक्य्रैट्ली रेप्रिसेन्टिंग साव्न्ड्स इन ऑल लैंग्ग्वैजैस, devnagri हैस
बिग्र सेट आव साव्न्ड्स. ऑल्सो निर्ली नो वान कैन फ्लूऐन्ट्ली रेड IPA (ट्राय रीडिंग
/ˈnjuːटीəएन/, बेस्ट आव लाक!), वेर ऐस देर ऑर आप्वर्ड्स आव ऐ 100 मिल्यैन हू कैन
रेड devnagri. सो दिस प्रॉजेक्ट ऑल्सो एऽम्स टू रीप्लेऽस IPA ऐन्ड आदर सिमैल्र
स्कीम्स, eg दै वान यूस्ड बाय [सीएम्यू](http://एन.विकीपीडीऐ.ऑर्ग/विकी/Arpabet)(ट्राय
रीडिंग बी AA1 ऑर बी ER0 सी), ऑर दै वान [गूगैल यूसैस](https://ww डाबैल्यु.dropbox.कॉम/एस/यू
73fuf022psrq3/Screenshot%202015-04-20%2016.11.51.png?dl=0)(लूक्स लाय्क Khuṇ
केऽ̄hxbkhuṇ).

यू सी ऑल दीस ऐप्रोचैस ऑर रॉंग. IPA, Arpabet, दैट थिंग दैट गूगैल
यूसैस, देऽ ऑर ऑल रीइन्वेन्टिंग क्रैप ऐफ्ट्र क्रैप. देऽ कैन'टी ऐग्री विद ईच
आदर. गूगैल चोस टू इग्नॉर बोथ IPA ऐन्ड Arpabet, विच ऑर बोथ स्टैन्ड्र्ड्स
विद सैग्निफिकैन्ट वॉल्युम आव वर्क डान इन. बिकॉस इट वॉस क्रैप. बाट देऽ ओन्ली
क्रीएऽटैड ऐनादर क्रैप, दैट नोबॉडी आदर दैन गूगैल विल यूस, ऐन्ड मेऽ बी वेन
ऐपैल रीऐलाय्सिस दैट ओ देर ऑर नॉन इंग्ग्लिश स्पीक्र्स इन दै वर्ल्ड, देऽ विल
इन्वेन्ट देर ओन क्रैप इग्नॉरिंग Googla/IPA/Arbabet. दिस मास्ट एन्ड.

वान कैन ऑर्ग्यु दैट नो इंग्ग्लिश स्पीक्र विल फाय्न्ड "रीपॉसैटारी"" मॉर रीडैबैल दैन
"रीपॉसैटारी", बाट देऽ विल नॉट फाय्न्ड दै IPA/Arpabet रीडैबैल ईदर. गूगैल'एस
स्कीम वूड वर्क फॉर देम दो. बाट दैट इस ऐन इंग्ग्लिश centric वर्ल्ड व्यू,
ऐन्ड दै प्रॉब्लैम आव "आय कैन नॉट प्रैनाव्न्स इंग्ग्लिश प्रॉप्र्ली" इस नॉट ऐ इंग्ग्लिश
स्पीकिंग वर्ल्ड प्रॉब्लैम, बाट ऐ प्रॉब्लैम आव पीपैल विद नॉन इंग्ग्लिश ऐस ऐ नेऽटिव
लैंग्ग्वैज. फॉर देम गूगैल/IPA/Arpabet वूड बी ऐस हॉर्ड ऐस Devnagri, बाट ऐट लीस्ट
फॉर क्लोस टू बिल्यैन पीपैल, देऽ आल्रेडी नो Devnagri (ऑर साम आदर [Brahmic
स्क्रिप्ट](http://एन.विकीपीडीऐ.ऑर्ग/विकी/Brahmic_scripts)).

मेऽ बी वर्ल्ड विल नेव्र सैपॉर्ट, मेऽ बी दिस विल ओन्ली मेऽक दै जॉब आव इन्डीऐन्स
बेट्र, सो वाट, दैट ऐलोन इस ऐ वर्दी गोल.


## ऐप्रोच

क्रैन्ट्ली आय ऐम यूसिंग [cmudict](https://github.कॉम/cmusphinx/cmudict), विच
लिस्ट्स इंग्ग्लिश pronounciation कोड फॉर साम 40-50K वर्ड्स. आय ऐम [मैपिंग दोस
कोड्स टू Devnagri](https://github.कॉम/amitu/brahmic/ब्लॉब/मैस्ट्र/सीएम्यू.py#L25-L68).



## रिसाल्ट सो फॉर

दै सेकैन्ड हैफ आव दिस पेऽज इस ऑटो transliterated विद सिरो मैन्युऐल क्रेक्शैन
यूसिंग दिस टूल.

लूक ऐट [दै जिस्ट](https://जिस्ट.github.कॉम/amitu/47e8438321d0b9e4b3cd) विच
शोस दै कैन्व्र्सैन आव 1000 मोस्ट फ्रीक्वैन्ट्ली यूस्ड वर्ड्स इन इंग्ग्लिश लैंग्ग्वैज. इट
इस ओन्ली 70-80% ऐक्य्रैट सो फॉर. ईविन दै ऐक्य्रैसी रेऽट इस नॉट नोन, ऐस आय ऐम नॉट
दैट ग्रेऽट इन इंग्ग्लिश प्रोन्ऽन्सीएऽशैन माय्सेल्फ.

## हेल्प मी प्लीस!

फॉर्क दै [जिस्ट](https://जिस्ट.github.कॉम/amitu/47e8438321d0b9e4b3cd), ऐन्ड क्रेक्ट
इट, ऐन्ड सेन्ड मी ऐ मेऽल. ऑर मेऽ बी जास्ट मॉर्क दै लाय्न्स यू थिंग्क ऑर रॉंग.

एनी हेल्प विद फिक्सिंग सीएम्यू.py इस हाय्ली ऐप्रीशीएऽटिड टू.

----

# బ्రाహ्మिక - ఐ Transliteration టूల

దिస ప्రॉజेక्ట ఇస ఫॉర ఐక्య्రैట క्రॉస-స्క्రिప्ట tranliteration. ఇట కैన्టेऽన्స ఐ బाన्చ आవ
సॉఫ्ట्వेర, ఐస వेల ఐస డिక्శैనेరीస ఐన्డ आదర mappings దैట హेల्ప ఇన ఇట.

ప्రाయ्మेరी ఫोకैస ఇస ఆన ఇंగ्గ्లिశ(లैंగ्గ्వैజ=ఇंగ्గ्లिశ, స्క्రिప्ట=లैటैన) టू
Devnagri(లैंగ्గ्వैజ=ఇंగ्గ्లिశ, స्క्రिప्ట=Devnagri).

మेనी ఇన्డीఐన లैंగ्గ्వैజैస శेర ఐ కॉమैన ఐల्ఫैబेట, కॉ, kha, గॉ, బाట రिటैన
డिఫ्రैన्ట्లी eg హिన्డी (క, ఖ, గ) వीఏస Telgu (క, ఖ, గ). आయ థिंగ्క ఇట्స దै సेऽమ సाవ्న्డ्స,
బाట రिటैన డिఫ्రैన्ట्లी, ఐన्డ హैస డिఫ्రैన्ట unicode కैరैక्ట्ర्స ఐసाయ्న्డ. आయ థिंగ्క
వी మेऽ హैవ బिన ఏऽబैల టू మेऽక డू వिద సेऽమ unicode కैరैక्ట्ర्స కोడ्స ఐన्డ
డिఫ्రैన्ట ఫॉన्ట्స టू ఐస వेల. దैట వूడ హैవ మेऽడ దिస పॉర्ట आవ దिస ప्రॉజेక्ట
redundent, బाట సिన्స ఇట्స నॉట సो, దिస ప्రॉజेక्ట కैన హेల्ప యू transliterate
హिన्డी(లैंగ्గ्వैజ=హिన्డी, స्క्రिప्ట=Devnagri) టू Telgu(లैंగ्గ्వैజ=హिన्డी, స्క्రिప्ట=Devnagri)
ఆర Telgu(లैंగ्గ्వैజ=Telgu, స्క्రिప्ట=Telgu) టू హिన्డी(లैंగ्గ्వैజ=Telgu,
స्క्రिప्ట=Devnagri).


## మोటैవेऽశैన

आయ ఐమ ట्రाయिंగ టू క्రीఏऽట ఐ transliteration థिंగ.

బेऽసिక्లी ఇమैజैన ఐ టूల ఫॉర మाయ మॉమ. శी నोస హाవ టू రेడ ఐన्డ రाయ्ట హिన्డी వेల,
బाట డाస నॉట నो ఇंగ्గ्లिశ. నाవ आయ వॉన्ట హర టू ల्ర्న ఇंగ्గ्లिశ, బाట ల्ర्నिंగ ఇंగ्గ्లिశ
మीన्స శी హैస టू ల्ర्న టू థिंగ्స సाయ्మैల्టेऽనीఐస्లी, దै ఇंగ्గ्లिశ లैंగ्గ्వैజ ఐన्డ
గ्రैమ्ర/వర्డ्స ఏట्సेట्రै, ఐన्డ రीడिंగ/రाయ्టिंగ థिंగ्స.

ఆర కैన्సिడ्ర వाన आవ మाయ ఫ्రेన्డ, హूస డैమेస्టिక లैंగ्గ्వैజ ఇస Telgu, బाట హिస వाయ्ఫ
నोస హिన्డी. నाవ శी ఇస ల्ర्నिंగ Telgu, బाట మेऽకिंగ హర ల्ర्న ఐ ఫॉరैన లूకिंగ
క, ఖ, గ, వेన ఇట्స రिలी క, ఖ, గ, ఇస ఐ wastage. శी కैన आల्రेడी రेడ ఐన्డ రाయ्ట
హర నेऽమ ఇన హिన्డी, బाట Telgu స्పीక्ర्స కैన రेడ ఇట. దिస టूల వिల హेల्ప హర ఆటो
transliterate టू Telgu సो Telgu స्పीక्ర्స కैన రेడ ఇట, ఐస వेల ఇట వिల
transliterate Telgu టेక्స्ట्స లाయ्క వेబ्సाయ्ట కॉన्టेన्ట ఏట्సेట्రै టू Devnagri, సो శी కैన రेడ
ఇట (ऽన्డ्ర्స्టैన्డिंగ ఇట వूడ బी ఐ డिఫ्రैన्ట మैట्ర, శी వिల హैవ టू ల्ర्న దै
వర्డ्స ఏట्సेట्రै).

ఇఫ యू లूక ఐట కिడ्స, దेऽ ఫ्ర्స्ట ల्ర्న గ्రैమ्ర/వర्డ्స ఐన्డ దेన వाన्స దेऽ ఆర
ఫ्లूఐన्ట దेऽ ల्ర्న రीడिंగ/రाయ्టिंగ.

ఇఫ आయ కैన మेऽక రीడिंగ రाయ्టिंగ ఈసी ఫॉర హర, ల्ర्నिंగ వूడ బी డिవाయ्డैడ ఇన టू
సेప्రेऽట ఫेऽసैస, శी కैన ఫोకैస ఆన వర्డ्స/గ्రैమ्ర ఐన्డ నॉట వరी ఐబाవ्ట
రीడिंగ/రाయ्టिंగ ఇన బिగिనिंగ.

ఐవेన्చुఐల గोల ఇస టू రाయ्ట ఐ బ्రाవ्స्ర ఇక्స्టेన्శैన, వिచ transliterates ఏవ्రीథिंగ,
బाట బिఫॉర దैట వी నीడ ఐ బेऽసिక transliteration లाయ्బ्రेరी. ఐన्డ బ्రाహ्మिక ఇస ఐన
ఏఫ्ర्ట టैవॉర्డ्స దैట.


## ఐనाదర మोటैవेऽశैన - రीప्లेऽస IPA వिద Devnagri

వिకीపीడीఐ యूసैస
[IPA](http://ఏన.వिకीపीడीఐ.ఆర्గ/వिకी/International_Phonetic_Alphabet), బाట IPA ఇస
నॉట కेऽపैబैల आవ ఐక्య्రैట्లी రेప्రिసेన्టिंగ సाవ्న्డ्స ఇన ఆల లैंగ्గ्వैజैస, devnagri హैస
బिగ्ర సेట आవ సाవ्న्డ्స. ఆల्సो నिర्లी నो వाన కैన ఫ्లूఐన्ట्లी రेడ IPA (ట्రाయ రीడिंగ
/ˈnjuːటीəఏన/, బेస्ట आవ లाక!), వेర ఐస దेర ఆర आప्వర्డ्స आవ ఐ ౧౦౦ మिల्యैన హू కैన
రेడ devnagri. సो దिస ప्రॉజेక्ట ఆల्సो ఏऽమ्స టू రीప्లेऽస IPA ఐన्డ आదర సिమैల्ర
స्కीమ्స, eg దै వाన యूస्డ బाయ [సीఏమ्యू](http://ఏన.వिకीపीడीఐ.ఆర्గ/వिకी/Arpabet)(ట्రाయ
రीడिंగ బी AA౧ ఆర బी ER౦ సी), ఆర దै వाన [గूగैల యूసैస](https://ww డाబैల्యु.dropbox.కॉమ/ఏస/యू
౭౩fuf౦౨౨psrq౩/Screenshot%౨౦౨౦౧౫-౦౪-౨౦%౨౦౧౬.౧౧.౫౧.png?dl=౦)(లूక्స లाయ्క Khuṇ
కेऽ̄hxbkhuṇ).

యू సी ఆల దीస ఐప्రोచैస ఆర రॉंగ. IPA, Arpabet, దैట థिंగ దैట గूగैల
యूసैస, దेऽ ఆర ఆల రीఇన्వेన्టिंగ క्రैప ఐఫ्ట्ర క्రैప. దेऽ కैన'టी ఐగ्రी వिద ఈచ
आదర. గूగैల చोస టू ఇగ्నॉర బोథ IPA ఐన्డ Arpabet, వिచ ఆర బोథ స्టैన्డ्ర्డ्స
వिద సैగ्నिఫिకैన्ట వॉల्యुమ आవ వర्క డाన ఇన. బिకॉస ఇట వॉస క्రैప. బाట దेऽ ఓన्లी
క्రीఏऽటैడ ఐనाదర క्రैప, దैట నोబॉడी आదర దैన గूగैల వिల యूస, ఐన्డ మेऽ బी వेన
ఐపैల రीఐలाయ्సिస దैట ఓ దेర ఆర నॉన ఇंగ्గ्లिశ స्పीక्ర्స ఇన దै వర्ల्డ, దेऽ వिల
ఇన्వेన्ట దेర ఓన క्రैప ఇగ्నॉరिंగ Googla/IPA/Arbabet. దिస మाస्ట ఏన्డ.

వाన కैన ఆర्గ्యु దैట నो ఇंగ्గ्లिశ స्పीక्ర వिల ఫाయ्న्డ "రीపॉసैటाరी"" మॉర రीడैబैల దैన
"రीపॉసैటाరी", బाట దेऽ వिల నॉట ఫाయ्న्డ దै IPA/Arpabet రीడैబैల ఈదర. గूగैల'ఏస
స्కीమ వूడ వర्క ఫॉర దेమ దो. బाట దैట ఇస ఐన ఇंగ्గ्లिశ centric వర्ల्డ వ्యू,
ఐన्డ దै ప्రॉబ्లैమ आవ "आయ కैన నॉట ప्రैనाవ्న्స ఇंగ्గ्లिశ ప्రॉప्ర्లी" ఇస నॉట ఐ ఇंగ्గ्లिశ
స्పीకिंగ వర्ల्డ ప्రॉబ्లैమ, బाట ఐ ప्రॉబ्లैమ आవ పीపैల వिద నॉన ఇंగ्గ्లिశ ఐస ఐ నेऽటिవ
లैंగ्గ्వैజ. ఫॉర దेమ గूగैల/IPA/Arpabet వूడ బी ఐస హॉర्డ ఐస Devnagri, బाట ఐట లीస्ట
ఫॉర క्లोస టू బिల्యैన పीపैల, దेऽ आల्రेడी నो Devnagri (ఆర సाమ आదర [Brahmic
స्క्రिప्ట](http://ఏన.వिకीపीడीఐ.ఆర्గ/వिకी/Brahmic_scripts)).

మेऽ బी వర्ల्డ వिల నेవ्ర సैపॉర्ట, మेऽ బी దिస వिల ఓన्లी మेऽక దै జॉబ आవ ఇన्డीఐన्స
బेట्ర, సो వाట, దैట ఐలोన ఇస ఐ వర्దी గोల.


## ఐప्రोచ

క्రैన्ట्లी आయ ఐమ యूసिंగ [cmudict](https://github.కॉమ/cmusphinx/cmudict), వिచ
లिస्ట्స ఇंగ्గ्లिశ pronounciation కोడ ఫॉర సाమ ౪౦-౫౦K వర्డ्స. आయ ఐమ [మैపिंగ దोస
కोడ्స టू Devnagri](https://github.కॉమ/amitu/brahmic/బ्లॉబ/మैస्ట्ర/సीఏమ्యू.py#L౨౫-L౬౮).



## రिసाల्ట సो ఫॉర

దै సेకैన्డ హैఫ आవ దिస పेऽజ ఇస ఆటो transliterated వिద సिరो మैన्యुఐల క्రेక्శैన
యूసिंగ దिస టूల.

లूక ఐట [దै జिస्ట](https://జिస्ట.github.కॉమ/amitu/౪౭e౮౪౩౮౩౨౧d౦b౯e౪b౩cd) వिచ
శोస దै కैన्వ्ర्సैన आవ ౧౦౦౦ మोస्ట ఫ्రीక्వैన्ట्లी యूస्డ వర्డ्స ఇన ఇंగ्గ्లिశ లैंగ्గ्వैజ. ఇట
ఇస ఓన्లी ౭౦-౮౦% ఐక्య्రैట సो ఫॉర. ఈవिన దै ఐక्య्రैసी రेऽట ఇస నॉట నोన, ఐస आయ ఐమ నॉట
దैట గ्రेऽట ఇన ఇंగ्గ्లिశ ప्రोన्ऽన्సीఏऽశैన మाయ्సेల्ఫ.

## హेల्ప మी ప्లीస!

ఫॉర्క దै [జिస्ట](https://జिస्ట.github.కॉమ/amitu/౪౭e౮౪౩౮౩౨౧d౦b౯e౪b౩cd), ఐన्డ క्రेక्ట
ఇట, ఐన्డ సेన्డ మी ఐ మेऽల. ఆర మेऽ బी జाస्ట మॉర्క దै లाయ्న्స యू థिंగ्క ఆర రॉंగ.

ఏనी హेల्ప వिద ఫिక्సिंగ సीఏమ्యू.py ఇస హाయ्లी ఐప्రीశीఏऽటिడ టू.

